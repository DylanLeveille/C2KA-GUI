from tkinter import*

#function to delete behaviours from the CBS page
def delete_CBS(bevDict, currRow, numRows, entriesCBS, delRows):
    #if the current passed the total number of rows, return
    if currRow > numRows:     
        return delRows
    
    #check to see if we still have the label in the dictionary's values
    elif entriesCBS[currRow, 0].cget("text") not in bevDict.values():
        #means there is a row to delete
        delRows += 1
        
        #shuffle entries/labels across the page
        for i in range(currRow, numRows):
            entriesCBS[i, 0].config(text = entriesCBS[i + 1, 0].cget("text"))
            entriesCBS[i, 1].delete(0, END)
            entriesCBS[i, 1].insert(0, entriesCBS[i + 1, 1].get())
        
        #search again from current row    
        return delete_CBS(bevDict, currRow, numRows - 1, entriesCBS, delRows)
   
    #if current row is good, search next row
    return delete_CBS(bevDict, currRow + 1, numRows, entriesCBS, delRows)