import ctypes
import os
import urllib.request


def download_web_image(url):
        name = ("alien" + ".jpg")
        myPath = ("C:\\Users\\Public\\Downloads")
        full_name = os.path.join(myPath, name)
        urllib.request.urlretrieve(url, full_name)


download_web_image("https://cdntube.b-cdn.net/thumbnails/8957b962930e15130dc51689276aab62a2877db2.jpg")


WALLPAPER_PATH = "C:\\Users\\Public\\Downloads\\alien.jpg"
ctypes.windll.user32.SystemParametersInfoW(20,0,WALLPAPER_PATH,3)


