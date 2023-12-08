from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def download():
    video_url = url_entry.get()
    save_path = filedialog.askdirectory()

    try:
        yt = YouTube(video_url)
        video = yt.streams.filter(file_extension='mp4', progressive=True).first()
        video.download(save_path)
        status_label.config(text="Download completed!")
    except Exception as e:
        status_label.config(text=f"Error:")
        
app = tk.Tk()
app.title("YT Video Downloader")

url_label = tk.Label(app, text="Enter Videoss URL:")
url_label.pack(pady=10)

url_entry = tk.Entry(app, width=50)
url_entry.pack(pady=10)

download_button = tk.Button(app, text="Download", command=download)
download_button.pack(pady=20)

status_label = tk.Label(app, text="")
status_label.pack(pady=10)

app.mainloop()
