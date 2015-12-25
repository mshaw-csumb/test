__author__ = "Markus"

import os
from os import listdir
from os.path import isfile,join
import tkinter
from tkinter import *
import tkinter.messagebox
from PIL import Image, ImageTk, ImageWin, ImageDraw

import ctypes

start = 0
from threading import Timer

def changeWallpaper(start):#print pathname
    #get pathname
    #print pathname
    pos = start
    currentDir = os.getcwd()
    currentDir = currentDir + "\pics\\"
    pictures = [f for f in listdir(currentDir) if isfile(join(currentDir, f))]
    print(currentDir +  pictures[pos]);
    wallpaper =  currentDir + pictures[pos] ##

    global imageLabel
    #image = Image.open(wallpaper)
    #photo = ImageTk.PhotoImage(image)
    #photo.show()


   # window = tkinter.Tk()
    img = Image.open(wallpaper)
    img.load()
    #img.show()
    # = ImageDraw.Draw(img)
    #dib = ImageWin.Dib(img,size=NONE)

    root = tkinter.Tk()
    canvas = tkinter.Canvas(root, width=500, height=500)
    canvas.pack()
    img = Image.open(wallpaper)
    tk_img = ImageTk.PhotoImage(img)
    canvas.create_image(250, 250, image=tk_img)
    root.mainloop()

    #hwnd = ImageWin.HWND(window.winfo_id())
    #dib.draw(hwnd, dst=(0,0,500,500),src=NONE)

    photoimg = ImageTk.PhotoImage(img)
    #container = tkinter.Label(window, image=photoimg)
    #container.pack()
    #label = Label(image=photoimg)
    #label.image = photoimg # keep a reference!
    #label.pack()

    #tkinter.mainloop()
    #imageLabel.image = photo
    #SPI_SETDESKWALLPAPER = 20
    #ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, 'r'+wallpaper , 0)
    pos += 1
    return pos

def startMethod():
    global start
    currentDir = os.getcwd()
    currentDir = currentDir + "\pics\\"
    pictures = [f for f in listdir(currentDir) if isfile(join(currentDir, f))]

    if start >= len(pictures):
        start = 0
    start = changeWallpaper(start)

def trigger():
    while(True):
        t = Timer(30.0,startMethod)
        t.start()





root = tkinter.Tk()

h=100
w=225
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry("%dx%d+%d+%d" % (w,h,x,y))


title = Label(root,text="Christmas Slideshow Manager")
title.pack()

tkinter.messagebox.showinfo("Welcome!","Merry Christmas Mom!")

leftFrame = Frame(root)
leftFrame.pack(side=LEFT)
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)
rightFrame = Frame(root)

rightFrame.pack(side=RIGHT)

startButton = Button(leftFrame,text="Cycle wallpaper",fg="purple",command=startMethod)
startButton.pack()

exitButton = Button(rightFrame,text="Exit",fg="red",command=exit)
exitButton.pack()

imageLabel = Label(bottomFrame,text="Picture")
imageLabel.pack()
root.mainloop()


#keepGoing = True



