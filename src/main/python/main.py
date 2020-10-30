from fbs_runtime.application_context.PySide2 import ApplicationContext, cached_property

from PySide2.QtCore import QThreadPool,QFile
from PySide2.QtGui import QImage
import sys ,os
from PySide2.QtWidgets import  QApplication,QMainWindow
from main_ui import Ui_MainWindow
from ui_function import UI_Functions
from ui_upadter import Ui_updater
from Workers import GetInfo,Downloader

class AppContext(ApplicationContext):
    def run(self):
        self.main_window.show()
        return self.app.exec_()
    @cached_property
    def main_window(self):
        return YouDer(self)
    @cached_property
    def dark(self):
        return (self.get_resource('resources/dark.css'))
    @cached_property
    def white(self):
        return (self.get_resource('resources/white.css'))
    @cached_property
    def thumbnail(self):
        return (self.get_resource('resources/thumbnail.png'))

class YouDer(QMainWindow):

    def __init__(self,ctx):

        super(YouDer, self).__init__()
        self.ctx = ctx
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

        '''Create a Instance for UI Functions and Updater'''
        self.ui_function = UI_Functions(self,self.ui,self.ctx)
        self.ui_updater = Ui_updater(self.ui,os.path.join(os.path.join(os.environ['USERPROFILE']), 'Videos'),self.ctx)

        #Set Defualt Download Location





        #Signal and Slots Which are Related to Ui Functions
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

        #Hide Unnessary content.. at Startup....

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

        # Done
        #Default values for some widgets

        self.ui_updater.update_status_bar("Ready...")
        self.ui.link_linedit.setPlaceholderText('Paste link')
        self.ui.link_linedit.setClearButtonEnabled(True)
        self.ui.combobox.clear()


        #Connect Signal to slots for paste , getinfo ,toolbutton and download button

        self.ui.button_paste.clicked.connect(self.ui_updater.paste_into_linedit)
        self.ui.button_getinfo.clicked.connect(self.goto_getinfo)
        self.ui.download_button.clicked.connect(self.download)
        self.ui.toolButton.clicked.connect(self.ui_updater.get_video_directory)

        #Threads for GetINfo and Download...

        self.threadpool_getinfo = QThreadPool()
        self.threadpool_download = QThreadPool()




    def goto_getinfo(self):
        self.link=self.ui.link_linedit.text()
        if self.link == "":
            self.ui_updater.show_error("Link is empty","It looks like is Empty")
            return

        self.ui_updater.getinfo_started(True)
        self.ui_updater.update_status_bar("Featching Data from YouTube . . .")
        self.getinfo = GetInfo(self.link,self.ctx)

        #Connect Custom Signal to Slots

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

        self.threadpool_getinfo.start(self.getinfo)

    def download(self):
        self.downloader=Downloader(self.ui_updater.get_yt(),
                                   self.ui_updater.get_current_stream(),
                                   os.path.dirname(self.ui_updater.get_video_path()))


        self.downloader.signals.progress.connect(self.ui_updater.update_progress)
        self.downloader.signals.status_bar_message.connect(self.ui_updater.update_status_bar)
        self.downloader.signals.error_dailog.connect(self.ui_updater.show_error)
        self.threadpool_download.start(self.downloader)


if __name__ == "__main__":
    appctxt = AppContext()
    exit_code = appctxt.run()
    sys.exit(exit_code)