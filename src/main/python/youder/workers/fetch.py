#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2022 Open Utilities
# Created by : Ram Durga Sai
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE

__organization__ = "OpenUtilites"
__application__ = "YouDer"
__version__ = "3.0"
__author__ = " Ram Durga Sai "


from typing import Union
from PySide2.QtCore import  QRunnable
from pytube import YouTube
from pytube.exceptions import RegexMatchError
import requests

from datetime import timedelta
import  logging

from youder.workers.Signals import Communication
from youder.utils.helpers import millify,humanbytes


class Fetch(QRunnable):
    '''This class is to get Video Information from YouTube Through Pytube API'''
    formats = {
            "1440p" : '2k',
            "2160p" : '4k',
            "4320"  : '8k'
        }

    def __init__(self,link:str,log_file:Union[str,None]=None) -> None:
        """
        @param : link >  Video Link to fetch info
        @param : log_file > log_file to setup log (Optional)

        @returns : None
        
        """
        super(Fetch, self).__init__()
        self.signals = Communication()
        self.link=link

        #Enable Logging ...
        logging.basicConfig(filename=log_file,
                            format='%(process)d-%(levelname)s-%(message)s',
                            level=logging.INFO
                            )
    def run(self) -> None:
        try:
            yt = YouTube(self.link)
            video = {
                'id' : yt.video_id,
                'title': yt.title,
                'author': yt.author,
                'length_raw': yt.length,
                'length' : str(timedelta(seconds=yt.length)),
                'views_raw' : yt.views,
                'views' : str(millify(yt.views)),
                'thumbnail_url':yt.thumbnail_url,
                'thumbnail':requests.get(yt.thumbnail_url).content
            }
            self.signals.video.emit(video)
    
            default_audio_stream = yt.streams.get_audio_only() #Audio Stream

            for stream in yt.streams.asc() :

                # Filter Streams Don't have Resolution

                stream_data = {
                    'stream' : stream,
                    'itag' : stream.itag,
                    'type' : stream.mime_type.split('/'),
                    'progressive' : stream.is_progressive,
                    'yt' : yt
                }
                

                stream_data['raw_size'], stream_data['common_size'] = stream.filesize, humanbytes(stream.filesize)

                if not stream.is_progressive : stream_data['raw_size'] += default_audio_stream.filesize 

                if stream.type == 'video':
                    if stream.resolution == None : continue
                    stream_data['resolution'] = stream.resolution
                    stream_data['fps'] = stream.fps
                    common_resolution_name = self.formats[stream.resolution] if int(stream.resolution[:-1]) > 1080 else stream.resolution
                    stream_data['title'] = f"{common_resolution_name} {stream.fps}fps ({stream.type}) - {stream_data['common_size']}"

                elif stream.type == 'audio':
                    stream_data['abr'] = stream.abr
                    stream_data['title'] = f"{stream.abr} ({stream.type}) - {stream_data['common_size']}"

                else: raise NotImplemented("Not Impleted Yet")

                self.signals.stream.emit(stream_data)
            self.signals.fetch.emit(True)
        except RegexMatchError as regex_exception :
            self.signals.error_dialog.emit("Link is Invalid","Provided link is in Invalid") 