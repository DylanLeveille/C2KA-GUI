from tkinter import*
from rows_to_delete import*
from columns_to_delete import*
from add_rows import*
from add_columns import*

def fix_grids(bevDict, stimDict, circleTableBoxes, lambdaTableBoxes, 
              circleGridFrame, lambdaGridFrame):
  #extract Table lenght and width (will be the same for both tables)
  numRows, numColumns = circleTableBoxes[0, 0]
  
  #keep track of rows to delete
  numTurns = 1 #turns to keep track in recursion
  delRows = 0
  delRows = rows_to_delete(numRows, numColumns, circleTableBoxes, 
                           lambdaTableBoxes, bevDict, numTurns, delRows)
  
  #keep track of columns to delete
  numTurns = 1 #turns to keep track in recursion
  delColumns = 0
  delColumns = columns_to_delete(numRows, numColumns, circleTableBoxes, 
                              lambdaTableBoxes, stimDict, numTurns, delColumns)  
  #save the tables' new size
  circleTableBoxes[0, 0] = numRows - delRows, numColumns - delColumns
  
  #delete the rows and columns
  while delRows > 0:
    for i in range(numColumns + 1):
      #start deleting from circleTable
      itemToDelete = circleTableBoxes[(numRows - delRows + 1, i)]
      del circleTableBoxes[(numRows - delRows + 1, i)] 
      itemToDelete.destroy()
      
      #then delete from lambdaTable
      itemToDelete = lambdaTableBoxes[(numRows - delRows + 1, i)]
      del lambdaTableBoxes[(numRows - delRows + 1, i)] 
      itemToDelete.destroy()       
    delRows -= 1
  
  while delColumns > 0:
    for i in range(numRows + 1):
      #start deleting from circleTable
      itemToDelete = circleTableBoxes[(i, numColumns - delColumns + 1)]
      del circleTableBoxes[(i, numColumns - delColumns + 1)]
      itemToDelete.destroy()
        
      #then delete from lambdaTable
      itemToDelete = lambdaTableBoxes[(i, numColumns - delColumns + 1)]
      del lambdaTableBoxes[(i, numColumns - delColumns + 1)] 
      itemToDelete.destroy()       
    delColumns -= 1  
    
  #save the new table size in local variables
  numRows, numColumns = circleTableBoxes[0, 0]
  
  #add new rows if behaviours were added
  add_rows(numRows, numColumns, circleTableBoxes, 
                 lambdaTableBoxes, bevDict, circleGridFrame, lambdaGridFrame) 
  
  #add new columns if stimuli were added
  add_columns(numRows, numColumns, circleTableBoxes, lambdaTableBoxes, 
              stimDict, circleGridFrame, lambdaGridFrame)