from pytube import YouTube
import os
import pytube.request

# Gán User-Agent để tránh lỗi 400
pytube.request.default_range_size = 9437184
pytube.request.user_agent = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/114.0.0.0 Safari/537.36"
)

def download_video(url):
    yt = YouTube(url)
    stream = yt.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()
    file_path = stream.download(filename='video.mp4')
    return file_path, yt.title, yt.description

if __name__ == "__main__":
    youtube_url = os.getenv("YOUTUBE_URL")
    if not youtube_url:
        print("❌ YOUTUBE_URL is missing")
    else:
        print("▶️ Đang tải video...")
        path, title, desc = download_video(youtube_url)
        print("✅ Tải xong:", path)
