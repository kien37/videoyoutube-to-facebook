from yt_dlp import YoutubeDL

url = "https://www.youtube.com/watch?v=oDv2abXHthY"  # Có thể đổi link

options = {
    'cookiefile': 'cookies.txt',
    'quiet': False,
    'noplaylist': True,
    'format': 'bestvideo+bestaudio/best',
}

with YoutubeDL(options) as ydl:
    info = ydl.extract_info(url, download=False)
    print("✅ Tiêu đề video:", info.get('title'))
