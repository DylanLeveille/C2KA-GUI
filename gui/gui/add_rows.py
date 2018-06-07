"""Imported modules."""
from tkinter import * ##Import the tkinter module to allow construction of the GUI interface.

"""Function to add rows to the table and shift rows."""
def add_rows(numRows, numColumns, circleTableBoxes, lambdaTableBoxes, bevDict,
             circleGridFrame, lambdaGridFrame):
  """ (int, int, dict, dict, dict, tkinter.Frame, tkinter.Frame) -> (none)
    
    Adds rows to the tables for the new stimuli. Once added,
    the rows are shifted to match the behaviour order defined
    by the user.
  
  """    
  ##Create a list containing all the labels the tables currently have 
  ##in their rows.
  listOfLabels = []
  
  ##Appending the labels in the data scructure.
  for row in range(1, numRows + 1):
    listOfLabels.append(circleTableBoxes[row, 0].cget("text"))
    
  ##compare current table labels to what bevDict has.
  for i in range(len(bevDict)): ##Rows
    label = bevDict[i + 1]
    if label not in listOfLabels: ##Means a behaviour was added if True.
      ##Therefore, we will add a new row.
      numRows += 1
      
      ##Save the new number of rows in the dictionary.
      circleTableBoxes[0, 0] = numRows, numColumns 
      
      ##Create label box for a new row.
      circleTableBoxes[numRows, 0] = Label(circleGridFrame, text = label)
      
      lambdaTableBoxes[numRows, 0] = Label(lambdaGridFrame, text = label)   
      
      ##Create the entry boxes at the bottom of each table (to the right
      ##of the new label).
      for column in range(1, numColumns + 1):
        circleTableBoxes[numRows, column] = Entry(circleGridFrame)
        
        lambdaTableBoxes[numRows, column] = Entry(lambdaGridFrame)      
      
  ##Now that all the new rows have been added, the rows' positions must 
  ##be switched to match the order defined by the user.  
  for row in range(1, len(bevDict) + 1): ##Rows
    if bevDict[row] != circleTableBoxes[row, 0].cget("text"): ##Means the row is not in the right position.
      
      ##Theregore, find the position of the row that is supposed to be there by iteration.
      rowPos = row + 1
      while bevDict[row] != circleTableBoxes[rowPos, 0].cget("text"):
        rowPos += 1
        
      ##Switch the labels of the rows with a temporary variable.
      auxLabel = bevDict[row]
      
      circleTableBoxes[rowPos, 0].config(text = circleTableBoxes[row, 0].cget("text"))
      circleTableBoxes[row, 0].config(text = auxLabel)
      
      lambdaTableBoxes[rowPos, 0].config(text = lambdaTableBoxes[row, 0].cget("text"))
      lambdaTableBoxes[row, 0].config(text = auxLabel)      
      
      ##Switch the column entries across each column in each table by using
      ##a temporary variable..
      for column in range(1, numColumns + 1):
        auxEntry = circleTableBoxes[rowPos, column].get()
        
        circleTableBoxes[rowPos, column].delete(0, END) 
        circleTableBoxes[rowPos, column].insert(0, circleTableBoxes[row, column].get())
        
        circleTableBoxes[row, column].delete(0, END) 
        circleTableBoxes[row, column].insert(0, auxEntry)    
        
        auxEntry = lambdaTableBoxes[rowPos, column].get()
        
        lambdaTableBoxes[rowPos, column].delete(0, END) 
        lambdaTableBoxes[rowPos, column].insert(0, lambdaTableBoxes[row, column].get())
        
        lambdaTableBoxes[row, column].delete(0, END) 
        lambdaTableBoxes[row, column].insert(0, auxEntry)