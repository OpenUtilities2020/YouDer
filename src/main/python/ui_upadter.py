from PySide2.QtCore import Slot,Qt
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QMessageBox,QFileDialog
from os.path import join

class Ui_updater():
    '''
    This Class Ui Updater

    Updates the UI Component of YouDer

    Updates are given by Custom Signal of Class GetInfo and Downloader

    All Custom Signal of GetInfo and Downloader

            is connceted to this class functions
    '''

    def __init__(self,ui,download_location,ctx):
        """
        UI for Update UI Components

        Dowload_location to update when User Selects Custom Path

        ctx to get Thumbnail Path
        """
        self.ui=ui
        self.download_location=download_location
        self.ctx = ctx
        self.title=''
        self.streams=[]
    @Slot(str)
    def update_status_bar(self,text):
        ''' Set Given Text to Status Bar
                    ( A QLabel at bottom at center frame named Status Bar)
        '''
        self.ui.status_bar.setText(text)
    @Slot(str)
    def update_auther(self,auther):
        '''Store Video Channel name or Author in self.auther'''
        self.auther=auther

    @Slot(str)
    def  update_video_title(self,title):

        """

        Store Given Title into self.titile
        Set Video path as per Titile
        Update Title Label with title and auther name

        """

        self.title=title
        self.video_path = join(self.download_location, str(self.title + ".mp4"))
        self.ui.title_label.setText(title+"\n\n\n By "+self.auther)
        self.ui.title_label.show()

    @Slot(str)
    def update_video_views(self,views):
        '''Update Views '''
        self.ui.views.setText(views)
        self.ui.views.show()
        self.ui.eye_icon_label.show()

    @Slot(str)
    def update_video_length(self,length):
        '''Update Video Duration or Length'''
        self.ui.length_label.setText(length)
        self.ui.video_length_icon_label.show()
        self.ui.length_label.show()

    @Slot(bool)
    def update_thumbnail(self,bool):
        """
        If GetInfo Downloads Thumbnail of Video passes True
        Set Pixmap > the thumbnail to Thumbnail label
        """
        if bool:
            pixmap = QPixmap(self.ctx.thumbnail)
            pixmap = pixmap.scaled(300, 200, Qt.KeepAspectRatio)
            self.ui.thubnail_label.setPixmap(pixmap)
            self.ui.thubnail_label.show()

    @Slot(str,object,bool)
    def add_new_format(self,text,stream,progressive):
        '''

        GetInfo emits the Signal with

            1 Text of Stream (With the Size)
            2 Available stream
            3 If Stream is Progressive passes Truw



        '''
        #Add stream to a list
        self.streams.append([stream,progressive])
        #Add Stream to Combo Box
        self.ui.combobox.addItem(text)

        self.ui.combobox.show()

    @Slot(bool)
    def getinfo_started(self,bool):
        """
        If Get info is Started
        Set Getinfo buttom as Disabled
        Show progress bar with unknown progression
        """
        if bool:
            self.ui.button_getinfo.setDisabled(True)
            self.ui.progressbar.setMaximum(0)
            self.ui.progressbar.show()
            self.ui.combobox.clear()
            self.streams=[]

    @Slot(bool)
    def getinfo_finished(self,bool):
        """
        If GetInfo is Finished
        set GetInfo Buttom as Enabled
        hide progress Bar
        """
        if bool:
            self.ui.button_getinfo.setDisabled(False)
            self.ui.progressbar.setMaximum(100)
            self.ui.progressbar.hide()
            self.ui.status_bar.setText("Ready . . . ")

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

            self.ui.save_as_linedit.setText(self.video_path)
            self.ui.save_as_linedit.show()
            self.ui.save_as_label.show()
            self.ui.download_button.show()
            self.ui.toolButton.show()
    def get_video_path(self):
        """
        Returns: Video Path (self.video_path)
        """

        return self.video_path

    def get_video_directory(self):

        """
        To get Custom Video Download location assigned by User
            using QFile Dialog()
        """

        dailog = QFileDialog()
        self.path = dailog.getExistingDirectory()

        if self.path =='':
            #If path is none return
            return

        #Store User Choosed Cutom Video Location to Video Path
        self.video_path = join(self.path, str(self.title+'.mp4'))

        self.ui.save_as_linedit.setText(self.video_path)

    def get_current_stream(self):
        """
        Return : User Choose Stream to Download
        """
        if self.ui.combobox.currentIndex()!=0:
            return self.streams[self.ui.combobox.currentIndex()]
        else:
            self.show_error("Select a Format","Select a Video/Audio Resolution ")

    @Slot(object)
    def set_yt(self,object):
        self.yt=object

    def get_yt(self):
        return self.yt
    @Slot(int)
    def update_progress(self,value):

        """
        Update Progress Bar as per integer of Value
        """
        if value>0:
            self.ui.progressbar.setMaximum(100)
            self.ui.progressbar.setValue(value)

        else:
            # Value is not positive > Set Progress is infinitive
            self.ui.progressbar.setMinimum(0)
            self.ui.progressbar.setMaximum(0)
            self.ui.progressbar.show()