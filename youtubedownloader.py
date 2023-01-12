import tkinter as tk
from tkinter import messagebox
from tkinter import GROOVE
from tkinter.filedialog import askdirectory
from pytube import YouTube

window = tk.Tk()
window.title("Youtube Downloader")
window.minsize(450, 200)
window.maxsize(450, 200)


def widgets():
    link_label = tk.Label(window, text="Video link")
    link_label.grid(row=0, padx=20, pady=20, column=0)
    link_label.config(font=("None", 15), fg="blue")

    link_input = tk.Entry(window, width=30, textvariable=video_link)
    link_input.grid(row=0, column=1)

    place_label = tk.Label(window, text="Directory")
    place_label.grid(row=1, column=0)
    place_label.config(font=("None", 15))

    place_input = tk.Entry(window, width=30, textvariable=download_dir)
    place_input.grid(row=1, column=1)

    place_btn = tk.Button(window, text="Open", width=10, fg="blue", command=browse)
    place_btn.grid(row=1, column=3, padx=20)

    download_btn = tk.Button(window, text="Download", command=download)
    download_btn.grid(row=2, column=1, pady=15)
    download_btn.config(height=2, width=15, bg="blue", fg="white")


def browse():
    directory = askdirectory(initialdir="YOUR DIRECTORY PATH", title="save")
    download_dir.set(directory)


def download():
    link = video_link.get()
    save_dir = download_dir.get()
    yt = YouTube(link)
    yt.streams.first().download(save_dir)
    messagebox.showinfo(title="success", message="Download is successfully")


download_dir = tk.StringVar()
video_link = tk.StringVar()
widgets()

window.mainloop()
