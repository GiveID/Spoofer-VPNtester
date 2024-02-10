import tkinter as tk
from tkinter import messagebox
import uuid
import socket
import os

# Function to get the HWID
def get_hwid():
    return str(uuid.getnode())

# Function to get the IP address
def get_ip():
    hostname = socket.gethostname()
    return socket.gethostbyname(hostname)

# Ban management
ban_file = 'bans.txt'

def is_banned():
    hwid = get_hwid()
    ip = get_ip()
    with open(ban_file, 'r') as file:
        bans = file.readlines()
    for ban in bans:
        if hwid in ban or ip in ban:
            return True
    return False

def ban_hwid():
    with open(ban_file, 'a') as file:
        file.write(get_hwid() + '\n')
    messagebox.showinfo("Ban", "HWID banned successfully.")

def ban_ip():
    with open(ban_file, 'a') as file:
        file.write(get_ip() + '\n')
    messagebox.showinfo("Ban", "IP banned successfully.")

def delete_ban():
    hwid = get_hwid()
    ip = get_ip()
    with open(ban_file, 'r') as file:
        bans = file.readlines()
    with open(ban_file, 'w') as file:
        for ban in bans:
            if hwid not in ban and ip not in ban:
                file.write(ban)
    messagebox.showinfo("Ban", "Ban deleted successfully.")

# GUI
def setup_gui():
    root = tk.Tk()
    root.title("Spoofer/VPN testing GUI")
    
    if is_banned():
        messagebox.showwarning("Banned", "BANNED/SPOOFER/VPN DIDN'T WORK")
        root.destroy()
        return

    tk.Button(root, text="Ban HWID", command=ban_hwid).pack(pady=10)
    tk.Button(root, text="Ban IP", command=ban_ip).pack(pady=10)
    tk.Button(root, text="Delete Ban", command=delete_ban).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    if not os.path.exists(ban_file):
        open(ban_file, 'w').close()
    setup_gui()
