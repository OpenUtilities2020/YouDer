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
from time import time
import  logging
import os
from os.path import isfile,dirname,basename
import subprocess
from time import time
from datetime import datetime, timedelta
from unicodedata import east_asian_width

from PySide2.QtCore import  QRunnable
from pytube.extract import publish_date
from youder.workers.Signals import Communication


from pytube import Stream, StreamQuery, YouTube
from requests import get

from youder.utils.helpers import millify,humanbytes
from youder.db.db import DB







def merge(ffmpeg,video_source:str, audio_source:str, callback, output_source:str=None) -> str:
    '''To Merge Video and Audio Sources
    
    @param : ffmpeg > ffmpeg Binary path
    @param : video_source > path of video file
    @param : audio_source > path of audio file
    @param : output_source > Merged Video Path (Optional)
    @param : call back > Function that takes output_file_size (kilo bytes)

    @return : merged_video_file > str
    

    Tiny/Small version of ffmpeg taken from 
                                            https://github.com/n00mkrad/smol-ffmpeg/
                                            '''


    #Update Status Bar
    # self.signals.status_bar_message.emit("Merging streams . . .")

    #Command to Merge Video and Audio Using ffmpeg
    if not output_source :
        path, format =video_source.split(".")
        output_source = path + "_merged.mp4"

    ffmpeg_command = f'{ffmpeg} -y -i "{video_source}" -i "{audio_source}" -map 0:v -map 1:a -c:v copy -shortest "{output_source}" '
    

    #Run ffmpeg command in a Terminal through subprocess
    CREATE_NO_WINDOW = 0x08000000
    process = subprocess.Popen(ffmpeg_command, stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT,
                                universal_newlines=True,creationflags=CREATE_NO_WINDOW)
    
    # Get Progress of Merging though ffmpeg output
    try:
        for line in process.stdout:
            
                size = int(line.split()[5][:-2])*1024 #Merged Video Size
                # progress = int(size * 100 / (self.stream.filesize+self.stream128kbps.filesize)) #Progression
                line9 = line.split()[9]
                line10 = line.split()[10]
                # Emiting the signal to status Bar
                callback(size,str(line9),str(line10))
    except:
        pass

    try:
        os.remove(video_source)
        os.remove(audio_source)
    except Exception as e:pass
        # logging.exception("Error while Clearing Temp  for Video " + str(self.stream))
        # self.signals.error_dailog.emit("Error", "Error While Deleting temp... Clear it manually ")
    return output_source









class Downloader(QRunnable):
    '''
    This Class for Download Video For Selected Streams
    '''
    def __init__(self,
                stream:dict,
                video_path:str,db:DB,tracking_downloads,
                log_file:Union[str,None]=None,
                ffmpeg:Union[str,None]=None):

        '''
        @param : stream > Stream to Download
        @param : video_path > Path of Dowloaded Video 
        @param : log_file > path of log_file (Optional)
        @param : ffmpeg > path of Ffmpeg binary file (Optional)
                 
        @raises : FileNotFoundError > If Audio file specified while ffmpeg not specified or not Exists

        '''
        super(Downloader, self).__init__()

        self.stream_data = stream
        self.stream :Stream = stream['stream']
        self.yt: YouTube = stream['yt']
        self.video_path = video_path
        self.db = db
        self.tracking_downloads = tracking_downloads
        self.log_file = log_file
        self.audio_stream : Stream = self.yt.streams.get_audio_only() if not self.stream_data['progressive'] else None
        self.ffmpeg_binary = ffmpeg

        self.signals = Communication()


        self.yt.register_on_progress_callback(self.on_progress)
        self.yt.register_on_complete_callback(self.on_completes)

        self.size = self.stream.filesize
        if self.audio_stream : self.size += self.audio_stream.filesize

        self.total = humanbytes(self.size) #Size of Stream

        if self.log_file:
            # Enable Logging ...
            logging.basicConfig(filename=self.log_file,
                                format='%(process)d-%(levelname)s-%(message)s',
                                level=logging.INFO
                                )



    def run(self):
        try:
            self.timer = time() # Get Time of Now

            self.video_path = self.stream.download(self.video_path,skip_existing=True)

            if self.audio_stream and self.stream.type == 'video':
                if not isfile(self.ffmpeg_binary) : raise FileNotFoundError(f"ffmpeg is not Found at {self.ffmpeg_binary}")

                self.audio_path=self.audio_stream.download(output_path=dirname(self.video_path),skip_existing=True,filename="audio")
                self.video_path = merge(self.ffmpeg_binary,self.video_path,self.audio_path,self.merge_progress)  
                #Completed Downloading and Merging
                self.signals.status_bar_message.emit("Download Completed")
                self.signals.progress.emit(100)

            if self.stream.type == 'audio' : 
                try : os.rename(self.video_path,self.video_path[:-4]+".mp3")
                except: pass

            if self.tracking_downloads == "True": 
                self.db.add_video(video_id = self.yt.video_id,
                                url =  self.yt.watch_url,
                                title = self.yt.title,
                                thumbnail = get(self.yt.thumbnail_url).content,
                                thumbnail_url = self.yt.thumbnail_url,
                                author = self.yt.author,
                                channel_id = self.yt.channel_id,
                                channel_url = self.yt.channel_url,
                                description = self.yt.description,
                                views = self.yt.views,
                                length = self.yt.length,
                                publish_date = self.yt.publish_date,
                                download_time = datetime.today(),
                                location = self.video_path)

            self.signals.status_bar_message.emit("Download Completed")
            self.signals.download_completed.emit(self.yt)
        except Exception as e:
            self.signals.error_dialog.emit("Something Went Wrong",str(e))



    def merge_progress(self,size,line9,line10): 

        progress = int(size * 100 / self.size)
        self.signals.progress.emit(progress)
        self.signals.status_bar_message.emit(f"Merging Streams with {line9}{line10}")

    def on_progress(self,stream,chuck,bytes_remaining):

        now=time()#Time of Now

        self.bytes_downloaded=self.size - bytes_remaining

        if now>self.timer:
            difference = now - self.timer
            speed=humanbytes(self.bytes_downloaded / difference)
            progress = self.bytes_downloaded * 100 / stream.filesize
            self.current= humanbytes(self.bytes_downloaded)
            self.signals.status_bar_message.emit("Downloading... "+ self.current+"/"+self.total+"     Speed: "+speed+"PS")
            self.signals.progress.emit(int(progress))

    def on_completes(self,stream,file_path): pass
        


        
