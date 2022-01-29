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

from PySide2.QtCore import QByteArray, Slot,Qt,QSize
from PySide2.QtGui import QImage, QPixmap, QIcon
from PySide2.QtWidgets import QMessageBox,QFileDialog

import sys
from os.path import join

from youder.ui.Ui_main_ui import Ui_YouDer


class Ui_updater():
    """
    Ui_Updater > To Update YouDer UI
    """

    def __init__(self,ui:Ui_YouDer) -> None:
        """
        @param : ui > Ui_YouDer (To Access Ui Components)
        @returns : None
        """
        if sys.platform == "win32" :
            from PySide2.QtWinExtras import QWinTaskbarProgress
            self.win_progress = QWinTaskbarProgress()
            self.win_progress.hide()
            self.win_progress.setValue(0)

        

        self.ui = ui
        self.streams=[]
        self.video = None



    @Slot(dict)
    def update_video_info(self,video:dict) -> None:
        """
        @param : video > Dictoinary 

        Updates Video Information
        """
        self.video = video
        self.update_video_title(video['title'],video['author'])
        self.update_video_length(video['length'])
        self.update_video_views(video['views'])
        self.update_thumbnail(video['thumbnail'])


        self.update_status_bar("Looking For Available Formats ...")


    def update_status_bar(self,text:str) -> None:
        '''
        @param : text : Text (string) to update Status Bar

        @returns : None
        '''
        self.ui.status_bar.setText(text)

    def  update_video_title(self,title,auther):
        """
        @param : title > Video Title (String)
        @param : auther > Video Channel Name (Auther| String)
        """
        self.ui.title_label.setText(title+"\n\n\n By "+auther)
        self.ui.title_label.show()

    def update_video_views(self,views:str) -> None:
        '''
        @param  : views > Human Readable Format of View (Ex:- 2k, 5M views)

        @returns : None
        '''
        self.ui.views.setText(views)
        self.ui.views.show()
        self.ui.eye_icon_label.show()

    def update_video_length(self,length:str) -> None:
        '''
        @param : length > Length of video in String Format like 17:05:25 
        @returns : None
        '''
        self.ui.length_label.setText(length)
        self.ui.video_length_icon_label.show()
        self.ui.length_label.show()

  
    def update_thumbnail(self,raw_data:bytes):
        pixmap = QPixmap()
        pixmap.loadFromData(raw_data)
        pixmap = pixmap.scaled(300, 200, Qt.KeepAspectRatio)
        self.ui.thubnail_label.setPixmap(pixmap)
        self.ui.thubnail_label.show()

    @Slot(dict)
    def add_new_stream(self,stream:dict) -> None:
        #Add stream to a list
        if len(self.streams) == 0: 
            self.ui.combobox.addItem("Select a Format")
            self.ui.combobox.show()
        self.streams.append(stream)
        self.ui.combobox.addItem(stream["title"])

    
    def fetching_started(self):
        self.update_status_bar("Featching Data from YouTube . . .") #Update Status Bar
        self.ui.button_getinfo.setDisabled(True)
        self.ui.progressbar.setMaximum(0)
        self.ui.progressbar.show()
        self.ui.combobox.clear()
        self.streams=[]

        
    @Slot(bool)
    def fetching_finished(self,bool):
        self.ui.button_getinfo.setDisabled(False)
        self.ui.progressbar.setMaximum(100)
        self.ui.progressbar.hide()
        self.ui.status_bar.setText("Ready ...")
        if bool :
            self.ui.download_button.show()
            self.ui.save_as_label.show()
            self.ui.save_as_linedit.show()
            self.ui.toolButton.show()
            self.ui.save_as_linedit.setText(join(self.ui.save_as_linedit.text(),self.video['title']))

    @Slot(str,str)
    def show_error(self,title,message):
        """This Slot or Method is called in several times
            To show Error Dialog box with QMessageBox()
            when a Error or Exception is happened in Get INfo or Downloader

            titile: Tiltle of Error Dialog Box
            Messaage: String to Display on Message Box 
        """
        dailog = QMessageBox()
        dailog.setText(message)
        dailog.setWindowTitle(title)
        dailog.setStandardButtons(QMessageBox.Ok)
        dailog.exec_()

    def paste_into_linedit(self):
        '''
        Pastes Clipboard Text to Link QLinkEdit
        '''
        self.ui.link_linedit.clear()
        self.ui.link_linedit.paste()

    def show_download_button(self,bool):
        """
        bool: IS time to show Download Button and other component

        """
        if bool:
            self.ui.save_as_linedit.show()
            self.ui.save_as_label.show()
            self.ui.download_button.show()
            self.ui.toolButton.show()

    

    def get_current_stream(self):
        """
        Return : User Choose Stream to Download
        """
        if self.ui.combobox.currentIndex()!=0:
            return self.streams[self.ui.combobox.currentIndex()-1]
            # Combo box has  one item("Select Stream") more than streaams list
        else:
            self.show_error("Select a Format","Select a Video/Audio Resolution ")

    def update_save_as_edit(self,text:str) -> None:
        """
        @param text : Text that used to update linedit
        """
        self.ui.save_as_linedit.setText(text)
        
    @Slot(int)
    def update_progress(self,value):

        """
        Update Progress Bar as per integer of Value
        """
        if value>0:
            self.ui.progressbar.setMaximum(100)
            self.ui.progressbar.setValue(value)
            if sys.platform == 'win32' :
                self.win_progress.setValue(value)
                self.win_progress.setMaximum(100)


        else:
            # Value is not positive > Set Progress is infinitive
            self.ui.progressbar.setMinimum(0)
            self.ui.progressbar.setMaximum(0)
            self.ui.progressbar.show()
            if sys.platform == 'win32' :
                self.win_progress.setMaximum(0)
                self.win_progress.setMinimum(0)
                self.win_progress.show()