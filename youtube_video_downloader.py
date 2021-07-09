from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube
from PIL import ImageTk,Image
import os
import time
folder_name=""
l=[]
abc=""
file_size=0
max_file_size=0
def back():
    root.quit()
def open_directry():
    global folder_name
    folder_name=filedialog.askdirectory()

    if len(folder_name)>1:
        location_error.config(text=folder_name, fg="green")
    else:
        location_error.config(text="Please choose a valid folder",fg="red")
def download_file():
    global max_file_size,file_size
    choice=choices.get()
    video=link.get()
    if len(video)>1:
        link_error.config(text='')
        print(video,"at",folder_name)
        yt=YouTube(video)
        name=str(yt.title)
        for i in(name):
            l.append(i)
            if len(l)%20==0:
                    print(l)
                    v_name.config(text=l, fg="green")
                #v_name.config(text="\n", fg="green")

        print(len(l))

        if choice==format_choice[0]:
            print("720p video is downloading")
            loading.config(text="720p file is downloading...")
            select_video=yt.streams.filter(progressive=True).first()
        elif choice==format_choice[1]:
            print("144p video is downloading")
            loading.config(text="144p file is downloading...")
            select_video = yt.streams.filter(progressive=True,file_extension='mp4').last()
        elif choice==format_choice[2]:
            print("3gp video is downloading")
            loading.config(text="144p file is downloading...")
            select_video = yt.streams.filter(file_extension='3gp').first()
        elif choice==format_choice[3]:
            print("mp3 is downloading")
            loading.config(text="mp3 file is downloading...")
            select_video = yt.streams.filter(only_audio=True).first()
        selected_video=select_video
        file_size=selected_video.filesize
        max_file_size=(file_size/1024000)
        MB=str(max_file_size)+ " MB"
        print('file size= : {:00.00f}'.format(max_file_size),"MB")
            #download
        selected_video.download(folder_name)
        complete()
    else:
        link_error.config(text="*please give a valid link", fg="red")


"""""
def progress_check(stream,chunk,file_handle,bytes_remaining):
    percent=(float(abs(1-bytes_remaining)/file_size)*100)
    print("downloading : {:00.0f} %".format(percent))
"""""
def complete():
    loading.config(text="Download complete")
root=Tk()
root.geometry("450x700")
#root.configure(bg="black")
b_image=ImageTk.PhotoImage(file = "C:\\Users\\Prasanta Banerjee\\webprojects\\webpyconda\\blog\\static\\blog\\bgrnd.png")

backgrnd=Label(root,image=b_image,bd=0)
backgrnd.grid()
root.title("YOUTUBE VIDEO DOWNLOADER")
root.grid_columnconfigure(0,weight=1)
utube_link_label=Label(root,text="Paste the YouTube link here:-",fg="blue",font=('Agency FB',30))
utube_link_label.grid()
link_var=StringVar()
link=Entry(root,width=50,textvariable=link_var)
link.grid(ipady=12)

link_error=Label(root,text='',fg="blue",font=('Agency FB',20,'bold'))
link_error.grid(pady=(0,10))
save_file=Label(root,text="Choose the location to download",fg="blue",font=('Agency FB',20,'bold'))
save_file.grid()
save_folder=Button(root,width=15,bg="green",fg='white',text='Choose folder',font=('Arial',20,'bold'),command=open_directry)
save_folder.grid()
location_error=Label(root,text=abc,fg="blue",font=('Agency FB',20,'bold'))
location_error.grid(pady=(0,0))

choose_format=Label(root,text="Choose the format",font=('Agency FB',20,'bold'))
choose_format.grid()
format_choice=["Mp4 720p",
               "Mp4 144p",
               "Video 3gp",
               "song Mp3 128 kbps"]
choices=ttk.Combobox(root,value=format_choice)
choices.grid(pady=(0,60))
download=Button(root,width=15,bg="green",fg='white',text='Download',font=('Arial',20,'bold'),command=download_file)
download.grid(pady=(0,10))
loading=Label(root,text='Devolped by Prasanta Banerjee',fg='black',font=('Arial',20,'bold'))
loading.grid()
v_name=Label(root,text='',fg='dark blue',font=('Arial',20,'bold'))
v_name.grid()

quit=Button(root,text='Cancel',fg='white',font='bold 10',bg='green',command=back)
quit.grid()
root.mainloop()

#https://xWOoBJUqlbI