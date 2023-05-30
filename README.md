# YouTube Playlist Downloader

This Python script allows you to download songs from a YouTube playlist based on the tracks obtained from a Spotify playlist. It uses the YouTube Data API to search for the songs and the pytube library to download the audio from the YouTube videos.

## Disclaimer

This project is intended for educational purposes only. The downloading and distribution of copyrighted material without proper authorization may infringe upon the rights of content creators and could be against the law in your jurisdiction. Please use this script responsibly and respect the intellectual property rights of others.


## Prerequisites

Before running the script, make sure you have the following libraries installed:

- youtubesearchpython
- pytube
- moviepy
- requests
- eyed3
- beautifulsoup4

You can install them using package_install.py
- Run the script package_install.py using `python(3) package_install.py`


## Usage

1. Clone the repository:


2. Install the required dependencies as mentioned in the prerequisites section.

3. Obtain Spotify API authentication codes:

- Visit the Spotify Developer Dashboard (https://developer.spotify.com/dashboard/) and create a new application.
- Copy the client ID and client secret and replace `YOUR_CLIENT_ID` and `YOUR_CLIENT_SECRET` in the code with your actual credentials.

4. Run the script: `python(3) main2.py`


5. Enter the playlist URL when prompted.

6. The script will download the songs from the playlist and save them in the current directory.

## Note

- Make sure you have a stable internet connection while running the script, as it requires internet access to search for YouTube videos and download them.
- The script relies on the availability of the songs on YouTube. If a song is not found on YouTube, it may not be downloaded.

## License

This project is licensed under the [MIT License](LICENSE).
