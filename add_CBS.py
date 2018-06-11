"""Imported modules."""
from tkinter import * ##Import the tkinter module to allow construction of the GUI interface.

"""Function to add rows to the CBS page if necessary."""
def add_CBS(bevDict, numRows, entriesCBS, frameCBS):
  """ (dict, int, dict, tkinter.Frame) -> (none)
    
    Adds rows to the CBS page if behaviours
    were added in the behaviour dictionary.
  
  """    
  ##Creating a list of the current labels in the CBS page.
  listofLabels = []
  
  ##Appending the labels to the data scructure.
  for row in range(1, numRows + 1):
      listofLabels.append(entriesCBS[row, 0].cget("text"))
      
  ##Check behaviour dictionary to see if new behaviours were added.   
  for i in range(1, len(bevDict) + 1):
      currLabel = bevDict[i]
      
      if currLabel not in listofLabels: ##New behaviour added if True, =>create a new row with new behaviour. 
          ##Add an extra row and save the size in the entries dictionary.
          numRows += 1
          entriesCBS[0, 0] = numRows
          
          ##Assign the new label to entries dictionary.
          entriesCBS[numRows, 0] = Label(frameCBS, text = currLabel)
          
          ##Assign new entry to entries dictionary.
          entriesCBS[numRows, 1] = Entry(frameCBS)
          
          ##Pack the new label/entry in the frame.
          entriesCBS[numRows, 0].pack(anchor = W)
          entriesCBS[numRows, 1].pack(anchor = W)
          
  ##Now that the new entries/labels are added to the dictionary, shuffle the 
  ##rows to match the order defined by the user.
  for row in range(1, len(bevDict) + 1):
      if bevDict[row] != entriesCBS[row, 0].cget("text"): ##Means row is not at right position.
          ##rowPos defines the correct position to move row.
          rowPos = row + 1
          
          ##Iterate until the row's good position is found.
          while bevDict[row] != entriesCBS[rowPos, 0].cget("text"):
              rowPos += 1 
          
          ##Switch the labels of the rows with a temporary variable.
          auxLabel = bevDict[row]
          
          entriesCBS[rowPos, 0].config(text = entriesCBS[row, 0].cget("text"))
          entriesCBS[row, 0].config(text = auxLabel)
          
          ##And switch the entries too.
          entriesCBS[rowPos, 1].delete(0, END)
          entriesCBS[rowPos, 1].insert(0, entriesCBS[row, 1].get())
          entriesCBS[row, 1].delete(0, END)