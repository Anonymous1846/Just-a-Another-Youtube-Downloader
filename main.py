#The Downloader File has the Downloader class, which hosts the methods for downloading the Single and Multiple Videos(Playlists)
from Downloader import Downloader
#For File handling functionality and checking and manipulating directories
import os


#pyfiglet is used to add the ascii art
import pyfiglet


yt_downloader_title=pyfiglet.figlet_format('Youtube Downloader',font='slant')
print(yt_downloader_title)

# Name of Output Directory!
Youtube_Video_Directory = 'Youtube Videos'
# parent Directory !
Downloads = 'C:/Users/USER/Downloads'
#The final path of the Youtube Download Directory is 'C:/Users/USER/Downloads/Youtube Videos'
FINAL_PATH = os.path.join(Downloads, Youtube_Video_Directory)
#we have to check whether the directory already exists, then we don't have to create the new Directory !
if not os.path.isdir(FINAL_PATH):
    # First Check if the Directory is Created then create Dir if Not Exists !
    os.mkdir(FINAL_PATH)
    print('New Download Directory Created !')
#Reference to The downloader Class
download = Downloader()
option=''
while option!=3:
    #The program will run till You Input The Number 3
    option = int(input('1)Video\n2)Playlist\n3)Exit\n>>'))
    #Option one for video
    if option == 1:
        link = input('Please Paste A Video Link : ')
        download.download_single_video(FINAL_PATH, link)
    # Option two for Playlist !
    elif option == 2:
        playlist_link = input('Please Paste A Playlist Link :')
        download.download_playlist(FINAL_PATH, playlist_link=playlist_link)
        #The loop will run indefinitely
    elif option == 3:
	    print('Exiting........!')
	    break
