from Downloader import Downloader
import os

print(
    '*******************************Youtube Video Downloader****************************\nVersion 1.0'
)
Youtube_Video_Directory = 'Youtube Videos'
Downloads = 'C:/Users/USER/Downloads/Youtube Videos'
FINAL_PATH = os.path.join(Downloads, Youtube_Video_Directory)
if os.path.isdir(FINAL_PATH):
    print('Path Already Exists !')
else:
    os.mkdir(FINAL_PATH)
option = int(input('1)Video\n2)Playlist'))
download = Downloader()
if option == 1:
    video_link = input('Paste Video Link: ')
    download.download_single_video(FINAL_PATH, video_link)
elif option == 2:
    playlist_link = input('Paste Playlist Link: ')
    download.download_playlist(FINAL_PATH,playlist_link)
