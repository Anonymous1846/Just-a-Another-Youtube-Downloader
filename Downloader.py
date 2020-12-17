# The Python file has two functions namely for downloading the Single Video and For Downloading the Playlist
# The functions defined in this module will be called there !
# Library for Downloading the Videos
import pytube
#Create a new Directory For Playlists !
import os
# For Regular Expressions
import re
# Time Module Imported to display the Download Time !
import time
import threading


class Downloader():
    def __init__(self):
        #The Dictionary to Store the Youtube Stream's
        self.dic_for_video = {}

    def download_single_video(self, Output_Path, video_link):
        try:
            # Fetching the Video Using the Youtube Object From the link provided by the user !
            y = pytube.YouTube(video_link)
            # printing the author information and The Video Title !
            print(f"The Video you Searched For is f{y.title} Author: {y.author}")
            # Counter needs to be assigned to the Video So that the User can choose the Video According to the Int Number !
            counter = 1
            format_value = input('1)video\n2)audio')
            for i in y.streams.filter(type='video' if format_value == '1' else 'audio'):
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
        # If Video/Audio Download Fails
        except Exception as e:
            print(f"Oops An Error Occured While Traversing the Link,Looks Like the Video URL is Corrupted !")
        finally:
            print('Done....')

    def download_playlist(self, Output_Path, playlist_link):
        FINAL_DIRECTORY = 'C:/Users/USER/Downloads/Youtube Videos'
        # Object of The Playlist Class
        initial = time.time()
        playlist = pytube.Playlist(playlist_link)
        print(f'Video Title: {playlist.title} Number of Videos: {len(playlist.video_urls)}')
        if os.path.isdir(FINAL_DIRECTORY):
            #If The Parent Directory of The Main Youtube Videos Exists then Create A Directory For Each Playlist By its Title !
            os.path.join(FINAL_DIRECTORY, playlist.title)
        for video in playlist.video_urls:
            threading.Thread(target=self.download_playlist_video(Output_Path, video)).start()
        print(f'Playlist Download Complete in {time.time() - initial} seconds')

    def download_playlist_video(self, Output_Path, video_url):
        initial = time.time()
        video = pytube.YouTube(video_url)
        video.streams.filter(progressive=True).get_highest_resolution().download(Output_Path)
        print(f'{video.title} Downloaded in {time.time() - initial} seconds')
