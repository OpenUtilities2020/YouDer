from fbs_runtime.application_context.PySide2 import ApplicationContext, cached_property
from PySide2.QtCore import QThreadPool
import sys ,os
from PySide2.QtWidgets import QMainWindow
from main_ui import Ui_YouDer
from ui_function import UI_Functions
from ui_upadter import Ui_updater
from Workers import GetInfo,Downloader
import logging
from pathlib import Path



class AppContext(ApplicationContext):
    '''Class Application Context'''
    def run(self):
        self.main_window.show()
        return self.app.exec_()
    @cached_property
    def main_window(self):
        return YouDer(self)
    @cached_property
    def dark(self):
        '''Returns Dark .css file path '''
        return (self.get_resource('resources/dark.css'))
    @cached_property
    def white(self):
        '''Returns White.css file path'''
        return (self.get_resource('resources/white.css'))
    @cached_property
    def thumbnail(self):
        '''Returns thumbnail.png file path '''
        return (self.get_resource('resources/thumbnail.png'))
    @cached_property
    def log(self):
        '''Returns log.txt file to store log data into a file'''
        return (self.get_resource('resources/log.txt'))

    @cached_property
    def ffmpeg(self):
        '''Returns ffmpeg.exe file path

        The size of official build of ffmpeg is  80Mb
        So Small and tiny version of ffmpeg is taken from the Following Github Page
        https://github.com/n00mkrad/smol-ffmpeg/'''
        return (self.get_resource('resources/ffmpeg.exe'))

class YouDer(QMainWindow):
    '''Class YOuDer'''

    def __init__(self,ctx):
        super(YouDer, self).__init__()

        '''Check Operating System for Path of Video'''
        if sys.platform == "linux" or sys.platform == "linux2":
            '''If YouDer is running on Linx machine'''
            self.video_path = os.path.join(Path.home(), 'Videos', 'YouDer')
            if not os.path.isdir(self.video_path):
                os.mkdir(self.video_path)
        elif sys.platform == "darwin":
            '''If YouDer is running on Mac Pc'''
            self.video_path = os.path.join(Path.home(), 'Videos', 'YouDer')
            if not os.path.isdir(self.video_path):
                os.mkdir(self.video_path)
        elif sys.platform == "win32":
            '''If YouDer is running on Windows Computer'''
            self.video_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Videos', 'YouDer')
            if not os.path.isdir(self.video_path):
                os.mkdir(self.video_path)


        '''Create a Instance for Application context ,YOuDer main window'''
        self.ctx = ctx
        self.ui=Ui_YouDer()

        #  all changes to main_ui file lost when recompiling that file
        # Add following lines in setupUi method after recompiling this file
        # from PySide2.QtGui import QFontDatabase
        # QFontDatabase.addApplicationFont(":/font/fonts/product_sans.ttf")
        self.ui.setupUi(self)


        '''Create a Instance for UI Functions and Updater'''
        self.ui_function = UI_Functions(self,self.ui,self.ctx)
        self.ui_updater = Ui_updater(self.ui,self.video_path,self.ctx)
        #Remove After Done





        '''Connect Signal Which are to change ui asper User request to slot'''
        self.ui.button_toggle.clicked.connect(self.ui_function.toggle_menu)
        self.ui.button_home.clicked.connect(lambda: self.ui_function.button_clicked(self.ui.button_home))
        self.ui.button_settings.clicked.connect(lambda: self.ui_function.button_clicked(self.ui.button_settings))
        self.ui.button_about.clicked.connect(lambda: self.ui_function.button_clicked(self.ui.button_about))
        self.ui.dark_mode_onoff_button.clicked.connect(self.ui_function.switch_mode)
        self.ui.green_radio_button.toggled.connect(lambda :self.ui_function.radio_toggled(self.ui.green_radio_button))
        self.ui.pink_radio_button.toggled.connect(lambda : self.ui_function.radio_toggled(self.ui.pink_radio_button))
        self.ui.default_radio_button.toggled.connect(lambda : self.ui_function.radio_toggled(self.ui.default_radio_button))
        self.ui.github_button.clicked.connect(self.ui_function.open_github)
        self.ui.telegram_button.clicked.connect(self.ui_function.open_telegram)
        self.ui.youtube_button.clicked.connect(self.ui_function.open_youtube)


        '''Connect Signal to Slot Which to Get Video Information and Download'''

        self.ui.button_paste.clicked.connect(self.ui_updater.paste_into_linedit)
        self.ui.button_getinfo.clicked.connect(self.goto_getinfo)
        self.ui.download_button.clicked.connect(self.download)
        self.ui.toolButton.clicked.connect(self.ui_updater.get_video_directory)


        '''Default Values for Some Widgets and Main Window'''

        self.ui_updater.update_status_bar("Ready...")
        self.ui.link_linedit.setPlaceholderText('Paste link')
        self.ui.link_linedit.setClearButtonEnabled(True)
        self.ui.combobox.clear()
        self.setWindowTitle("YouDer - Free, YouTube Video Downloader")
        self.show()


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

        ''' Used QThreadPool to Get Video Info and Download
        
            Always use QThreadPoll or QThread to do long running tasks 
            It will not block Ui execution         '''

        self.threadpool_getinfo = QThreadPool()
        self.threadpool_download = QThreadPool()




        '''Enable Logging '''
        logging.basicConfig(filename=self.ctx.log,
                            format='%(process)d-%(levelname)s-%(message)s',
                            level=logging.INFO
                            )



    def goto_getinfo(self):
        '''This Method is Connected to GetINfo Button

            Gets Video's title ,length,thumbnail using link
                                    which is provided in LineEdit

            Using Pytube Api Updates title,thumbnail,etc
        '''




        self.link=self.ui.link_linedit.text() #Gets Link in self.link
        if self.link == "":
            '''If Link is empty string or not Provided'''
            self.ui_updater.show_error("Link is empty","It looks like is Empty")
            return

        #Store Link in log file
        logging.info("Getting Video Information for the Video link "+self.link)


        # Pass true for get info started

        self.ui_updater.getinfo_started(True)


        self.ui_updater.update_status_bar("Featching Data from YouTube . . .") #Update Status Bar

        '''Creating Instance for GetInfo class'''
        self.getinfo = GetInfo(self.link,self.ctx)


        '''Connect Custom Signal in Get Info Class to Ui Updater Slots(Functions)'''

        self.getinfo.signals.error_dailog.connect(self.ui_updater.show_error)
        self.getinfo.signals.status_bar_message.connect(self.ui_updater.update_status_bar)
        self.getinfo.signals.video_title.connect(self.ui_updater.update_video_title)
        self.getinfo.signals.video_auther.connect(self.ui_updater.update_auther)
        self.getinfo.signals.video_views.connect(self.ui_updater.update_video_views)
        self.getinfo.signals.video_length.connect(self.ui_updater.update_video_length)
        self.getinfo.signals.thumbnail.connect(self.ui_updater.update_thumbnail)
        self.getinfo.signals.new_format.connect(self.ui_updater.add_new_format)
        self.getinfo.signals.getinfo_finished.connect(self.ui_updater.getinfo_finished)
        self.getinfo.signals.show_download_button.connect(self.ui_updater.show_download_button)
        self.getinfo.signals.transmit_yt.connect(self.ui_updater.set_yt)


        #Start ThreadPoll of Get Info

        self.threadpool_getinfo.start(self.getinfo)

        #Update Log
        logging.info("Getting Info for link:-"+self.link +"is Done")

    def download(self):
        '''This Method is connected to Download Button

            Passes Selected Stream from Combo Box to Download ThreadPoll
                                                to Download Video


        '''


        #Creating Instance for Downloader Class
        self.downloader=Downloader(self.ui_updater.get_yt(),
                                   self.ctx,
                                   self.ui_updater.get_current_stream(),
                                   os.path.dirname(self.ui_updater.get_video_path()))

        '''Connect Custom Signal of Download Class to Ui Updater Slots(function)'''
        self.downloader.signals.progress.connect(self.ui_updater.update_progress)
        self.downloader.signals.status_bar_message.connect(self.ui_updater.update_status_bar)
        self.downloader.signals.error_dailog.connect(self.ui_updater.show_error)

        #Update Log
        logging.info("Download Video for the Stream : \n" + str(self.ui_updater.get_current_stream()))

        '''Start the Threadpool of Download to Start the Download'''
        self.threadpool_download.start(self.downloader)

        # Update Log
        logging.info("Downloaded Video for the Stream : \n" +  str(self.ui_updater.get_current_stream()))


if __name__ == "__main__":

    '''
        YouDer is free Youtube Video Downloader 
    '''
    appctxt = AppContext()
    exit_code = appctxt.run()
    sys.exit(exit_code)