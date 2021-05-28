from Downloader import Downloader
import pyfiglet
import os


__author__ = 'Sharath Sunil'
__version__= 1.10
yt_downloader_title = pyfiglet.figlet_format('Youtube Downloader',font='slant') #the title for the yt downloader script !

print(yt_downloader_title)
print(f'Version : {__version__}')
print(f'Author  : {__author__}')

YOUTUBE_VID_DIR = 'Youtube Videos' # Parent directory for all Yt videos !
DOWNLOADS = 'C:/Users/USER/Downloads'
FINAL_PATH = os.path.join(DOWNLOADS, YOUTUBE_VID_DIR) # joining the downloads and the new vids directory !

if not os.path.isdir(FINAL_PATH):
    os.mkdir(FINAL_PATH)
    print('New Download Directory Created !')

download = Downloader()

while True:

    option = int(input('1)Video\n2)Playlist\n3)Exit\n>>'))
    if option == 1:
        link = input('Please Paste A Video Link : ')
        download.download_single_video(FINAL_PATH, link)

    elif option == 2:
        playlist_link = input('Please Paste A Playlist Link :')
        download.download_playlist(FINAL_PATH, playlist_link=playlist_link)

    elif option == 3:
	    print('Exiting........!')
	    break
    
    else:
        print('Invalid Option !!\nPlease Try Again !')
