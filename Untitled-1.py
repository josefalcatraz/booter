import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import sys
import os
import re
import urllib.request

def resource_path(relative_path):
    """ Get absolute path to resource, works for PyInstaller and dev """
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

def download_if_missing(filename, url):
    """Download file from URL if it doesn't exist locally."""
    if not os.path.exists(filename):
        try:
            print(f"Downloading {filename}...")
            urllib.request.urlretrieve(url, filename)
            print(f"{filename} downloaded successfully.")
        except Exception as e:
            messagebox.showerror("Download Error", f"Failed to download {filename}.\n{e}")
            sys.exit(1)

def validate_and_attack():
    ip = ip_entry.get()
    port = port_entry.get()
    power = power_entry.get()

    # Validate IP
    if not re.match(r"^\d{1,3}(\.\d{1,3}){3}$", ip):
        messagebox.showerror("Error", "IP Not Found")
        return

    # Validate Port
    if not (port.isdigit() and len(port) == 5):
        messagebox.showerror("Error", "Port Not Found")
        return

    # Validate Power
    if not power.isdigit() or int(power) > 1000:
        messagebox.showerror("Error", "Too Much Power")
        return

    messagebox.showinfo("Success", "Attack Sent")

# URLs for resources — replace with your actual file URLs!
BG_URL = "https://skreet.milf-hunter.lol/content/cdn/omZqxQKAamvQ.png"
ICON_URL = "https://skreet.milf-hunter.lol/content/cdn/gOTwnSPfjLQp.ico"

# Download resources if missing before loading GUI
download_if_missing("background.png", BG_URL)
download_if_missing("anonymous.ico", ICON_URL)

# Create main window FIRST
root = tk.Tk()
root.title("fent overdoser")
root.geometry("400x300")
root.resizable(False, False)

# Load and display background image AFTER root created
bg_image = Image.open(resource_path("background.png"))
bg_image = bg_image.resize((400, 300), Image.Resampling.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

background_label = tk.Label(root, image=bg_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Add UI elements on top of the background
tk.Label(root, text="IP", bg="#ffffff").place(x=80, y=50)
ip_entry = tk.Entry(root)
ip_entry.place(x=170, y=50)

tk.Label(root, text="Port", bg="#ffffff").place(x=80, y=90)
port_entry = tk.Entry(root)
port_entry.place(x=170, y=90)

tk.Label(root, text="Power (fent mg)", bg="#ffffff").place(x=80, y=130)
power_entry = tk.Entry(root)
power_entry.place(x=170, y=130)

tk.Button(root, text="Attack", command=validate_and_attack).place(x=160, y=180)

# Custom texts at top-left
header = tk.Label(root, text="Fent Gigabooter", font=("Arial", 12, "bold"), bg="#ffffff")
header.place(x=10, y=10)

watermark = tk.Label(root, text="Made by Skreet", font=("Arial", 7, "bold"), fg="black", bg="#ffffff")
watermark.place(x=10, y=35)

# Set window icon
root.iconbitmap(resource_path("anonymous.ico"))

root.mainloop()