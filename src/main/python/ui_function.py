from PySide2.QtGui import QIcon,QPixmap
from PySide2.QtCore import QSize,QPropertyAnimation,QEasingCurve

import resources_rc
import webbrowser
class UI_Functions():
    '''This class contains build in Theming functions'''

    def __init__(self,youder,ui,ctx):

        self.youder=youder
        self.ui = ui
        self.ctx = ctx
        self.github_link="https://github.com/OpenUtilities2020/YouDer"
        self.telegram_link="https://t.me/Open_Utilities"
        self.ui.pages.setCurrentIndex(0)

        self.dark_mode=True
        self.green_mode=False
        self.pink_mode=False
        if self.dark_mode==True:
            icon = QIcon()
            icon.addFile(u":/toggle_on/icons/white/toggle_on.png", QSize(), QIcon.Normal, QIcon.Off)
            self.ui.dark_mode_onoff_button.setIcon(icon)
            self.ui.dark_mode_onoff_button.setIconSize(QSize(80, 30))
            self.youder.setStyleSheet(open(self.ctx.dark).read())
            self.load_white_icons()



        #self.load_green_icons()

    def open_github(self):
        '''
        TO Open OpenUtilities Github link in browser
        :return:
        '''
        webbrowser.open(url=self.github_link,autoraise=True)

    def open_telegram(self):
        '''
        TO Open OpenUtilities Telegram link in browser
        :return:
        '''
        webbrowser.open(url=self.telegram_link,autoraise=True)


    def load_white_icons(self):
        """Loading  Dark  icon for Buttons and labels...etc"""
        '''Loading Icon for Buttons'''

        icon = QIcon() #For Toggle Button
        icon.addFile(u":/toggle/icons/white/toggle_hor.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ui.button_toggle.setIcon(icon)
        self.ui.button_toggle.setIconSize(QSize(42, 42))

        icon1 = QIcon()#For HOme Button
        icon1.addFile(u":/home/icons/white/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ui.button_home.setIcon(icon1)
        self.ui.button_home.setIconSize(QSize(36, 36))


        icon2 = QIcon()# For Settings Button
        icon2.addFile(u":/settings/icons/white/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ui.button_settings.setIcon(icon2)
        self.ui.button_settings.setIconSize(QSize(24, 24))

        icon3 = QIcon()#For About Button
        icon3.addFile(u":/about/icons/white/about.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ui.button_about.setIcon(icon3)
        self.ui.button_about.setIconSize(QSize(36, 36))

        icon4 = QIcon()#For Paste Button
        icon4.addFile(u":/paste/icons/white/paste.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ui.button_paste.setIcon(icon4)
        self.ui.button_paste.setIconSize(QSize(16, 16))

        icon5 = QIcon()#For Button Get Info
        icon5.addFile(u":/getinfo/icons/white/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ui.button_getinfo.setIcon(icon5)
        self.ui.button_getinfo.setIconSize(QSize(16, 16))

        icon6 = QIcon()#For Download Button
        icon6.addFile(u":/download/icons/white/download.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ui.download_button.setIcon(icon6)
        self.ui.download_button.setIconSize(QSize(24, 24))

        icon7 = QIcon()#For Night MOde Button
        icon7.addFile(u":/toggle_on/icons/white/toggle_on.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ui.dark_mode_onoff_button.setIcon(icon7)
        self.ui.dark_mode_onoff_button.setIconSize(QSize(80, 30))

        '''Icons for  Labels'''

        self.ui.eye_icon_label.setPixmap(QPixmap(u":/eye/icons/white/eye.png"))
        self.ui.video_length_icon_label.setPixmap(QPixmap(u":/video_length/icons/white/video_length.png"))
        self.ui.label_for_gear_icon.setPixmap(QPixmap(u":/gear_icon/icons/white/settings_gear.png"))

        """Text for some labels"""

        '''self.ui.night_mode_label.setStyleSheet(u"color: rgb(240,240,240);")
        self.ui.choose_you_theme_label.setStyleSheet(u"color: rgb(240,240,240);")'''

    def load_black_icons(self):
        icon = QIcon()  # For Toggle Button
        icon.addFile(u":/toggle_black/icons/black/toggle_hor.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ui.button_toggle.setIcon(icon)
        self.ui.button_toggle.setIconSize(QSize(42, 42))

        icon1 = QIcon()  # For HOme Button
        icon1.addFile(u":/home_black/icons/black/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ui.button_home.setIcon(icon1)
        self.ui.button_home.setIconSize(QSize(36, 36))

        icon2 = QIcon()  # For Settings Button
        icon2.addFile(u":/settings_black/icons/black/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ui.button_settings.setIcon(icon2)
        self.ui.button_settings.setIconSize(QSize(24, 24))

        icon3 = QIcon()  # For About Button
        icon3.addFile(u":/about_black/icons/black/about.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ui.button_about.setIcon(icon3)
        self.ui.button_about.setIconSize(QSize(36, 36))

        icon4 = QIcon()  # For Paste Button
        icon4.addFile(u":/paste_black/icons/black/paste.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ui.button_paste.setIcon(icon4)
        self.ui.button_paste.setIconSize(QSize(16, 16))

        icon5 = QIcon()  # For Button Get Info
        icon5.addFile(u":/search_black/icons/black/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ui.button_getinfo.setIcon(icon5)
        self.ui.button_getinfo.setIconSize(QSize(16, 16))

        icon6 = QIcon()  # For Download Button
        icon6.addFile(u":/dowload_black/icons/black/download.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ui.download_button.setIcon(icon6)
        self.ui.download_button.setIconSize(QSize(24, 24))

        icon7 = QIcon()  # For Night MOde Button
        icon7.addFile(u":/toggle_off/icons/white/toggle_off.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ui.dark_mode_onoff_button.setIcon(icon7)
        self.ui.dark_mode_onoff_button.setIconSize(QSize(80, 30))

        '''Icons for  Labels'''

        self.ui.eye_icon_label.setPixmap(QPixmap(u":/eye_black/icons/black/eye.png"))
        self.ui.video_length_icon_label.setPixmap(QPixmap(u":/video_length/icons/white/video_length.png"))
        '''#pixmap=QPixmap(u":/video_length_black/icons/black/length.png")
        #pixmap.scaledToHeight(30)
        #pixmap.scaledToWidth(80)
        #self.ui.video_length_icon_label.setPixmap(QPixmap(pixmap))
        #self.ui.video_length_icon_label.setScaledContents(False)'''
        self.ui.video_length_icon_label.setPixmap(QPixmap(u":/video_length_black/icons/black/length.png"))
        self.ui.label_for_gear_icon.setPixmap(QPixmap(u":/gear_black/icons/black/settings_gear.png"))

        """Text for some labels"""

        '''self.ui.night_mode_label.setStyleSheet(u"color: rgb(0,0,0);")
        self.ui.choose_you_theme_label.setStyleSheet(u"color: rgb(0,0,0);")'''

    def load_green_icons(self):
        """Loading green  icon for Buttons and labels...etc"""
        '''Loading Icon for Buttons'''

        icon = QIcon() #For Toggle Button
        icon.addFile(u":/toggle_green/icons/green/toggle_hor_green.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ui.button_toggle.setIcon(icon)
        self.ui.button_toggle.setIconSize(QSize(42, 42))

        icon1 = QIcon()#For HOme Button
        icon1.addFile(u":/home_green/icons/green/home_green.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ui.button_home.setIcon(icon1)
        self.ui.button_home.setIconSize(QSize(36, 36))


        icon2 = QIcon()# For Settings Button
        icon2.addFile(u":/settings_green/icons/green/settings_green.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ui.button_settings.setIcon(icon2)
        self.ui.button_settings.setIconSize(QSize(24, 24))

        icon3 = QIcon()#For About Button
        icon3.addFile(u":/about_green/icons/green/about_green.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ui.button_about.setIcon(icon3)
        self.ui.button_about.setIconSize(QSize(36, 36))

        icon4 = QIcon()#For Paste Button
        icon4.addFile(u"/paste_green/icons/green/paste_green.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ui.button_paste.setIcon(icon4)
        self.ui.button_paste.setIconSize(QSize(16, 16))

        icon5 = QIcon()#For Button Get Info
        icon5.addFile(u":/getinfo_green/icons/green/search_green.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ui.button_getinfo.setIcon(icon5)
        self.ui.button_getinfo.setIconSize(QSize(16, 16))

        icon6 = QIcon()#For Download Button
        icon6.addFile(u":/download_green/icons/green/download_green.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ui.download_button.setIcon(icon6)
        self.ui.download_button.setIconSize(QSize(24, 24))



        '''Icons for  Labels'''

        self.ui.eye_icon_label.setPixmap(QPixmap(u":/eye_green/icons/green/eye_green.png"))
        #self.ui.eye_icon_label.setScaledContents(True)
        self.ui.video_length_icon_label.setPixmap(QPixmap(u":/length_green/icons/green/length_green.png"))
        #self.ui.video_length_icon_label.setScaledContents(True)
        self.ui.label_for_gear_icon.setPixmap(QPixmap(u":/gear_green/icons/green/gear_green.png"))

        """Text for some labels"""

    def load_pink_icons(self):
        """Loading  Pink  icon for Buttons and labels...etc"""
        '''Loading Icon for Buttons'''

        icon = QIcon()  # For Toggle Button
        icon.addFile(u":/toggle_pink/icons/pink/toggle_hor_pink.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ui.button_toggle.setIcon(icon)
        self.ui.button_toggle.setIconSize(QSize(42, 42))

        icon1 = QIcon()  # For HOme Button
        icon1.addFile(u":/home_pink/icons/pink/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ui.button_home.setIcon(icon1)
        self.ui.button_home.setIconSize(QSize(36, 36))

        icon2 = QIcon()  # For Settings Button
        icon2.addFile(u":/settings_pink/icons/pink/settings_pink.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ui.button_settings.setIcon(icon2)
        self.ui.button_settings.setIconSize(QSize(24, 24))

        icon3 = QIcon()  # For About Button
        icon3.addFile(u":/about_pink/icons/pink/about_pink.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ui.button_about.setIcon(icon3)
        self.ui.button_about.setIconSize(QSize(36, 36))

        icon4 = QIcon()  # For Paste Button
        icon4.addFile(u":/paste_pink/icons/pink/search_pink.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ui.button_paste.setIcon(icon4)
        self.ui.button_paste.setIconSize(QSize(16, 16))

        icon5 = QIcon()  # For Button Get Info
        icon5.addFile(u":/getinfo_pink/icons/pink/search_pink.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ui.button_getinfo.setIcon(icon5)
        self.ui.button_getinfo.setIconSize(QSize(16, 16))

        icon6 = QIcon()  # For Download Button
        icon6.addFile(u":/dowload_pink/icons/pink/download_pink.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ui.download_button.setIcon(icon6)
        self.ui.download_button.setIconSize(QSize(24, 24))



        '''Icons for  Labels'''

        self.ui.eye_icon_label.setPixmap(QPixmap(u":/eye_pink/icons/pink/eye_pink.png"))
        self.ui.video_length_icon_label.setPixmap(QPixmap(u":/length_pink/icons/pink/length_pink.png"))
        self.ui.label_for_gear_icon.setPixmap(QPixmap(u":/gear_pink/icons/pink/gear.png"))

        """Text for some labels"""

    def switch_mode(self):
        if self.dark_mode==True:
            self.youder.setStyleSheet(open(self.ctx.white).read())

            self.dark_mode=False
            icon = QIcon()
            icon.addFile(u":/toggle_off/icons/white/toggle_off.png", QSize(), QIcon.Normal, QIcon.Off)
            self.ui.dark_mode_onoff_button.setIcon(icon)
            self.ui.dark_mode_onoff_button.setIconSize(QSize(80, 30))
            if self.pink_mode:
                self.load_pink_icons()
                return
            elif self.green_mode:
                self.load_green_icons()
                return
            else:
                self.load_black_icons()


        elif self.dark_mode==False:
            self.youder.setStyleSheet(open(self.ctx.dark).read())
            self.load_white_icons()
            self.dark_mode=True
            icon = QIcon()
            icon.addFile(u":/toggle_on/icons/white/toggle_on.png", QSize(), QIcon.Normal, QIcon.Off)
            self.ui.dark_mode_onoff_button.setIcon(icon)
            self.ui.dark_mode_onoff_button.setIconSize(QSize(80, 30))
            if self.pink_mode:
                self.load_pink_icons()
                return
            elif self.green_mode:
                self.load_green_icons()
                return
            else:
                self.load_white_icons()

    def radio_toggled(self,button):
        if button==self.ui.green_radio_button:
            if self.ui.green_radio_button.isChecked():
                self.load_green_icons()
                self.green_mode=True
                self.pink_mode=False
                return
            else:
                if self.dark_mode:
                    self.load_white_icons()
                else:
                    self.load_black_icons()

        elif button==self.ui.pink_radio_button:
            if self.ui.pink_radio_button.isChecked():
                self.load_pink_icons()
                self.pink_mode=True
                self.green_mode=False
                return
            else:
                if self.dark_mode:
                    self.load_white_icons()
                else:
                    self.load_black_icons()
        elif button==self.ui.default_radio_button:
            if self.dark_mode:
                self.load_white_icons()
            else:
                self.load_black_icons()
            self.green_mode=False
            self.pink_mode=False





    def toggle_menu(self):
        standard = 50
        extended = 150

        #Check width of fram main left....

        width =self.ui.frame_main_left.width()

        #Swap Values
        if width==standard:
            self.ui.button_home.setText(u"Home")
            self.ui.button_settings.setText(u"Settings")
            self.ui.button_about.setText(u"About")

            start=standard
            end=extended
        else:
            self.ui.button_home.setText(u"")
            self.ui.button_settings.setText(u"")
            self.ui.button_about.setText(u"")

            start=extended
            end=standard

        #Define animations...

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


        if button==self.ui.button_home:
            self.ui.pages.setCurrentIndex(0)
        elif button==self.ui.button_settings:
            self.ui.pages.setCurrentIndex(1)
        elif button==self.ui.button_about:
            self.ui.pages.setCurrentIndex(2)

















