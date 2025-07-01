import json
import pyperclip

netscape_header = "# Netscape HTTP Cookie File\n"

def json_to_netscape(cookie_json):
    output = netscape_header
    for cookie in cookie_json:
        domain = cookie.get("domain", "")
        include_subdomain = "TRUE" if domain.startswith(".") else "FALSE"
        path = cookie.get("path", "/")
        secure = "TRUE" if cookie.get("secure", False) else "FALSE"
        expires = int(cookie.get("expirationDate", 0))
        name = cookie.get("name", "")
        value = cookie.get("value", "")
        output += f"{domain}\t{include_subdomain}\t{path}\t{secure}\t{expires}\t{name}\t{value}\n"
    return output

try:
    # Lấy JSON từ clipboard
    clipboard_content = pyperclip.paste()
    cookies_json = json.loads(clipboard_content)

    # Chuyển sang định dạng Netscape
    netscape_cookies = json_to_netscape(cookies_json)

    # Lưu vào cookies.txt
    with open("cookies.txt", "w", encoding="utf-8") as f:
        f.write(netscape_cookies)

    print("✅ Đã lưu cookies thành công vào cookies.txt")

except Exception as e:
    print("❌ Lỗi khi xử lý cookies:", str(e))
