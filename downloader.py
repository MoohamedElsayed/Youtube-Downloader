from pytube import YouTube

# Function to extract and download mp3 audios from youtube urls
def download_mp3(url):

    # Creating a YouTube object for the desired url
    yt = YouTube(url)
    video_title = yt.title

    # Getting the best audio stream
    best_stream =  yt.streams.get_audio_only(subtype='mp4')


    # Downloading the best Stream if found
    if best_stream: 
        name = video_title + '.mp3'
        best_stream.download(filename=name)
        print(video_title+' '+ 'Downloaded succesfully')
    else:
        print('Couldn\'t find audio to extract')
    


# Function to parse a txt file that contains urls of videos 
def file_parser(path):

    # Reading each line in the file and downloading it
    with open(path,'r') as file:
        for url in file:
            download_mp3(url)


file_parser('/home/mohamed/Desktop/Youtube-MP3-Downloader/videos.txt')