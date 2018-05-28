from tkinter import*

def columns_to_delete(numRows, numColumns, circleTableBoxes, 
                   lambdaTableBoxes, stimDict, numTurns, delColumns):
  
  if numTurns > numColumns: 
    return delColumns
  
  elif circleTableBoxes[0, numTurns].cget("text") not in stimDict.values(): 
    #columns to delete goes up by one
    delColumns += 1
    #shuffle the data from column to column
    for j in range(numTurns, numColumns):
      circleTableBoxes[0, j].config(text = circleTableBoxes[0, j + 1].cget("text"))
      lambdaTableBoxes[0, j].config(text = lambdaTableBoxes[0, j + 1].cget("text"))
      #go across the column (row by row) to update the values
      for k in range(1, numRows + 1):
        circleTableBoxes[k, j].delete(0, END) 
        circleTableBoxes[k, j].insert(0, circleTableBoxes[k, j + 1].get()) 
        
        lambdaTableBoxes[k, j].delete(0, END) 
        lambdaTableBoxes[k, j].insert(0, lambdaTableBoxes[k, j + 1].get())  
        
    #reduce the number of columns to search by one in next recursive call
    #and re-check at same column (=> keep same number of turns)
    return columns_to_delete(numRows, numColumns - 1, circleTableBoxes, 
                         lambdaTableBoxes, stimDict, numTurns, delColumns) 
  
  #if the above conditions aren't met, search next column
  return columns_to_delete(numRows, numColumns, circleTableBoxes, 
                       lambdaTableBoxes, stimDict, numTurns + 1, delColumns)  