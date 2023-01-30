import os
from pytube import YouTube

def down_song(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download("/Users/rootapollo/Documents/Docs/Practice/mp3down/videos")
        print("Download is completed successfully")
    except:
        print("An error has occurred")


link = input("Enter the youtube link: ")
down_song(link)
# https://www.youtube.com/watch?v=8hly31xKli0&list=WL&index=4&ab_channel=freeCodeCamp.org
# https://www.youtube.com/watch?v=tPEE9ZwTmy0&ab_channel=MylotheCat