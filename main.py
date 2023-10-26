# import packages
from pytube import YouTube
import os

# Defining some text color to the output
# ANSI escape codes for text color
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RESET = '\033[0m'  # Reset text color to default


# url input from user
link = YouTube(str(input(YELLOW + "Enter URL av youtube videoen du vil laste ned: \n>>" + RESET)))

# extract only audio
video = link.streams.filter(only_audio=True).first()

# specify which folder on your mac, that already exists
destination = os.path.dirname('/Users/sivertsaeter/Documents/NotOnSpotify/')

# download the file 
out_file = video.download(output_path=destination)

# save the file
base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)

# result of succes
print(GREEN + "SUCCESS " + RESET + video.title + " har blitt lagret i mappen: " + GREEN + destination + RESET)
 