from PySide2.QtCore import QObject,Signal


class Communication(QObject):
    '''
    This Contains Qt Custom Signal to Carry Data from GetInfo and Downloader Classes
    to Ui Updater Class
    '''

    status_bar_message = Signal(str)

    getinfo_finished = Signal (bool)

    error_dailog = Signal(str,str)

    video_title = Signal(str)

    video_auther = Signal(str)

    video_length = Signal(str)

    video_views = Signal(str)

    thumbnail = Signal(bool)

    new_format = Signal(str,object,bool)

    show_download_button = Signal(bool)

    transmit_yt = Signal(object)

    progress = Signal(int)