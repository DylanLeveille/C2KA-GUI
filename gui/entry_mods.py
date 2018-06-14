"""Imported modules."""
from tkinter import * ##Import the tkinter module to allow construction of the GUI interface.
import vertSuperscroll ##Module containing the widget allowing a vertical scrollbar.

"""Functions which modify entry boxes in the program."""
##Function to add a new stimuli. 
def add_stim(main, stimList, stimFrameList, stimScrollingArea, remove_x, return_arrow):
  """ (tkinter.Tk, dict, tkinter.Frame) -> (none)
    
    Adds a stimuli entry box to the addStim page,
    and updates the scrolling area.  
  
  """ 
  ##Make a new frame capable of scrolling to the new entry box.
  stimScrollingAreaTemp = vertSuperscroll.Scrolling_Area(main)
  stimScrollingAreaTemp.pack(expand = 1, fill=BOTH)
  
  ##Make a new title for the frame.
  stimTitle = Label(stimScrollingAreaTemp.innerframe, text='Please Enter The Stimuli')
  stimTitle.pack(side = TOP) 
  
  ##Generate the boxes.    
  for i in range(len(stimList)):
    ##Declare a frame in the scrolling area.
    stimEntryFrame = Frame(stimScrollingAreaTemp.innerframe, height = 27)
    
    ##Declare widgets in the frame.
    stimEntry = Entry(stimEntryFrame)
    stimDeleteButton = Button(stimEntryFrame, image = remove_x, border = 0, 
                              command = lambda boxIndex = i: remove_stim(main, stimList, stimFrameList, stimScrollingArea, boxIndex, remove_x))
    
    ##Insert frame/widgets in their respective data structures.
    stimEntry.insert(0, stimList[i].get()) ##Get previous text.    
    stimList[i] = stimEntry
    stimFrameList[i] = stimEntryFrame
    
    ##Pack new frame/widgets.
    stimEntryFrame.pack(side = TOP, pady = 10)
    stimEntry.pack(side = LEFT)
    stimDeleteButton.pack(side = RIGHT)
  
  ##Assign a new entry box to the scrolling area by making a new frame.
  stimEntryFrame = Frame(stimScrollingAreaTemp.innerframe, height = 27)
  
  ####Declare widgets in the new frame.
  stimEntry = Entry(stimEntryFrame) 
  stimDeleteButton = Button(stimEntryFrame, image = remove_x, border = 0, 
                            command = lambda boxIndex=len(stimList): remove_stim(main, stimList, stimFrameList, stimScrollingArea, boxIndex, remove_x))   
  
  ##Pack new frame/widgets.
  stimEntryFrame.pack(side = TOP, pady = 10)
  stimEntry.pack(side = LEFT)
  stimDeleteButton.pack(side = RIGHT)
  
  ##Add the new entry and the frame to their respective list.
  stimList.append(stimEntry)
  stimFrameList.append(stimEntryFrame)  
  
  ##Destroy old frame.
  stimScrollingArea[0].destroy()
  
  ##Assign new frame.
  stimScrollingArea[0] = stimScrollingAreaTemp
    
##Function to remove stimuli. 
def remove_stim(main, stimList, stimFrameList, stimScrollingArea, boxIndex, remove_x):
  """ (tkinter.Tk, dict, dict, tkinter.Frame, int) -> (none)
    
    Removes the specified stimuli entry box if the delete entry 
    button was pressed. Also updates the scrolling area to
    apadt to this change.
  
  """  
  ##Make a new frame capable of scrolling to the new entry box.
  stimScrollingAreaTemp = vertSuperscroll.Scrolling_Area(main)
  stimScrollingAreaTemp.pack(expand = 1, fill=BOTH)
  
  ##Make a new title for the frame.
  stimTitle = Label(stimScrollingAreaTemp.innerframe, text='Please Enter The Stimuli')
  stimTitle.pack(side = TOP)
   
  ##Delete entry at specified index in the frame lsit and stimuli list. 
  del stimList[boxIndex]
  del stimFrameList[boxIndex]           
  
  ##Generate the boxes.       
  for i in range(len(stimList)):
    ##Declare a frame in the scrolling area.
    stimEntryFrame = Frame(stimScrollingAreaTemp.innerframe, height = 27)
    
    ##Declare widgets in the frame.
    stimEntry = Entry(stimEntryFrame)
    stimDeleteButton = Button(stimEntryFrame, image = remove_x, border = 0, 
                              command = lambda boxIndex = i: remove_stim(main, stimList, stimFrameList, stimScrollingArea, boxIndex, remove_x))
    
    ##Insert frame/widgets in their respective data structures.
    stimEntry.insert(0, stimList[i].get()) ##Get previous text.    
    stimList[i] = stimEntry
    stimFrameList[i] = stimEntryFrame
    
    ##Pack new frame/widgets.
    stimEntryFrame.pack(side = TOP, pady = 10)
    stimEntry.pack(side = LEFT)
    stimDeleteButton.pack(side = RIGHT)
  
  ##Destroy old frame
  stimScrollingArea[0].destroy()
  
  ##Assign new frame
  stimScrollingArea[0] = stimScrollingAreaTemp 
    
##Button function to fill lambda table with neutral stimulus.
def fill_n(bevDict, stimDict, circleTableBoxes, lambdaTableBoxes):
  """ (dict, dict, dict, dict) -> (none)
    
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