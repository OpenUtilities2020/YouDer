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
__application__  = "YouDer"
__version__ = "3.0"
__author__ = " Ram Durga Sai "


import logging

from PySide2.QtCore import *
from PySide2.QtCore import QThreadPool
from PySide2.QtWidgets import  QMainWindow
from pytube.__main__ import YouTube


from youder.ui.Ui_main_ui import Ui_YouDer
from youder.ui.functions.ui_function import UI_Functions
from youder.ui.functions.ui_updater import Ui_updater
from youder.ui.Ui_frame_video import Ui_widget_main
from youder.workers.fetch import Fetch
from youder.workers.downloader import Downloader
from youder.settings.Settings import Settings
from youder.db.db import DB
from youder.utils.utils import ask_to_choose_directory,user_profile
from youder.data import strings




class YouDer(QMainWindow):
    
    def __init__(self,context,*args,**kwargs):
        super(YouDer, self).__init__()

        self.context = context #Application Context

        self.settings = Settings(__organization__,__application__)

        self.db = DB(self.context.db)


        self.ui = Ui_YouDer()
        self.ui.setupUi(self)
        self.ui_function :UI_Functions = UI_Functions(self,self.ui,self.context,self.settings,self.db)
        self.ui_updater = Ui_updater(self.ui)

        

        self.threadpool_fetch = QThreadPool()
        self.threadpool_download = QThreadPool()

        logging.basicConfig(filename=self.context.log,format='%(process)d-%(levelname)s-%(message)s',level=logging.INFO)

        
        self.connect_signal_to_slots()
        self.settings.video_location = self.video_location()

        self.setWindowTitle(strings.title)
        self.show()


    

    def connect_signal_to_slots(self) -> None:
        
        self.ui.button_toggle.clicked.connect(self.ui_function.toggle_menu)
        self.ui.button_home.clicked.connect(lambda: self.ui_function.button_clicked(self.ui.button_home))
        self.ui.button_settings.clicked.connect(lambda: self.ui_function.button_clicked(self.ui.button_settings))
        self.ui.button_history.clicked.connect(lambda: self.ui_function.button_clicked(self.ui.button_history))
        self.ui.button_about.clicked.connect(lambda: self.ui_function.button_clicked(self.ui.button_about))

        self.ui.button_paste.clicked.connect(self.ui_updater.paste_into_linedit)
        self.ui.button_getinfo.clicked.connect(lambda :self.fetch_data(self.ui.link_linedit.text()))
        self.ui.download_button.clicked.connect(self.download)
        self.ui.toolButton.clicked.connect(self.set_video_location)

        self.ui.dark_mode_onoff_button.clicked.connect(self.ui_function.switch_mode)

        

        self.ui.green_radio_button.toggled.connect(lambda :self.ui_function.radio_toggled(self.ui.green_radio_button))
        self.ui.pink_radio_button.toggled.connect(lambda : self.ui_function.radio_toggled(self.ui.pink_radio_button))
        self.ui.default_radio_button.toggled.connect(lambda : self.ui_function.radio_toggled(self.ui.default_radio_button))

        
        self.ui.history_delete_button.clicked.connect(self.delete_history)
        self.ui.track_downloads_button.clicked.connect(self.ui_function.track_history)
        self.ui.download_location_tool_button.clicked.connect(
                            lambda  : self.set_video_location(self.ui.download_location_tool_button)
                            )

    def delete_history(self):
        self.db.delete_all_records()
        self.ui_function.load_history_frames()

    

    def set_video_location(self,button):
        path = ask_to_choose_directory()
        if path : 
            self.settings.video_location = path
            self.ui.save_as_linedit.setText(path)
            self.ui.download_location_linedit.setText(path)


    def video_location(self) -> str:
        """
        :returns video _location > String
        """

        if not self.settings.video_location:  self.settings.video_location = user_profile('Videos',__application__)
        return self.settings.video_location


    def fetch_data(self,link:str)->None:
        '''
        Fetches Video Information From Youtube
        Updates supplied to UI
        '''
        #Gets Link in self.link
        
        if link == "":
            '''If Link is empty string or not Provided'''
            self.ui_updater.show_error("Link is empty","It looks like is Empty")
            return

        logging.info("Fetching data for the Video link "+link)

        self.ui_updater.fetching_started()

        fetcher = Fetch(link,self.context.log)
        fetcher.signals.video.connect(self.ui_updater.update_video_info)
        fetcher.signals.stream.connect(self.ui_updater.add_new_stream)
        fetcher.signals.fetch.connect(self.ui_updater.fetching_finished)
        fetcher.signals.error_dailog.connect(self.ui_updater.show_error)

        
        self.threadpool_fetch.start(fetcher)

        # self.ui_updater.fetching_finished()

        

    def download(self):
        #Creating Instance for Downloader Class
        downloader = Downloader(self.ui_updater.get_current_stream(),self.settings.video_location,
                                self.db,self.settings.tracking_downloads,
                                self.context.log,self.context.ffmpeg)


        '''Connect Custom Signal of Download Class to Ui Updater Slots(function)'''
        downloader.signals.progress.connect(self.ui_updater.update_progress)
        downloader.signals.status_bar_message.connect(self.ui_updater.update_status_bar)
        downloader.signals.error_dailog.connect(self.ui_updater.show_error)
        downloader.signals.download_completed.connect(self.on_download_completes)

        #Update Log
        logging.info("Download Video for the Stream : \n" + str(self.ui_updater.get_current_stream()))

        '''Start the Threadpool of Download to Start the Download'''
        self.threadpool_download.start(downloader)

        # Update Log
        logging.info("Downloaded Video for the Stream : \n" +  str(self.ui_updater.get_current_stream()))

    @Slot(object)
    def on_download_completes(self,yt:YouTube) -> None:
        self.ui_function.load_history_frames()






