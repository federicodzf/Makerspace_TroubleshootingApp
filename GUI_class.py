import os
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import sys
import datetime

class gui():
    def __init__(self):
        self.window = tk.Tk() # create the tkinder object 
        self.window.title("Printer Troubleshooting Guide")
        self.window.attributes('-fullscreen', True)
        # Set window size 
        self.window.geometry('200x200')
       
        # Create first instance messages
        self.msg = tk.Label(self.window, text="Are you having issue with a printer?",bg="#330000",font=(50),fg="#FFD700")
        self.msg.grid(row=1,column=2)
        # Create YES button
        self.yes_button = tk.Button(self.window,text="Yes",command=self.pressedYes)
        self.yes_button.place(relx= 0.5,rely=0.4,anchor=CENTER,height=50,width=400)
        # Create exit button on GUI
        exit_button = tk.Button(self.window, text="Exit", command=self.quitWindow)
        exit_button.place(relx = .5, rely =.7,anchor=CENTER,height=50, width=200)
        self.window.protocol("WM_DELETE_WINDOW", self.quitWindow)

         # Always include this mainloop line on Tk object at the end of constructor
        self.window.mainloop()

    def pressedYes(self):
        # Must refresh gui
        txt = tk.Label(self.window,text="You are having issues")

    def quitWindow(self):
        # Add exit message
        #exit_message = tk.Label(self.window,text="You are exiting.")
        # exit_message.grid(row=2,column=3) # show message in grid
        # close window after 2 seconds
        self.window.destroy() 
        

def main():
    ui = gui()

if __name__ == "__main__":
    main()