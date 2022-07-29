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
                          "Connection": "Is the Printer plugged in?",
                          "New status": "Turns on?", 
                          "Filament": "Is filament inserted?",
                          "Bed": "Is the bed dirty?",
                          "Purge": "Purging?"}
        # Add Exit button
        self.addExitButton()
        # Add text frame
        self.createTextFrame()
        # Add intiial basic question text
        self.addQuestion("Welcome to this interactive app.", 'yellow')
        self.addQuestion("""Does the printer turn on?
                            \nThings to check: 
                            \na) Fan noises? b) Screen illuminates?""")
        # Add button frame 
        self.createButtonFrame()
        # Create buttons, where parameters are the next stages in the flowchart
        self.addYesNoButtons(self.cleanBed,self.printerNotOn)
        
        
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
        self.txtFrame = tk.Frame(master=self.masterWindow,height=200,bg=gui.bgColor,padx=20, pady=20)
        self.txtFrame.pack(side=TOP, fill=BOTH)

    def addQuestion(self,msg,color='black'):
        # Create message
        self.label = tk.Label(
            master=self.txtFrame,
            anchor=CENTER,
            text=msg,
            font=(120),
            fg=color,
            bg=gui.bgColor)
        self.label.pack()

    # Method that creates a button Frame
    def createButtonFrame(self):
        self.buttons_frame = Frame(master=self.masterWindow,height=100,bg=gui.bgColor)
        self.buttons_frame.pack(fill=BOTH)

    # Method that adds Yes/No buttons to frame. Parameters are the corresponding stages of the troubleshooting guide
    # depending on whether yes or no was clicked. 
    def addYesNoButtons(self,nextYesStage, nextNoStage):
        # Add Yes button to frame
        self.yesBtn = tk.Button(
            master= self.buttons_frame,
            text= "Yes",
            fg= "black",
            bg='green',
            anchor= CENTER,
            command= nextYesStage) # Need to properly check instance of troubleshooting to see next step
        self.yesBtn.pack(side=LEFT,fill=BOTH,ipadx=10, ipady=10, padx=10, pady=10)
        # Add No button to frame
        self.noBtn = tk.Button(
            master= self.buttons_frame,
            text= "No",
            fg= "black",
            anchor=CENTER,
            command= nextNoStage) # Need to properly check instance of troubleshooting to see next step 
        self.noBtn.pack(side=RIGHT,fill=BOTH,ipadx=10, ipady=10, padx=10, pady=10)

    def addContinueButton(self,nextStage):
        self.continueBtn = tk.Button(
            master= self.buttons_frame,
            text= "Continue",
            fg= "black",
            relief= RIDGE,
            anchor= CENTER,
            command= nextStage) # Need to properly check instance of troubleshooting to see next step
        self.continueBtn.pack(fill=BOTH,ipadx=10, ipady=10, padx=10, pady=10)

    # Method to clear all widgets in the frame but maintain frame
    def clearFrame(self,frame):
        for widget in frame.winfo_children():
            widget.destroy()

    #---------------------------------Connection Troubleshooting----------------------------------#
    def printerNotOn(self):
        print("Im in printer does not turn on")
        self.clearFrame(self.txtFrame)
        self.buttons_frame.destroy()
        # Check connection status
        self.addQuestion("\n"+self.questions.get("Connection"))
        self.addQuestion("(Check the back of the printer for power cable)",'yellow')
        self.question = self.label['text']
        print(self.question)
        # Add button frame below question
        self.createButtonFrame()
        self.addYesNoButtons(self.screenConnections,self.connectAndTurnOn)

    #-----If printer is connected, then go to this method
    def screenConnections(self):
        print("Im in checking screen connections")
        self.clearFrame(self.txtFrame)
        self.buttons_frame.destroy()
        # Instruct user to purge filament
        self.addQuestion("TO-DO: Check Screen Connections",'white')
        self.addQuestion("""Steps: 
                         \n1) Ensure screen is connected and secure in place.
                         \n(Screen connections are in the back of the display) 
                         \n2) Turn on printer and wait for display to illuminate.\n""", 'yellow')
        self.addQuestion("Continue Troubleshooting if needed.\nElse press Exit.")
        # Add button frame below question
        self.createButtonFrame()
        self.addContinueButton(self.runSelfTests)

    #-----If printer is NOT plugged in, then go to this method:
    def connectAndTurnOn(self):
        print("Im in printer not connected")
        self.clearFrame(self.txtFrame)
        self.buttons_frame.destroy()
        # Instruct user to purge filament
        self.addQuestion("TO-DO: Plug in Printer",'white')
        self.addQuestion("Step: Plug in power cable, turn on, and wait for display to illuminate.\n", 'yellow')
        self.addQuestion(self.questions.get("New status"))
        # Add button frame below question
        self.createButtonFrame()
        self.addYesNoButtons(self.cleanBed,self.screenConnections)
    
    #--------------------------- SW/HW troubleshooting -------------------------------#
    def cleanBed(self):
        print("Im in Clean Bed")
        self.clearFrame(self.txtFrame)
        self.buttons_frame.destroy()
        # Instruct user to purge filament
        self.addQuestion("TO-DO: CLEAN the BED",'white')
        self.addQuestion("""Steps:
                         \n1) Remove bed from printer. 
                         \n2) Use IPA wipes or wash in sink with water & soap.
                         \n3) Dry bed before putting back in printer.\n""", 'yellow')
        self.addQuestion("Have you run a Self Test?",'black')
        self.question = self.label['text']
        print(self.question)
        # Add button frame below question
        self.createButtonFrame()
        self.addYesNoButtons(self.layerCalibration,self.runSelfTests)

    #-----When printer is connected, first assessment is to run self tests
    def runSelfTests(self):
        self.clearFrame(self.txtFrame)
        self.buttons_frame.destroy()
        # Instruct user to run self diagnostics test
        self.addQuestion("TO-DO: Run Self Test",'white')
        self.addQuestion("""Steps: 
                         \n1) Go to Calibration -> Run XYZ test.
                         \n (Run the XYZ test to assess motor issue)
                         \n2) Ensure the cables in the back are not stuck.\n""", 'yellow')
        # Ask whether filament is inserted
        self.addQuestion("\n"+self.questions.get("Filament"))
        # Add button frame below question
        self.createButtonFrame()
        self.addYesNoButtons(self.purgeFilament,self.insertFilament)
    
    def insertFilament(self):
        print("Im in inserting filament")
        self.clearFrame(self.txtFrame)
        self.buttons_frame.destroy()
        # Instruct user to purge filament
        self.addQuestion("TO-DO: Load Filament",'white')
        self.addQuestion("""Steps:
                         \n1) Insert filament through sensor until you feel resistance.
                         \n2) Go to Filament -> Load Filament.
                         \n3) Keep tension on  filament while gears are moving.
                         \n4) Once the filament starts moving fast, let go.\n""", 'yellow')
        self.addQuestion("Press continue to go Purging stage")
        # Add button frame below question
        self.createButtonFrame()
        self.addContinueButton(self.purgeFilament)

    def purgeFilament(self):
        print("Im in purge filament")
        self.clearFrame(self.txtFrame)
        self.buttons_frame.destroy()
        # Instruct user to purge filament
        self.addQuestion("TO-DO: Purge Filament",'white')
        self.addQuestion("""Steps:
                         \n1) After loading filment, it should start purging.
                         \n2) To check for clogged hotend, purge filament like so:
                         \n3) Go to Filament -> Purge Filament.
                         \n4) To increase nozzle temperature:
                         \n(Settings -> Temperature -> Nozzle)\n""", 'yellow')
        self.addQuestion("\n"+self.questions.get("Purge"))
        # Add button frame below question
        self.createButtonFrame()
        self.addYesNoButtons(self.layerCalibration,self.extruderAndHotend)

    # NEED TO FINISH --------- OJO----------- OJO----------------- OJO----------------------- OJO
    def layerCalibration(self):
        print("Im in First Layer Calibration")
        self.clearFrame(self.txtFrame)
        self.buttons_frame.destroy()
        # Instruct user to purge filament
        self.addQuestion("""TO-DO breakdown:
                         \nPerform first layer calibration like so:
                         \nGo to Calibration -> First Layer Calibration.
                         \nPrinter functionality test: find and print a Benchy.
                         \nMake sure first layer prints well before leaving it unattended.\n""", 'yellow')
        self.addQuestion("\nIs the filament sticking to the bed?\n")
        print(self.label['text'])
        # Add button frame below question
        self.createButtonFrame()
        self.addYesNoButtons(self.endTroubleshoot,self.cleanBed)

    def extruderAndHotend(self):
        print("Im in Extruder and Hotend Issues")
        self.clearFrame(self.txtFrame)
        self.buttons_frame.destroy()
        # Instruct user to purge filament
        self.addQuestion("""TO-DO breakdown:
                         \nClean extruder gears/pulleys:
                         \nFor further details, copy paste link below:
                         https://help.prusa3d.com/guide/how-to-access-and-clean-the-extruder-pulley-mini-mini_126457""", 'yellow')
        self.addQuestion("""NEXT:
                         \nCleaning or Replacing Hotend: 
                         \nThis process is one of the most demanding and tedious.
                         \nScan QR code below for step by step breakdown\n""")
        # Add image of QR code
        qrCode = tk.PhotoImage(file="hotend_QRcode.png")
        self.hotend_qrCode = tk.Label(master=self.txtFrame, image= qrCode, anchor= CENTER)
        self.hotend_qrCode.pack()
        self.addQuestion("Press continue to end Troubleshooting.")
        self.createButtonFrame()
        self.addContinueButton(self.endTroubleshoot)



    def endTroubleshoot(self):
        print("Im end of troubleshhot")
        self.clearFrame(self.txtFrame)
        self.buttons_frame.destroy()
        # Instruct user to purge filament
        self.addQuestion("""This guide covered basic 3D printer maintenance.
                     \nIf you are yet unable to figure out and/or fix the issue:
                     \nGo to Prusa Mini troubleshooting guide for more in-depth 
                     \nprinter issues and/or if fixing the printer has become stagnant.\n""", 'yellow')
        qrCode_guide = tk.PhotoImage(file="prusaMini_helpguide.png")
        self.hotend_qrCode = tk.Label(master=self.txtFrame, image= qrCode_guide, anchor= CENTER)
        self.hotend_qrCode.pack()

if __name__ == "__main__":
    ui = gui()
    # Make program event Driven 
    ui.masterWindow.mainloop()
    
