"""Imported modules."""
from tkinter import * ##Import the tkinter module to allow construction of the GUI interface.
import vertSuperscroll ##Module containing the widget allowing a vertical scrollbar.
from entry_mods import remove_stim ##Import the remove_stim() function to bind to each delete stim entry button.

"""Functions which validate entries/create pop-ups."""
##Function to warn user that current stims will be deleted.
def specify_stim(main, stimList, numStims, stimScrollingArea, remove_x, return_arrow):
  """ (tkinter.Tk, dict, int, tkinter.Frame) -> (none)
    
    Pop-up when the user specifies a number of
    stimuli to add.
  
  """   
  global warningStims
  
  ##Test to see if there is more than one word in the entry box
  ##and test to see if it is a number only.
  if len(numStims.split()) > 1 or numStims.replace(' ', '').isdigit() != True:    
    
    ##Call a function to pop up.
    incorrect_stim_num(main, return_arrow) 
    
  else: ##True if entry is valid.  
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
    warningStims.geometry('%dx%d+%d+%d' % (windowSize, windowSize/4, 
                                      positionRight, positionDown)) 
    
    warningStims.resizable(width = False, height = False) ##The window is not resizeable.
  
    warningStims.wm_title("WARNING")

    ##Disable main window until pop up is closed
    warningStims.grab_set()
    
    Label(warningStims, text = 'This action will permenantly delete the current stimuli').pack(side = TOP)
    
    pressToContinue = Button(warningStims, text = "Continue", 
                          command = lambda: return_to_stims_deletion(main, stimList, numStims, stimScrollingArea, remove_x))
    
    pressToClose = Button(warningStims, image = return_arrow, border = 0, 
                          command = lambda: return_to_stims_cancellation(main))
    
    pressToContinue.pack(side = BOTTOM)
    
    pressToClose.pack(side = BOTTOM, anchor = E)
        

##Function to warn the user that the specified number of stims is invalid.
def incorrect_stim_num(main, return_arrow):
  """ (tkinter.Tk, dict, int, tkinter.Frame) -> (none)
    
    Pop-up when the user specifies a wrong number of
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
  wrongStimNum.geometry('%dx%d+%d+%d' % (windowSize, windowSize/4, 
                                    positionRight, positionDown)) 
  
  wrongStimNum.resizable(width = False, height = False) ##The window is not resizeable.

  wrongStimNum.wm_title("Incorrect stimuli number")
  
  ##Disable main window until pop up is closed
  wrongStimNum.grab_set()
  
  Label(wrongStimNum, text = 'Please enter a valid number of stimuli').pack(side = TOP)
  
  pressToClose = Button(wrongStimNum, image = return_arrow, border = 0, 
                        command = lambda: return_to_stim_num(main))
  pressToClose.pack(side = BOTTOM, anchor = E)
   

##Function is called when an incorrect stimuli is entered.
def incorrect_stims(main, return_arrow):
  """ (tkinter.Tk) -> (none)
    
    Pop-up to tell user that a stimulis (or stimuli) 
    are invalid.
  
  """       
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
  wrongStims.geometry('%dx%d+%d+%d' % (windowSize, windowSize/4, 
                                    positionRight, positionDown)) 
  
  wrongStims.resizable(width = False, height = False) ##The window is not resizeable.

  wrongStims.wm_title("Incorrect stimuli")
  ##Disable main window until pop up is closed
  wrongStims.grab_set()
  
  Label(wrongStims, text = 'Please enter at least one valid stimulus').pack(side = TOP)
  Label(wrongStims, text = 'or remove invalid stimuli').pack(side = TOP)
  
  pressToClose = Button(wrongStims, image = return_arrow, border = 0,
                        command = lambda: return_to_stims(main))
  pressToClose.pack(side = BOTTOM, anchor = E)
   

##Function is called when an incorrect agent is entered.
def incorrect_agent(main, return_arrow):
  """ (tkinter.Tk) -> (none)
    
    Pop-up to tell the user that the agent entry
    is incorrect.
  
  """       
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
  wrongAgent.geometry('%dx%d+%d+%d' % (windowSize, windowSize/4, 
                                      positionRight, positionDown)) 
    
  wrongAgent.resizable(width = False, height = False) ##The window is not resizeable.

  wrongAgent.wm_title("Incorrect behaviour(s)")

  ##Disable main window until pop up is closed
  wrongAgent.grab_set()
    
  Label(wrongAgent, text = 'Please enter one valid agent').pack(side = TOP)
    
  pressToClose = Button(wrongAgent, image = return_arrow, border = 0, 
                        command = lambda: return_to_bevs_agent(main))
  pressToClose.pack(side = BOTTOM, anchor = E)
  

##Function is called when an incorrect behaviour is entered.
def incorrect_bevs(main, return_arrow):
  """ (tkinter.Tk) -> (none)
    
    Pop-up to tell the user that the agent behaviour entry
    is incorrect.
  
  """       
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
  wrongBevs.geometry('%dx%d+%d+%d' % (windowSize, windowSize/4, 
                                      positionRight, positionDown)) 
    
  wrongBevs.resizable(width = False, height = False) ##The window is not resizeable.

  wrongBevs.wm_title("Incorrect behaviour(s)")
  
  ##Disable main window until pop up is closed
  wrongBevs.grab_set()
    
  Label(wrongBevs, text = 'Please enter at least one valid behaviour').pack(side = TOP)
  Label(wrongBevs, text = 'or remove invalid behaviours').pack(side = TOP)
    
  pressToClose = Button(wrongBevs, image = return_arrow, border = 0, 
                        command = lambda: return_to_bevs_bevs(main))
  pressToClose.pack(side = BOTTOM, anchor = E)
  

##Function is called when an incorrect concrete behaviour is entered.

def incorrect_CBS(main, return_arrow):
  """ (tkinter.Tk) -> (none)
    
    Pop-up to tell the user that the concrete behaviour entries
    are incorrect.
  
  """    
  global wrongCBS

  ##Create pop-up window.
  wrongCBS = Toplevel()

  wrongCBS.config(takefocus = True) ##Get focus on screen.  

  windowSize = 300 ##Pop up size (300 x 300). 

  ##Collect screen (monitor) width and height to position the window in the center. 
  screenWidth = wrongCBS.winfo_screenwidth() 
  screenHeight = wrongCBS.winfo_screenheight()

  ##Calculate the center position.
  positionRight = screenWidth/2 - windowSize/2
  positionDown = screenHeight/2 - windowSize/2

  ##Set the window size using the geometry() method.
  wrongCBS.geometry('%dx%d+%d+%d' % (windowSize, windowSize/4, 
                                    positionRight, positionDown)) 

  wrongCBS.resizable(width = False, height = False) ##The window is not resizeable.

  wrongCBS.wm_title("Incorrect Concrete Behaviour")

  ##Disable main window until pop up is closed
  wrongCBS.grab_set()

  Label(wrongCBS, text = 'Please enter at least one valid concrete behaviour').pack(side = TOP)

  Label(wrongCBS, text = 'or remove invalid concrete behaviour').pack(side = TOP) 

  pressToClose = Button(wrongCBS, image = return_arrow, border = 0, 
                        command = lambda: return_to_CBS(main))

  pressToClose.pack(side = BOTTOM, anchor = E)


def check_if_good_CBS(main, allEntriesCBS, allRadioButtons, allTextBoxCBS):
  """ (tkinter.Tk, dict, tupple) -> (Bool)
    
    Pop-up to tell the user that the agent behaviour entry
    is incorrect.
  
  """    
  ##Extract the number of agents.
  numAgents = len(allEntriesCBS)
  
  ##Flag to check if there are any invalid entries. Assumming everything is good.
  goodCBS = True
  for boxIndex in range(numAgents):
    
    ##Extract the radio button that was pressed for each window.
    whichRadio = allRadioButtons[boxIndex][2]
  
    ##Check which template is being used (either Rows or Box).
    if whichRadio.get() == 'Rows':
      for entry in range(1, allEntriesCBS[boxIndex][0, 0] + 1):
        ##Check through CBS dictionary to find specific invalidities.
        if allEntriesCBS[boxIndex][entry, 1].get() == ' ' * len(allEntriesCBS[boxIndex][entry, 1].get()):
          if goodCBS == True:
            goodCBS = False
            
          ##If entry is invalid, change the background to white.
          allEntriesCBS[boxIndex][entry, 1].config(background = 'tomato')
    
        else:
          ##If entry is valid, change the backgound to white.
          allEntriesCBS[boxIndex][entry, 1].config(background = 'white')
  
    else: ##Concrete behaviours was on box display.
      ##Create list of texbox lines, filters out empty lines.
      textBoxWords = allTextBoxCBS[boxIndex].get("1.0", END).split()
      
      ##Check if the textbox is empty.
      if len(textBoxWords) == 0:
        if goodCBS == True:
          goodCBS = False 
      
      ##Check to see if the number of 'if' equals to the number of 'fi' and check if there 
      ##are any 'if' as well.  
      if textBoxWords.count('if') != textBoxWords.count('fi'):   
        if goodCBS == True:
          goodCBS = False
      
  ##If there are no invalid entries, return True; else return False  
  return goodCBS 

##Function is called to verify entries in tables.
def check_if_good_table(allBevDict, stimDict, allCircleTableBoxes, allLambdaTableBoxes, 
                  allCircleTableValues, allLambdaTableValues):
  """ (dict, dict, dict, dict, dict, dict) -> (bool)
    
    Validates all data in the tables by returning True
    if the data is valid, or False if it is not.
  
  """       
  invalidEntries = 0 ##A counter for invalid entries.
  
  ##Extract the number of agents.
  numAgents = len(allCircleTableBoxes)  
  
  ##Assuming both tables are good for each agent.
  circleTablesGood = True
  lambdaTablesGood = True
  
  for boxIndex in range(numAgents):

    ##Search for incorrect value in circleTableValues. 
    for key in allCircleTableValues[boxIndex + 1].keys():
      if allCircleTableValues[boxIndex + 1][key] not in allBevDict[boxIndex + 1].values():
        if circleTablesGood == True:
          circleTablesGood = False 
  
        allCircleTableBoxes[boxIndex + 1][key].config(bg = 'tomato')
        invalidEntries += 1
        
      ##Change background to white (normal) if the value is now valid.  
      else:
        allCircleTableBoxes[boxIndex + 1][key].config(bg = 'white')    
    
    
    ##Search for incorrect value in lambdaTableValues.     
    for key in allLambdaTableValues[boxIndex + 1].keys():
      if allLambdaTableValues[boxIndex + 1][key] not in stimDict.values() and allLambdaTableValues[boxIndex + 1][key] != 'N' and allLambdaTableValues[boxIndex + 1][key] != 'D':
        if lambdaTablesGood == True:
          lambdaTablesGood = False 
         
        allLambdaTableBoxes[boxIndex + 1][key].config(bg = 'tomato') 
        invalidEntries += 1
        
      ##Change background to white (normal) if the value is now valid.  
      else: 
        allLambdaTableBoxes[boxIndex + 1][key].config(bg = 'white')
  
  ##If both tables contain valid values, return True; else return False.    
  if circleTablesGood == True and lambdaTablesGood == True:
    return True, invalidEntries
  else:
    return False, invalidEntries 

def incorrect_table(main, numInvalid, return_arrow):
  """ (tkinter.Tk, int) -> (none)
    
    Pop-up to tell the user that some entries are inccorect
    in the table. The pop-up specifies the number of entries 
    to fix.
  
  """       
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
  invalidEntryPop.geometry('%dx%d+%d+%d' % (windowSize, windowSize/4, 
                                            positionRight, positionDown))    
  
  invalidEntryPop.resizable(width = False, height = False) ##The window is not resizeable.

  invalidEntryPop.wm_title("INVALID ENTRIES!")
  
  ##Disable main window until pop up is closed
  invalidEntryPop.grab_set()
  
  Label(invalidEntryPop, text = 'Invalid Entries:').pack(side = TOP)
  invalidEntriesLabel = Label(invalidEntryPop, text = str(numInvalid) + 
                              ' entries to fix')
  invalidEntriesLabel.pack(side = TOP)
  
  pressToClose = Button(invalidEntryPop, image = return_arrow, border = 0, 
                        command = lambda: return_to_tables(main))
  pressToClose.pack(side = BOTTOM, anchor = E)
  

"""Functions which get rid of the pop-up window."""

##Generate the specified stim entries. 
def return_to_stims_deletion(main, stimList, numStims, stimScrollingArea, remove_x):
  """ (tkinter.Tk, dict, int, tkinter.Frame) -> (none)
    
    After confirming with the user that the stimuli entries
    will be deleted, this function begins deleting the current
    entries and creates the specified number of stimuli.
  
  """       
  warningStims.destroy()
  
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
    stimEntryFrame = Frame(stimScrollingArea[0].innerframe)
    stimEntry = Entry(stimEntryFrame)
    stimDeleteButton = Button(stimEntryFrame, image = remove_x, border = 0, 
                              command = lambda boxIndex=i: remove_stim(main, stimList, stimScrollingArea, boxIndex, remove_x))
    stimList.append(stimEntry)
    stimEntry.pack(side = LEFT)
    stimDeleteButton.pack(side = RIGHT)
    stimEntryFrame.pack(side = TOP, pady = 10)   

##Function to return to main when user wishes to cancel inputting the stimuli.   
def return_to_stims_cancellation(main):
  """ (tkinter.Tk) -> (none)
    
    Destroys the warningStims window and re-generates
    the main window.
  
  """       
  warningStims.destroy()

##Function to return to main when invalid number is enetred for the stimuli.  
def return_to_stim_num(main):
  """ (tkinter.Tk) -> (none)
    
    Destroys the wrongStimNum window and re-generates
    the main window.
  
  """   
  wrongStimNum.destroy()  

##Function to return to the stimuli entry page after the pop-up. 
def return_to_stims(main):
  """ (tkinter.Tk) -> (none)
    
    Destroys the wrongStims window and re-generates
    the main window.
  
  """   
  wrongStims.destroy() 

##Function to return to the behaviour entry page after the pop-up. 
def return_to_bevs_agent(main):
  """ (tkinter.Tk) -> (none)
    
    Destroys the wrongAgent window and re-generates
    the main window.
  
  """   
  wrongAgent.destroy() 

##Function to return to the behaviour entry page after the pop-up. 
def return_to_bevs_bevs(main):
  """ (tkinter.Tk) -> (none)
    
    Destroys the wrongBevs window and re-generates
    the main window.
  
  """   
  wrongBevs.destroy() 
  
##Function to return to the concrete behaviour page after the pop-up
def return_to_CBS(main):
  """ (tkinter.Tk) -> (none)
    
    Destroys the wrongCBS window and re-generates
    the main window.
  
  """     
  wrongCBS.destroy()    
  
##Function to return to the tables after the pop-up. 
def return_to_tables(main):
  """ (tkinter.Tk) -> (none)
    
    Destroys the invalidEntryPop window and re-generates
    the main window.
  
  """   
  invalidEntryPop.destroy()