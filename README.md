# 🔥 KENSPLOIT - DDoS Attack Toolkit 💀

**KENSPLOIT** is a Layer 4 (UDP/TCP) and Layer 7 (HTTP) network stress testing tool written in Python.
It comes with interactive terminal UI, colorful output (thanks to `rich` and `colorama`), and a secure login system via Pastebin API.

> ⚠️ For educational and authorized testing purposes only.

---

## 📦 Features

* 🛡️ **Pastebin-Based Authentication**
* 🌐 **Layer 4 Attacks**:

  * UDP Flood (Plain & Random)
  * TCP SYN Flood (Single/Multi)
  * TCP Data Flood (Single/Multi)
* 📡 **Layer 7 Attacks**:

  * HTTP Flood (GET/POST/HEAD)
* 🧠 **Interactive Interface**
* 🌈 Terminal output with `rich` + `colorama`

---

## 🛠 Installation Guide


# 1. Clone the repo
```bash
git clone https://github.com/kenairforces/KENXDDOS.git
cd KENXDDOS
```
# 2. Create virtual env (optional but recommended)
```bash
sudo python -m venv venv
sudo source venv/bin/activate  # or venv\Scripts\activate on Windows
```

# 3. Install dependencies
with env
```bash
sudo pip install -r requirements.txt 
```
no env
```bash
sudo pip install -r requirements.txt --break-system-package
```

### Required packages

* `requests`
* `rich`
* `colorama`
* `scapy`

---

## 🔑 Login System (buy for the username and pasword)

KENSPLOIT DDOS using username and password just follow me and i give the username and password for free or buy my tools

If valid credentials are entered, access is granted to the main tool interface.

---

## 🚀 Usage Guide

### Run the tool:

```bash
sudo python start.py
```

### Available Commands:

| Command      | Description                      |
| ------------ | -------------------------------- |
| `1`        | Update Script |
| `2`        | Launch TCP / UDP attack       |
| `3` | HTTP Flooding                    |
| `4`       | Nmap Feature                  |
| `5`       | Exit the tool                    |

---

## 📡 Attack Modes

### 🔹 UDP Flood

* **Plain**: Sends `b"A" * size` continuously
* **Random**: Sends random bytes of defined size

### 🔹 TCP Flood

* **SYN Flood (Single/Multi)**: Repeated TCP connection attempts
* **Data Flood (Single/Multi)**: Continuous data payload on TCP

### 🔹 HTTP Flood

* Random GET/POST/HEAD requests with spoofed headers and paths

---

## 📁 Required Files

* `useragents.txt` — (must) list of user-agents, one per line.

If not found,use ua.py for create the useragent (only input 10000 user agent dont too much)

---

## ⚙️ Example Attack Flow

1. **Login** → Enter username & password (from Pastebin)
2. **Choose Command** → `udp`, `tcp`, `http-flood`
3. **Select Sub-Method** → e.g., `random` for UDP
4. **Input Target Parameters** → IP, port, duration, packet size
5. **Launch** → Tool shows attack status in real-time

---

## ❌ KeyboardInterrupt

Press `Ctrl + C` at any time during attack to cancel and return to main menu.

---

## 📣 Notes

* Tool will auto-clear screen and show banner each time a command is selected.
* All network activities are local — no logging or uploads occur.

---

## 🧪 Disclaimer

KENSPLOIT is strictly for **educational & stress testing** purposes **with permission** of the target.
Any unauthorized use is **not the responsibility of the author.**

---

## 🔗 Credits

* Built by \[KenXploit 🔥]
* ASCII Banner powered by `rich`
* Inspired by tools like LOIC, HOIC, and custom pentest utilities

---

## 🧵 Contribution

Feel free to fork and contribute. Pull requests welcome.
