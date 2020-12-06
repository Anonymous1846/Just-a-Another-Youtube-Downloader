from Downloader import Downloader
import os

print(
    '*******************************Youtube Video Downloader****************************\nVersion 1.0'
)

option=int(input('1)Video\n2)Playlist'))
download=Downloader()
if option==1:
    download.download_single_video()
elif option==2:
    download.download_playlist()