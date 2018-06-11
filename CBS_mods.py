"""Imported modules."""
from tkinter import * ##Import the tkinter module to allow construction of the GUI interface.
from delete_CBS import * ##Contains a function which deletes concrete behaviour rows. 
from add_CBS import * ##Contains a function which adds concrete behaviour rows.

"""Functions which will adapt to any changes brought to the concrete behaviours."""
##Function called when no CBS were yet generated.
def create_CBS_entries(bevDict, frameCBS):
  """ (dict, tkinter.Frame) -> (dict)
    
    Creates the first set of concrete behaviours on the
    CBS page. The entries are saved 
  
  """    
  ##Create an empty dictionary to hold entries on concrete behaviours page.
  entriesCBS = {}
  
  ##Iterate across the behaviour dictionary to create concrete behaviours
  ##in the frameCBS.
  for i in range(1, len(bevDict) + 1):
      ##Create label/entry.
      labelCBS = Label(frameCBS, text = bevDict[i])
      entryCBS = Entry(frameCBS)
      
      ##Pack label/entry.
      labelCBS.pack(anchor = W)
      entryCBS.pack(anchor = W)
      
      ##Assign label/entry to dictionary.
      entriesCBS[i, 0] = labelCBS
      entriesCBS[i, 1] = entryCBS
  
  ##Return data structure.
  return entriesCBS

##Called to see if any modifications are necessary to the CBS data.
def fix_CBS(bevDict, frameCBS, entriesCBS):
  """ (dict, tkinter.Frame, dict) -> (dict)
    
    Modifies the concrete behaviour data based on
    any modifications to the behavioursthat may have 
    been made when returning to a previous page.
  
  """    
  ##Extract current number of rows in CBS.
  numRows = entriesCBS[0, 0]
  
  ##Keep track of the current row for recursion in delete_CBS.
  currRow = 1
  
  ##Number of rows to delete.
  delRows = 0
  
  ##Check to see how many rows need to be deleted.
  delRows = delete_CBS(bevDict, currRow, numRows, entriesCBS, delRows)
  
  ##Save new number of rows in the dictionary.
  entriesCBS[0, 0] = numRows - delRows    
  
  while delRows > 0:
      ##Get rid of label.
      entriesCBS[numRows - delRows + 1, 0].destroy()
      
      ##Get rid of entry.
      entriesCBS[numRows - delRows + 1, 1].destroy()        
      
      ##Remove the label/entry from the dictionary.
      del entriesCBS[numRows - delRows + 1, 0]
      del entriesCBS[numRows - delRows + 1, 1]
      
      ##Decrease number of rows to delete by 1.
      delRows -= 1
  
  ##Save new number of rows.
  numRows = entriesCBS[0, 0]
  
  ##Check to see how many rows need to be added.
  add_CBS(bevDict, numRows, entriesCBS, frameCBS)
  
  ##Return data scructure of new CBS entries/labels.
  return entriesCBS

##Function that recreates the concrete behaviours on the page.
def recreate_CBS_entries(bevDict, entriesCBS, frameCBS):
  """ (dict, tkinter.Frame, dict) -> (dict)
    
    Recreates the scrolling area and frame
    for the concrete behaviours based on the
    new data.
  
  """   
  ##Iterate through the rows to re-generate them.
  for row in range(1, len(bevDict) + 1):
      
      ##Create CBS label.
      labelCBS = Label(frameCBS, text = bevDict[row])
      
      ##Create CBS entry.
      entryCBS = Entry(frameCBS)
      entryCBS.insert(0, entriesCBS[row, 1].get())
      
      ##Pack new label/entry.
      labelCBS.pack(anchor = W)
      entryCBS.pack(anchor = W)
      
      ##Save label/entry in the data structure.
      entriesCBS[row, 0] = labelCBS
      entriesCBS[row, 1] = entryCBS
  
  ##Return updated data structure.    
  return entriesCBS