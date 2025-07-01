import pyperclip
import json

try:
    # Lấy nội dung từ clipboard
    clipboard_data = pyperclip.paste()

    # Kiểm tra xem có phải JSON không
    cookies = json.loads(clipboard_data)

    # Ghi vào file cookies.json
    with open("cookies.json", "w", encoding="utf-8") as f:
        json.dump(cookies, f, indent=4, ensure_ascii=False)

    print("✅ Đã lưu cookies vào file cookies.json")

except Exception as e:
    print("❌ Lỗi: Dữ liệu clipboard không hợp lệ hoặc không phải JSON.")
    print(e)
