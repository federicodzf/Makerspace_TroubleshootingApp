import os
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import sys
import datetime

class gui():
    # static class variable of the background color
    bgColor = "#34A2FE"
    # static variables to change grid size in window depending on next changes
    cols = 3
    rows = 3

    def __init__(self):
        self.masterWindow = tk.Tk() # create the tkinder object 
        self.masterWindow.title("Printer Troubleshooting Guide")
        # Set standard size of window
        self.masterWindow.geometry("500x500+400+250")
        self.masterWindow.configure(bg=gui.bgColor)

        # Add Exit button
        self.addExitButton()
        # Add text frame
        self.createTextFrame()
        # Add intiial basic question text
        self.addQuestion("Does the printer turn on?")
        # Add button frame 
        self.createButtonFrame()

        self.addYesBtn()
        self.addNoBtn()

        ## Make program event-driven
        self.masterWindow.mainloop()
 
    def addExitButton(self):
        # create exit btn frameconda 
        self.exitBtnFrame = tk.Frame(self.masterWindow,bg="green")
        self.exitBtnFrame.pack(side=BOTTOM, anchor=E)
        # Exit button 
        self.exit_btn = tk.Button(self.exitBtnFrame, text="Exit", command=self.quitWindow,relief=tk.RAISED, bg="red")
        self.exit_btn.pack(anchor=W,side=RIGHT, ipadx=10, ipady=10)
        self.masterWindow.protocol("WM_DELETE_WINDOW", self.quitWindow) 
        
    def quitWindow(self):
        # Need to ask client if they are sure they want to exit
        self.masterWindow.destroy() # close window

    def createTextFrame(self):
        self.txtFrame = tk.Frame(
            master=self.masterWindow,
            height=200,
            bg=gui.bgColor,
            padx=20, pady=20)
        self.txtFrame.pack(side=TOP, fill=BOTH)

    def addQuestion(self,msg):
        # Create Intro message
        self.lbl_intro = tk.Label(
            master=self.txtFrame,
            anchor='w',
            text=msg,
            font=(120),
            fg='black',
            bg=gui.bgColor)
        self.lbl_intro.pack()

    # Method that creates a button Frame
    def createButtonFrame(self):
        self.buttons_frame = Frame(
            master=self.masterWindow,
            height=100,
            bg="green",)
        self.buttons_frame.pack(fill=BOTH)

    def addYesBtn(self):
        # Add Yes button to frame
        self.yesBtn = tk.Button(
            master=self.buttons_frame,
            text="Yes",
            fg="black",
            anchor=CENTER)
        self.yesBtn.pack(side=LEFT,fill=BOTH,ipadx=10, ipady=10, padx=10, pady=10)

    def addNoBtn(self):
        # Add No button to button frame
        self.noBtn = tk.Button(
            master=self.buttons_frame,
            text="No",
            fg="black",
            anchor=CENTER)
        self.noBtn.pack(side=RIGHT,fill=BOTH,ipadx=10, ipady=10, padx=10, pady=10)



if __name__ == "__main__":
    ui = gui()
    
