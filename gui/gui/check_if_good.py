"""Imported modules."""
from tkinter import * ##Import the tkinter module to allow construction of the GUI interface.
import vertSuperscroll ##Module containing the widget allowing a vertical scrollbar.

"""Functions which validate entries/create pop-ups."""

##Function to warn user that current stims will be deleted.
def specify_stim(main, stimList, numStims, stimScrollingArea):
  """ (tkinter.Tk, dict, int, tkinter.Frame) -> (none)
    
    Pop-up when the user specifies a number of
    stimuli to add.
  
  """   
  global warningStims
  ##Create pop-up window.
  warningStims = Toplevel()

  warningStims.config(takefocus = True) ##Get focus on screen.  
  
  windowSize = 300 ##Pop up size (300 x 300).
  
  ##Collect screen (monitor) width and height to position the window in the center. 
  screenWidth = warningStims.winfo_screenwidth() 
  screenHeight = warningStims.winfo_screenheight()
  
  ##Calculate the center position.
  positionRight = screenWidth/2 - windowSize/2
  positionDown = screenHeight/2 - windowSize/2
  
  ##Set the window size using the geometry() method.
  warningStims.geometry('%dx%d+%d+%d' % (windowSize, windowSize, 
                                    positionRight, positionDown)) 
  
  warningStims.resizable(width = False, height = False) ##The window is not resizeable.

  warningStims.wm_title("WARNING")
  warningStims.overrideredirect(1) ##Removes task bar.
  
  Label(warningStims, text = 'This action will permenantly delete the current stimuli').pack(side = TOP)
  
  pressToContinue = Button(warningStims, text = "Continue", 
                        command = lambda: return_to_stims_deletion(main, stimList, numStims, stimScrollingArea))
  
  pressToClose = Button(warningStims, text = "Return", 
                        command = lambda: return_to_stims_cancellation(main))
  
  pressToContinue.pack(side = BOTTOM)
  
  pressToClose.pack(side = BOTTOM)
  ##Removes main window.  
  main.withdraw()      

##Function to warn the user that the specified number of stims is invalid.
def incorrect_stim_num(main):
  """ (tkinter.Tk, dict, int, tkinter.Frame) -> (none)
    
    Pop-up when the user specifies a number of
    stimuli to add.
  
  """     
  global wrongStimNum
  ##create pop-up window
  wrongStimNum = Toplevel()
  
  wrongStimNum.config(takefocus = True) ##Get focus on screen.  
  
  windowSize = 300 ##Pop up size (300 x 300).
  
  ##Collect screen (monitor) width and height to position the window in the center. 
  screenWidth = wrongStimNum.winfo_screenwidth() 
  screenHeight = wrongStimNum.winfo_screenheight()
  
  ##Calculate the center position.
  positionRight = screenWidth/2 - windowSize/2
  positionDown = screenHeight/2 - windowSize/2
  
  ##Set the window size using the geometry() method.
  wrongStimNum.geometry('%dx%d+%d+%d' % (windowSize, windowSize, 
                                    positionRight, positionDown)) 
  
  wrongStimNum.resizable(width = False, height = False) ##The window is not resizeable.

  wrongStimNum.wm_title("Incorrect stimuli number")
  wrongStimNum.overrideredirect(1) ##Removes task bar.
  
  Label(wrongStimNum, text = 'Please enter a valid number of stimuli').pack(side = TOP)
  
  pressToClose = Button(wrongStimNum, text = "Return", 
                        command = lambda: return_to_stim_num(main))
  pressToClose.pack(side = BOTTOM)
  ##Removes main window.  
  main.withdraw()    

##Function is called when an incorrect stimuli is entered.
def incorrect_stims(main):
  global wrongStims
  ##Create pop-up window.
  wrongStims = Toplevel()
  
  wrongStims.config(takefocus = True) ##Get focus on screen. 
  
  windowSize = 300 ##Pop up size (300 x 300).
  
  ##Collect screen (monitor) width and height to position the window in the center. 
  screenWidth = wrongStims.winfo_screenwidth() 
  screenHeight = wrongStims.winfo_screenheight()
  
  ##Calculate the center position.
  positionRight = screenWidth/2 - windowSize/2
  positionDown = screenHeight/2 - windowSize/2
  
  ##Set the window size using the geometry() method.
  wrongStims.geometry('%dx%d+%d+%d' % (windowSize, windowSize, 
                                    positionRight, positionDown)) 
  
  wrongStims.resizable(width = False, height = False) ##The window is not resizeable.

  wrongStims.wm_title("Incorrect stimuli")
  wrongStims.overrideredirect(1) ##Removes task bar.
  
  Label(wrongStims, text = 'Please enter at least one valid stimulus').pack(side = TOP)
  Label(wrongStims, text = 'or remove invalid stimuli').pack(side = TOP)
  
  pressToClose = Button(wrongStims, text = "Return", 
                        command = lambda: return_to_stims(main))
  pressToClose.pack(side = BOTTOM)
  ##Removes main window.  
  main.withdraw()    

##Function is called when an incorrect agent is entered.
def incorrect_agent(main):
  global wrongAgent
  ##Create pop-up window.
  wrongAgent = Toplevel()
    
  wrongAgent.config(takefocus = True) ##Get focus on screen.   
    
  windowSize = 300 ##Pop up size (300 x 300).
  
  ##Collect screen (monitor) width and height to position the window in the center. 
  screenWidth = wrongAgent.winfo_screenwidth() 
  screenHeight = wrongAgent.winfo_screenheight()
  
  ##Calculate the center position.  
  positionRight = screenWidth/2 - windowSize/2
  positionDown = screenHeight/2 - windowSize/2
  
  ##Set the window size using the geometry() method.  
  wrongAgent.geometry('%dx%d+%d+%d' % (windowSize, windowSize, 
                                      positionRight, positionDown)) 
    
  wrongAgent.resizable(width = False, height = False) ##The window is not resizeable.

  wrongAgent.wm_title("Incorrect behaviour(s)")
  wrongAgent.overrideredirect(1) ##Removes task bar.
    
  Label(wrongAgent, text = 'Please enter one valid agent').pack(side = TOP)
    
  pressToClose = Button(wrongAgent, text = "Return", 
                        command = lambda: return_to_bevs_agent(main))
  pressToClose.pack(side = BOTTOM)
  
  ##Removes main window.   
  main.withdraw()    

##Function is called when an incorrect behaviour is entered.
def incorrect_bevs(main):
  global wrongBevs
  ##Create pop-up window.
  wrongBevs = Toplevel()
  
  wrongBevs.config(takefocus = True) ##Get focus on screen. 
    
  windowSize = 300 ##Pop up size (300 x 300).
  
  ##Collect screen (monitor) width and height to position the window in the center. 
  screenWidth = wrongBevs.winfo_screenwidth() 
  screenHeight = wrongBevs.winfo_screenheight()
    
  ##Calculate the center position.  
  positionRight = screenWidth/2 - windowSize/2
  positionDown = screenHeight/2 - windowSize/2
  
  ##Set the window size using the geometry() method.  
  wrongBevs.geometry('%dx%d+%d+%d' % (windowSize, windowSize, 
                                      positionRight, positionDown)) 
    
  wrongBevs.resizable(width = False, height = False) ##The window is not resizeable.

  wrongBevs.wm_title("Incorrect behaviour(s)")
  wrongBevs.overrideredirect(1) ##Removes task bar.
    
  Label(wrongBevs, text = 'Please enter at least one valid behaviour').pack(side = TOP)
  Label(wrongBevs, text = 'or remove invalid behaviours').pack(side = TOP)
    
  pressToClose = Button(wrongBevs, text = "Return", 
                        command = lambda: return_to_bevs_bevs(main))
  pressToClose.pack(side = BOTTOM)
  
  ##Removes main window.  
  main.withdraw()    

##Function is called to verify entries in tables.
def check_if_good_table(bevDict, stimDict, circleTableBoxes, lambdaTableBoxes, 
                  circleTableValues, lambdaTableValues):
  invalidEntries = 0 ##A counter for invalid entries.
  
  firstFlag = True
  secondFlag = True
  
  found = False
  ##Search for incorrect value in circleTableValues. 
  for key in circleTableValues.keys():
    if circleTableValues[key] not in bevDict.values():
      if found == False:
        firstFlag = False 
        found = True
      circleTableBoxes[key].config(bg = 'red')
      invalidEntries += 1
    ##Change background to white (normal) if the value is now valid.  
    else:
      circleTableBoxes[key].config(bg = 'white')    
  
  found = False    
  ##Search for incorrect value in lambdaTableValues.     
  for key in lambdaTableValues.keys():
    if lambdaTableValues[key] not in stimDict.values() and lambdaTableValues[key] != 'N' and lambdaTableValues[key] != 'D':
      if found == False:
        secondFlag = False 
        found = True
      lambdaTableBoxes[key].config(bg = 'red') 
      invalidEntries += 1
    ##Change background to white (normal) if the value is now valid.  
    else: 
      lambdaTableBoxes[key].config(bg = 'white')
  
  ##If both tables contain valid values, return True; else return False.    
  if firstFlag == True and secondFlag == True:
    return True, invalidEntries
  else:
    return False, invalidEntries 

def incorrect_table(main, numInvalid):
  global invalidEntryPop
  ##Create pop-up window
  invalidEntryPop = Toplevel()
  invalidEntryPop.config(takefocus = True) ##Get focus on screen. 
  
  windowSize = 300 ##Pop up size (300 x 300).
  
  ##Collect screen (monitor) width and height to position the window in the center. 
  screenWidth = invalidEntryPop.winfo_screenwidth() 
  screenHeight = invalidEntryPop.winfo_screenheight()
  
  ##Calculate the center position.
  positionRight = screenWidth/2 - windowSize/2
  positionDown = screenHeight/2 - windowSize/2
  
  ##Set the window size using the geometry() method.
  invalidEntryPop.geometry('%dx%d+%d+%d' % (windowSize, windowSize, 
                                            positionRight, positionDown))    
  
  invalidEntryPop.resizable(width = False, height = False) ##The window is not resizeable.

  invalidEntryPop.wm_title("INVALID ENTRIES!")
  invalidEntryPop.overrideredirect(1) ##Removes task bar.
  
  Label(invalidEntryPop, text = 'Invalid Entries:').pack(side = TOP)
  invalidEntriesLabel = Label(invalidEntryPop, text = str(numInvalid) + 
                              ' entries to fix')
  invalidEntriesLabel.pack(side = TOP)
  
  pressToClose = Button(invalidEntryPop, text = "Return", 
                        command = lambda: return_to_tables(main))
  pressToClose.pack(side = BOTTOM)
  
  ##Removes main window.  
  main.withdraw()  

"""Functions which get rid of the pop-up window."""

##Generate the specified stim entries. 
def return_to_stims_deletion(main, stimList, numStims, stimScrollingArea):
  warningStims.destroy()
  
  ##Test to see if there is more than one word in the entry box
  ##and test to see if it is a number only.
  if len(numStims.split()) > 1 or numStims.replace(' ', '').isdigit() != True: 
    ##Call a function to pop up.
    incorrect_stim_num(main) 
  
  else:
    ##Extract the number from the string.
    numStims = int(numStims.replace(' ', ''))  
    
    ##Destroy the old frame. 
    stimScrollingArea[0].destroy()

    ##Clear list for specified entries.
    stimList.clear()   
    
    ##Make a new frame capable of scrolling to the new entry boxes specified
    ##by the user.
    stimScrollingArea[0] = vertSuperscroll.Scrolling_Area(main)
    stimScrollingArea[0].pack(expand = 1, fill=BOTH)
    
    stimTitle = Label(stimScrollingArea[0].innerframe, text='Please Enter The Stimuli')
    stimTitle.pack(side = TOP) 
        
    for i in range(numStims):
      stimEntry = Entry(stimScrollingArea[0].innerframe)   
      stimList.append(stimEntry)
      stimEntry.pack(side = TOP, pady = 10)    
  
    main.update()
    main.deiconify()  

##Function to return to main when user wishes to cancel inputting the stimuli.   
def return_to_stims_cancellation(main):
  main.update()
  main.deiconify()
  warningStims.destroy()

##Function to return to main when invalid number is enetred for the stimuli.  
def return_to_stim_num(main):
  main.update()
  main.deiconify()
  wrongStimNum.destroy()  

##Function to return to the stimuli entry page after the pop-up. 
def return_to_stims(main):
  main.update()
  main.deiconify()
  wrongStims.destroy() 

##Function to return to the behaviour entry page after the pop-up. 
def return_to_bevs_agent(main):
  main.update()
  main.deiconify()
  wrongAgent.destroy() 

##Function to return to the behaviour entry page after the pop-up. 
def return_to_bevs_bevs(main):
  main.update()
  main.deiconify()
  wrongBevs.destroy() 
  
##Function to return to the tables after the pop-up. 
def return_to_tables(main):
  main.update()
  main.deiconify()
  invalidEntryPop.destroy()