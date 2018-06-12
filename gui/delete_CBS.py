"""Imported modules."""
from tkinter import * ##Import the tkinter module to allow construction of the GUI interface.

"""function to delete behaviours from the CBS page."""
def delete_CBS(bevDict, entriesCBS, currRow, numRows, delRows):
  """ (dict, dict, int, int, int) -> (int)
    
    Calculates the number of rows to delete from the
    concrete behaviours. 
  
  """   
  ##If the current passed the total number of rows, return.  
  if currRow > numRows:   
      return delRows
  
  ##Check to see if we still have the label in the dictionary's values.
  elif entriesCBS[currRow, 0].cget("text") not in bevDict.values():
      ##Means there is a row to delete.
      delRows += 1
      
      ##Suffle entries/labels across the page.
      for i in range(currRow, numRows):
          entriesCBS[i, 0].config(text = entriesCBS[i + 1, 0].cget("text"))
          entriesCBS[i, 1].delete(0, END)
          entriesCBS[i, 1].insert(0, entriesCBS[i + 1, 1].get())
      
      ##Search again from current row.    
      return delete_CBS(bevDict, entriesCBS, currRow, numRows - 1, delRows)
 
  ##If current row is good, search next row.
  return delete_CBS(bevDict, entriesCBS, currRow + 1, numRows, delRows)