import random

os_templates = [
    # Windows
    "Windows NT 10.0; Win64; x64",
    "Windows NT 6.1; Win64; x64",
    "Windows NT 6.3; WOW64",
    "Windows NT 5.1; Win32",
    # Linux
    "X11; Linux x86_64",
    "X11; Linux i686",
    "X11; Ubuntu; Linux x86_64",
    "X11; Fedora; Linux x86_64",
    "X11; Arch; Linux x86_64",
    "X11; Kali; Linux x86_64",
    # MacOS
    "Macintosh; Intel Mac OS X 10_15_7",
    "Macintosh; Intel Mac OS X 11_2_3",
    "Macintosh; Intel Mac OS X 13_0",
    "Macintosh; Intel Mac OS X 14_1_2",
    # Android
    "Linux; Android 14; SM-G991B",
    "Linux; Android 13; Pixel 7 Pro",
    "Linux; Android 12; Mi 11",
    "Linux; Android 11; Samsung A52",
    "Linux; Android 10; Realme 6 Pro",
    "Linux; Android 9; Vivo Y91",
    # iOS
    "iPhone; CPU iPhone OS 16_3 like Mac OS X",
    "iPhone; CPU iPhone OS 15_2 like Mac OS X",
    "iPad; CPU OS 13_3 like Mac OS X",
    "iPod touch; CPU iPhone OS 12_1_4 like Mac OS X",
]

def get_browser_versions():
    return {
        "Chrome": [f"{v}.0.{random.randint(1000, 6000)}.{random.randint(0, 300)}" for v in range(80, 122)],
        "Firefox": [f"{v}.0" for v in range(60, 122)],
        "Safari": [f"{v}.0.{random.randint(1, 9)}" for v in range(10, 17)],
        "Edge": [f"{v}.0.{random.randint(1000, 5000)}.{random.randint(0, 200)}" for v in range(80, 121)],
        "Opera": [f"{v}.0.{random.randint(1000, 5000)}.{random.randint(0, 200)}" for v in range(70, 101)],
        "Brave": [f"{v}.0.{random.randint(1000, 5000)}.{random.randint(0, 200)}" for v in range(90, 121)],
        "Vivaldi": [f"{v}.0.{random.randint(1000, 5000)}.{random.randint(0, 200)}" for v in range(70, 100)],
        "DuckDuckGo": [f"{v}.0" for v in range(5, 10)],
        "SamsungBrowser": [f"{v}.2" for v in range(10, 16)],
        "UCBrowser": [f"{v}.0.{random.randint(1000, 2000)}.{random.randint(50, 99)}" for v in range(12, 16)],
        "QQBrowser": [f"{v}.0.{random.randint(100, 999)}.{random.randint(0,9)}" for v in range(10, 14)],
        "Maxthon": [f"{v}.0.{random.randint(1000, 4000)}.0" for v in range(5, 8)],
        "Puffin": [f"{v}.0.{random.randint(1, 20)}.0AP" for v in range(5, 10)],
        "Yandex": [f"{v}.0.{random.randint(1000, 4000)}" for v in range(15, 23)],
    }

def generate_user_agents(amount):
    browsers = get_browser_versions()
    count = 0
    while count < amount:
        os = random.choice(os_templates)
        browser = random.choice(list(browsers.keys()))
        version = random.choice(browsers[browser])

        if browser in ["Chrome", "Edge", "Opera", "Brave", "Vivaldi", "Yandex", "SamsungBrowser", "UCBrowser", "QQBrowser", "Maxthon", "Puffin"]:
            ua = f"Mozilla/5.0 ({os}) AppleWebKit/537.36 (KHTML, like Gecko) {browser}/{version} Safari/537.36"
        elif browser == "Firefox":
            ua = f"Mozilla/5.0 ({os}; rv:{version}) Gecko/20100101 Firefox/{version}"
        elif browser == "Safari":
            ua = f"Mozilla/5.0 ({os}) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/{version} Safari/605.1.15"
        elif browser == "DuckDuckGo":
            ua = f"Mozilla/5.0 ({os}) AppleWebKit/537.36 (KHTML, like Gecko) DuckDuckGo/{version}"
        else:
            ua = f"Mozilla/5.0 ({os}) {browser}/{version}"

        yield ua
        count += 1

def save_to_file(filename, amount):
    with open(filename, "w", encoding="utf-8") as f:
        for ua in generate_user_agents(amount):
            f.write(ua + "\n")
    print(f"✅ {amount} UserAgent saved to {filename} 🔥")

if __name__ == "__main__":
    jumlah = int(input("🔥 Jumlah User-Agent (max 100.000.000): "))
    nama_file = input("📁 Nama file output (contoh: useragent.txt): ")
    save_to_file(nama_file, jumlah)
