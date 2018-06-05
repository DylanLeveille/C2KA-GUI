from tkinter import*
import vertSuperscroll 

#
#Functions which validate entries/create pop-ups:
#

#function to warn user that stims will be deleted
def specify_stim(main, stimList, numStims, stimScrollingArea):
  global warningStims
  #create pop-up window

  warningStims = Toplevel()

  warningStims.config(takefocus = True)  
  
  windowSize = 300
  
  screenWidth = warningStims.winfo_screenwidth() 
  screenHeight = warningStims.winfo_screenheight()
  
  positionRight = screenWidth/2 - windowSize/2
  positionDown = screenHeight/2 - windowSize/2
  
  warningStims.geometry('%dx%d+%d+%d' % (windowSize, windowSize, 
                                    positionRight, positionDown)) 
  
  warningStims.resizable(width = False, height = False) 

  warningStims.wm_title("WARNING")
  warningStims.overrideredirect(1)
  Label(warningStims, text = 'This action will permenantly delete the current stimuli').pack(side = TOP)
  
  pressToContinue = Button(warningStims, text = "Continue", 
                        command = lambda: return_to_stims_deletion(main, stimList, numStims, stimScrollingArea))
  
  pressToClose = Button(warningStims, text = "Return", 
                        command = lambda: return_to_stims_cancellation(main))
  
  pressToContinue.pack(side = BOTTOM)
  
  pressToClose.pack(side = BOTTOM)
  #remove main window  
  main.withdraw()      

#function to warn the user that the specified number of stims is invalid
def incorrect_stim_num(main):
  global wrongStimNum
  #create pop-up window
  wrongStimNum = Toplevel()
  
  wrongStimNum.config(takefocus = True)  
  
  windowSize = 300
  
  screenWidth = wrongStimNum.winfo_screenwidth() 
  screenHeight = wrongStimNum.winfo_screenheight()
  
  positionRight = screenWidth/2 - windowSize/2
  positionDown = screenHeight/2 - windowSize/2
  
  wrongStimNum.geometry('%dx%d+%d+%d' % (windowSize, windowSize, 
                                    positionRight, positionDown)) 
  
  wrongStimNum.resizable(width = False, height = False) 

  wrongStimNum.wm_title("Incorrect stimuli number")
  wrongStimNum.overrideredirect(1)
  Label(wrongStimNum, text = 'Please enter a valid number of stimuli').pack(side = TOP)
  
  pressToClose = Button(wrongStimNum, text = "Return", 
                        command = lambda: return_to_stim_num(main))
  pressToClose.pack(side = BOTTOM)
  #remove main window
  main.withdraw()    

#function is called when an incorrect stimuli is entered
def incorrect_stims(main):
  global wrongStims
  #create pop-up window
  wrongStims = Toplevel()
  
  wrongStims.config(takefocus = True)  
  
  windowSize = 300
  
  screenWidth = wrongStims.winfo_screenwidth() 
  screenHeight = wrongStims.winfo_screenheight()
  
  positionRight = screenWidth/2 - windowSize/2
  positionDown = screenHeight/2 - windowSize/2
  
  wrongStims.geometry('%dx%d+%d+%d' % (windowSize, windowSize, 
                                    positionRight, positionDown)) 
  
  wrongStims.resizable(width = False, height = False) 

  wrongStims.wm_title("Incorrect stimuli")
  wrongStims.overrideredirect(1)
  Label(wrongStims, text = 'Please enter at least one valid stimulus').pack(side = TOP)
  Label(wrongStims, text = 'or remove invalid stimuli').pack(side = TOP)
  
  pressToClose = Button(wrongStims, text = "Return", 
                        command = lambda: return_to_stims(main))
  pressToClose.pack(side = BOTTOM)
  #remove main window  
  main.withdraw()    

#function is called when an incorrect agent is entered
def incorrect_agent(main):
  global wrongAgent
  #create pop-up window
  wrongAgent = Toplevel()
    
  wrongAgent.config(takefocus = True)  
    
  windowSize = 300
  
  screenWidth = wrongAgent.winfo_screenwidth() 
  screenHeight = wrongAgent.winfo_screenheight()
    
  positionRight = screenWidth/2 - windowSize/2
  positionDown = screenHeight/2 - windowSize/2
    
  wrongAgent.geometry('%dx%d+%d+%d' % (windowSize, windowSize, 
                                      positionRight, positionDown)) 
    
  wrongAgent.resizable(width = False, height = False) 

  wrongAgent.wm_title("Incorrect behaviour(s)")
  wrongAgent.overrideredirect(1)
    
  Label(wrongAgent, text = 'Please enter one valid agent').pack(side = TOP)
    
  pressToClose = Button(wrongAgent, text = "Return", 
                        command = lambda: return_to_bevs_agent(main))
  pressToClose.pack(side = BOTTOM)
  
  #remove main window  
  main.withdraw()    


#function is called when an incorrect behaviour is entered
def incorrect_bevs(main):
  global wrongBevs
  #create pop-up window
  wrongBevs = Toplevel()
  
  wrongBevs.config(takefocus = True)
    
  windowSize = 300
  
  screenWidth = wrongBevs.winfo_screenwidth() 
  screenHeight = wrongBevs.winfo_screenheight()
    
  positionRight = screenWidth/2 - windowSize/2
  positionDown = screenHeight/2 - windowSize/2
    
  wrongBevs.geometry('%dx%d+%d+%d' % (windowSize, windowSize, 
                                      positionRight, positionDown)) 
    
  wrongBevs.resizable(width = False, height = False) 

  wrongBevs.wm_title("Incorrect behaviour(s)")
  wrongBevs.overrideredirect(1)
    
  Label(wrongBevs, text = 'Please enter at least one valid behaviour').pack(side = TOP)
  Label(wrongBevs, text = 'or remove invalid behaviours').pack(side = TOP)
    
  pressToClose = Button(wrongBevs, text = "Return", 
                        command = lambda: return_to_bevs_bevs(main))
  pressToClose.pack(side = BOTTOM)
  
  #remove main window  
  main.withdraw()    

#function is called to verify entries in tables
def check_if_good(bevDict, stimDict, circleTableBoxes, lambdaTableBoxes, 
                  circleTableValues, lambdaTableValues):
  invalidEntries = 0 #a counter for invalid entries
  
  firstFlag = True
  secondFlag = True
  
  found = False
  #search for incorrect value in circleTableValues 
  for key in circleTableValues.keys():
    if circleTableValues[key] not in bevDict.values():
      if found == False:
        firstFlag = False 
        found = True
      circleTableBoxes[key].config(bg = 'red')
      invalidEntries += 1
    #change background to white (normal) if the value is now valid  
    else:
      circleTableBoxes[key].config(bg = 'white')    
  
  found = False    
  #search for incorrect value in lambdaTableValues     
  for key in lambdaTableValues.keys():
    if lambdaTableValues[key] not in stimDict.values() and lambdaTableValues[key] != 'N' and lambdaTableValues[key] != 'D':
      if found == False:
        secondFlag = False 
        found = True
      lambdaTableBoxes[key].config(bg = 'red') 
      invalidEntries += 1
    #change background to white (normal) if the value is now valid  
    else: 
      lambdaTableBoxes[key].config(bg = 'white')
  
  #if both tables contain valid values, return True; else return False    
  if firstFlag == True and secondFlag == True:
    return True, invalidEntries
  else:
    return False, invalidEntries 

def incorrect_table(main, numInvalid):
  global invalidEntryPop
  #create pop-up window
  invalidEntryPop = Toplevel()
  invalidEntryPop.config(takefocus = True)
  
  windowSize = 300
  
  screenWidth = invalidEntryPop.winfo_screenwidth() 
  screenHeight = invalidEntryPop.winfo_screenheight()
  
  positionRight = screenWidth/2 - windowSize/2
  positionDown = screenHeight/2 - windowSize/2
  
  invalidEntryPop.geometry('%dx%d+%d+%d' % (windowSize, windowSize, 
                                            positionRight, positionDown))    
  invalidEntryPop.resizable(width = False, height = False) 

  invalidEntryPop.wm_title("INVALID ENTRIES!")
  invalidEntryPop.overrideredirect(1)
  
  Label(invalidEntryPop, text = 'Invalid Entries:').pack(side = TOP)
  invalidEntriesLabel = Label(invalidEntryPop, text = str(numInvalid) + 
                              ' entries to fix')
  invalidEntriesLabel.pack(side = TOP)
  
  pressToClose = Button(invalidEntryPop, text = "Return", 
                        command = lambda: return_to_tables(main))
  pressToClose.pack(side = BOTTOM)
  
  #remove main window
  main.withdraw()  

#
#Functions which get rid of the pop-up window
#

#generate the specified stim entries 
def return_to_stims_deletion(main, stimList, numStims, stimScrollingArea):
  warningStims.destroy()
  
  #test to see if more than one word in the entry box
  #and test to see if it is a number only
  if len(numStims.split()) > 1 or numStims.replace(' ', '').isdigit() != True: 
    #call a function to pop up
    incorrect_stim_num(main) 
  
  else:
    #extract the number from the string
    numStims = int(numStims.replace(' ', ''))  
    
    #destroy the old frame 
    stimScrollingArea[0].destroy()

    #clear list for specified entries
    stimList.clear()   
    
    #make a new frame capable of scrolling to the new entry boxes specified
    #by the user
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

#return to main when user wishes to cancel inputting the stimuli   
def return_to_stims_cancellation(main):
  main.update()
  main.deiconify()
  warningStims.destroy()

#return to main when invalid number is enetred for the stimuli  
def return_to_stim_num(main):
  main.update()
  main.deiconify()
  wrongStimNum.destroy()  

#function to return to the stimuli entry page after the pop-up 
def return_to_stims(main):
  main.update()
  main.deiconify()
  wrongStims.destroy() 

#function to return to the behaviour entry page after the pop-up 
def return_to_bevs_agent(main):
  main.update()
  main.deiconify()
  wrongAgent.destroy() 

#function to return to the behaviour entry page after the pop-up 
def return_to_bevs_bevs(main):
  main.update()
  main.deiconify()
  wrongBevs.destroy() 
  
#function to return to the tables after the pop-up 
def return_to_tables(main):
  main.update()
  main.deiconify()
  invalidEntryPop.destroy()