
# Import all the mdoules form requirements.txt

# start time for the script
start_time = time.time()

# current directory for absraction.
cwd = "/Users/rootapollo/Downloads/Music/"
# gets me the playlist_id, just the id
def get_playlist_id(str):
    playlist_id_0 = str.split("playlist/")
    playlist_id_1 = playlist_id_0[1]
    playlist_id_2 = playlist_id_1.split("?")
    return playlist_id_2[0]

# playlist_id     
playlist_id = get_playlist_id((input("Enter the playlist url: ")))


# authentication codes from spotify API
# Use spotify dev to get these details, very important
SPOTIPY_CLIENT_ID = '58db0e7ae228450ab8ba7341dd6c67de' 
SPOTIPY_CLIENT_SECRET = 'a72c3ce108664c30904266207dc39c4a'

def get_new_token():
    r = requests.request("GET", "https://open.spotify.com/")
    r_text = BeautifulSoup(r.content, "html.parser").find("script", {"id": "session"}).get_text()
    return json.loads(r_text)['accessToken']

def get_track1234(playlist_id, offset, limit, token):
    url = "https://api.spotify.com/v1/playlists/" + str(playlist_id) + "/tracks?offset=" + str(offset) + "&limit=" + str(limit) + "&market=GB"
    payload={}
    headers = {
      'authorization': 'Bearer ' + str(token),
      'Sec-Fetch-Dest': 'empty',
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    return json.loads(response.text)

a = get_track1234(playlist_id, 0, 100, get_new_token())
dict_track = a['items']
no_of_songs = len(dict_track)

# list of song names

list_song_tracks = []

list_song_artists = []

# list of album name corresponding to their names
list_song_album = []

# list of songs' cover art url
list_cover_url = []

# for downloading tracks from youtube 
list_song_url = []



# function that fills all the above list
def get_track(dict_tracks, no_songs):
    for i in range(0, no_songs):
        if i == 100:
            break
        song_name = dict_tracks[i]['track']['name']
        dir_sep = "/"
        if dir_sep in song_name:
            lst_names = song_name.split('/')
            song_name = lst_names[0] + " " + lst_names[1]
            song_dir =  cwd + song_name + ".mp3"
            if os.path.exists(song_dir) == True:
                i = i + 1
            else:
                list_song_tracks.append(song_name)
                list_song_artists.append(dict_tracks[i]['track']['artists'][0]['name'])
                list_song_album.append(dict_tracks[i]['track']['album']['name']) 
                list_cover_url.append(dict_tracks[i]['track']['album']['images'][0]['url'])
        else:
            song_dir = cwd + song_name + ".mp3"
            if os.path.exists(song_dir) == True:
                i = i + 1
            else:
                list_song_tracks.append(song_name)
                list_song_artists.append(dict_tracks[i]['track']['artists'][0]['name'])
                list_song_album.append(dict_tracks[i]['track']['album']['name']) 
                list_cover_url.append(dict_tracks[i]['track']['album']['images'][0]['url'])
       

# fills the lists defined above
get_track(dict_track, no_of_songs)

song_no = len(list_song_tracks)
# function that get a list of youtube urls for each songs

# fills the list define above
def get_id(no_songs):
    for i in range(0, no_songs):
        try:
            videosSearch = VideosSearch(list_song_tracks[i] + list_song_artists[i] + " audio", limit = 1)
            video_id = videosSearch.result()['result'][0]['id']
            list_song_url.append("https://www.youtube.com/watch?v=" + video_id)
        except:
            break

get_id(song_no)

# function to download the song
def down_song(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        song = youtubeObject.download(output_path= cwd + "mp3down/videos")
        song_title = song.title()
        print("Download is completed successfully")
        return song_title
    except:
        print("An error has occurred")

for i in range(0, song_no):
    print(f"Downloading {i + 1} of {song_no} songs")
    video_dir = down_song(list_song_url[i])
    mp3_file = cwd + list_song_tracks[i] + ".mp3"
    video_name = moviepy.editor.VideoFileClip(video_dir)
    audio = video_name.audio
    audio.write_audiofile(mp3_file)
    
    link = list_cover_url[i]
    img_data = requests.get(link).content
    file_name = "/Users/rootapollo/Documents/Docs/Practice/mp3down/cover-art/abc.jpg"
    with open(file_name, 'wb') as handler:
        handler.write(img_data)
    
    
    audiofile = eyed3.load(mp3_file)
    if (audiofile.tag == None):
        audiofile.initTag()

    audiofile.tag.images.set(ImageFrame.FRONT_COVER, open(file_name,'rb').read(), 'image/jpeg')
    audiofile.tag.album = list_song_album[i]
    audiofile.tag.artist = list_song_artists[i]
    audiofile.tag.save(version=eyed3.id3.ID3_V2_3)
    os.remove(video_dir)
    os.remove(file_name)

end_time = time.time()
print(f"Your program took: {end_time - start_time} seconds")
>>>>>>> 4b45ab5 (Improved)
