from ppadb.client import Client as AdbClient
import subprocess

def establish_connection(ip, port="5555"):  # <--- Make sure this matches!
    try:
        subprocess.run(f"adb connect {ip}:{port}", shell=True)
        client = AdbClient(host="127.0.0.1", port=5037)
        device = client.device(f"{ip}:{port}")
        return device
    except Exception as e:
        print(f"Connection failed: {e}")
        return None