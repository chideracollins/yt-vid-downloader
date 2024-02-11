import tkinter as tk
from tkinter import filedialog
from downloader import download_vid


def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"You selected {folder} folder.")
    return folder


root = tk.Tk()
root.withdraw()
video_url = input("Please enter a YouTube video url: ")
save_path = open_file_dialog()
download_vid(video_url, save_path)
