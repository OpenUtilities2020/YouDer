# !/usr/bin/env python3
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


from os import link
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *

from os.path import dirname


from webbrowser import open as open_in_browser

from youder.db.db import DB

from youder.ui.Ui_frame_video import Ui_widget_main
from youder.ui.Ui_main_ui import Ui_YouDer
from youder.settings.Settings import Settings
from youder.data import elements_icons,strings


""" 
all changes to main_ui file lost when recompiling that file
Add following lines in setupUi method after recompiling this file
from PySide2.QtGui import QFontDatabase
QFontDatabase.addApplicationFont(":/font/fonts/product_sans.ttf")
"""

class UI_Functions():

    '''This class contains build in Theming functions'''

    def __init__(self,youder,ui,context,settings:Settings,db:DB):
        self.youder  = youder
        self.ui : Ui_YouDer = ui
        self.context = context
        self.ui_settings = settings
        self.db = db

        #Set Home Page is Default Page
        self.ui.pages.setCurrentIndex(0)
      
        if not self.ui_settings.dark_mode : self.ui_settings.dark_mode = "True"
        if not self.ui_settings.theme : self.ui_settings.theme = 'default'
        if not self.ui_settings.tracking_downloads : self.ui_settings.tracking_downloads = "True"


        
        self.load_history_frames()
        self.load_icons()


        
        self.initial_widgets_values()
    def initial_widgets_values(self) -> None:

        self.youder.setStyleSheet(
            open(self.context.dark if self.ui_settings.dark_mode == 'True' else self.context.white).read()
            )

        self.ui.status_bar.setText("Ready...")
        self.ui.link_linedit.setPlaceholderText('Paste link')
        self.ui.link_linedit.setClearButtonEnabled(True)
     
        self.ui.combobox.clear()
        


        ''' Hiding Some Widgets at Startup '''
        self.ui.thubnail_label.hide()
        self.ui.eye_icon_label.hide()
        self.ui.views.hide()
        self.ui.video_length_icon_label.hide()
        self.ui.length_label.hide()
        self.ui.title_label.hide()
        self.ui.combobox.hide()
        self.ui.save_as_linedit.hide()
        self.ui.save_as_label.hide()
        self.ui.toolButton.hide()
        self.ui.progressbar.hide()
        self.ui.download_button.hide()

        self.ui.save_as_linedit.setText(self.youder.video_location())
        self.ui.download_location_linedit.setText(self.youder.video_location())


        self.ui.github_button.clicked.connect(lambda : open_in_browser(strings.links["github"]))
        self.ui.telegram_button.clicked.connect(lambda : open_in_browser(strings.links['telegram']))
        self.ui.youtube_button.clicked.connect(lambda : open_in_browser(strings.links['youtube']))

        if self.ui_settings.theme == 'default' : self.ui.default_radio_button.setChecked(True)
        elif self.ui_settings.theme == 'pink'  : self.ui.pink_radio_button.setChecked(True)
        elif self.ui_settings.theme == 'green' : self.ui.green_radio_button.setChecked(True)


        icon = QIcon()
        button = elements_icons.element_data["dark_mode_onoff_button"]  
        on,off = button['white'],button['black']
        icon.addFile(on if self.ui_settings.dark_mode == "True" else off, QSize(), QIcon.Normal, QIcon.Off)
        self.ui.dark_mode_onoff_button.setIcon(icon)

        icon = QIcon()
        button = elements_icons.element_data["track_downloads_button"]  
        on,off = button['white'],button['black']
        icon.addFile(on if self.ui_settings.tracking_downloads == "True" else off, QSize(), QIcon.Normal, QIcon.Off)
        self.ui.track_downloads_button.setIcon(icon)

        

        self.ui.version_label.setText(f"{__application__} Version {__version__}") # Set Version to Ui

    def load_icons(self,theme=None):
        if not theme : theme = self.ui_settings.theme
        if theme == 'default' :
            theme = "white" if self.ui_settings.dark_mode == "True" else "black"

        for element_name, data in elements_icons.element_data.items():
            element  = getattr(self.ui,element_name)
            keys = data.keys()
            if isinstance(element, QPushButton) and theme in keys:
                icon = QIcon() 
                icon.addFile(data[theme], QSize(), QIcon.Normal, QIcon.Off)
                element.setIcon(icon)
                if 'size' in keys :
                    element.setIconSize(QSize(*data['size']))

            elif isinstance(element,QLabel) : element.setPixmap(QPixmap(data[theme]))


    def track_history(self):
        self.ui_settings.tracking_downloads = "False" if self.ui_settings.tracking_downloads == "True" else "True"
        icon = QIcon()
        if self.ui_settings.tracking_downloads == "True":      
            icon.addFile(u":/toggle_on/icons/white/toggle_on.png", QSize(), QIcon.Normal, QIcon.Off)
        else:
            icon.addFile(u":/toggle_off/icons/white/toggle_off.png", QSize(), QIcon.Normal, QIcon.Off)

        self.ui.track_downloads_button.setIcon(icon)
        self.ui.track_downloads_button.setIconSize(QSize(80, 30))


    def switch_mode(self):
        self.ui_settings.dark_mode = "False" if self.ui_settings.dark_mode == "True" else "True"
        self.load_icons()
        self.youder.setStyleSheet(
            open(self.context.dark if self.ui_settings.dark_mode == 'True' else self.context.white).read()
            )
        icon = QIcon()
        button = elements_icons.element_data["dark_mode_onoff_button"]  
        on,off = button['white'],button['black']
        icon.addFile(on if self.ui_settings.dark_mode == "True" else off, QSize(), QIcon.Normal, QIcon.Off)
        self.ui.dark_mode_onoff_button.setIcon(icon)
         

    def radio_toggled(self,button):
        '''This Function is for set Green Pink and Black White Icons
            When  A Radio Button is Toggled
         '''

        if button==self.ui.green_radio_button: self.ui_settings.theme = "green"

        elif button==self.ui.pink_radio_button: self.ui_settings.theme = "pink"
            
        elif button==self.ui.default_radio_button: self.ui_settings.theme = "default"

        if button.isChecked() : self.load_icons(self.ui_settings.theme)



    def toggle_menu(self):
        """Toggle Menu

            This Function is for Expanding or Collapsing Left frame when
            Upper left toggled button pressed

        """

        #This are Standard and Extended width for left panel

        standard = 50
        extended = 150

        #Check frame is expanded or not by

        # Checking by current width

        width =self.ui.frame_main_left.width()

        #Swap Values

        if width==standard:
            # If width is standard Or Intial State

            #Set Text for button
            self.ui.button_home.setText(u"Home")
            self.ui.button_settings.setText(u"settings")
            self.ui.button_history.setText(u"History")
            self.ui.button_about.setText(u"About")

            start=standard
            end=extended
        else:
            #If width is extended or Extended State

            #Remove Text from Buttons
            self.ui.button_home.setText(u"")
            self.ui.button_settings.setText(u"")
            self.ui.button_history.setText(u"")
            self.ui.button_about.setText(u"")

            start=extended
            end=standard




        '''
        
            Changing Width of Left Frame by animating with QProperty Animation
         
            Duration : 400 milli Seconds
            QEasing Curve : InOUtQUary
            
            Start Value , End Value : as per Expend or Collapse
        
        '''

        self.animation_frame_main_left=QPropertyAnimation(self.ui.frame_main_left,b"minimumWidth")
        self.animation_frame_main_left.setDuration(400)
        self.animation_frame_main_left.setStartValue(start)
        self.animation_frame_main_left.setEndValue(end)
        self.animation_frame_main_left.setEasingCurve((QEasingCurve.InOutQuart))

        self.animation_frame_toggle = QPropertyAnimation(self.ui.frame_toggle, b"minimumWidth")
        self.animation_frame_toggle.setDuration(400)
        self.animation_frame_toggle.setStartValue(start)
        self.animation_frame_toggle.setEndValue(end)
        self.animation_frame_toggle.setEasingCurve((QEasingCurve.InOutQuart))




        #Start Both Animations

        self.animation_frame_main_left.start()
        self.animation_frame_toggle.start()


    

    def button_clicked(self,button):
        ''' This Method to Set Current Page
            for QStacked Widget
            If Button

                Home  Pressed : Current Index = 0

                settings Pressed : Current Index = 1

                About Pressed : Current Index = 2
        '''
        if button==self.ui.button_home: self.ui.pages.setCurrentIndex(0)
        elif button==self.ui.button_settings: self.ui.pages.setCurrentIndex(1)
        elif button==self.ui.button_history: self.ui.pages.setCurrentIndex(2)
        elif button==self.ui.button_about: self.ui.pages.setCurrentIndex(3)

    def re_run(self,link):
        self.youder.fetch_data(link)
        self.ui.pages.setCurrentIndex(0)

    def delete_frame(self,frame:QFrame,id:int) -> None:
        frame.hide()
        frame.setParent(None)
        self.db.remove_video(id)

    def history_frame(self,id,title,thumbnail,url,location) -> QFrame:
        frame, frame_ui = QFrame(), Ui_widget_main()
        frame_ui.setupUi(frame)

        frame_ui.title_label.setText(title)
        frame_ui.delete_button.clicked.connect(lambda : self.delete_frame(frame,id))
        frame_ui.open.clicked.connect(lambda : open_in_browser(dirname(location)))
        frame_ui.play.clicked.connect(lambda : open_in_browser(location))
        frame_ui.run.clicked.connect(lambda : self.re_run(url))
        frame_ui.youtube.clicked.connect(lambda : self.open(url))

        pixmap = QPixmap()
        pixmap.loadFromData(thumbnail)
        pixmap = pixmap.scaled(300, 200, Qt.KeepAspectRatio)

        frame_ui.thumbnail.setPixmap(pixmap)

        frame.setStyleSheet(open(self.context.dark_frame,'r').read())

        return frame
    
   
        
    def load_history_frames(self):
        while self.ui.history_layout.count():
            child = self.ui.history_layout.takeAt(0)
            if child.widget():
             child.widget().deleteLater()
        history = self.db.select('id','title','thumbnail','url','location')

        for video in history:
            id, title, thumbnail, url,location = video
            self.ui.history_layout.addWidget(self.history_frame(id, title, thumbnail, url,location))

        end_frame = QFrame()
        self.verticalLayout = QVBoxLayout(end_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_end_main = QFrame(end_frame)
        self.frame_end_main.setObjectName(u"frame_end_main")
        self.frame_end_main.setFrameShape(QFrame.StyledPanel)
        self.frame_end_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_end_main)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.history_end_label = QLabel(self.frame_end_main)
        self.history_end_label.setObjectName(u"history_end_label")
        font = QFont()
        font.setFamily(u"Product Sans")
        font.setPointSize(12)
        self.history_end_label.setFont(font)
        self.history_end_label.setStyleSheet(u"")
        self.history_end_label.setAlignment(Qt.AlignCenter)
        self.verticalLayout_2.addWidget(self.history_end_label)
        self.verticalLayout.addWidget(self.frame_end_main)

        text = "Your History is Empty" if history == [] else "You Reached The End"

        self.history_end_label.setText(text)
        self.ui.history_layout.addWidget(end_frame)

    
    




    







