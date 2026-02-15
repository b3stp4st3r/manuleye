import os
import tkinter as tk
from tkinter import filedialog


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def select_file():
    root = tk.Tk()
    root.withdraw()
    root.attributes("-topmost", True)
    file_path = filedialog.askopenfilename()
    root.destroy()
    return file_path


def validate_ip(ip):
    import re
    ipv4_pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    ipv6_pattern = r'^([0-9a-fA-F]{0,4}:){7}[0-9a-fA-F]{0,4}$'
    
    if re.match(ipv4_pattern, ip):
        parts = ip.split('.')
        return all(0 <= int(part) <= 255 for part in parts)
    elif re.match(ipv6_pattern, ip):
        return True
    return False
