import yt_dlp


def subtitleextractor(url):
    
   

    ydl_opts = {
        'writesubtitles': True,             # Download subtitles
        'writeautomaticsub': True,          # Fallback to auto subs
        'subtitleslangs': ['en','hi'],           # Language (change to ['all'] for all)
        'skip_download': True,              # Don’t download video
        'outtmpl': 'subtitles/%(title)s.%(ext)s', 
     
        
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)

    return "Subtitle downloaded successfully."
