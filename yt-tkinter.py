from tkinter import *
from tkinter import ttk
from pytube import YouTube

class Gui:
  def __init__(self, url):
    self.root = Tk()
    self.empty = True
    self.root.geometry('400x400')
    self.root.title('Simple Youtube Downloader')
    self.Frame()
    self.root.mainloop()

  def Frame(self):
    self.frame1 = ttk.Frame()
    self.frame2 = ttk.Frame()
    self.frame3 = ttk.Frame()
    self.url = ttk.Entry(self.frame1)
    self.url.focus()
    self.url.pack(side=LEFT, padx=10, pady=5)
    button = ttk.Button(self.frame1, text='Get Info', command=self.getInfoUrl)
    button.pack(side=RIGHT, padx=10, pady=5)
    self.frame1.pack(side=TOP, padx=10)
    self.frame2.pack(side=TOP, padx=10)
    self.frame3.pack(side=BOTTOM, padx=10)
  def destroy(self):
    if not self.empty:
        self.title.destroy()
        self.author.destroy()
        self.length.destroy()
        self.resolution.destroy()
        self.download.destroy()
        self.choice.destroy()

  def getInfoUrl(self):
    self.destroy()
    self.yt = YouTube(self.url.get())
    self.video = self.yt.streams.filter(file_extension='mp4', progressive=True)
      
    self.title = ttk.Label(self.frame2, text=f"Title  : {self.yt.title}", justify='left', anchor='w')
    self.author = ttk.Label(self.frame2, text=f"Author  : {self.yt.author}", justify='left', anchor='w')
    self.length = ttk.Label(self.frame2, text=f"Length  : {self.yt.length}", justify='left', anchor='w')
    
    self.choice = ttk.Label(self.frame3, text="Pilih Resolusi", justify='left', anchor='w')
    self.empty = False

    res = []
    
    for stream in self.video.order_by('resolution'):
    #   self.res[stream.resolution] = stream
      if stream.resolution not in res:
        res.append(stream.resolution)

    self.clicked = StringVar()
    self.clicked.set(res[0])
    self.resolution = ttk.OptionMenu(self.frame3, self.clicked, *res)
    self.download = ttk.Button(self.frame3, text="Download", command=self.download)
    
    

    self.title.pack(fill='both', padx=5, pady=5)
    self.author.pack(fill='both', padx=5, pady=5)
    self.length.pack(fill='both', padx=5, pady=5)
    self.choice.pack(fill='both', padx=5, pady=5)
    self.resolution.pack(fill='both', padx=5, pady=10)
    self.download.pack(padx=5, pady=10)
  def download(self):
    
    self.downloading = ttk.Label(self.frame3, text='Downloading ...')
    self.downloading.pack(padx=5, pady=5)
    

    self.video.get_by_resolution(self.clicked.get()).download()
    # self.res.get(self.clicked.get()).download()
    self.downloading.configure(text="Download selesai ...")


# https://youtu.be/Vqpa3KFFZEk?si=5TL_g7ItXyyY2CjC
    



Gui('url')




