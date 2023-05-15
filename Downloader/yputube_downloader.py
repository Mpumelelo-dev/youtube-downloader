import time
from tkinter import ttk, filedialog, messagebox
from urllib import request
import requests
from pytube import YouTube
from tkinter import*









def main_page():
    root = Tk()
    
    
    
    root.title("YouTube Downloader")
    root.geometry("500x350")
    
    
    bg_image = PhotoImage(file="images/background image.png")
    bg_label = Label(root, image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    root.resizable(width=False, height=False)
    global frame1,save_path,path_list
    top = Frame(root)
    top.pack(side=TOP, anchor=N, padx=10)
    
    top = Frame(root)
    top.pack(side=TOP, anchor=N, padx=10)
    
    frame1 = Frame(top)
    frame1.pack(side=TOP,anchor=N,padx=10)
    
    def checkConnection():
        url = "https://www.google.com"
        timeout = 5
        try:
            request = requests.get(url,timeout=timeout)
            return True
        except:
            return False
        
    if checkConnection() == True:
        lbl = Label(frame1, text="Internet Connected", font= 'san-serif 14 bold',foreground="green").pack()
    elif checkConnection()== False:
        lbl = Label(frame1, text="Internet Disconnected", font= 'san-serif 14 bold', foreground="red").pack()
    
    def select():
        global save_path, path_list
        path = filedialog.askdirectory()
        path_list.set(path)
        save_path= f"{path}"
        
    def check_details():
        root.geometry("550x700")
        root.resizable(width=False, height=False)
        
        url = YouTube(str(link.get()))
        
        if link.get() == "":
            messagebox.showerror("Link Error", "Please paste a youtube link")
        else:
            try: 
                video_tittle.set(url.title)
                video_views.set(url.views)
                video_author.set(url.author)
                duration = time.strftime("%H:%M:%S", time.gmtime(url.length))
                video_length.set(duration)
                video_upload.set(url.publish_date)
            except:
                messagebox.showerror("Link Error", "Please paste a youtube link")
              
              
        lbl = Label(frame4, text="Video Tittle", font= 'san-serif 14 bold').grid(row=0,column=0)
        lbl = Label(frame4, text="", font= 'san-serif 14 bold',textvariable=video_tittle).grid(row=1,column=0)
        lbl = Label(frame4, text="Video View(s)", font= 'san-serif 14 bold').grid(row=2,column=0)
        lbl = Label(frame4, text="", font= 'san-serif 14 bold',textvariable=video_views).grid(row=3,column=0)
        lbl = Label(frame4, text="Video Length", font= 'san-serif 14 bold').grid(row=4,column=0)
        lbl = Label(frame4, text="", font= 'san-serif 14 bold',textvariable=video_length).grid(row=5,column=0)
        lbl = Label(frame4, text="Video Author", font= 'san-serif 14 bold').grid(row=6,column=0)
        lbl = Label(frame4, text="", font= 'san-serif 14 bold',textvariable=video_author).grid(row=7,column=0)
        lbl = Label(frame4, text="Date Uploaded", font= 'san-serif 14 bold').grid(row=8,column=0)
        lbl = Label(frame4, text="", font= 'san-serif 14 bold',textvariable=video_upload).grid(row=9,column=0)

        
        more_button()
        
        
    def download_video():
         
        if path_list.get() == "":
            messagebox.showerror("Path Error", "Please choose a path")
            
        else:
            url = YouTube(str(link.get()))
            
            video_D = url.streams.filter(progressive= True).get_highest_resolution()
            video_D.download(save_path)
            
    def download_audio():
         
        if path_list.get() == "":
            messagebox.showerror("Path Error", "Please choose a path")
            
        else:
            url = YouTube(str(link.get()))
            
            audio_D = url.streams.filter(only_audio= True).first()
            audio_D.download(save_path)
    
    def more_button():
        frame5 = Frame(top)
        frame5.pack(pady=10)
        
        btn = Button(frame5,text="Download Video", command=download_video,font= 'san-serif 14 bold',foreground="white", background="red").grid(row=0, column=0)
        btn = Button(frame5,text="Download Audio", command=download_audio,font= 'san-serif 14 bold',foreground="white", background="red").grid(row=0, column=1)
        
    lbl = Label(frame1, text="Download YouTube videos for free", font= 'san-serif 14 bold').pack()
    
    frame2 = Frame(top)
    frame2.pack(pady=10)
    
    link = StringVar()
    
    lbl = Label(frame2, text="Paste your link here!", font= 'san-serif 14 bold').pack()
    entry= Entry(frame2, width=60, textvariable=link).pack()
    btn = ttk.Button(frame2, text="Clear").pack()
    
    frame3 = Frame(top)
    frame3.pack(pady=10)
    
    path_list = StringVar()
    
    lbl = Label(frame3, text="Choose path to save", font= 'san-serif 14 bold').grid(row=0,column=0)
    btn = ttk.Button(frame3,text="Select", command=select).grid(row=0, column=1)
    lbl = Label(frame3, text="Path selected", font= 'san-serif 14 bold').grid(row=1,column=0)
    lbl = Label(frame3, text="", font= 'san-serif 14 bold',textvariable=path_list).grid(row=1,column=1)
    
    frame4 = Frame(top)
    frame4.pack(pady=10)
    
    video_quality = StringVar()
    video_tittle = StringVar()
    video_views = StringVar()
    video_length = StringVar()
    video_author = StringVar()
    video_upload = StringVar()
    
    
    
    btn = Button(frame4,text="Check", command=check_details,font= 'san-serif 14 bold',foreground="white", background="red").grid(row=0, column=0)
    
    
    
    checkConnection()
    root.mainloop()
    
main_page()
    
    
    