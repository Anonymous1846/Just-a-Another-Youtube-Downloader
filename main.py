import  pytube
import os
import re
print('**********Youtube Video Downloader*************')
print('V1.0')
dic_for_video={}
PARENT_PATH="C:/Users/USER/Downloads"
#A New Directory Will Be Created by the program !
YT_DOWNLOAD_DIR="YTDownloads"
FINAL_PATH=os.path.join(PARENT_PATH,YT_DOWNLOAD_DIR)

if os.path.isdir(FINAL_PATH):
    print(f"The requested Directory {FINAL_PATH} already Exists ")
else:
    os.mkdir(FINAL_PATH)
    print(f"The requested Directory {FINAL_PATH} Created ! ")

link="https://www.youtube.com/watch?v=do4vb0MdLFY"
try:
    y=pytube.YouTube(link)
    print(f"The Video you Searched For is f{y.title} Author: {y.author}")
    counter=1
    for i in y.streams:
        list=str(i).split(" ")
        itag,type,quality= re.findall(r'"([^"]*)"',str(list[1])+str(list[2]) +str(list[3]))
        dic_for_video[counter]=itag
        print(f"{counter}) Type:{type} Quality: {quality}")
        counter=counter+1
    id_number=input('Enter The Id Number of The Video To Download The Video !')
    y.streams.get_by_itag(dic_for_video.get(int(id_number))).download(FINAL_PATH)

except Exception as e:
        print(f"Oops An Error Occured While Traversing the Link,Looks Like the Video URL is Corrupted !")
