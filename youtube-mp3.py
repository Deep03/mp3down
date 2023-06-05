# importing all the necessary libraries
from __future__ import unicode_literals
from youtubesearchpython import VideosSearch
import time
from pytube import YouTube
import moviepy.editor
import os
import requests
import eyed3
from eyed3.id3.frames import ImageFrame
import json
from bs4 import BeautifulSoup


cwd = "current_working_directory"
video_path = "path_to_video_fule"
def down_song(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        print("Downloading.....")
        youtubeObject.download(video_path)
        print("Video downloaded successfully")
    except:
        print("An error has occurred")


link = input("Enter the youtube link: ")
song_name = input("Enter the song name: ")
artist_name = input("Enter the artist name: ")
album_name = input("Enter the album name: ")

down_song(link)
video_name = os.listdir(video_path)
video_dir = video_path + "/" + video_name[0]

def mp3_down(video_dir):
    mp3_file = cwd + song_name + ".mp3"
    video_name = moviepy.editor.VideoFileClip(video_dir)
    audio = video_name.audio
    audio.write_audiofile(mp3_file)

    audiofile = eyed3.load(mp3_file)
    if (audiofile.tag == None):
        audiofile.initTag()

    audiofile.tag.album = album_name
    audiofile.tag.artist = artist_name
    audiofile.tag.save(version=eyed3.id3.ID3_V2_3)
    os.remove(video_dir)
    print("\nVideo converted successfully into mp3 file")

mp3_down(video_dir)
