"""Imported modules."""
from tkinter import * ##Import the tkinter module to allow construction of the GUI interface.

"""Function to add columns to the table and shift columns."""
def add_columns(numRows, numColumns, circleTableBoxes, lambdaTableBoxes, stimDict,
             circleGridFrame, lambdaGridFrame):
  """ (int, int, dict, dict, dict, tkinter.Frame, tkinter.Frame) -> (none)
    
    Adds columns to the tables for the new stimuli. Once added,
    the columns are shifted to match the stimuli order defined
    by the user.
  
  """      
  ##Create a list containing all the labels the tables currently have 
  ##in their columns.
  listOfLabels = []
  
  ##Appending the labels in the data scructure.
  for column in range(1, numColumns + 1):
    listOfLabels.append(circleTableBoxes[0, column].cget("text"))
    
  ##Compare current table labels to what stimDict has.
  for i in range(len(stimDict)): ##Columns.
    label = stimDict[i + 1]
    if label not in listOfLabels: ##Means a stimuli was added if True.
      ##Therefore, we will add a new column.
      numColumns += 1
      
      ##Save the new number of columns in the dictionary.
      circleTableBoxes[0, 0] = numRows, numColumns 
      
      ##Create a label box for a new column in each table.
      circleTableBoxes[0, numColumns] = Label(circleGridFrame, text = label)
      
      lambdaTableBoxes[0, numColumns] = Label(lambdaGridFrame, text = label)   
      
      ##Create the entry boxes at the right side of each table (underneath
      ##the new label).
      for row in range(1, numRows + 1):
        circleTableBoxes[row, numColumns] = Entry(circleGridFrame)
        
        lambdaTableBoxes[row, numColumns] = Entry(lambdaGridFrame)       
      
  ##Now that all the new columns have been added, the columns' positions must 
  ##be switched to match the order defined by the user.  
  for column in range(1, len(stimDict) + 1): ##Columns.
    if stimDict[column] != circleTableBoxes[0, column].cget("text"): ##Means the column is not in the right position.
      
      ##Therefore, find the position of the column that is supposed to be there by iteration.
      columnPos = column + 1
      while stimDict[column] != circleTableBoxes[0, columnPos].cget("text"):
        columnPos += 1
        
      ##Switch the labels of the two columns with a temporary variable.
      auxLabel = stimDict[column]
      
      circleTableBoxes[0, columnPos].config(text = circleTableBoxes[0, column].cget("text"))
      circleTableBoxes[0, column].config(text = auxLabel)
      
      lambdaTableBoxes[0, columnPos].config(text = lambdaTableBoxes[0, column].cget("text"))
      lambdaTableBoxes[0, column].config(text = auxLabel)      
      
      ##Switch the row entries across each column in each table by using
      ##a temporary variable..
      for row in range(1, numRows + 1):
        auxEntry = circleTableBoxes[row, columnPos].get()
        
        circleTableBoxes[row, columnPos].delete(0, END) 
        circleTableBoxes[row, columnPos].insert(0, circleTableBoxes[row, column].get())
        
        circleTableBoxes[row, column].delete(0, END) 
        circleTableBoxes[row, column].insert(0, auxEntry)    
        
        auxEntry = lambdaTableBoxes[row, columnPos].get()
        
        lambdaTableBoxes[row, columnPos].delete(0, END) 
        lambdaTableBoxes[row, columnPos].insert(0, lambdaTableBoxes[row, column].get())
        
        lambdaTableBoxes[row, column].delete(0, END) 
        lambdaTableBoxes[row, column].insert(0, auxEntry)                  