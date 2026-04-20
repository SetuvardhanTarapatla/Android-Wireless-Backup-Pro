# Android Wireless Backup Pro 📱💻

Developed by **Setuvardhan Tarapatla**

A robust Python-based utility designed to wirelessly migrate data from Android devices to a PC. This tool was specifically built to bypass the common "Permission Denied" and "Scoped Storage" issues found in modern Android versions (11+) when transferring large datasets (10GB+).

## 🚀 Key Features
* **Wireless Connection:** Uses ADB over TCP/IP (Port 5555) for cable-free transfers.
* **Multi-Threaded GUI:** Built with Tkinter; the interface remains responsive during long file transfers.
* **Recursive File Pulling:** Mirrors the phone's directory structure (DCIM, WhatsApp, Documents) on your PC.
* **Data Integrity:** Identifies and pulls individual files to ensure no data is lost due to folder-level permission locks.

## 🛠️ Tech Stack
* **Language:** Python 3.12
* **Libraries:** `pure-python-adb`, `tkinter`, `threading`
* **Protocol:** Android Debug Bridge (ADB)

## 📂 Project Structure
- `main_gui.py`: The primary user interface.
- `backend.py`: The core logic for file discovery and transfer.
- `connector.py`: Handles the wireless handshake with the Android device.

## ⚙️ Setup
1. Enable **Developer Options** and **Wireless Debugging** on your Android device.
2. Install dependencies: `pip install pure-python-adb`.
3. Run `python main_gui.py` and enter your phone's IP address.
