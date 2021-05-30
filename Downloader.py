# from win10toast import ToastNotifier
from notifypy import Notify 
import threading
import pytube
import time
import os
import re


thread_lock = threading.Lock() # thread lock initiated so that the other threads cannot access it !

'''
The timer function is actaully a decorator used to used calculate the time taken to download 
the video/playlist. It is used along with playlist and single video download(playlist).
'''

def timer(func):
    
    def wrapper(*args,**kwargs):
        start = time.time()
        return_val = func(*args,**kwargs)
        print(f'Download Completed In {round(time.time() - start)} seconds !')
        return return_val
    return wrapper

'''
    A simple fucntion to send notification after downloading a video/playlist 

    return: None

    params: msg(str)
'''
def notify(msg:str):
    notification = Notify()
    notification.title = "YT Downloader v1.1"
    notification.message = msg                  #custom msg for playlists and video !
    notification.icon = 'media_resources\\yt.ico'
    notification.audio = 'media_resources\\notification_sound.wav'
    notification.send()


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

    '''
        The below function is used for downloading a single video from youtube,
        the checks are made for empty links and then the video is saved as the 
        same name as the title itself in the Youtube Videos Download folder.

        \Downloads
            |
            |
            \Youtube Videos(Created by the script)
                |
                |
                ----Currently Downloaded Video.pm4
        
        params: video_directory and the video link

        return: None
    '''

    def download_single_video(self, VID_DIR:str, video_link:str):

        try:

            y = pytube.YouTube(video_link)          
            print(f"The Video you Searched For is {y.title} Author: {y.author}")
            counter = 1
            format_value = input('1)video\n2)audio\n>>')
            for i in y.streams.filter(type='video' if format_value == '1' else 'audio',file_extension='mp4'):
                
                list = str(i).split(" ")
                itag, type, quality, fps_bitrate, audio_video = re.findall(r'"([^"]*)"',str(list[1]) + str(list[2]) + str(list[3]) + str(list[4]) + str(list[6]))
                self.dic_for_video[counter] = itag
                print(f"{counter}) Type:{type} \tQuality: {quality} \tFPS/BitRate: {fps_bitrate} \tHas Both Video/Audio: {audio_video}")

                counter += 1
            id_number = input('Enter the ID mumber of The video to download the video >> ')
            start = time.time()
            print('Starting download....')
            y.streams.get_by_itag(self.dic_for_video.get(int(id_number))).download(VID_DIR)
            print(f'Video download complete in {round(time.time() - start,3)} secs !')
            notify(f'Download complete and the video is saved to {VID_DIR}')

        except Exception as e:
            print(e)

        finally:
            print('Done....\n')

    '''
    The playlist downloader downloads all the playslist videos from the playlist,
    into a folder which is created after the name of the playlist itself.
    /Downloads
        |
        |
        /Youtube Videos
            |
            |
            /<Playlist Name>(created by the script)
                |
                Videos(corresponding playlist videos)

    params: directory_path, and the playlist link
    '''
    @timer
    def download_playlist(self, VID_DIR:str, playlist_link:str):

        thread_pool_list=[]
        playlist =pytube.Playlist(playlist_link)
        print(f'Playlist Title: {playlist.title} Number of Videos: {len(playlist.video_urls)}')
        PLAYLIST_DIR = playlist.title                               #the playlist title will be the playlist videos folder
        PLAYLIST_DIR = re.sub('\\ /', ' or ', PLAYLIST_DIR)         # remove the / or / and replace with or 
        PLAYLIST_VIDS_DIR = os.path.join(VID_DIR,PLAYLIST_DIR)      # join path
        
        if not os.path.isdir(PLAYLIST_VIDS_DIR):                    # create a new folder if not exists
            os.mkdir(PLAYLIST_VIDS_DIR)
            print(PLAYLIST_VIDS_DIR)
        print(f'The Current Playlist Will be Saved in {PLAYLIST_VIDS_DIR} Directory !')
        print('Playlist download started')
        try:    
            for video in playlist:
                thread  = threading.Thread(target=self.download_single_playlist_video,args=(PLAYLIST_VIDS_DIR, video))
                thread.daemon = True
                thread_pool_list.append(thread)
                
                thread.start()
            
            for thread in thread_pool_list:
                thread.join()

            notify(f'{playlist.title} Download Complete !\n',)
            print(PLAYLIST_DIR,end=' ')

        except Exception as e:
            print(e)
        
    '''
    The function downloads the max resolution video(with audio) from the playist.

    params: Playlist dir and the playlist video link
    '''
    @timer
    def download_single_playlist_video(self, VID_DIR, video_url):
        try:
            thread_lock.acquire()   #thread lock acqured !
            video = pytube.YouTube(video_url)
            video.streams.filter(progressive=True).get_highest_resolution().download(r'{}'.format(VID_DIR))
            print(video.title,end=' ')
            thread_lock.release()   #thread lock released !
        except Exception as e:
            print(e)