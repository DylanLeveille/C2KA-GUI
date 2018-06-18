"""Imported modules."""
from tkinter import * ##Import the tkinter module to allow construction of the GUI interface.

"""Function to count the number of rows to delete from table."""
def rows_to_delete(numRows, numColumns, circleTableBoxes, 
                   lambdaTableBoxes, bevDict, numTurns, delRows):
  """ (int, int, dict, dict, dict, int, int) -> (int)
    
    Calculates the number of rows to delete from the
    tables. 
  
  """      
  if numTurns > numRows: ##When current turn is above the total number of rows, then return.
    return delRows
  
  elif circleTableBoxes[numTurns, 0].cget("text") not in bevDict.values(): 
    ##Rows to delete goes up by one.
    delRows += 1
    
    ##Shuffle the data from row to row.
    for j in range(numTurns, numRows):
      circleTableBoxes[j, 0].config(text = circleTableBoxes[j + 1, 0].cget("text"))
      lambdaTableBoxes[j, 0].config(text = lambdaTableBoxes[j + 1, 0].cget("text"))
      
      ##Go across the row (column by column) to update the values.
      for k in range(1, numColumns + 1):
        circleTableBoxes[j, k].delete(0, END) 
        circleTableBoxes[j, k].insert(0, circleTableBoxes[j + 1, k].get()) 
        
        lambdaTableBoxes[j, k].delete(0, END) 
        lambdaTableBoxes[j, k].insert(0, lambdaTableBoxes[j + 1, k].get()) 
        
    ##Reduce the number of rows to search by one in next recursive call
    ##and re-check at same row (=> keep same number of turns).
    return rows_to_delete(numRows - 1, numColumns, circleTableBoxes, 
                         lambdaTableBoxes, bevDict, numTurns, delRows)    
  
  ##If the above conditions aren't met, search next row.
  return rows_to_delete(numRows, numColumns, circleTableBoxes, 
                       lambdaTableBoxes, bevDict, numTurns + 1, delRows)  