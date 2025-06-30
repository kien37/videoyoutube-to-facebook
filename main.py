import os
import yt_dlp

def download_video(url):
    ydl_opts = {
        'cookiefile': 'cookies.txt',
        'outtmpl': 'video.mp4',
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
        'quiet': False,
        'nocheckcertificate': True,
        'force_generic_extractor': False,
        'noplaylist': True,
        'listformats': True  # 👉 chỉ in danh sách format để xem có gì
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.extract_info(url, download=False)  # 👉 không tải, chỉ hiện định dạng

if __name__ == "__main__":
    youtube_url = os.getenv("YOUTUBE_URL")
    if not youtube_url:
        print("❌ YOUTUBE_URL is missing")
    else:
        print("▶️ Danh sách định dạng video có thể tải:")
        download_video(youtube_url)
