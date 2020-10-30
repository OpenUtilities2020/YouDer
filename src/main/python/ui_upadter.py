from PySide2.QtCore import Slot,Qt
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QMessageBox,QFileDialog
from os.path import join

class Ui_updater():

    def __init__(self,ui,download_location,ctx):
        self.ui=ui
        self.download_location=download_location
        self.ctx = ctx
        self.title=''
        self.streams=[]
    @Slot(str)
    def update_status_bar(self,text):
        self.ui.status_bar.setText(text)
    @Slot(str)
    def update_auther(self,auther):
        self.auther=auther

    @Slot(str)
    def  update_video_title(self,title):
        self.title=title
        self.video_path = join(self.download_location, str(self.title + ".mp4"))
        self.ui.title_label.setText(title+"\n\n\n By "+self.auther)
        self.ui.title_label.show()

    @Slot(str)
    def update_video_views(self,views):
        self.ui.views.setText(views)
        self.ui.views.show()
        self.ui.eye_icon_label.show()

    @Slot(str)
    def update_video_length(self,length):
        self.ui.length_label.setText(length)
        self.ui.video_length_icon_label.show()
        self.ui.length_label.show()

    @Slot(bool)
    def update_thumbnail(self,bool):
        if bool:
            pixmap = QPixmap(self.ctx.thumbnail)
            pixmap = pixmap.scaled(300, 200, Qt.KeepAspectRatio)
            self.ui.thubnail_label.setPixmap(pixmap)
            self.ui.thubnail_label.show()

    @Slot(str,object)
    def add_new_format(self,text,stream):
        self.streams.append(stream)
        self.ui.combobox.addItem(text)
        self.ui.combobox.show()

    @Slot(bool)
    def getinfo_started(self,bool):
        if bool:
            self.ui.button_getinfo.setDisabled(True)
            self.ui.progressbar.setMaximum(0)
            self.ui.progressbar.show()
            self.ui.combobox.clear()
            self.streams=[]

    @Slot(bool)
    def getinfo_finished(self,bool):
        if bool:
            self.ui.button_getinfo.setDisabled(False)
            self.ui.progressbar.setMaximum(100)
            self.ui.progressbar.hide()
            self.ui.status_bar.setText("Ready . . . ")

    @Slot(str,str)
    def show_error(self,title,message):
        dailog = QMessageBox()
        dailog.setText(message)
        dailog.setWindowTitle(title)
        dailog.setStandardButtons(QMessageBox.Ok)
        dailog.exec_()

    def paste_into_linedit(self):
        self.ui.link_linedit.clear()
        self.ui.link_linedit.paste()

    def show_download_button(self,bool):
        if bool:

            self.ui.save_as_linedit.setText(self.video_path)
            self.ui.save_as_linedit.show()
            self.ui.save_as_label.show()
            self.ui.download_button.show()
            self.ui.toolButton.show()
    def get_video_path(self):
        return self.video_path

    def get_video_directory(self):
        dailog = QFileDialog()
        self.path = dailog.getExistingDirectory()
        self.video_path = join(self.path, str(self.title+'.mp4'))
        self.ui.save_as_linedit.setText(self.video_path)

    def get_current_stream(self):
        if self.ui.combobox.currentIndex()!=0:
            return self.streams[self.ui.combobox.currentIndex()]
        else:
            self.show_error("Select a Format","Select a Video/Audio ")
    @Slot(object)
    def set_yt(self,object):
        self.yt=object

    def get_yt(self):
        return self.yt
    @Slot(int)
    def update_progress(self,value):
        self.ui.progressbar.setMaximum(100)
        self.ui.progressbar.setValue(value)
        self.ui.progressbar.show()