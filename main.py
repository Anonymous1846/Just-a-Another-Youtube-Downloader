from Downloader import Downloader
import os


import threading

print(
    '*******************************Youtube Video Downloader****************************\nVersion 1.0'
)
# Name of Output Directory!
Youtube_Video_Directory = 'Youtube Videos'
# parent Directory !
Downloads = 'C:/Users/USER/Downloads'
FINAL_PATH = os.path.join(Downloads, Youtube_Video_Directory)
if not os.path.isdir(FINAL_PATH):
    # First Check if the Directory is Created then create Dir if Not Exists !
    os.mkdir(FINAL_PATH)
    print('New Download Directory Created !')
#Reference to The downloader Class
download = Downloader()
option = None
while option != 3:
    #The program will run till You Input The Number 3
    option = int(input('1)Video\n2)Playlist\n3)Exit'))
    #Option one for video
    if option == 1:
        link = input('Please Paste A Video Link : ')
        threading.Thread(target=download.download_single_video(FINAL_PATH, link)).start()
    # Option two for Playlist !
    elif option == 2:
        playlist_link = input('Please Paste A Playlist Link :')
        download.download_playlist(FINAL_PATH, playlist_link=playlist_link)
    elif option == 3:
        #The Program
        print('Exiting......')
        exit(0)
