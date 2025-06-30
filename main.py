import os
import yt_dlp

def download_video(url):
    ydl_opts = {
        'cookiefile': 'cookies.txt',
        'outtmpl': 'video.mp4',
        'format': '18',  # Định dạng 360p
        'merge_output_format': 'mp4',
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',  # giả làm trình duyệt thật
        'quiet': False,
        'nocheckcertificate': True,
        'noplaylist': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        title = info.get('title', 'No Title')
        description = info.get('description', '')
    
    return 'video.mp4', title, description

if __name__ == "__main__":
    youtube_url = os.getenv("YOUTUBE_URL")
    if not youtube_url:
        print("❌ YOUTUBE_URL is missing")
    else:
        print("▶️ Đang tải video...")
        path, title, desc = download_video(youtube_url)
        print("✅ Tải xong:", path)
