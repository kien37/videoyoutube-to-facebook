import os
from yt_dlp import YoutubeDL

# Đường dẫn tới file cookie đã xuất từ trình duyệt (định dạng Netscape)
COOKIE_FILE = 'cookies.txt'

# Hàm tải video từ YouTube
def download_video(url):
    ydl_opts = {
        'outtmpl': 'downloaded_video.%(ext)s',
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
        'cookies': COOKIE_FILE,
        'quiet': False,
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)
        title = info.get('title', 'No Title')
        description = info.get('description', '')

        return filename, title, description

# ------------------------------------
# ▶️ Phần kiểm tra tải video

if __name__ == "__main__":
    import sys

    # Cách dùng: python main.py "https://youtube.com/..."
    if len(sys.argv) != 2:
        print("❌ Bạn cần cung cấp URL YouTube.\n📌 Ví dụ: python main.py https://www.youtube.com/watch?v=ID")
        sys.exit(1)

    youtube_url = sys.argv[1]
    print(f"🔽 Đang tải video từ: {youtube_url}")
    
    try:
        path, title, desc = download_video(youtube_url)
        if os.path.exists(path):
            print(f"✅ Video đã tải về thành công tại: {path}")
            print(f"🎥 Tiêu đề: {title}")
        else:
            print("❌ Không tìm thấy file video sau khi tải.")
    except Exception as e:
        print("❌ Lỗi khi tải video:", str(e))