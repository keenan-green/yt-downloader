import os

while True:
    link = input("Enter yt link: ")
    os.system("yt-dlp --no-abort-on-error {0}".format(link))