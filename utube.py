"""
Youtube video downloader
"""
import tkinter as tk
from tkinter import  ttk
import youtube_dl

quality = ['1080', '720', '480', '360']
root = tk.Tk()
root.geometry('500x300')
root.title('Youtube Downloader')

view = tk.Frame(root)
view.pack(side=tk.TOP)
rez = tk.StringVar()
url = tk.StringVar()

L1 = tk.Label(view, text= 'Enter youtube url:')
L1.pack(pady=10)
E1 = tk.Entry(view,textvariable=url)
E1.pack()
q= ttk.OptionMenu(view, rez, quality[3], *quality)
q.pack(side=tk.RIGHT, pady=10)


def youtube():
    ytb_url=url.get()
    print('ytb_url')
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([ytb_url])

B1 = ttk.Button(view, text="Download", command=youtube)
B1.pack(pady=10)
root.mainloop()
