from pytube import YouTube, Playlist
import os

# Function download the specified youtube url weather audio or video
def downloadURL(url, type):
    """
    Function to download a youtube video weather video or only the audio    
    It downloads the video in the same working directory.
    It selects the best stream available (720p max for video type).

    Inputs:
        url: the specified youtube video url
        type: the type of the download ('audio','video')

    Outputs:
        None    
        
    """
    # Creating a YouTube object for the desired url
    yt = YouTube(url)
    video_title = yt.title

    if type == 'audio':
    # Getting the best audio stream
        best_stream =  yt.streams.get_audio_only(subtype='mp4')
    # Fetting the best video stream
    elif type== 'video':
        best_stream =  yt.streams.get_highest_resolution()

    extention = '.mp3' if type == 'audio' else '.mp4'
    # Downloading the best Stream if found
    if best_stream: 
        name = video_title + extention
        download_dir = os.path.join(os.getcwd(),'Downloads')
        os.makedirs(download_dir, exist_ok=True)
        best_stream.download(filename=name, output_path= download_dir)
    

# Function to parse a txt file that contains urls of videos 
def file_parser(path, type):
    """
    Function to parse a file contains youtube videos urls and downloads them.
    """
    # Reading each line in the file and downloading it
    with open(path,'r') as file:
        for url in file:
            downloadURL(url, type)


def playlist_parser(url, type):
    """
    Function to parse a youtube playlist and download it.
    """
    pl = Playlist(url)
    for video_url in pl.video_urls:
        downloadURL(video_url, type)
