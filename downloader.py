from pytube import YouTube, Playlist

# Function download the specified youtube url weather audio or video
def downloadURL(url, type):

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
        best_stream.download(filename=name)
        print(video_title+' '+ 'Downloaded succesfully')
    else:
        print('Couldn\'t find a stream to download. Please try again.')
    

# Function to parse a txt file that contains urls of videos 
def file_parser(path, type):

    # Reading each line in the file and downloading it
    with open(path,'r') as file:
        for url in file:
            downloadURL(url, type)


def playlist_parser(url, type):
    pl = Playlist(url)
    for video_url in pl.video_urls:
        downloadURL(video_url, type)



#playlist_parser('https://www.youtube.com/playlist?list=PLLVDNsvw7fOdFLZz6c7dOvmD3YSUHdRWm', 'video')