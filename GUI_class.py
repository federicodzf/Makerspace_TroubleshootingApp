import os
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import sys
import datetime

class gui():
    # static class variable of the background color
    bgColor = "#34A2FE"

    def __init__(self):
        self.masterWindow = tk.Tk() # create the tkinder object 
        self.masterWindow.title("Printer Troubleshooting Guide")
        # Set standard size of window
        self.masterWindow.geometry("250x250")
        self.masterWindow.configure(bg=gui.bgColor)
        # Configure rows and columns in order to use .grid() and change weight of widgets 
        self.masterWindow.columnconfigure([0,1], minsize=250, weight=1)
        self.masterWindow.rowconfigure([0,1],minsize=100, weight=1)

        # Testing grid 
        
        # Create Exit button
        self.addExitButton()
        # Add introductory text
        self.createTextFrame("Encountering issues with a printer?")
        # Make program event-driven
        self.masterWindow.mainloop()
 
    def addExitButton(self):
        self.exit_btn = tk.Button(self.masterWindow, text="Exit", command=self.quitWindow,relief=tk.RAISED)
        self.exit_btn.grid(row=1,sticky="se",padx=5,pady=5)
        self.masterWindow.protocol("WM_DELETE_WINDOW", self.quitWindow)       

    def createTextFrame(self,msg):
        self.txtFrame = tk.Frame(master=self.masterWindow,width=500,height=100,bg="#34A2FE")
        self.txtFrame.grid(row=0,column=0,padx=5,pady=5)
        # Create Intro message
        self.lbl_intro = tk.Label(
            master=self.txtFrame,
            relief = tk.RAISED,
            anchor='w',
            text=msg,
            font=(70),
            fg='black',
            bg=gui.bgColor)
        # Need to place now
        self.lbl_intro.pack()



    #def buttonWidgets(self):
    #    # Parent widget for the buttons
    #    self.buttons_frame = Frame(self.masterWindow)
        


    def pressedYes(self):
        # Must refresh gui
        txt = tk.Label(self.masterWindow,text="You are having issues")

    def quitWindow(self):
        # Add exit message
        # exit_message = tk.Label(self.window,text="You are exiting.")
        # exit_message.grid(row=2,column=3) # show message in grid
        # close window
        self.masterWindow.destroy() 
        

def main():
    ui = gui()
    

if __name__ == "__main__":
    main()