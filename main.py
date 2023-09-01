from pytube import YouTube

class Download:
  def __init__(self, highest=False, lowest=False, get_by_resolution=False, stream_extension='mp4'):
    self.highest = highest
    self.lowest = lowest
    self.get_by_resolution = get_by_resolution
    self.youtube_downloader()
    self.yt = YouTube(self.url)
    self.video = self.yt.streams.filter(file_extension=stream_extension)
    self.get()
  
  def youtube_downloader(self):
    self.url = input('masukan url / link yang akan di download : ')
    method = input("""
    Pilih metode yang diinginkan ... 
    1. resolution tertinggi
    2. resolution terendah
    3. pilih resolution
    """)
    if method == '1':
      self.highest = True
    elif method == '2':
      self.lowest = True
    elif method == '3':
      self.get_by_resolution = True

  def info(self):
    print('Title  : ',self.yt.title)
    print('Author : ',self.yt.author)
    print('Length : ',self.yt.length)

    
  def get(self):
    self.info()
    if self.highest:
      stream = self.video.get_highest_resolution()
    elif self.lowest:
      stream = self.video.get_lowest_resolution()
    elif self.get_by_resolution:
      stream = self.download_by_resolution()
    print('Downloading ... ')
    stream.download()
    print('Complete')

  def download_by_resolution(self):
    print('list resolution : ... ')
    resolution = []
    i = 1
    for stream in self.video.order_by('resolution'):
      print(i ,'. ', stream.resolution)
      resolution.append(stream)
      i += 1

    res = int(input('pilih resolution : '))
    return resolution[res-1]
    
    
Download()
