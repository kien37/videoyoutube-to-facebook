from pytube import YouTube
import os

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
