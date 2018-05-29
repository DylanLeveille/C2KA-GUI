from tkinter import*

def add_rows(numRows, numColumns, circleTableBoxes, lambdaTableBoxes, bevDict,
             circleGridFrame, lambdaGridFrame):
#create a list containing all the labels the tables currently have 
#in their rows
  listOfLabels = []
  for row in range(1, numRows + 1):
    listOfLabels.append(circleTableBoxes[row, 0].cget("text"))
    
  #compare current table labels to what bevDict has
  for i in range(len(bevDict)): #Columns
    label = bevDict[i + 1]
    if label not in listOfLabels: #means a behaviour was added
      #therefore, we will add a new row
      numRows += 1
      circleTableBoxes[0, 0] = numRows, numColumns #new number of columns
      #create label box for a new row
      circleTableBoxes[numRows, 0] = Label(circleGridFrame, text = label)
      
      lambdaTableBoxes[numRows, 0] = Label(lambdaGridFrame, text = label)   
      
      #create the entry boxes at the bottom of each table
      for column in range(1, numColumns + 1):
        circleTableBoxes[numRows, column] = Entry(circleGridFrame)
        
        lambdaTableBoxes[numRows, column] = Entry(lambdaGridFrame)      
      
  #Now that all the new rows have been added, the rows' positions must 
  #be switched to match the order defined by the user  
  for row in range(1, len(bevDict) + 1): #Rows
    #means the row is not in the right position
    if bevDict[row] != circleTableBoxes[row, 0].cget("text"):
      #find the position of the row that is supposed to be there
      rowPos = row + 1
      while bevDict[row] != circleTableBoxes[rowPos, 0].cget("text"):
        rowPos += 1
        
      #switch the labels of the rows
      auxLabel = bevDict[row]
      
      circleTableBoxes[rowPos, 0].config(text = circleTableBoxes[row, 0].cget("text"))
      circleTableBoxes[row, 0].config(text = auxLabel)
      
      lambdaTableBoxes[rowPos, 0].config(text = lambdaTableBoxes[row, 0].cget("text"))
      lambdaTableBoxes[row, 0].config(text = auxLabel)      
      
      #switch the column entries
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
