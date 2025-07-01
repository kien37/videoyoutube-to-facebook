import os
import requests
from yt_dlp import YoutubeDL

# Lấy access token và Page ID từ biến môi trường (hoặc thay trực tiếp nếu test)
FB_PAGE_TOKEN = os.getenv("FB_PAGE_TOKEN") or "THAY_BANG_PAGE_TOKEN_CUA_BAN"
FB_PAGE_ID = os.getenv("FB_PAGE_ID") or "THAY_BANG_PAGE_ID_CUA_BAN"

# Hàm tải video YouTube
def download_video(url):
    ydl_opts = {
        'cookiefile': 'cookies.txt',
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',
        'merge_output_format': 'mp4',
        'quiet': False,
        'noplaylist': True
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        title = info.get("title")
        description = info.get("description", "")
        file_path = ydl.prepare_filename(info)
        return file_path, title, description

# Hàm đăng video lên Facebook Page
def upload_to_facebook(video_path, title, description):
    upload_url = f"https://graph-video.facebook.com/v18.0/{FB_PAGE_ID}/videos"
    params = {
        "access_token": FB_PAGE_TOKEN,
        "title": title,
        "description": description
    }

    with open(video_path, "rb") as f:
        files = {
            "source": f
        }
        print("📤 Đang tải video lên Facebook...")
        response = requests.post(upload_url, data=params, files=files)

    if response.status_code == 200:
        video_id = response.json().get("id")
        print(f"✅ Đăng video thành công! ID: {video_id}")
    else:
        print("❌ Lỗi khi đăng video:")
        print(response.text)

# === CHẠY CHÍNH ===
if __name__ == "__main__":
    youtube_url = input("🔗 Dán link YouTube: ").strip()

    try:
        video_path, title, description = download_video(youtube_url)
        print(f"📥 Đã tải video: {title}")
        upload_to_facebook(video_path, title, description)
    except Exception as e:
        print("❌ Lỗi:", str(e))
