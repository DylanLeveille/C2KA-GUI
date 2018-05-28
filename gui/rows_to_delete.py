from tkinter import*

def rows_to_delete(numRows, numColumns, circleTableBoxes, 
                   lambdaTableBoxes, bevDict, numTurns, delRows):
  
  if numTurns > numRows: 
    return delRows
  
  elif circleTableBoxes[numTurns, 0].cget("text") not in bevDict.values(): 
    #rows to delete goes up by one
    delRows += 1
    #shuffle the data from row to row
    for j in range(numTurns, numRows):
      circleTableBoxes[j, 0].config(text = circleTableBoxes[j + 1, 0].cget("text"))
      lambdaTableBoxes[j, 0].config(text = lambdaTableBoxes[j + 1, 0].cget("text"))
      #go across the row (column by column) to update the values
      for k in range(1, numColumns + 1):
        circleTableBoxes[j, k].delete(0, END) 
        circleTableBoxes[j, k].insert(0, circleTableBoxes[j + 1, k].get()) 
        
        lambdaTableBoxes[j, k].delete(0, END) 
        lambdaTableBoxes[j, k].insert(0, lambdaTableBoxes[j + 1, k].get()) 
        
    #reduce the number of rows to search by one in next recursive call
    #and re-check at same row (=> keep same number of turns)
    return rows_to_delete(numRows - 1, numColumns, circleTableBoxes, 
                         lambdaTableBoxes, bevDict, numTurns, delRows)    
  
  #if the above conditions aren't met, search next row
  return rows_to_delete(numRows, numColumns, circleTableBoxes, 
                       lambdaTableBoxes, bevDict, numTurns + 1, delRows)  