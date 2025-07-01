import os
from yt_dlp import YoutubeDL

# 🔧 Cấu hình thư mục lưu video
DOWNLOAD_DIR = "downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# 📌 Gán sẵn link YouTube cần tải (dùng để test)
youtube_url = "https://www.youtube.com/watch?v=oDv2abXHthY"

# 🔐 Đường dẫn đến file cookies (đã xuất từ Cookie-Editor)
COOKIES_FILE = "cookies.txt"

def download_video(url):
    ydl_opts = {
        "cookiefile": COOKIES_FILE,
        "outtmpl": os.path.join(DOWNLOAD_DIR, "%(title)s.%(ext)s"),
        "quiet": False,
        "format": "bestvideo+bestaudio/best",
        "merge_output_format": "mp4",
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        title = info.get("title")
        description = info.get("description")
        filename = ydl.prepare_filename(info)
        print(f"✅ Đã tải: {filename}")
        return filename, title, description

if __name__ == "__main__":
    print(f"▶️ Bắt đầu tải video từ: {youtube_url}")
    try:
        path, title, desc = download_video(youtube_url)
        print(f"\n🎉 Hoàn tất tải video: {title}")
    except Exception as e:
        print(f"❌ Lỗi khi tải video: {e}")
