__author__ = "Markus"
import tkinter
from tkinter import *
import tkinter.messagebox

import webbrowser

#tkinter gui, set up a window, have a link to typing practice website
#https://www.typingclub.com/typing-qwerty-en.html

def goToWebsite():
    #will open in chrome
    url = "https://www.typingclub.com/typing-qwerty-en.html"
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s' #protip: must use linux like forward slashes (/) even on windows in this case
    webbrowser.get(chrome_path).open(url)
    #webbrowser.open(url)


def main():
    root = tkinter.Tk()
    h=100
    w=200
    ws = root.winfo_screenwidth() # width of the screen
    hs = root.winfo_screenheight() # height of the screen

    # calculate x and y coordinates for the Tk root window
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root.geometry("%dx%d+%d+%d" % (w,h,x,y))
    title = Label(root,text="Where to find typing skills!")
    title.pack()

    tkinter.messagebox.showinfo("Welcome!","Merry Christmas Dad!")
    leftFrame = Frame(root)
    leftFrame.pack(side=LEFT)

    rightFrame = Frame(root)
    rightFrame.pack(side=RIGHT)

    startButton = Button(leftFrame,text="Typing Lessons website",fg="purple",command=goToWebsite)
    startButton.pack()

    exitButton = Button(rightFrame,text="Exit",fg="red",command=exit)
    exitButton.pack()
    root.mainloop()


main()