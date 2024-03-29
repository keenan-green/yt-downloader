# yt-downloader

## About
A youtube downloader based on pytube that allows unlimited videos and/or playlists to be downloaded.

The writing of this program was inspired by my girlfriend's (Kuyuri Nadasen) need of downloading a large number of youtube videos for her university course.

## RUN
Change directory to yt-downloader/src/
```bash
python3 ytdownloader.py
```

The program will prompt the user to download:
* Video
* Playlist
* Quit the prgram

In the event of: 
* Video:
    * The program will prompt the user or the video's youtube link.
* Playlist:
    * The program will prompt the user for the playlist's youtube link.
        * The user will further be prompted to select downloading the entire playlist or selected videos along the way.

### Packages
* pytube: package that allows for the downloading of youtube videos.
    * To install pytube, run:
```bash
pip install pytube
```

## To Implement:
1. Option for resolution picking.
2. Display a list of videos in a playlist and allowing a user to select which to download.
3. GUI using 'customtkinter'.
4. Download progress bar.

### Implemented:
Features that were implemented since the first 'final' product.
1. Individually downloaded videos to be stored in dated folders
