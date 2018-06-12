"""Imported modules."""
from tkinter import * ##Import the tkinter module to allow construction of the GUI interface.
from rows_to_delete import * ##Module to count number of rows to remove from the table.
from columns_to_delete import * ##Module to count number of columns to remove from the table.
from add_rows import * ##Module to add and shuffle the rows in the table.
from add_columns import * ##Module to add and shuffle the columns in the table.

"""Function that takes care in modifying the table."""
def fix_grids(bevDict, stimDict, circleTableBoxes, lambdaTableBoxes, 
              circleGridFrame, lambdaGridFrame):
  """ (dict, dict, dict, dict, tkinter.Frame, tkinter.Frame) -> (none)
    
    Updates the table data and the table itself by checking
    the rows and columns that must be removed and/or
    added.
  
  """    
  ##Extract Table lenght and width (will be the same for both tables).
  numRows, numColumns = circleTableBoxes[0, 0]
  
  ##Keep track of rows to delete.
  numTurns = 1 ##Turns to keep track in recursion.
  delRows = 0
  delRows = rows_to_delete(numRows, numColumns, circleTableBoxes, 
                           lambdaTableBoxes, bevDict, numTurns, delRows)
  
  ##Keep track of columns to delete.
  numTurns = 1 ##Turns to keep track in recursion.
  delColumns = 0
  delColumns = columns_to_delete(numRows, numColumns, circleTableBoxes, 
                              lambdaTableBoxes, stimDict, numTurns, delColumns)  
  
  ##Save the tables' new size.
  circleTableBoxes[0, 0] = numRows - delRows, numColumns - delColumns
  
  ##Since numRows may have changed, we will save the new number of rows in a
  ##copy variable to itearte through when deleting the columns.
  currNumRows = numRows - delRows
  
  ##Delete the rows and columns
  while delRows > 0:
    for i in range(numColumns + 1):
      ##Start deleting from circleTable.
      del circleTableBoxes[(numRows - delRows + 1, i)] 
      
      ##Then delete from lambdaTable.
      del lambdaTableBoxes[(numRows - delRows + 1, i)]       
    delRows -= 1
  
  while delColumns > 0:
    for i in range(currNumRows + 1):
      ##Start deleting from circleTable.
      del circleTableBoxes[(i, numColumns - delColumns + 1)]
        
      ##Then delete from lambdaTable.
      del lambdaTableBoxes[(i, numColumns - delColumns + 1)]     
    delColumns -= 1      
    
  ##Save the new table size in local variables.
  numRows, numColumns = circleTableBoxes[0, 0]
  
  ##Add new rows if behaviours were added.
  add_rows(numRows, numColumns, circleTableBoxes, 
                 lambdaTableBoxes, bevDict, circleGridFrame, lambdaGridFrame)
  
  ##If rows were added, the new size must be saved in local variables to be used
  ##when calling the add_columns() function.
  numRows, numColumns = circleTableBoxes[0, 0]      
  
  ##Add new columns if stimuli were added.
  add_columns(numRows, numColumns, circleTableBoxes, lambdaTableBoxes, 
              stimDict, circleGridFrame, lambdaGridFrame)