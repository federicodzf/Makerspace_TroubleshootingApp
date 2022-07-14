from doctest import master
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
        ## Configure rows and columns in order to use .grid() and change weight of widgets 
        self.masterWindow.columnconfigure(list(range(gui.cols)), minsize=75, weight=1)
        self.masterWindow.rowconfigure(list(range(gui.rows)),minsize=50, weight=1)

        # Add Exit button
        self.addExitButton()
        ## Add introductory text
        self.createTextFrame("Encountering issues with a printer?")
        ## Make program event-driven
        self.masterWindow.mainloop()
 
    def addExitButton(self):
        # create exit btn frame
        self.exitBtnFrame = tk.Frame(self.masterWindow,bg="red")
        self.exitBtnFrame.grid(row=gui.rows-1,columnspan=gui.cols,sticky="se",padx=10,pady=10)
        # Exit button 
        self.exit_btn = tk.Button(self.exitBtnFrame, text="Exit", command=self.quitWindow,relief=tk.RAISED)
        self.exit_btn.grid(row=gui.rows-1, column=gui.cols-1, sticky="se", padx=5, pady=5)
        self.masterWindow.protocol("WM_DELETE_WINDOW", self.quitWindow) 
        
    def quitWindow(self):
        # Need to ask client if they are sure they want to exit
        self.masterWindow.destroy() # close window

    def createTextFrame(self,msg):
        self.txtFrame = tk.Frame(
            master=self.masterWindow,
            width=500,
            height=100,
            bg=gui.bgColor)
        self.txtFrame.grid(row=0,columnspan=10,sticky='n')
        # Create Intro message
        self.lbl_intro = tk.Label(
            master=self.txtFrame,
            relief = tk.RAISED,
            anchor='w',
            text=msg,
            font=(100),
            fg='black',)
        self.lbl_intro.grid(row=0,columnspan=gui.cols,padx=10,pady=10)
        
    def buttonWidgets(self):
        # Parent widget for the buttons
        self.buttons_frame = Frame(master=self.masterWindow)
        

if __name__ == "__main__":
    ui = gui()