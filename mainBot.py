from pytube import YouTube

URL = "https://www.youtube.com/watch?v=7BXJIjfJCsA"
yt = YouTube(URL)
print("start")
stream = yt.streams.get_by_itag(22)
stream.download()
