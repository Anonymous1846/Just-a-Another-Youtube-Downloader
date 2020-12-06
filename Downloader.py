#The Python file has two functions namely for downloading the Single Video and For Downloading the Playlist
#The functions defined in this module will be called there !
#Library for Downloading the Videos
import pytube
#For Regular Expressions
import re
#Time Module Imported to display the Download Time !
import time
class Downloader():
    def __init__(self):
        self.dic_for_video = None

    def download_single_video(self,Output_Path,video_link):
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
    def download_playlist(self,Output_Path,playlist_link):
        # Object of The Playlist Class
        playlist=pytube.Playlist(playlist_link)
        print(f'Video Title: {playlist.title} Number of Videos: {len(playlist.video_urls)}')
        try:
            video=pytube.YouTube(playlist.video_urls.__getitem__(0))
            counter = 1
            format_value = input('1)video\n2)audio')
            for i in video.streams.filter(type='video' if format_value == '1' else 'audio'):
                # used to show the Type and Quality which are seperated by Spaces
                list = str(i).split(" ")
                itag, type, quality, fps_bitrate, audio_video = re.findall(r'"([^"]*)"',
                                                                           str(list[1]) + str(list[2]) + str(
                                                                               list[3]) + str(
                                                                               list[4]) + str(list[6]))
                # The Integer is mapped to an unique iTag so that user can choose easily
                self.dic_for_video[counter] = itag
                counter=counter+1
                id_number = input('Enter The Id Number of The Video To Download The Video !')
                for video in playlist.videos:
                    video.streams.get_by_itag(self.dic_for_video.get(id_number)).download(Output_Path)
        except Exception as exp:
            print('Something Went Wrong !')