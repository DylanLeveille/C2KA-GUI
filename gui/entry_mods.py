"""Imported modules."""
from tkinter import * ##Import the tkinter module to allow construction of the GUI interface.
import vertSuperscroll ##Module containing the widget allowing a vertical scrollbar.

"""Functions which modify entry boxes in the program."""
##Function to add a new stimuli. 
def add_stim(main, stimList, stimScrollingArea, remove_x):
  """ (tkinter.Tk, list, tkinter.Frame, tkinter.PhotoImage) -> (none)
    
    Adds a stimuli entry box to the addStim page,
    and updates the scrolling area.  
  
  """ 
  ##Make a new frame capable of scrolling to the new entry box.
  stimScrollingAreaTemp = vertSuperscroll.Scrolling_Area(main)
  stimScrollingAreaTemp.pack(expand = 1, fill=BOTH)  
  
  ##Generate the boxes.    
  for i in range(len(stimList)):
    ##Declare a frame in the scrolling area.
    stimEntryFrame = Frame(stimScrollingAreaTemp.innerframe, height = 27)
    
    ##Declare widgets in the frame.
    stimEntry = Entry(stimEntryFrame)
    stimDeleteButton = Button(stimEntryFrame, image = remove_x, border = 0, 
                              command = lambda boxIndex = i: remove_stim(main, stimList, stimScrollingArea, boxIndex, remove_x))
    
    ##Insert widget in the data structure.
    stimEntry.insert(0, stimList[i].get()) ##Get previous text.    
    stimList[i] = stimEntry
    
    ##Pack new frame/widgets.
    stimEntryFrame.pack(side = TOP, pady = 10)
    stimEntry.pack(side = LEFT)
    stimDeleteButton.pack(side = RIGHT)
  
  ##Assign a new entry box to the scrolling area by making a new frame.
  stimEntryFrame = Frame(stimScrollingAreaTemp.innerframe, height = 27)
  
  ####Declare widgets in the new frame.
  stimEntry = Entry(stimEntryFrame) 
  stimDeleteButton = Button(stimEntryFrame, image = remove_x, border = 0, 
                            command = lambda boxIndex=len(stimList): remove_stim(main, stimList, stimScrollingArea, boxIndex, remove_x))   
  
  ##Pack new frame/widgets.
  stimEntryFrame.pack(side = TOP, pady = 10)
  stimEntry.pack(side = LEFT)
  stimDeleteButton.pack(side = RIGHT)
  
  ##Add the new entry and the frame to their respective list.
  stimList.append(stimEntry)
  
  ##Destroy old frame.
  stimScrollingArea[0].destroy()
  
  ##Assign new frame.
  stimScrollingArea[0] = stimScrollingAreaTemp
    
##Function to remove stimuli. 
def remove_stim(main, stimList, stimScrollingArea, boxIndex, remove_x):
  """ (tkinter.Tk, list, tkinter.Frame, int, tkinter.PhotoImage) -> (none)
    
    Removes the specified stimuli entry box if the delete entry 
    button was pressed. Also updates the scrolling area to
    adapt to this change.
  
  """  
  ##Get screen width to make dimensions relative to that value.
  screenWidth = main.winfo_screenwidth()   
  
  ##Make a new frame capable of scrolling to the new entry box.
  stimScrollingAreaTemp = vertSuperscroll.Scrolling_Area(main)
  stimScrollingAreaTemp.pack(expand = 1, fill=BOTH)

   
  ##Delete entry at specified index in the frame lsit and stimuli list. 
  del stimList[boxIndex]         
  
  ##Generate the boxes.       
  for i in range(len(stimList)):
    ##Declare a frame in the scrolling area.
    stimEntryFrame = Frame(stimScrollingAreaTemp.innerframe, height = 27)
    
    ##Declare widgets in the frame.
    stimEntry = Entry(stimEntryFrame)
    stimDeleteButton = Button(stimEntryFrame, image = remove_x, border = 0, 
                              command = lambda boxIndex = i: remove_stim(main, stimList, stimScrollingArea, boxIndex, remove_x))
    
    ##Insert the widget in the data structure.
    stimEntry.insert(0, stimList[i].get()) ##Get previous text.    
    stimList[i] = stimEntry
    
    ##Pack new frame/widgets.
    stimEntryFrame.pack(side = TOP, pady = 10)
    stimEntry.pack(side = LEFT)
    stimDeleteButton.pack(side = RIGHT)
  
  ##Destroy old frame
  stimScrollingArea[0].destroy()
  
  ##Assign new frame
  stimScrollingArea[0] = stimScrollingAreaTemp 

##Function to add an agent in the behaviours page.  
def add_agent(main, agentFrames, agentScrollingArea, remove_x):  
  """ (tkinter.Tk, dict, tkinter.Frame, tkinter.PhotoImage) -> (none)
    
    Adds a frame to hold a new agent and its behaviour in the addBev page,
    and updates the scrolling area.  
  
  """ 
  ##Make a new frame capable of scrolling to the new agent frames.
  agentScrollingAreaTemp = vertSuperscroll.Scrolling_Area(main)
  agentScrollingAreaTemp.pack(expand = 1, fill=BOTH, pady = (0, 80))
  
  ##Generate the agents.    
  for i in range(len(agentFrames['agentNames'])):
    ##Declare a frame in the scrolling area.
    agentEntryFrame = Frame(agentScrollingAreaTemp.innerframe, height = 80)
    
    ####Declare widgets in the new frame.
    agentLabel = Label(agentEntryFrame, text = 'Agent Name:')
    agentEntry = Entry(agentEntryFrame, width = 40)
    agentBevLabel = Label(agentEntryFrame, text = 'Agent Behaviour:')
    agentBevEntry = Entry(agentEntryFrame, width = 40)   
  
    agentDeleteButton = Button(agentEntryFrame, image = remove_x, border = 0, 
                              command = lambda boxIndex=i: remove_agent(main, agentFrames, agentScrollingArea, boxIndex, remove_x))   
    
    ##Insert widgets in their respective data structures.
    agentEntry.insert(0, agentFrames['agentNames'][i].get()) ##Get previous text.    
    agentFrames['agentNames'][i] = agentEntry
    
    agentBevEntry.insert(0, agentFrames['agentBev'][i].get()) ##Get previous text.    
    agentFrames['agentBev'][i] = agentBevEntry    
    
    ##Pack new frame/widgets.
    agentLabel.pack(side = TOP, anchor = W)
    agentEntry.pack(side = TOP, anchor = W)
    agentDeleteButton.pack(in_=agentEntryFrame, side = RIGHT, anchor = N, padx = 20)
    agentBevLabel.pack(side = TOP, anchor = W)
    agentBevEntry.pack(side = TOP, anchor = W)    
    agentEntryFrame.pack(side = TOP, anchor = W, fill = X, pady = 20)
  
  ##Assign a the new entry boxes to the scrolling area by making a new frame.
  agentEntryFrame = Frame(agentScrollingAreaTemp.innerframe, height = 80)
  
  ####Declare widgets in the new frame.
  agentLabel = Label(agentEntryFrame, text = 'Agent Name:')
  agentEntry = Entry(agentEntryFrame, width = 40)
  agentBevLabel = Label(agentEntryFrame, text = 'Agent Behaviour:')
  agentBevEntry = Entry(agentEntryFrame, width = 40)   
  
  agentDeleteButton = Button(agentEntryFrame, image = remove_x, border = 0, 
                            command = lambda boxIndex=len(agentFrames['agentNames']): remove_agent(main, agentFrames, agentScrollingArea, boxIndex, remove_x))   
  
  ##Pack new frame/widgets.
  agentLabel.pack(side = TOP, anchor = W)
  agentEntry.pack(side = TOP, anchor = W)
  agentDeleteButton.pack(in_=agentEntryFrame, side = RIGHT, anchor = N, padx = 20)
  agentBevLabel.pack(side = TOP, anchor = W)
  agentBevEntry.pack(side = TOP, anchor = W)    
  agentEntryFrame.pack(side = TOP, anchor = W, fill = X, pady = 20)

  ##Add the new entries to their respective list.
  agentFrames['agentNames'].append(agentEntry)
  agentFrames['agentBev'].append(agentBevEntry)
  
  ##Destroy old frame.
  agentScrollingArea[0].destroy()
  
  ##Assign new frame.
  agentScrollingArea[0] = agentScrollingAreaTemp  

def remove_agent(main, agentFrames, agentScrollingArea, boxIndex, remove_x):
  """ (tkinter.Tk, dict, tkinter.Frame, int, tkinter.PhotoImage) -> (none)
    
    Removes the specified agent if the delete entry 
    button was pressed. Also updates the scrolling area to
    adapt to this change.
  
  """  
  ##Make a new frame capable of scrolling to the new entry box.
  agentScrollingAreaTemp = vertSuperscroll.Scrolling_Area(main)
  agentScrollingAreaTemp.pack(expand = 1, fill=BOTH, pady = (0, 80))

  ##Delete agent at specified index in both lists. 
  del agentFrames['agentNames'][boxIndex]         
  del agentFrames['agentBev'][boxIndex]      
  
  ##Generate the agents.       
  for i in range(len(agentFrames['agentNames'])):
    ##Declare a frame in the scrolling area.
    agentEntryFrame = Frame(agentScrollingAreaTemp.innerframe, height = 80)
    
    ####Declare widgets in the new frame.
    agentLabel = Label(agentEntryFrame, text = 'Agent Name:')
    agentEntry = Entry(agentEntryFrame, width = 40)
    agentBevLabel = Label(agentEntryFrame, text = 'Agent Behaviour:')
    agentBevEntry = Entry(agentEntryFrame, width = 40)   
  
    agentDeleteButton = Button(agentEntryFrame, image = remove_x, border = 0, 
                              command = lambda boxIndex=i: remove_agent(main, agentFrames, agentScrollingArea, boxIndex, remove_x))   
    
    ##Insert widgets in their respective data structures.
    agentEntry.insert(0, agentFrames['agentNames'][i].get()) ##Get previous text.    
    agentFrames['agentNames'][i] = agentEntry
    
    agentBevEntry.insert(0, agentFrames['agentBev'][i].get()) ##Get previous text.    
    agentFrames['agentBev'][i] = agentBevEntry    
    
    ##Pack new frame/widgets.
    agentLabel.pack(side = TOP, anchor = W)
    agentEntry.pack(side = TOP, anchor = W)
    agentDeleteButton.pack(in_=agentEntryFrame, side = RIGHT, anchor = N, padx = 20)
    agentBevLabel.pack(side = TOP, anchor = W)
    agentBevEntry.pack(side = TOP, anchor = W)    
    agentEntryFrame.pack(side = TOP, anchor = W, fill = X, pady = 20)
  
  ##Destroy old frame
  agentScrollingArea[0].destroy()
  
  ##Assign new frame
  agentScrollingArea[0] = agentScrollingAreaTemp   

##Button function to fill circle table with each row's behaviour.
def fill_bev(bevDict, stimDict, circleTableBoxes):
  """ (dict, dict, dict) -> (none)
    
    Fills the circle tables entry boxes with each row's 
    behaviour if that box is empty.  
  
  """    
  for i in range(1, len(bevDict) + 1): ##Rows
    for j in range(1, len(stimDict) + 1): ##Columns
      ##Checking if empty in circle table.
      if circleTableBoxes[i, j].get() == ' ' * len(circleTableBoxes[i, j].get()):
        ##If empty, put behaviour name from the row.
        circleTableBoxes[i, j].delete(0, END) 
        circleTableBoxes[i, j].insert(0, circleTableBoxes[i, 0].cget("text"))
    
##Button function to fill lambda table with neutral stimulus.
def fill_n(bevDict, stimDict, lambdaTableBoxes):
  """ (dict, dict, dict) -> (none)
    
    Fills the lambda tables entry boxes with the neutral 
    stimulus if that box is empty.  
  
  """    
  for i in range(1, len(bevDict) + 1): ##Rows
    for j in range(1, len(stimDict) + 1): ##Columns
      ##Checking if empty in lambda table.
      if lambdaTableBoxes[i, j].get() == ' ' * len(lambdaTableBoxes[i, j].get()):
        ##If empty, put neutral stimulus.
        lambdaTableBoxes[i, j].delete(0, END) 
        lambdaTableBoxes[i, j].insert(0, 'N')