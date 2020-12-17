from Downloader import Downloader
import os

print(
    '*******************************Youtube Video Downloader****************************\nVersion 1.0'
)
#Name of Output Directory!
Youtube_Video_Directory = 'Youtube Videos'
#parent Directory !
Downloads = 'C:/Users/USER/Downloads'
FINAL_PATH = os.path.join(Downloads, Youtube_Video_Directory)
if not os.path.isdir(FINAL_PATH):
    #First Check if the Directory is Created then create Dir if Not Exists !
    os.mkdir(FINAL_PATH)
    print('New Download Directory Created !')


option = int(input('1)Video\n2)Playlist'))
download = Downloader()
if option == 1:
    video_link = input('Paste Video Link: ')
    download.download_single_video(FINAL_PATH, video_link)
elif option == 2:
    playlist_link = input('Paste Playlist Link: ')
    download.download_playlist(FINAL_PATH, playlist_link)
