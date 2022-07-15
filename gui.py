import os
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import sys
import datetime
import time

class gui():
    # static class variable of the background color
    bgColor = "#34A2FE"
    # static variable that holds all questions
    

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
        self.addYesNoButtons()
        

        # dictionary that holds the questions and the respective function mappings
        #self.stages = {"Printer connected?": gui.isPrinterNotConnected(),
        #               "Turns on?": gui.turnsOn(), 
        #               "Is filament inserted?": gui.isFilamentInserted,
        #               "Is bed dirty?": gui.cleanBed(),
        #               "Purging?": gui.purge()}
        
 
    def addExitButton(self):
        # create exit btn frameconda 
        self.exitBtnFrame = tk.Frame(self.masterWindow,bg="white")
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
            bg=gui.bgColor)
        self.buttons_frame.pack(fill=BOTH)

    def addYesNoButtons(self):
        # Add Yes button to frame
        self.yesBtn = tk.Button(
            master=self.buttons_frame,
            text="Yes",
            fg="black",
            bg='green',
            anchor=CENTER,
            command=self.printerNotConnected) # Need to properly check instance of troubleshooting to see next step
        self.yesBtn.pack(side=LEFT,fill=BOTH,ipadx=10, ipady=10, padx=10, pady=10)
        # Add No button to frame
        self.noBtn = tk.Button(
            master=self.buttons_frame,
            text="No",
            fg="black",
            anchor=CENTER,
            ) # Need to properly check instance of troubleshooting to see next step 
        self.noBtn.pack(side=RIGHT,fill=BOTH,ipadx=10, ipady=10, padx=10, pady=10)

    # Method to clear all widgets in the frame but maintain frame
    def clearFrame(self,frame):
        for widget in frame.winfo_children():
            widget.destroy()
    
    def printerNotConnected(self):
        # Clear button frame
        self.clearFrame(self.buttons_frame)
        # Clear the text frame to ask new question
        self.clearFrame(self.txtFrame)
        #Ask new question
        self.addQuestion("Is the printer connected?")
        self.addYesNoButtons()
        
    def checkYesStage(self):
        count = 1


if __name__ == "__main__":
    ui = gui()
    # Make program event Driven 
    ui.masterWindow.mainloop()
    
