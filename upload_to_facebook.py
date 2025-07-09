import requests
import os

# 📌 Page Access Token và Page ID
ACCESS_TOKEN = "EAAKHZB2IZBzMsBPCJhA06AgZBAzd6DWPdwoFwZAX1fCPAUayBjnty7ZApUjWWPOdxO04dPhhKWOAlyfClMpURAWJwiByXJkzfSyD7UpXh3AjnEP9kIOGOjsKNu2c2fXL9ajOtZAQly2EqAspJZAKdwAk7DzkjOqGI2LagaC4qrvdgJ3ZBGIpVlhdhdsaswDBr3TLSs3LXccY8HLbBKxYYnvWYhB6f3DNNZAHxsZCa2jgKzkn8tLDrsPzqXX9ClBQZDZD"
PAGE_ID = "174117579302558"

# 📁 Thư mục chứa video tải về
DOWNLOAD_DIR = "downloads"

def get_latest_video_file():
    files = [os.path.join(DOWNLOAD_DIR, f) for f in os.listdir(DOWNLOAD_DIR) if f.endswith(".mp4")]
    if not files:
        raise Exception("❌ Không tìm thấy video trong thư mục downloads")
    return max(files, key=os.path.getctime)

def upload_video():
    video_path = get_latest_video_file()
    video_title = os.path.splitext(os.path.basename(video_path))[0]
    video_description = f"Đăng tự động: {video_title}"

    print(f"🚀 Đang tải video: {video_title}")

    with open(video_path, 'rb') as video_file:
        url = f"https://graph-video.facebook.com/v18.0/{PAGE_ID}/videos"
        params = {
            "access_token": ACCESS_TOKEN,
            "title": video_title,
            "description": video_description
        }
        files = {
            "source": video_file
        }

        response = requests.post(url, params=params, files=files)

        print("🧾 Phản hồi từ Facebook:")
        print(response.text)

        try:
            data = response.json()
        except Exception as e:
            print("❌ Lỗi khi phân tích phản hồi JSON:", str(e))
            with open("fb_response_debug.txt", "w", encoding="utf-8") as f:
                f.write(response.text)
            print("📁 Phản hồi đã được lưu vào fb_response_debug.txt")
            return

        if 'id' in data:
            print(f"✅ Đã đăng video thành công! Video ID: {data['id']}")
        else:
            print(f"❌ Lỗi khi đăng video: {data}")

if __name__ == "__main__":
    upload_video()
