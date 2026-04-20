import tkinter as tk
from tkinter import messagebox, scrolledtext
import threading
import os
from connector import establish_connection
from backend import run_segregation_backup

def start_backup_thread():
    # Run the backup in a separate thread so the window stays active
    threading.Thread(target=process_backup, daemon=True).start()

def process_backup():
    ip = ip_entry.get().strip()
    # Change this path to your preferred backup location
    destination = r"C:\Users\tarap\Phone_Backup\Full_Mobile_Backup"
    
    if not ip:
        messagebox.showerror("Error", "Please enter your Phone's IP address")
        return
    
    log_area.insert(tk.END, f"> Attempting connection to {ip}...\n")
    log_area.see(tk.END)
    
    device = establish_connection(ip)
    
    if device:
        log_area.insert(tk.END, "> Connection Successful!\n")
        log_area.insert(tk.END, f"> Target Folder: {destination}\n")
        log_area.insert(tk.END, "> Starting Full Sweep (this will take a while)...\n")
        log_area.see(tk.END)
        
        try:
            # This calls the updated 'Full Sweep' logic in backend.py
            run_segregation_backup(device, destination)
            
            log_area.insert(tk.END, "\n" + "="*30 + "\n")
            log_area.insert(tk.END, "   BACKUP COMPLETED!\n")
            log_area.insert(tk.END, "="*30 + "\n")
            messagebox.showinfo("Success", f"All data backed up to {destination}")
        except Exception as e:
            log_area.insert(tk.END, f"> Error during backup: {str(e)}\n")
    else:
        log_area.insert(tk.END, "> Error: Device not found. Ensure Wireless Debugging is ON.\n")
    log_area.see(tk.END)

# --- GUI Layout ---
root = tk.Tk()
root.title("Android Wireless Pro Backup")
root.geometry("600x500")
root.configure(bg="#f0f0f0")

# Header
tk.Label(root, text="Wireless Mobile Backup Tool", font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=10)

# IP Input
frame_ip = tk.Frame(root, bg="#f0f0f0")
frame_ip.pack(pady=10)
tk.Label(frame_ip, text="Phone IP:", font=("Arial", 10), bg="#f0f0f0").pack(side=tk.LEFT)
ip_entry = tk.Entry(frame_ip, width=20, font=("Arial", 10))
ip_entry.insert(0, "10.2.8.98") 
ip_entry.pack(side=tk.LEFT, padx=5)

# Start Button
start_btn = tk.Button(root, text="START FULL BACKUP", command=start_backup_thread, 
                      bg="#2ecc71", fg="white", font=("Arial", 12, "bold"), width=25)
start_btn.pack(pady=15)

# Activity Log
tk.Label(root, text="Activity Log:", bg="#f0f0f0").pack()
log_area = scrolledtext.ScrolledText(root, width=70, height=15, font=("Consolas", 9))
log_area.pack(pady=5, padx=10)

root.mainloop()