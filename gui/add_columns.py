from tkinter import*

def add_columns(numRows, numColumns, circleTableBoxes, lambdaTableBoxes, stimDict,
             circleGridFrame, lambdaGridFrame):
  #create a list containing all the labels the tables currently have 
  #in their columns
  listOfLabels = []
  for column in range(1, numColumns + 1):
    listOfLabels.append(circleTableBoxes[0, column].cget("text"))
    
  #compare current table labels to what stimDict has
  for i in range(len(stimDict)): #Columns
    label = stimDict[i + 1]
    if label not in listOfLabels: #means a stimuli was added
      #therefore, we will add a new column
      numColumns += 1
      circleTableBoxes[0, 0] = numRows, numColumns #new number of columns
      #create label box for a new column
      circleTableBoxes[0, numColumns] = Label(circleGridFrame, text = label)
      circleTableBoxes[0, numColumns].grid(row = 0, column = numColumns)
      
      lambdaTableBoxes[0, numColumns] = Label(lambdaGridFrame, text = label)
      lambdaTableBoxes[0, numColumns].grid(row = 0, column = numColumns)     
      
      #create the entry boxes at the right side of each table
      for row in range(1, numRows + 1):
        circleTableBoxes[row, numColumns] = Entry(circleGridFrame)
        circleTableBoxes[row, numColumns].grid(row = row, column = numColumns)
        
        lambdaTableBoxes[row, numColumns] = Entry(lambdaGridFrame)
        lambdaTableBoxes[row, numColumns].grid(row = row, column = numColumns)        
      
  #Now that all the new columns have been added, the columns' positions must 
  #be switched to match the order defined by the user  
  for column in range(1, len(stimDict) + 1): #Columns
    #means the column is not in the right position
    if stimDict[column] != circleTableBoxes[0, column].cget("text"):
      #find the position of the column that is supposed to be there
      columnPos = column + 1
      while stimDict[column] != circleTableBoxes[0, columnPos].cget("text"):
        columnPos += 1
        
      #switch the labels of the columns
      auxLabel = stimDict[column]
      
      circleTableBoxes[0, columnPos].config(text = circleTableBoxes[0, column].cget("text"))
      circleTableBoxes[0, column].config(text = auxLabel)
      
      lambdaTableBoxes[0, columnPos].config(text = lambdaTableBoxes[0, column].cget("text"))
      lambdaTableBoxes[0, column].config(text = auxLabel)      
      
      #switch the row entries
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