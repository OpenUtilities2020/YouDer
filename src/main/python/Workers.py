from PySide2.QtCore import  QRunnable
from Signals import Communication
from pytube import YouTube
import requests
from datetime import timedelta
from helpers import millify,humanbytes
from time import time
import  logging
import os
import subprocess
class GetInfo(QRunnable):
    '''This class is to get Video Information from YouTube Through Pytube API'''

    def __init__(self,link,ctx):
        """
        link: Video LInk
        ctx : instace of Application Context to Update Thumbnail
        """
        super(GetInfo, self).__init__()
        self.signals = Communication()
        self.link=link
        self.ctx = ctx

        #Enable Logging ...
        logging.basicConfig(filename=self.ctx.log,
                            format='%(process)d-%(levelname)s-%(message)s',
                            level=logging.INFO
                            )
    def run(self):

        '''
        Fetches Video related data from YouTube
        Passed INformation to UI Update to Custom Signals
        '''


        try:
            '''
            Getting Video Information Except Video Formats
            '''
            # Creating YouTube Object for Given Video Link
            self.yt = YouTube(self.link)
            #Pass Yt to UI Updater
            self.signals.transmit_yt.emit(self.yt)

            try:
                self.title = self.yt.title # To Get Video Title
                self.author = self.yt.author # To Get Video Author
                self.length = self.yt.length # To Get Video length/Duration
                self.views = self.yt.views # To Get Video Views
                self.thumbnail_url = self.yt.thumbnail_url # To Get Video Thumbnail url
            except Exception as e:
                # If Exception
                logging.exception("Error at PreFetching ... for video link : \n"+self.link)

                #Show a Error Dialog Box
                self.signals.error_dailog.emit("Error", "Error at PreFetching Video Information")
                #Return
                self.signals.getinfo_finished.emit(True)
                return

            #Write Thumbnail to Disk
            try:
                url = self.thumbnail_url
                r = requests.get(url, allow_redirects=True)

                open(self.ctx.thumbnail, 'wb').write(r.content)
            except Exception as e:
                logging.exception("Error at writing thumbnail to disk ... for video link: "+self.link)
                # Show a Error Dialog Box
                self.signals.error_dailog.emit("Error", "Unable to Write Thumbnail")
                # Return
                self.signals.getinfo_finished.emit(True)
                return

            #Emit Custom Signal to Slot with Video Information
            self.signals.thumbnail.emit(True)
            self.signals.video_auther.emit(self.author)
            self.signals.video_title.emit(self.title)
            self.signals.video_views.emit(str(millify(self.views)))
            self.signals.video_length.emit(str(timedelta(seconds=self.length)))



        except Exception as e:
            logging.exception("Error for Video link:"+self.link)
            self.signals.error_dailog.emit("error", "Link is Broken or NetWork Error")
            #Return
            self.signals.getinfo_finished.emit(True)
            return


        try:
            """
            Getting Availble Video Formats
            """
            #Update Status Bar
            self.signals.status_bar_message.emit("Looking for Available Formats")

            # Emit Default Format
            self.signals.new_format.emit("Choose a Format", "Choose a format",True)

            try:
                """
                Getting Formats from 144 p to 4k 60 fps HDR by their ITags
                """
                # Streams for 144 p
                self.stream144p_mp4 = self.yt.streams.get_by_itag(160)
                self.stream144p_webm = self.yt.streams.get_by_itag(160)

                #Streams for 240 p
                self.stream240p_mp4 = self.yt.streams.get_by_itag(133)
                self.stream240p_webm = self.yt.streams.get_by_itag(242)

                #Streams for 360p
                self.stream360p_prog = self.yt.streams.get_by_itag('18')
                self.stream360p_mp4 = self.yt.streams.get_by_itag(134)
                self.stream360p_webm = self.yt.streams.get_by_itag(243)

                #Streams for 480p
                self.stream480p_mp4 = self.yt.streams.get_by_itag(135)
                self.stream480p_webm = self.yt.streams.get_by_itag(244)

                #Streams for 720p
                self.stream720p_prog = self.yt.streams.get_by_itag('22')
                # 30 fps streams ....
                self.stream720p_mp4_30fps = self.yt.streams.get_by_itag(136)
                self.stream720p_webm_30fps = self.yt.streams.get_by_itag(247)
                # 60 fps streams .....
                self.stream720p_mp4_60fps = self.yt.streams.get_by_itag(298)
                self.stream720p_webm_60fps = self.yt.streams.get_by_itag(302)

                # Streams for 1080p
                # 30 fps streams .  .  .
                self.stream1080p_mp4_30fps = self.yt.streams.get_by_itag(137)
                self.stream1080p_webm_30fps = self.yt.streams.get_by_itag(247)
                # 60 fps streams .....
                self.stream1080p_mp4_60fps = self.yt.streams.get_by_itag(299)
                self.stream1080p_webm_60fps = self.yt.streams.get_by_itag(303)
                self.stream1080p_webm_60fps_hdr = self.yt.streams.get_by_itag(335)

                # Streams for 2K ....
                # 30 fps streams ...
                self.stream2k_mp4_30fps = self.yt.streams.get_by_itag(264)
                self.stream2k_webm_30fps = self.yt.streams.get_by_itag(271)
                # 60 fps streams ...
                self.stream2k_webm_60fps = self.yt.streams.get_by_itag(308)
                self.stream2k_webm_60fps_hdr = self.yt.streams.get_by_itag(336)

                # Streams for 4k ....
                # 30 fps streams ...
                self.stream4k_webm_30fps = self.yt.streams.get_by_itag(272)
                self.stream4k_webm_60fps = self.yt.streams.get_by_itag(315)
                self.stream4k_webm_60fps_hdr = self.yt.streams.get_by_itag(337)



                ''' ._._. Audio Streams ._._. '''

                self.stream128kbps = self.yt.streams.get_by_itag('140')
                self.stream160kbps = self.yt.streams.get_by_itag('251')
                self.stream50kbps = self.yt.streams.get_by_itag('249')
                self.stream70kbps = self.yt.streams.get_by_itag('250')

            except Exception as e:
                logging.exception("Error at PreFetching streams ... for link: "+self.link)
                self.signals.status_bar_message.emit("Failed to get formats . . .")
                self.signals.error_dailog.emit("Error", "Failed to get formats . . . Try Again")
                self.signals.getinfo_finished.emit(True)
                return

            """
            Filtering Not Available Formats and Emiting to UI Updater
            """
            '''   .... 4K Streams .... '''

            try:
                if self.stream4k_webm_30fps != None:
                    video_size = humanbytes(self.stream4k_webm_30fps.filesize + self.stream128kbps.filesize)
                    vid_info = '4K 30fps(Video)  - ' + video_size

                    self.signals.new_format.emit(vid_info, self.stream4k_webm_30fps, False)
            except Exception as e:
                logging.exception("Error at 4K Stream ...")


            try:
                if self.stream4k_webm_60fps != None:
                    video_size = humanbytes(self.stream4k_webm_60fps.filesize + self.stream128kbps.filesize)
                    vid_info = '4K 60fps(Video)  - ' + video_size

                    self.signals.new_format.emit(vid_info, self.stream4k_webm_60fps, False)
            except Exception as e:
                logging.exception("Error at 4K Stream ...")
            try:
                if self.stream4k_webm_60fps != None:
                    video_size = humanbytes(self.stream4k_webm_60fps.filesize + self.stream128kbps.filesize)
                    vid_info = '4K 60fps(Video)  - ' + video_size

                    self.signals.new_format.emit(vid_info, self.stream4k_webm_60fps, False)
            except Exception as e:
                logging.exception("Error at 4K Stream ...")
            try:
                if self.stream4k_webm_60fps_hdr != None:
                    video_size = humanbytes(self.stream4k_webm_60fps_hdr.filesize + self.stream128kbps.filesize)
                    vid_info = '4K 30fps(Video)  - ' + video_size

                    self.signals.new_format.emit(vid_info, self.stream4k_webm_60fps_hdr, False)
            except Exception as e:
                logging.exception("Error at 4K Stream ...")







            ''' 2 K Streams'''

            try:
                if self.stream2k_mp4_30fps != None:
                    video_size = humanbytes(self.stream2k_mp4_30fps.filesize + self.stream128kbps.filesize)
                    vid_info = '2K 30fps(Video)  - ' + video_size

                    self.signals.new_format.emit(vid_info, self.self.stream2k_mp4_30fps, False)
            except Exception as e:
                logging.exception("Error at 2K Stream ...")
            try:
                if self.stream2k_mp4_30fps == None and self.stream2k_webm_30fps != None:
                    video_size = humanbytes(self.stream2k_webm_30fps.filesize + self.stream128kbps.filesize)
                    vid_info = '2K 30fps(Video/Webm)  - ' + video_size

                    self.signals.new_format.emit(vid_info, self.stream2k_webm_30fps, False)
            except Exception as e:
                logging.exception("Error at 2K Stream ...")
            try:
                if self.stream2k_webm_60fps != None:
                    video_size = humanbytes(self.stream2k_webm_60fps.filesize + self.stream128kbps.filesize)
                    vid_info = '2K 60fps(Video)  - ' + video_size

                    self.signals.new_format.emit(vid_info, self.stream2k_webm_60fps, False)
            except Exception as e:
                logging.exception("Error at 2K Stream ...")
            try:
                if self.stream2k_webm_60fps_hdr != None:
                    video_size = humanbytes(self.stream2k_webm_60fps_hdr.filesize + self.stream128kbps.filesize)
                    vid_info = '2K 60fps HDR(Video)  - ' + video_size

                    self.signals.new_format.emit(vid_info, self.stream2k_webm_60fps_hdr, False)
            except Exception as e:
                logging.exception("Error at 2K Stream ...")







            ''' 1080p Streams'''
            try:
                if self.stream1080p_mp4_30fps != None:
                    video_size = humanbytes(self.stream1080p_mp4_30fps.filesize + self.stream128kbps.filesize)
                    vid_info = '1080p 30fps (Video)  - ' + video_size

                    self.signals.new_format.emit(vid_info, self.stream1080p_mp4_30fps, False)
            except Exception as e:
                logging.exception("Error at 1080p Stream ...")
            try:
                if self.stream1080p_mp4_30fps == None and self.stream1080p_webm_30fps != None:
                    vid_info = '1080p 30fps (Video) - ' + \
                               humanbytes(self.stream1080p_webm_30fps.filesize + self.stream128kbps.filesize)

                    self.signals.new_format.emit(vid_info, self.stream1080p_webm_30fps, False)
            except Exception as e:
                logging.exception("Error at 1080p Stream ...")
            try:

                if self.stream1080p_webm_60fps != None:
                    vid_info = '1080p 60fps (Video) - ' + \
                               humanbytes(self.stream1080p_webm_60fps.filesize + self.stream128kbps.filesize)

                    self.signals.new_format.emit(vid_info, self.stream1080p_webm_60fps, False)
            except Exception as e:
                logging.exception("Error at 1080p Stream ...")





            try:
                if self.stream1080p_webm_60fps_hdr != None:
                    vid_info = '1080p 60fps HDR(Video) - ' + \
                               humanbytes(self.stream1080p_webm_60fps_hdr.filesize + self.stream128kbps.filesize)

                    self.signals.new_format.emit(vid_info, self.stream1080p_webm_60fps_hdr, False)

            except Exception as e:
                logging.exception("Error at 1080p Stream ...")


            ''' 720 P Streams '''
            try:
                if self.stream720p_prog != None:
                    vid_info = '720p 30fps (Video) - ' + \
                               humanbytes(self.stream720p_prog.filesize)

                    self.signals.new_format.emit(vid_info, self.stream720p_prog, True)

            except Exception as e:
                logging.exception("Error at 720p Stream ...")
            try:
                if self.stream720p_mp4_30fps != None and self.stream720p_prog == None:
                    vid_info = '720p 30fps (Video) - ' + \
                               humanbytes(self.stream720p_mp4_30fps.filesize + self.stream128kbps.filesize)

                    self.signals.new_format.emit(vid_info, self.stream720p_mp4_30fps, False)

            except Exception as e:
                logging.exception("Error at 720p Stream ...")
            try:
                if self.stream720p_webm_60fps != None:
                    vid_info = '720p 60fps (Video) - ' + \
                               humanbytes(self.stream720p_webm_60fps.filesize + self.stream128kbps.filesize)

                    self.signals.new_format.emit(vid_info, self.stream720p_webm_60fps, False)

            except Exception as e:
                logging.exception("Error at 720p Stream ...")











            ''' 480 P Streams '''
            try:
                if self.stream480p_mp4 != None:
                    video_size = humanbytes(self.stream480p_mp4.filesize + self.stream128kbps.filesize)
                    vid_info = '480p (Video)  - ' + video_size

                    self.signals.new_format.emit(vid_info, self.stream480p_mp4, False)
            except Exception as e:
                logging.exception("Error at 480p Stream ...")
            try:
                if self.stream480p_mp4 == None and self.stream480p_webm != None:
                    vid_info = '480p (Video) - ' + \
                               humanbytes(self.stream480p_webm.filesize + self.stream128kbps.filesize)

                    self.signals.new_format.emit(vid_info, self.stream480p_webm, False)

            except Exception as e:
                logging.exception("Error at 480p Stream ...")








            ''' 360 P Streams '''
            try:
                if self.stream360p_prog != None:
                    vid_info = '360p (Video) - ' + \
                               humanbytes(self.stream360p_prog.filesize)

                    self.signals.new_format.emit(vid_info, self.stream360p_prog, True)

            except Exception as e:
                logging.exception("Error at 360p Stream ...")
            try:
                if self.stream360p_mp4 != None and self.stream360p_prog == None:
                    vid_info = '360p (Video) - ' + \
                               humanbytes(self.stream360p_mp4.filesize + self.stream128kbps.filesize)

                    self.signals.new_format.emit(vid_info, self.stream360p_mp4, False)


            except Exception as e:
                logging.exception("Error at 360p Stream ...")










            ''' 240 P Streams '''
            try:
                if self.stream240p_mp4 != None:
                    video_size = humanbytes(self.stream240p_mp4.filesize + self.stream128kbps.filesize)
                    vid_info = '240p (Video)  - ' + video_size

                    self.signals.new_format.emit(vid_info, self.stream240p_mp4, False)
            except Exception as e:
                logging.exception("Error at 240p Stream ...")
            try:
                if self.stream240p_mp4 == None and self.stream240p_webm != None:
                    vid_info = '240p (Video) - ' + \
                               humanbytes(self.stream240p_webm.filesize + self.stream128kbps.filesize)

                    self.signals.new_format.emit(vid_info, self.stream240p_webm, False)

            except Exception as e:
                logging.exception("Error at 240p Stream ...")







            ''' 144 P Streams '''
            try:
                if self.stream144p_mp4 != None:
                    video_size = humanbytes(self.stream144p_mp4.filesize + self.stream128kbps.filesize)
                    vid_info = '144p (Video)  - ' + video_size

                    self.signals.new_format.emit(vid_info, self.stream144p_mp4, False)

            except Exception as e:
                logging.exception("Error at 144p Stream ...")
            try:
                if self.stream144p_mp4 == None and self.stream144p_webm != None:
                    vid_info = '144p (Video) - ' + \
                               humanbytes(self.stream144p_webm.filesize + self.stream128kbps.filesize)

                    self.signals.new_format.emit(vid_info, self.stream144p_webm, False)

            except Exception as e:
                logging.exception("Error at 144p Stream ...")






            '''   Audio Streams '''
            try:
                if self.stream128kbps != None:
                    vid_info = '128kbps (Audio) - ' + \
                               humanbytes(self.stream128kbps.filesize)

                    self.signals.new_format.emit(vid_info, self.stream128kbps, True)

            except Exception as e:
                logging.exception("Error at 128kbps Stream ...")
            try:
                if self.stream50kbps != None:
                    vid_info = '50kbps (Audio) - ' + \
                               humanbytes(self.stream50kbps.filesize)

                    self.signals.new_format.emit(vid_info, self.stream50kbps, True)

            except Exception as e:
                logging.exception("Error at 50kbps Stream ...")

            try:
                if self.stream70kbps != None:
                    vid_info = '70kbps (Audio) - ' + \
                               humanbytes(self.stream70kbps.filesize)

                    self.signals.new_format.emit(vid_info, self.stream70kbps, True)

            except Exception as e:
                logging.exception("Error at 70kbps Stream ...")
            try:
                if self.stream160kbps != None:
                    vid_info = '160kbps (Audio) - ' + \
                               humanbytes(self.stream160kbps.filesize)

                    self.signals.new_format.emit(vid_info, self.stream160kbps, True)

            except Exception as e:
                logging.exception("Error at 160kbps Stream ...")










        except Exception as e:
            logging.exception("Error at Streams emiting  ... for link:"+self.link)
            self.signals.status_bar_message.emit("Failed to get formats . . .")
            self.signals.error_dailog.emit("Error", "Failed to get formats . . . Try Again")
            self.signals.getinfo_finished.emit(True)
            return



        #All Work of Get INfo Class is Finished emiting success signals
        self.signals.status_bar_message.emit("Ready to Download . . . ")
        self.signals.getinfo_finished.emit(True)
        self.signals.show_download_button.emit(True)







class Downloader(QRunnable):
    '''
    This Class for Download Video For Selected Streams
    '''
    def __init__(self,yt,ctx,stream,video_path):

        '''
        yt: instace of YouTube for given link
            Used for 128 kbps stream in non progressive downloads

        ctx: Instace of Application Conetext
            To get ffmpeg path

        Stream [list] : User Selected Stream to Download

        Video Path: Location of video to download

        '''
        super(Downloader, self).__init__()
        self.signals = Communication()
        self.yt=yt
        self.ctx=ctx
        self.stream=stream[0]
        self.progressive=stream[1]
        self.stream128kbps = self.yt.streams.get_by_itag('140')
        self.video_path=video_path

        # Enable Logging ...
        logging.basicConfig(filename=self.ctx.log,
                            format='%(process)d-%(levelname)s-%(message)s',
                            level=logging.INFO
                            )



    def run(self):
        #Register Call Back Function to YT
        self.yt.register_on_progress_callback(self.on_progress)
        self.yt.register_on_complete_callback(self.on_completes)


        if self.progressive:
            # If Selected Stream is Progressive
            try:

                self.size = self.stream.filesize
                self.total = humanbytes(self.size)# Size of Stream

                self.timer = time() #Start The Timer

                #Download the Video by selected Stream

                self.stream.download(self.video_path)
            except:
                logging.exception("Error while Downloading  stream" + str(self.stream))
                self.signals.error_dailog.emit("error", "Error While Downloading _ May be NetWork Lost")
                # Return
                return

        else:
            # If Selected stream is non Progressive
            self.total=self.stream.filesize+self.stream128kbps.filesize
            try:
                self.size = self.stream.filesize
                self.total = humanbytes(self.size) #Size of Stream
                self.timer = time() # Get Time of Now
                #Download Video Source
                self.full_video_path=self.stream.download(self.video_path)
                self.timer = time()  # Get Time of Now
                #Download Audio Source
                self.full_audio_path=self.stream128kbps.download(output_path=self.video_path,filename="audio")

            except Exception as e:
                logging.exception("Error while Downloading  stream" + str(self.stream))
                self.signals.error_dailog.emit("error", "Error While Downloading _ May be NetWork Lost")
                # Return
                return


            '''Merging Both Video and Audio Sources
                Tiny/Small version of ffmpeg taken from 
                                                        https://github.com/n00mkrad/smol-ffmpeg/'''
            #Update Status Bar
            self.signals.status_bar_message.emit("Merging streams . . .")

            #Command to Merge Video and Audio Using ffmpeg

            self.ffmpeg_command = self.ctx.ffmpeg\
                                  + ' -y -i "' + self.full_video_path\
                                  + '" -i "' + self.full_audio_path\
                                  +'" -map 0:v -map 1:a -c:v copy -shortest "'\
                                  + self.full_video_path[:-4] +'_merged.mp4"'


            #Run ffmpeg command in a Terminal through subprocess
            CREATE_NO_WINDOW = 0x08000000
            process = subprocess.Popen(self.ffmpeg_command, stdout=subprocess.PIPE,
                                       stderr=subprocess.STDOUT,
                                       universal_newlines=True,creationflags=CREATE_NO_WINDOW)
            
            # Get Progress of Merging though ffmpeg output
            for line in process.stdout:
                try:
                    size = int(line.split()[5][:-2])*1024 #Merged Video Size
                    progress = int(size * 100 / (self.stream.filesize+self.stream128kbps.filesize)) #Progression
                    #Emiting the progress to Progress Bar
                    self.signals.progress.emit(progress)
                except:
                    pass
                try:
                    line9 = line.split()[9]
                    line10 = line.split()[10]
                    # Emiting the signal to status Bar
                    self.signals.status_bar_message.emit("Merging Streams with " + str(line9) + str(line10))
                except:
                    pass





            # Delete Audio and Video Files....

            try:
                os.remove(self.full_video_path)
                os.remove(self.full_audio_path)
            except Exception as e:
                logging.exception("Error while Clearing Temp  for Video " + str(self.stream))
                self.signals.error_dailog.emit("Error", "Error While Deleting temp... Clear it manually ")
                return



            #Completed Downloading and Merging
            self.signals.status_bar_message.emit("Download Completed")
            self.signals.progress.emit(100)










    def on_progress(self,stream,chuck,bytes_remaining):

        now=time()#Time of Now

        self.bytes_downloaded=self.size - bytes_remaining

        if now>self.timer:

            difference = now - self.timer
            speed=humanbytes(self.bytes_downloaded / difference)

            progress = self.bytes_downloaded * 100 / stream.filesize
            self.current= humanbytes(self.bytes_downloaded)
            self.signals.status_bar_message.emit("Downloading... "+ self.current+"/"+self.total+"     Speed: "+speed+"PS")
            self.signals.progress.emit(int(progress))

    def on_completes(self,stream,file_path):
        self.signals.status_bar_message.emit("Download Completed")




