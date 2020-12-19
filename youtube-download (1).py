from pytube import YouTube
import os
from tkinter import *

root=Tk()
root.geometry('600x200')
root.title('Youtube Video Downloader')


Label_1=Label(root,text="Paste The Youtube Link Here", font=("bold",20))
Label_1.place(x=120,y=20)


mylink=StringVar()

pastelink=Entry(root, width=60, textvariable=mylink)
pastelink.place(x=140, y=80)

#link="https://youtu.be/S19UcWdOA-I"

def downloadVideo():
    x=str(mylink.get())
    ytvideo=YouTube(x).streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if not os.path.exists('D:\'):
        os.makedirs('D:\')
    ytvideo.download('D:\e') 

Button(root,text="Download Video", width=20, bg='green',fg="white", command=downloadVideo).place(x=220, y=110)

root.mainloop()
