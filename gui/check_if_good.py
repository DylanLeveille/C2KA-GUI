from tkinter import*

#
#Functions which validate entries/create pop-ups:
#

#function is called when an incorrect stimuli is entered
def incorrect_stims(main):
  global wrongStims
  #create pop-up window
  wrongStims = Toplevel()
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

#function is called when an incorrect behaviour is entered
def incorrect_bevs(main):
  global wrongBevs
  #create pop-up window
  wrongBevs = Toplevel()
    
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
                        command = lambda: return_to_bevs(main))
  pressToClose.pack(side = BOTTOM)
  
  #remove main window  
  main.withdraw()    

#function is callled to verify entries in tables
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

#
#Functions which regenerate the main window
#

#function to return to the stimuli entry page after the pop-up 
def return_to_stims(main):
  main.update()
  main.deiconify()
  wrongStims.destroy() 
 
 #regenerate the stim boxes that were un-packed
 #for i in range(len(stimList)):   
 # stimList[i].pack(side = TOP) 

#function to return to the behaviour entry page after the pop-up 
def return_to_bevs(main):
  main.update()
  main.deiconify()
  wrongBevs.destroy() 
