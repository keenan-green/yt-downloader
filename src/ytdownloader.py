#Author: Keenan Michael Green
#Downloading youtube playlists or videos

import sys
import datetime
from pytube import Playlist, YouTube

def getDate():
    pass

# Setting up date for output to folder
date = getDate()

if __name__ == '__main__':
        
    count = 0
    while (True):
        if (count > 0):
            print("Would you like to download another Video or Playlist?")
        else:
            print("Would you like to download a Video or Playlist?")
        type = input("Enter 'p' for playlist, 'v' for video, 'q' to exit program: ")
        valid_link = False
        if (type == 'p'):
            while (not valid_link):
                playlist_link = input('Enter link to playlist: ')
                try:
                    p = Playlist(playlist_link)
                    p_title = p.title
                    valid_link = True
                except:
                    print("Not a valid YouTube playlist link")
                print()

            #Asking user if they would like to authorise each video download
            print("Would you like to skip certain videos in this playlist?")
            print("If you would like to do so, you will be required to\nsupply input for every video downloaded")
            skipping_str = input("input 'y' for yes, 'n' for no: ")
            print()
            #Setting up boolean depending on users input
            skipping_bool = False
            if (skipping_str == 'y'):
                skipping_bool = True

            #Printing out the title of playlist that is being downloaded
            print()
            print(f'Downloading: {p_title}')
            print()

            #For loop that downloads individual videos
            for video in p.videos:
                #Printing title of video currently being downloaded
                print()
                print()
                print("Video title: "+ video.title)
                print()

                #If user specified they would like to authorise each video's download
                #Asking for authorisation for this video
                skip_video = False
                skip_rem = False
                if skipping_bool:
                    print("\tWould you like to download this video?")
                    print("\tAlternatively you can download the remainder\n\tor skip the remainder")
                    print("\tof the playlist automatically.")
                    print()
                    valid_input = False
                    while (not valid_input):
                        skip = input("\tInput options:\n\t'y' for yes,\n\t'n' for no,\
                        \n\t'a' for download remainder,\n\t's' for skip remainder.\
                        \n\tEnter input : ")
                        if (skip == 'y'):
                            valid_input = True
                            print()
                        elif (skip == 'n'):
                            print()
                            valid_input = True
                            skip_video = True
                        elif(skip == 'a'):
                            skipping_bool = False
                            valid_input = True
                            print()
                        elif(skip == 's'):
                            valid_input = True
                            skip_rem = True
                        else:
                            print()
                            print("\tInvalid input")
                    if (skip_video):
                        continue
                    elif (skip_rem):
                        break
                        
                #Getting all videos formats of 720p
                list = video.streams.filter(type='video', resolution='720p')
                #Boolean will turn to false when video has been dowloaded
                #Ensuring only one resolution of video is downloaded
                bool = True 


                #Set up for Filename and Destination of download
                output_path = "../output/Playlist_Downloads/{0}".format(p.title)
                filename=video.title+".mp4"


                #Iterating through videos and downloading them in a specific video codec
                #If this codec is not available, an alternate resolution will be tried
                for l in list:
                    if l.video_codec.startswith('avc1'):
                        print("\tDownloading in 720p...")
                        l.download(filename=filename, output_path=output_path)
                        print("\tDownload Successful")
                        bool = False
                        break
                #If 720p video was not found, trying 480p
                if bool:
                    list = video.streams.filter(type='video', resolution='480p')
                    for l in list:
                        if l.video_codec.startswith('avc1'):
                            print("\tDownloading in 480p...")
                            l.download(filename=filename, output_path=output_path)
                            print("\tDownload Successful")
                            bool = False
                            break
                #If 480p video was not found, trying 360p
                if bool:
                    list = video.streams.filter(type='video', resolution='360p')
                    for l in list:
                        if l.video_codec.startswith('avc1'):
                            print("\tDownloading in 360p...")
                            l.download(filename=filename, output_path=output_path)
                            print("\tDownload Successful")
                            bool = False
                            break
            print()
            print("Playlist downloaded successfully")
            count = count + 1
            print()
            print()

        elif (type == 'v'):
            while (not valid_link):
                video_link = input('Enter link to video: ')
                try:
                    v = YouTube(video_link)
                    v_title = v.title
                    valid_link = True
                except:
                    print("Not a valid YouTube video link")
                print()
            print("Downloading: "+ v_title)
            print()

            #Getting all videos formats of 720p
            list = v.streams.filter(type='video', resolution='720p')

            #Set up for Filename and Destination of download
            output_path = "../output/Video_Downloads"
            filename=v_title+".mp4"


            #Iterating through videos and downloading them in a specific video codec
            #If this codec is not available, an alternate resolution will be tried
            for l in list:
                if l.video_codec.startswith('avc1'):
                    print("\tDownloading in 720p...")
                    l.download(filename=filename, output_path=output_path)
                    bool = False
                    break
            #If 720p video was not found, trying 480p
            if bool:
                list = v.streams.filter(type='video', resolution='480p')
                for l in list:
                    if l.video_codec.startswith('avc1'):
                        print("\tDownloading in 480p...")
                        l.download(filename=filename, output_path=output_path)
                        bool = False
                        break
            #If 480p video was not found, trying 360p
            if bool:
                list = v.streams.filter(type='video', resolution='360p')
                for l in list:
                    if l.video_codec.startswith('avc1'):
                        print("\tDownloading in 360p...")
                        l.download(filename=filename, output_path=output_path)
                        bool = False
                        break
            print()
            print("Video downloaded successfully")
            count = count + 1
            print()
            print()

        elif (type == 'q'):
            print()
            sys.exit("User terminated program")
        else:
            print()
            print("input was not a valid option")
