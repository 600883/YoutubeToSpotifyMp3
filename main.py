# import packages
from pytube import YouTube
import os

# url input from user
link = YouTube(str(input("Enter URL av youtube videoen du vil laste ned: \n>>")))

# extract only audio
video = link.streams.filter(only_audio=True).first()

# check for destination to save file
# print("Hvilken mappe vil du lagre filen i (la være blank for gjeldene mappe)")
# destination = str(input(">> ")) or '.'

# specify which folder on your mac, that already exists
# destination = 'Users/sivertsaeter/Documents/NotOnSpotify/'
destination = os.path.dirname('/Users/sivertsaeter/Documents/NotOnSpotify/')

# download the file 
out_file = video.download(output_path=destination)

# save the file
base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)

# result of succes
print(video.title + " har blitt lagret i mappen: " + destination)
 