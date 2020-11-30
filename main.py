import  pytube
#Os Library is used to Manipulate the Paths in our Computer !
import os
#Used to Extract the Text Between the Double Quotes !
import re
print('**********Youtube Video Downloader*************')
print('V1.0')
# The Ditictionary where the The Integers are mapped to the iTag
dic_for_video={}
#The directory of the Download
PARENT_PATH="C:/Users/USER/Downloads"
#A New Directory Will Be Created by the program !
#The Name of the Directory specified here !
YT_DOWNLOAD_DIR="YTDownloads"
#The Final Path is PARENT_PATH+YTDOWNLOAD,joined using the os.path.join
FINAL_PATH=os.path.join(PARENT_PATH,YT_DOWNLOAD_DIR)
#Check if the Path Already Exists if yes no need to create PATH for Download,otherwise create new FINAL_PATH
if os.path.isdir(FINAL_PATH):
    print(f"The requested Directory {FINAL_PATH} already Exists ")
else:
    os.mkdir(FINAL_PATH)
    print(f"The requested Directory {FINAL_PATH} Created ! ")

link=input('Paste the Link of the Video')
try:
    #Fetching the Video Using the Youtube Object From the link provided by the user !
    y=pytube.YouTube(link)
    #printing the author information and The Video Title !
    print(f"The Video you Searched For is f{y.title} Author: {y.author}")
    #Counter needs to be assigned to the Video So that the User can choose the Video According to the Int Number !
    counter=1
    format_value=input('1)video\n2)audio')
    for i in y.streams.filter(type='video' if format_value=='1' else 'audio'):
        #used to show the Type and Quality which are seperated by Spaces
        list=str(i).split(" ")
        itag,type,quality= re.findall(r'"([^"]*)"',str(list[1])+str(list[2]) +str(list[3]))
        #The Integer is mapped to an unique iTag so that user can choose easily
        dic_for_video[counter]=itag
        print(f"{counter}) Type:{type} Quality: {quality}")
        #Increamenting the counter so that Shows A Sequence order !
        counter=counter+1
    id_number=input('Enter The Id Number of The Video To Download The Video !')
    #out of the video streams the video selected by the user gets downloaded to the FINAL_PATH
    file_name=input('Save as :')
    y.streams.get_by_itag(dic_for_video.get(int(id_number))).download(FINAL_PATH,file_name)
    print(f'File Saved to {FINAL_PATH} as {file_name}')
#If Video/Audio Download Fails
except Exception as e:
        print(f"Oops An Error Occured While Traversing the Link,Looks Like the Video URL is Corrupted !")
finally:
    print('Program Exiting......')
