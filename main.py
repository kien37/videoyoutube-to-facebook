import os
import yt_dlp

def download_video(url):
    ydl_opts = {
        'outtmpl': 'video.mp4',
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
        'cookiefile': 'cookies.txt',  # Sử dụng cookie để vượt xác minh
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        title = info.get('title', 'No Title')
        description = info.get('description', '')
        return 'video.mp4', title, description  # ✅ Trả về kết quả trong khối with

if __name__ == "__main__":
    youtube_url = os.getenv("YOUTUBE_URL")
    if not youtube_url:
        print("❌ YOUTUBE_URL is missing")
    else:
        print("▶️ Đang tải video...")
        path, title, desc = download_video(youtube_url)
        print("✅ Tải xong:", path)
