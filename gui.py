from tkinter import *
from tkinter import messagebox
import tkinter as tk
import webbrowser
from PIL import ImageTk, Image

class gui():
    # static class variable of the background color
    bgColor = "#34A2FE"
    # static variable that holds all urls
    urlGuides = {"Hotend": "https://help.prusa3d.com/en/article/clogged-nozzle-hotend-mini-mini_112011",
                 "Extruder Gear": "https://help.prusa3d.com/guide/how-to-access-and-clean-the-extruder-pulley-mini-mini_126457",
                 "General": "https://help.prusa3d.com/en/tag/mini-2/troubleshooting_194",
                 "Service Manuals": "https://help.prusa3d.com/category/printer-maintenance_247",
                 "First Layer": "https://help.prusa3d.com/article/first-layer-calibration-mini-mini_229122",
                 "Selftest": "https://help.prusa3d.com/article/selftest-mini-mini_112055"}
    new = 1 #variable to open webbrowsers 

    # dictionary to access and then move to respective stage depending on Question on current frame
    questions = {"Initial Status": "Does the printer turn on?",
                 "Connection": "Is the Printer plugged in?",
                 "New status": "Turns on?", 
                 "Filament": "Is filament inserted?",
                 "Bed": "Is the bed dirty?",
                 "Purge": "Purging?"}



    def __init__(self):
        self.masterWindow = tk.Tk() # create the tkinder object 
        self.masterWindow.title("Printer Troubleshooting Guide")
        # Set standard size of window
        self.masterWindow.geometry("800x700+300+10")
        self.masterWindow.configure(bg=gui.bgColor)
        # Add Exit button
        self.addExitButton()
        self.addLinkButton(self.openGeneral)
        self.addExtraHelpButton()
        # Add text frame
        self.createTextFrame()  
        # Add intiial basic question text
        self.addText("Welcome to this interactive app.\n", 'yellow')
        self.addText("""Does the printer turn on?
        \n(Things to check): 
        a) Hear fan noises? b) Screen illuminates?""")
        # Add button frame 
        self.createButtonFrame()
        # Create buttons, where parameters are the next stages in the flowchart
        self.addYesNoButtons(self.cleanBed,self.printerNotOn)
   
    def addExitButton(self):
        # create exit btn frameconda 
        self.bottomFrame = tk.Frame(self.masterWindow,bg=gui.bgColor)
        self.bottomFrame.pack(side=BOTTOM, fill=BOTH)
        # Exit button 
        self.exit_btn = tk.Button(self.bottomFrame, text="Exit", command=self.quitWindow,relief=tk.RAISED, bg="red")
        self.exit_btn.pack(side=RIGHT, ipadx=10, ipady=10, padx=10, pady=10)
        self.masterWindow.protocol("WM_DELETE_WINDOW", self.quitWindow) 

    def addLinkButton(self,browser,txt="Troubleshooting Guides"):
        self.helpBtn = tk.Button(master=self.bottomFrame,text= txt,fg='black',bg='#EEEE6A',anchor=CENTER,command=browser, font=(0))
        self.helpBtn.pack(fill=BOTH,side=LEFT,ipadx=10, ipady=10, padx=10, pady=10) 
    
    def addExtraHelpButton(self,msg="Maintenance Manuals",extruder=False):
        if(extruder):
            self.extraBtn = tk.Button(master=self.bottomFrame,command=self.openExtruder,text=msg,
                                        fg='black',bg='#EEEE6A',anchor=CENTER,font=(0))
            self.extraBtn.pack(fill=BOTH,side=LEFT,ipadx=10, ipady=10, padx=10, pady=10)
        else:
            self.extraBtn = tk.Button(master=self.bottomFrame,command=self.openServiceManual,text=msg,
                                        fg='black',bg='#EEEE6A',anchor=CENTER,font=(0))
            self.extraBtn.pack(fill=BOTH,side=LEFT,ipadx=10, ipady=10, padx=10, pady=10)

    def quitWindow(self):
        self.masterWindow.destroy() # close window

    # Method to open web browsers ---------------------------------------------------------------------
    def openServiceManual(self):
        webbrowser.open(gui.urlGuides.get("Service Manuals"),new=gui.new)

    def openGeneral(self):
        webbrowser.open(gui.urlGuides.get("General"),new=gui.new)

    def openHotend(self):
        webbrowser.open(gui.urlGuides.get("Hotend"),new=gui.new)

    def openFirstLayer(self):
        webbrowser.open(gui.urlGuides.get("First Layer"),new=gui.new)

    def openSelfTest(self):
        webbrowser.open(gui.urlGuides.get("Selftest"),new=gui.new)

    def openExtruder(self):
        webbrowser.open(gui.urlGuides.get("Extruder Gear"),new=gui.new)

    #--------------------------------------------------------------------------------------------------

    # Frames ------------------------------------------------------------------------------------------
    def createTextFrame(self):
        self.txtFrame = tk.Frame(master=self.masterWindow,height=200,bg=gui.bgColor,padx=20, pady=20)
        self.txtFrame.pack(side=TOP, fill=BOTH)
    # Method that creates a button Frame
    def createButtonFrame(self):
        self.buttons_frame = Frame(master=self.masterWindow,height=100,bg=gui.bgColor)
        self.buttons_frame.pack(fill=BOTH)

    # Method to clear all widgets in the frame but maintain frame
    def clearFrame(self,frame):
        for widget in frame.winfo_children():
            widget.destroy()
    #---------------------------------------------------------------------------------------------------


    # Method that adds text to Frame
    def addText(self,msg,color='black'):
        # Create message
        self.label = tk.Label(master=self.txtFrame, anchor=CENTER, text=msg,font=(120),fg=color, bg=gui.bgColor)
        self.label.pack()

    # Method that adds Yes/No buttons to frame. Parameters are the corresponding stages of the guide depending if yes or no was clicked. 
    def addYesNoButtons(self,nextYesStage, nextNoStage):
        # Add Yes button to frame
        self.yesBtn = tk.Button(master= self.buttons_frame, text= "Yes", fg= "black", anchor= CENTER, command= nextYesStage) 
        self.yesBtn.pack(side=LEFT,fill=BOTH,ipadx=10, ipady=10, padx=10, pady=10)
        # Add No button to frame
        self.noBtn = tk.Button(master= self.buttons_frame, text= "No", fg= "black", anchor=CENTER, command= nextNoStage) 
        self.noBtn.pack(side=RIGHT,fill=BOTH,ipadx=10, ipady=10, padx=10, pady=10)

    def addContinueButton(self,nextStage):
        self.continueBtn = tk.Button(master= self.buttons_frame,text= "Continue",fg= "black",anchor= CENTER, command= nextStage)
        self.continueBtn.pack(fill=BOTH,ipadx=10, ipady=10, padx=10, pady=10)
 
        
    #---------------------------------Connection Troubleshooting----------------------------------#
    def printerNotOn(self):
        print("Im in printer does not turn on")
        self.clearFrame(self.txtFrame)
        self.buttons_frame.destroy()
        # Check connection status
        self.addText("\n"+gui.questions.get("Connection"))
        self.addText("(Check the back of the printer for power cable)",'yellow')
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
        self.addText("TO-DO: CHECK SCREEN CONNECTIONS\n",'white')
        self.addText("""1) Ensure screen is connected and secure in place.
                      \n(Screen connections are in the back of the display) 
                      \n2) Turn on printer and wait for display to illuminate.\n""", 'yellow')
        self.addText("Continue Troubleshooting if needed.\nElse press Exit.")
        # Add button frame below question
        self.createButtonFrame()
        self.addContinueButton(self.cleanBed)

    #-----If printer is NOT plugged in, then go to this method:
    def connectAndTurnOn(self):
        print("Im in printer not connected")
        self.clearFrame(self.txtFrame)
        self.buttons_frame.destroy()
        # Instruct user to purge filament
        self.addText("TO-DO: Plug in Printer\n",'white')
        self.addText("1) Plug in power cable, turn on, and wait for display to illuminate.\n", 'yellow')
        self.addText(gui.questions.get("New status"))
        # Add button frame below question
        self.createButtonFrame()
        self.addYesNoButtons(self.cleanBed,self.screenConnections)
    
    #--------------------------- SW/HW troubleshooting -------------------------------#
    def cleanBed(self):
        print("Im in Clean Bed")
        self.clearFrame(self.txtFrame)
        self.buttons_frame.destroy()
        self.helpBtn.destroy()
        self.extraBtn.destroy()
        self.addLinkButton(self.openGeneral)
        self.addExtraHelpButton()
        # Instruct user to purge filament
        self.addText("TO-DO: CLEAN the BED\n",'white')
        self.addText("""1) Remove bed from printer. 
                      \n2) Use IPA wipes or wash in sink with water & soap.
                      \n3) Dry bed before putting back in printer.\n""", 'yellow')
        self.addText("Have you run a Selftest?",'black')
        self.question = self.label['text']
        print(self.question)
        # Add button frame below question
        self.createButtonFrame()
        self.addYesNoButtons(self.selfTestPassed,self.runSelfTests)

    #When printer is connected, first assessment is to run self tests
    def runSelfTests(self):
        self.clearFrame(self.txtFrame)
        self.buttons_frame.destroy()
        self.helpBtn.destroy()
        self.extraBtn.destroy()
        self.addLinkButton(self.openSelfTest,"Guide = Selftest")
        self.addExtraHelpButton()
        # Instruct user to run self diagnostics test
        self.addText("TO-DO: RUN SELFTEST\n",'white')
        self.addText("""1) Either run entire Selftest (Go to Calibration -> Selftest)
                      \nOr instead run individual selftests
                      \na) Calibration -> Test XYZ-axis
                      \nb) Calibration -> Test FANs
                      \nc) Calibration -> Test heaters""", 'yellow')
        # Ask whether filament is inserted
        self.addText("\nDid the Selftest passed succesfully?")
        # Add button frame below question
        self.createButtonFrame()
        self.addYesNoButtons(self.selfTestPassed,self.errorInSelfTest)
    
    def errorInSelfTest(self):
        self.clearFrame(self.txtFrame)
        self.buttons_frame.destroy()
        self.helpBtn.destroy()
        self.extraBtn.destroy()
        self.addLinkButton(self.openSelfTest,"Guide = Selftest")
        self.addExtraHelpButton()
        # Instruct user to run self diagnostics test
        self.addText("SELFTEST FAILED\n",'white')
        self.addText("What instance of the self test failed?")
        self.createButtonFrame()
        axisBtn = tk.Button(master= self.buttons_frame, text= "XYZ-axis test", fg= "black", anchor= CENTER, command= self.fixAxis)
        axisBtn.pack(fill=BOTH,ipadx=10, ipady=10, padx=80, pady=10)
        heaterBtn = tk.Button(master= self.buttons_frame, text= "Heater test", fg= "black", anchor= CENTER, command= self.fixHeater)
        heaterBtn.pack(fill=BOTH,ipadx=10, ipady=10, padx=80, pady=10)
        fanBtn = tk.Button(master= self.buttons_frame,text= "Fan test", fg= "black", anchor= CENTER)
        fanBtn.pack(fill=BOTH,ipadx=10, ipady=10, padx=80, pady=10)

    # NEED TO FINISH FINDING SOLUTION TO 2 BUTTON----------------------
    def fixAxis(self):
        self.clearFrame(self.txtFrame)
        self.buttons_frame.destroy()
        self.helpBtn.destroy()
        self.extraBtn.destroy()
        self.addLinkButton(self.openSelfTest,"Guide = Selftest")
        self.addExtraHelpButton("Fix (X/Y) bearings-Consult Lead")

        # Instruct user to run self diagnostics test
        self.addText("XYZ-AXIS TEST FAILED\n",'white')
        self.addText("""1) Move axes by hand to ensure nothing blocks their path
        2) Ensure the belt pulleys are secured on the Y- and X-motor shaft.
        3) Check if the belts aren't extremely loose
        4) Try to clean, then apply lubricant to the smooth rods.
        5) If a failure happens on the Z-axis, problem might be with the 
        M.I.N.D.A./SuperPINDA sensor.\n""", 'yellow')
        self.addText("""Click the HELP button (BOTTOM LEFT) for further assistance and details.
        Scroll down to 'Troubleshoot a failed component' and look for 'Axes'.
        Press Continue to go back to Running Selftest""")
        self.createButtonFrame()
        self.addContinueButton(self.runSelfTests)

    # NEED TO FINISH FINDING SOLUTION TO 2 BUTTON----------------------
    def fixHeater(self):
        self.clearFrame(self.txtFrame)
        self.buttons_frame.destroy()
        self.helpBtn.destroy()
        self.extraBtn.destroy()
        self.addLinkButton(self.openSelfTest,"Guide = Selftest")
        self.addExtraHelpButton("Fix Heaters-Consult Lead")
        # Instruct user to run self diagnostics test
        self.addText("Heater TEST FAILED\n",'white')
        self.addText("""1) Ensure the flexible steel sheet is on the bed.
        2) Ensure the ambient temperature is above 18 degrees Celsius.
        3) Ensure the printer is not standing on a draft or close to AC.\n""", 'yellow')
        self.addText("""\nClick the HELP button (BOTTOM LEFT) for further assistance and details.
        Scroll down to 'Troubleshoot a failed component' and look for 'Heater'.
        Press Continue to go back to Running Selftest""")
        self.createButtonFrame()
        self.addContinueButton(self.runSelfTests)

    # NEED TO FINISH FINDING SOLUTION TO 2 BUTTON----------------------
    def fixFan(self):
        self.clearFrame(self.txtFrame)
        self.buttons_frame.destroy()
        self.helpBtn.destroy()
        self.extraBtn.destroy()
        self.addLinkButton(self.openSelfTest,"Guide = Selftest")
        self.addExtraHelpButton("Fix FANs-Consult Lead")
        # Instruct user to run self diagnostics test
        self.addText("Fan TEST FAILED\n",'white')
        self.addText("""1) Verify if there is nothing blocking the rotation of the fans
        a) Debris might get between the blades. Bigger parts can be cleared with tweezers,
        and dust can be cleared with a computer cleaner spray).
        b) Hold the fan with your hand while using the compressed air otherwise, you might damage the blades.""", 'yellow')
        self.addText("""\nClick the HELP button (BOTTOM LEFT) for further assistance and details.
        Scroll down to 'Troubleshoot a failed component' and look for 'Fans'.
        Press Continue to go back to Running Selftest""")
        self.createButtonFrame()
        self.addContinueButton(self.runSelfTests)


    def selfTestPassed(self):
        self.clearFrame(self.txtFrame)
        self.buttons_frame.destroy()
        self.helpBtn.destroy()
        self.extraBtn.destroy()
        self.addLinkButton(self.openSelfTest)
        self.addExtraHelpButton()

        # Instruct user to run self diagnostics test
        self.addText("SELFTEST PASSED SUCCESFULLY\n",'white')
        self.addText("""All phases of the selftest were passed. It's time to check the filament.""", 'yellow')
        # Ask whether filament is inserted
        self.addText("\n"+gui.questions.get("Filament"))
        # Add button frame below question
        self.createButtonFrame()
        self.addYesNoButtons(self.purgeFilament,self.insertFilament)

    def insertFilament(self):
        print("Im in inserting filament")
        self.clearFrame(self.txtFrame)
        self.buttons_frame.destroy()
        self.helpBtn.destroy()
        self.extraBtn.destroy()
        self.addLinkButton(self.openGeneral, "Guides/Help")
        self.addExtraHelpButton()
        self.addText("TO-DO: LOAD FILAMENT\n",'white')
        self.addText("""1) Insert filament through sensor until you feel resistance.
                      \n2) Go to Filament -> Load Filament.
                      \n3) Keep tension on  filament while gears are moving.
                      \n4) Once the filament starts moving fast, let go.\n""", 'yellow')
        self.addText("Press continue to go Purging stage")
        # Add button frame below question
        self.createButtonFrame()
        self.addContinueButton(self.purgeFilament)

    def purgeFilament(self):
        print("Im in purge filament")
        self.clearFrame(self.txtFrame)
        self.buttons_frame.destroy()
        self.helpBtn.destroy()
        self.extraBtn.destroy()
        self.addLinkButton(self.openGeneral)
        self.addExtraHelpButton()
        # Instruct user to purge filament
        self.addText("TO-DO: PURGE FILAMENT\n",'white')
        self.addText("""1) After loading filment, it should start purging.
                      \n2) To check for clogged hotend, purge filament like so:
                      \n3) Go to Filament -> Purge Filament.
                      \n4) To increase nozzle temperature:
                      \n(Settings -> Temperature -> Nozzle)\n""", 'yellow')
        self.addText("\n"+gui.questions.get("Purge"))
        # Add button frame below question
        self.createButtonFrame()
        self.addYesNoButtons(self.layerCalibration,self.extruderAndHotend)

    def layerCalibration(self):
        print("Im in First Layer Calibration")
        self.clearFrame(self.txtFrame)
        self.buttons_frame.destroy()
        self.helpBtn.destroy()
        self.extraBtn.destroy()
        self.addLinkButton(self.openFirstLayer, "How to do First-Layer Calibration")
        self.addExtraHelpButton("Manuals")
        self.addText("TO-DO: FIRST LAYER CALIBRATION\n",'white')
        self.addText("""1) Go to Calibration -> First Layer Calibration.
                      \n2) Follow instructions on display
                      \n3) Adjust z-axis height until filament sticks well to the bed.
                      \n(Click yellow button for further explanation/ how-to-do)
                      \nPerform a functionality test: find and print a Benchy.
                      \nMake sure first layer prints well before leaving it unattended.\n""", 'yellow')
        self.addText("Is the filament sticking to the bed?")
        # Add button frame below question
        self.createButtonFrame()
        self.addYesNoButtons(self.endTroubleshoot,self.cleanBed)

    # REDUCE SCALE OF QR CODE TO SEE CONTINUE BUTTON----------------------
    def extruderAndHotend(self):
        print("Im in Extruder and Hotend Issues")
        self.clearFrame(self.txtFrame)
        self.buttons_frame.destroy()
        self.helpBtn.destroy()
        self.extraBtn.destroy()
        self.addLinkButton(self.openHotend, "Clogged Hotend")
        self.addExtraHelpButton("Extruder Pulley",True)

        self.addText("TO-DO: CLEAN EXTRUDER GEARS and/or HOTEND",'white')
        self.addText("""1) Clean extruder gears/pulleys:
        2) Click on 'Clogged Hotend' button for detailed instructions.
        3) Click on 'Extruder Pulley' button for detailed instructions.""", 'yellow')
        self.addText("""Cleaning or Replacing Hotend:
        This process is one of the most demanding and tedious.
        Scan QR code for step by step process.\n""")
        # Add image of QR code
        self.hotend_guide = ImageTk.PhotoImage(Image.open("cloggedHotend_qrCode.png"))
        self.hotendQRCode = tk.Label(master=self.txtFrame)
        self.hotendQRCode.image = self.hotend_guide
        self.hotendQRCode.configure(image=self.hotend_guide)
        self.hotendQRCode.pack()

        self.addText("Press continue to retest.")
        self.createButtonFrame()
        self.addContinueButton(self.layerCalibration)



    def endTroubleshoot(self):
        print("Im end of troubleshhot")
        self.clearFrame(self.txtFrame)
        self.buttons_frame.destroy()
        self.helpBtn.destroy()
        self.extraBtn.destroy()
        self.addLinkButton(self.openGeneral)
        self.addExtraHelpButton()
        
        # Instruct user to purge filament
        self.addText("""This guide covered basic 3D printer maintenance.
        If you are yet unable to figure out and/or fix the issue:
        Go to Prusa Mini troubleshooting guide for more in-depth 
        printer issues and/or if fixing the printer has become stagnant.
        Click on the 'Troubleshoot' button or scan QR code.\n""", 'yellow')
        # Add image of QR code
        self.qrCode_guide = ImageTk.PhotoImage(Image.open("cloggedHotend_qrCode.png"))
        self.general_qrCode = tk.Label(master=self.txtFrame)
        self.general_qrCode.image = self.qrCode_guide
        self.general_qrCode.configure(image=self.qrCode_guide)
        self.general_qrCode.pack()

if __name__ == "__main__":
    ui = gui()
    # Make program event Driven 
    ui.masterWindow.mainloop()
    
