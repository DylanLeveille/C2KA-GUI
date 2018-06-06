from tkinter import*
from delete_CBS import *
from add_CBS import*

#function called when no CBS were yet generated
def create_CBS_entries(bevDict, frameCBS):
    #create an empty dictionary to hold entries on concrete behaviours page
    entriesCBS = {}
    
    #iterate across the behaviour dictionary to create concrete behaviours
    #in the frameCBS
    for i in range(1, len(bevDict) + 1):
        #create label/entry
        labelCBS = Label(frameCBS, text = bevDict[i])
        entryCBS = Entry(frameCBS)
        #pack label/entry
        labelCBS.pack(anchor = W)
        entryCBS.pack(anchor = W)
        
        #assign label/entry to dictionary
        entriesCBS[i, 0] = labelCBS
        entriesCBS[i, 1] = entryCBS
    
    #return data structure
    return entriesCBS

#called to see if any modifications are necessary to the CBS data
def fix_CBS(bevDict, frameCBS, entriesCBS):
    #extract current number of rows in CBS
    numRows = entriesCBS['numRows']
    
    #keep track of the current row for recursion in delete_CBS
    currRow = 1
    
    #number of rows to delete
    delRows = 0
    
    #check to see how many rows need to be deleted
    delRows = delete_CBS(bevDict, currRow, numRows, entriesCBS, delRows)
    
    #save new number of rows in the dictionary
    entriesCBS['numRows'] = numRows - delRows    
    
    while delRows > 0:
        #get rid of label
        entriesCBS[numRows - delRows + 1, 0].destroy()
        
        #get rid of entry
        entriesCBS[numRows - delRows + 1, 1].destroy()        
        
        #remove the label/entry from the dictionary
        del entriesCBS[numRows - delRows + 1, 0]
        del entriesCBS[numRows - delRows + 1, 1]
        
        #decrease number of rows to delete by 1
        delRows -= 1
    
    #save new number of rows
    numRows = entriesCBS['numRows']
    
    #check to see how many rows need to be added
    add_CBS(bevDict, numRows, entriesCBS, frameCBS)
    
    #return data scructure of new CBS entries/labels
    return entriesCBS

def recreate_CBS_entries(bevDict, entriesCBS, frameCBS):
    #itearte through the rows to re-generate them
    for row in range(1, len(bevDict) + 1):
        
        #create CBS label
        labelCBS = Label(frameCBS, text = bevDict[row])
        
        #create CBS entry
        entryCBS = Entry(frameCBS)
        entryCBS.insert(0, entriesCBS[row, 1].get())
        
        #pack new label/entry
        labelCBS.pack(anchor = W)
        entryCBS.pack(anchor = W)
        
        #save label/entry in the data structure
        entriesCBS[row, 0] = labelCBS
        entriesCBS[row, 1] = entryCBS
    
    #return updated data structure    
    return entriesCBS