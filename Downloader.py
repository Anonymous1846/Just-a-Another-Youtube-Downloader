'''The Following Python file has a single class Downloader, which is has An __init__ method for initializing the
The List for Holding the Streams
download_single-video is for Downloading a Single video
Download_playlist_video is for downloading a Playlist, Iteratively !
For Single Video, download the All the Available Streams will be Shown and The
The File Extnsion will be of Mp4
Library for Downloading the Videos
There's an Issue with the Pytube Package, which has been resolved in the latest version as of now(10.1.0)
from concurrent.futures import ThreadPoolExecutor
Please Upgrade from 10.0.0 to 10.1.0'''
import pytube
import multiprocessing
#Create a new Directory For Playlists !
import os
# For Regular Expressions
import re
# Time Module Imported to display the Download Time !
import time
#For Creating a new Thread for the Download Playlist !
import threading
#For Showing the Notification for The Download Complete !
from win10toast import ToastNotifier

class Downloader():
    def __init__(self):
        #The Dictionary to Store the Youtube Stream's
        self.dic_for_video = {}
        #the ctr for notification Desktop !
        
        print(f'Using Pytube Version :{pytube.__version__}')


    def download_single_video(self, Output_Path, video_link):
        try:
            # Fetching the Video Using the Youtube Object From the link provided by the user !
            y = pytube.YouTube(video_link)
            # printing the author information and The Video Title !
            print(f"The Video you Searched For is {y.title} Author: {y.author}")
            # Counter needs to be assigned to the Video So that the User can choose the Video According to the Int Number !
            counter = 1
            format_value = input('1)video\n2)audio')
            for i in y.streams.filter(type='video' if format_value == '1' else 'audio',file_extension='mp4'):
                # used to show the Type and Quality which are seperated by Spaces
                list = str(i).split(" ")
                itag, type, quality, fps_bitrate, audio_video = re.findall(r'"([^"]*)"',
                                                                           str(list[1]) + str(list[2]) + str(
                                                                               list[3]) + str(
                                                                               list[4]) + str(list[6]))
                # The Integer is mapped to an unique iTag so that user can choose easily
                self.dic_for_video[counter] = itag
                print(
                    f"{counter}) Type:{type} \tQuality: {quality} \tFPS/BitRate: {fps_bitrate} \tHas Both Video/Audio: {audio_video}")

                # Incrementing the counter so that Shows A Sequence order !
                counter = counter + 1
            id_number = input('Enter The Id Number of The Video To Download The Video !')
            # out of the video streams the video selected by the user gets downloaded to the FINAL_PATH

            initial = time.time()
            y.streams.get_by_itag(self.dic_for_video.get(int(id_number))).download(Output_Path)
            print(f'File Saved to {Output_Path} Download Time :{time.time() - initial} seconds')
            notification=ToastNotifier()
            notification.show_toast(
                'YT Downloader v1.0',
                f'Download Completed in {time.time()-initial} seconds !',
                duration=5,
                icon_path='C:\\Users\\USER\\Documents\\Workspace\\YTDownloader\\image_rescources\\yt.ico'
            )
        # If Video/Audio Download Fails
        except Exception as e:
            print(f"Oops An Error Occured While Traversing the Link,Looks Like the Video URL is Corrupted !")
        finally:
            print('Done....')
#playlist Download,iteratively !
    def _download_playlist(self, Output_Path, playlist_link):
        thread_pool_list=[]
        # Object of The Playlist Class
        initial = time.time()
        playlist =pytube.Playlist(playlist_link)
        print(f'Video Title: {playlist.title} Number of Videos: {len(playlist.video_urls)}')
        print(f'The Current Playlist Will be Saved in {playlist.title} Directory !')
         #If The Parent Directory of The Main Youtube Videos Exists then Create A Directory For Each Playlist By its Title !
        playlist_output_path=os.path.join(Output_Path, playlist.title)
        for video in playlist:
            self.download_playlist_video(playlist_output_path, video)
        notification=ToastNotifier()
        notification.show_toast(
            'YT Downloader v1.0', f'{playlist.title} Download Complete !\nDownload Time :{time.time() - initial} seconds',
            duration=5,
            icon_path='C:\\Users\\USER\\Documents\\Workspace\\YTDownloader\\image_rescources\\yt.ico'
        )

    def download_playlist(self, Output_Path, playlist_link):
        executer=ThreadPoolExecutor(max_workers=12)
        #submitting the function to the executer submit method,(The function arguements are Output path and the Playlist Link!)
        executer.submit(self._download_playlist,Output_Path,playlist_link)


    def download_playlist_video(self, Output_Path, video_url):
        initial = time.time()
        video = pytube.YouTube(video_url)
        #The Video with Highest Resolution will be Dwnloaded !
        video.streams.filter(progressive=True).get_highest_resolution().download(Output_Path)
        #Will Show The Time Taken for Individual Video Download !
        print(f'{video.title} Downloaded in {time.time() - initial} seconds')
