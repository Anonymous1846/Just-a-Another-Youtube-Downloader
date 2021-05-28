
from concurrent.futures import ThreadPoolExecutor
from win10toast import ToastNotifier
import threading
import pytube
import os
import re
import time

def timer(func):
    
    def wrapper(*args,**kwargs):
        start = time.time()
        return_val = func(*args,**kwargs)
        print(f'Download Completed In {round(time.time() - start)} seconds !')
        return return_val
    return wrapper

class Downloader():

    '''
    The Downloader class contains the methods for downloading both single and playlist videos
    The user has the option to choose from only audio/video/full hd etc when it comes to 
    downloading single videos, and in the case of playlists, the download is defaulted to 
    max resolution !
    '''

    def __init__(self):
        self.dic_for_video = {}
        print(f'Powered By : Pytube {pytube.__version__}\n')


    def download_single_video(self, VID_DIR:str, video_link:str):

        try:

            y = pytube.YouTube(video_link)          
            print(f"The Video you Searched For is {y.title} Author: {y.author}")
            counter = 1
            format_value = input('1)video\n2)audio')
            for i in y.streams.filter(type='video' if format_value == '1' else 'audio',file_extension='mp4'):
                
                list = str(i).split(" ")
                itag, type, quality, fps_bitrate, audio_video = re.findall(r'"([^"]*)"',
                                                                           str(list[1]) + str(list[2]) + str(
                                                                               list[3]) + str(
                                                                               list[4]) + str(list[6]))
                
                self.dic_for_video[counter] = itag
                print(f"{counter}) Type:{type} \tQuality: {quality} \tFPS/BitRate: {fps_bitrate} \tHas Both Video/Audio: {audio_video}")

                counter += 1
            id_number = input('Enter The Id Number of The Video To Download The Video !')
            start = time.time()
            y.streams.get_by_itag(self.dic_for_video.get(int(id_number))).download(VID_DIR)
            print(f'Video download complete in {round(time.time() - start,3)} secs !')
            notification=ToastNotifier()
            notification.show_toast(
                'YT Downloader v1.0',
                f'Download complete and the video is saved to {VID_DIR}',
                duration=5,
                icon_path='image_rescources\yt.ico'
            )

        except Exception as e:
            print(e)

        finally:
            print('Done....')

    def _download_playlist(self, VID_DIR, playlist_link):
        thread_pool_list=[]
        # Object of The Playlist Class
        initial = time.time()
        playlist =pytube.Playlist(playlist_link)
        print(f'Video Title: {playlist.title} Number of Videos: {len(playlist.video_urls)}')
        print(f'The Current Playlist Will be Saved in {playlist.title} Directory !')
         #If The Parent Directory of The Main Youtube Videos Exists then Create A Directory For Each Playlist By its Title !
        playlist_output_path=os.path.join(VID_DIR, playlist.title)
        for video in playlist:
            self.download_playlist_video(playlist_output_path, video)
        notification=ToastNotifier()
        notification.show_toast(
            'YT Downloader v1.0', f'{playlist.title} Download Complete !\nDownload Time :{time.time() - initial} seconds',
            duration=5,
            icon_path='C:\\Users\\USER\\Documents\\Workspace\\YTDownloader\\image_rescources\\yt.ico'
        )

    def download_playlist(self, VID_DIR, playlist_link):
        executer=ThreadPoolExecutor(max_workers=12)
        #submitting the function to the executer submit method,(The function arguements are Output path and the Playlist Link!)
        executer.submit(self._download_playlist,VID_DIR,playlist_link)
        


    def download_playlist_video(self, VID_DIR, video_url):
        video = pytube.YouTube(video_url)
        video.streams.filter(progressive=True).get_highest_resolution().download(VID_DIR)
        
