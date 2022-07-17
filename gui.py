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
         # dictionary to access and then move to respective stage depending on Question on current frame
        self.questions = {"Initial Status": "Does the printer turn on?",
                          "Connection": "Is Printer connected?",
                          "New status": "Turns on?", 
                          "Filament": "Is filament inserted?",
                          "Bed": "Is bed dirty?",
                          "Purge": "Purging?"}
        # Add Exit button
        self.addExitButton()
        # Add text frame
        self.createTextFrame()
        # Add intiial basic question text
        self.addQuestion("Does the printer turn on?",'black')
        # Add button frame 
        self.createButtonFrame()
        # Create buttons, where parameters are the next stages in the flowchart
        self.addYesNoButtons(self.runSelfTests)
        
        
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

    def addQuestion(self,msg,color):
        # Create message
        self.label = tk.Label(
            master=self.txtFrame,
            anchor='w',
            text=msg,
            font=(120),
            fg=color,
            bg=gui.bgColor)
        self.label.pack()

    # Method that creates a button Frame
    def createButtonFrame(self):
        self.buttons_frame = Frame(
            master=self.masterWindow,
            height=100,
            bg=gui.bgColor)
        self.buttons_frame.pack(fill=BOTH)

    def addYesNoButtons(self,nextYesStage):
        # Add Yes button to frame
        self.yesBtn = tk.Button(
            master=self.buttons_frame,
            text="Yes",
            fg="black",
            bg='green',
            anchor=CENTER,
            command=nextYesStage) # Need to properly check instance of troubleshooting to see next step
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
    
    # Method for showing run self tests
    def runSelfTests(self):
        self.clearFrame(self.txtFrame)
        self.buttons_frame.destroy()
        # Instruct user to run self diagnostics test
        self.addQuestion("""TO DO: 
                             \nRun the XYZ test to asses motor issue:
                             \nGo to Calibration -> Run XYZ test.
                             \nNote: make sure the cables in the back are not stuck.\n""", 'yellow')
        # Ask whether filament is inserted
        self.addQuestion("\n"+self.questions.get("Filament"),'black')
        self.question = self.label['text']
        print(self.question)

        # Add button frame below question
        self.createButtonFrame()
        self.addYesNoButtons(self.purgeFilament)

    def purgeFilament(self):
        print("Im in purge filament")
        self.clearFrame(self.txtFrame)
        self.buttons_frame.destroy()
        # Instruct user to purge filament
        self.addQuestion("""TO DO:
                         \nPurge filament to check for clogged hotend:
                         \nGo to Filament -> Purge Filament.
                         \nNote: make nozzle temperature is increasing
                         \nGo to Settings -> Temperature -> Nozzle.\n""", 'yellow')
        self.addQuestion("\n"+self.questions.get("Purge"),'black')
        self.question = self.label['text']
        print(self.question)
        # Add button frame below question
        self.createButtonFrame()
        self.addYesNoButtons(self.layerCalibration)

    def layerCalibration(self):
        print("Im in First Layer Calibration")
        self.clearFrame(self.txtFrame)
        self.buttons_frame.destroy()
        # Instruct user to purge filament
        self.addQuestion("""TO DO:
                         \nPerform first layer calibration:
                         \nGo to Calibration -> First Layer Calibration.\n""", 'yellow')
        self.addQuestion("""\nPrinter functionality test: find and print a Benchy.
                            \n Make sure first layer prints well before leaving it unattended.\n""",'black')
        self.question = self.label['text']
        print(self.question)


if __name__ == "__main__":
    ui = gui()
    # Make program event Driven 
    ui.masterWindow.mainloop()
    
