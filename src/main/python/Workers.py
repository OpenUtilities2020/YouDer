from PySide2.QtCore import  QRunnable
from Signals import Communication
from pytube import YouTube
import requests
from datetime import timedelta
from helpers import millify,humanbytes
from time import time

class GetInfo(QRunnable):

    def __init__(self,link,ctx):

        super(GetInfo, self).__init__()
        self.signals = Communication()
        self.link=link
        self.ctx = ctx
    def run(self):



        try:
            self.yt = YouTube(self.link)
            self.signals.transmit_yt.emit(self.yt)
            self.title = self.yt.title
            self.author = self.yt.author
            self.length = self.yt.length
            self.thumbnail_url = self.yt.thumbnail_url
            self.views = self.yt.views

            self.signals.video_auther.emit(self.author)
            self.signals.video_title.emit(self.title)

            self.signals.video_views.emit(str(millify(self.views)))
            self.signals.video_length.emit(str(timedelta(seconds=self.length)))

            url = self.thumbnail_url
            r = requests.get(url, allow_redirects=True)

            open(self.ctx.thumbnail, 'wb').write(r.content)
            self.signals.thumbnail.emit(True)
        except:
            self.signals.error_dailog.emit("error", "Link is Broken or NetWork Error")
            self.signals.getinfo_finished.emit(True)
            return

        try:
            self.p720 = str
            self.p360 = str
            self.kbps128 = str
            self.kbps160 = str
            self.kbps50 = str
            self.kbps70 = str

            self.signals.status_bar_message.emit("Looking for Available Formats")
            self.signals.new_format.emit("Choose a Format", "Choose a format")
            self.stream720p = self.yt.streams.get_by_itag('22')
            self.stream360p = self.yt.streams.get_by_itag('18')
            self.stream128kbps = self.yt.streams.get_by_itag('140')
            self.stream160kbps = self.yt.streams.get_by_itag('251')
            self.stream50kbps = self.yt.streams.get_by_itag('249')
            self.stream70kbps = self.yt.streams.get_by_itag('250')

            if self.stream720p != None:
                size = self.stream720p.filesize
                video_size = humanbytes(size)

                self.p720 = '720p(Video)  - ' + video_size

                self.signals.new_format.emit(self.p720, self.stream720p)

            if self.stream360p != None:
                size = self.stream360p.filesize
                video_size = humanbytes(size)

                self.p360 = '360p(Video)  - ' + video_size

                self.signals.new_format.emit(self.p360, self.stream360p)

            if self.stream128kbps != None:
                size = self.stream128kbps.filesize
                video_size = humanbytes(size)

                self.kbps128 = '128kbps(Audio) - ' + video_size

                self.signals.new_format.emit(self.kbps128, self.stream128kbps)

            if self.stream160kbps != None:
                size = self.stream160kbps.filesize
                video_size = humanbytes(size)

                self.kbps160 = '160kbps(Audio) -  ' + video_size

                self.signals.new_format.emit(self.kbps160, self.stream160kbps)

            if self.stream50kbps != None:
                size = self.stream50kbps.filesize
                video_size = humanbytes(size)

                self.kbps50 = '50kbps(Audio) -  ' + video_size

                self.signals.new_format.emit(self.kbps50, self.stream50kbps)

            if self.stream70kbps != None:
                size = self.stream70kbps.filesize
                video_size = humanbytes(size)

                self.kbps70 = '70kbps(Audio) -  ' + video_size

                self.signals.new_format.emit(self.kbps70, self.stream70kbps)

        except:
            self.signals.status_bar_message.emit("Failed to get formats . . .")
            self.signals.error_dailog.emit("Error","Failed to get formats . . . Try Again")
            self.signals.getinfo_finished.emit(True)
            return


        self.signals.status_bar_message.emit("Ready to Download . . . ")

        self.signals.getinfo_finished.emit(True)
        self.signals.show_download_button.emit(True)

class Downloader(QRunnable):

    def __init__(self,yt,stream,video_path):
        super(Downloader, self).__init__()
        self.yt=yt
        self.stream=stream

        self.video_path=video_path
        self.signals = Communication()

    def run(self):
        try:
            self.size = self.stream.filesize
            self.total = humanbytes(self.size)
            self.yt.register_on_progress_callback(self.on_progress)
            self.yt.register_on_complete_callback(self.on_completes)
            self.timer = time()
            self.stream.download(self.video_path)
        except:
            self.signals.error_dailog.emit("Error","Error While Downloading... May NetWork Issue")
            return


    def on_progress(self,stream,chuck,bytes_remaining):
        now=time()
        self.bytes_downloaded=self.size - bytes_remaining
        if now>self.timer:
            difference = now - self.timer
            speed=humanbytes(self.bytes_downloaded / difference)
            progress = self.bytes_downloaded * 100 / self.size
            self.current= humanbytes(self.bytes_downloaded)
            self.signals.status_bar_message.emit("Downloading... "+ self.current+"/"+self.total+"     Speed: "+speed+"PS")
            self.signals.progress.emit(int(progress))

    def on_completes(self,stream,file_path):
        self.signals.status_bar_message.emit("Download Completed")




