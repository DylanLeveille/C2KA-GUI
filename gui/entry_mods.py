"""Imported modules."""
from tkinter import * ##Import the tkinter module to allow construction of the GUI interface.
import vertSuperscroll ##Module containing the widget allowing a vertical scrollbar.

"""Functions which modify entry boxes in the program."""
##Function to add a new stimuli. 
def add_stim(main, stimList, stimScrollingArea):
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
    stimEntry = Entry(stimScrollingAreaTemp.innerframe)
    stimEntry.insert(0, stimList[i].get())    
    stimList[i] = stimEntry
    stimEntry.pack(side = TOP, pady=10)
  
  ##Assign new entry box.
  stimEntry = Entry(stimScrollingAreaTemp.innerframe)    
  stimEntry.pack(side = TOP, pady=10)     
  
  ##Destroy old frame.
  stimScrollingArea[0].destroy()
  
  ##Assign new frame.
  stimScrollingArea[0] = stimScrollingAreaTemp
  
  ##Add new entry to the list.
  stimList.append(stimEntry)
    
##Function to remove stimuli. 
def remove_stim(main, stimList, stimScrollingArea):
  """ (tkinter.Tk, dict, tkinter.Frame) -> (none)
    
    Removes a stimuli entry box to the addStim page,
    and updates the scrolling area.  
  
  """  
  ##We need at least one entry to be able to remove a stimulus.
  if len(stimList) > 0:
    ##Make a new frame capable of scrolling to the new entry box.
    stimScrollingAreaTemp = vertSuperscroll.Scrolling_Area(main)
    stimScrollingAreaTemp.pack(expand = 1, fill=BOTH)
    
    ##Make a new title for the frame.
    stimTitle = Label(stimScrollingAreaTemp.innerframe, text='Please Enter The Stimuli')
    stimTitle.pack(side = TOP) 
    
    ##Generate the boxes.       
    for i in range(len(stimList) - 1):
      stimEntry = Entry(stimScrollingAreaTemp.innerframe)
      stimEntry.insert(0, stimList[i].get())    
      stimList[i] = stimEntry
      stimEntry.pack(side = TOP, pady=10)
    
    ##Remove last entry in list. 
    stimList[len(stimList) - 1].destroy()
    del stimList[len(stimList) - 1]
    
    ##Destroy old frame
    stimScrollingArea[0].destroy()
    
    ##assign new frame
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