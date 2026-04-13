import yt_dlp as yt

link = input('link?: ')
options = {'format': 'best'}

with yt.YoutubeDL(options) as ydl:
    ydl.download([link])
    