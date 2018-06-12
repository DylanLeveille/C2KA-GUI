"""Imported modules."""
from tkinter import * ##Import the tkinter module to allow construction of the GUI interface.

"""Function to count the number of columns to delete from table."""
def columns_to_delete(numRows, numColumns, circleTableBoxes, 
                   lambdaTableBoxes, stimDict, numTurns, delColumns):
  """ (int, int, dict, dict, dict, int, int) -> (int)
    
    Calculates the number of columns to delete from the
    tables. 
  
  """      
  if numTurns > numColumns: ##When current turn is above the total number of columns, then return.
    return delColumns
  
  elif circleTableBoxes[0, numTurns].cget("text") not in stimDict.values(): 
    ##Columns to delete goes up by one.
    delColumns += 1
    
    ##Shuffle the data from column to column.
    for j in range(numTurns, numColumns):
      circleTableBoxes[0, j].config(text = circleTableBoxes[0, j + 1].cget("text"))
      lambdaTableBoxes[0, j].config(text = lambdaTableBoxes[0, j + 1].cget("text"))
      
      ##Go across the column (row by row) to update the values.
      for k in range(1, numRows + 1):
        circleTableBoxes[k, j].delete(0, END) 
        circleTableBoxes[k, j].insert(0, circleTableBoxes[k, j + 1].get()) 
        
        lambdaTableBoxes[k, j].delete(0, END) 
        lambdaTableBoxes[k, j].insert(0, lambdaTableBoxes[k, j + 1].get())  
        
    ##Reduce the number of columns to search by one in next recursive call
    ##and re-check at same column (=> keep same number of turns)
    return columns_to_delete(numRows, numColumns - 1, circleTableBoxes, 
                         lambdaTableBoxes, stimDict, numTurns, delColumns) 
  
  ##If the above conditions aren't met, search next column.
  return columns_to_delete(numRows, numColumns, circleTableBoxes, 
                       lambdaTableBoxes, stimDict, numTurns + 1, delColumns)  