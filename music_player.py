import os
import tkinter.messagebox
from tkinter import *
from tkinter import filedialog

from pygame import mixer

root = Tk()

# Create the menubar
menubar = Menu(root)
root.config(menu=menubar)

# Create the submenu
subMenu = Menu(menubar, tearoff=0)

def browse_file():
    global filename
    filename = filedialog.askopenfilename()

menubar.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Open", command=browse_file)
subMenu.add_command(label="Exit", command=root.destroy)

def about_us():
    tkinter.messagebox.showinfo('About Melody', 'This is music player Build using Python Tkinter by @apurv_dhadankar')

subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=subMenu)
subMenu.add_command(label="About_Us", command=about_us)

mixer.init()    # Initializing the mixer
mixer.music.load("path") # Load the song

root.geometry('400x400')
root.title('Melody')
root.iconbitmap(r'pause.png')

text = Label(root, text='Lets make some noise!')
text.pack()

def play_music():
    mixer.music.play()
    statusbar['text'] = "Music Played"

def stop_music():
    mixer.music.stop()
    statusbar['text'] = "Music Stopped"

def pause_music():
    global paused
    mixer.music.pause()
    statusbar['text'] = "Music Paused"

def set_vol(val):
    volume = int(val) / 100
    mixer.music.set_volume(volume)
    # set_volume of mixer takes value only from 0 to 1. Example - 0,0.1, 0.55, 0.54.0.9,1

# playPhoto = PhotoImage(file='play.jpg')
playBtn = Button(root, text="Play", bg="yellow", width=10, command=play_music)
#  image=playPhoto,
playBtn.pack()

# stopPhoto = PhotoImage(file='stop.jpg')
stopBtn = Button(root, text="Stop", bg="yellow", width=10, command=stop_music)
stopBtn.pack()

# pausePhoto = PhotoImage(file='pause.png')
pauseBtn = Button(root, text="Pause", bg="yellow", width=10, command=pause_music)
pauseBtn.pack()

scale = Scale(root, bg="grey", from_=0, to=100, orient=HORIZONTAL, command=set_vol)
scale.set(70)
mixer.music.set_volume(0.7)
scale.pack()

statusbar = Label(root, text="Welcome to Melody", relief=SUNKEN, anchor=W)
statusbar.pack(side=BOTTOM, fill=X)

root.mainloop()

