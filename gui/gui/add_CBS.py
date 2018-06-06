from tkinter import*

#function to add rows to the CBS page if necessary
def add_CBS(bevDict, numRows, entriesCBS, frameCBS):

    #Creating a list of the current labels in the CBS page
    listofLabels = []
    
    #appending the labels to the data scructure
    for row in range(1, numRows + 1):
        listofLabels.append(entriesCBS[row, 0].cget("text"))
        
    #check behaviour dictionary to see if new behaviour was added    
    for i in range(1, len(bevDict) + 1):
        currLabel = bevDict[i]
        
        #new behaviour added if True, =>create a new row with new behaviour
        if currLabel not in listofLabels:
            
            #add an extra row
            numRows += 1
            entriesCBS['numRows'] = numRows
            
            #assign new label to entries dictionary
            entriesCBS[numRows, 0] = Label(FrameCBS, text = currLabel)
            
            #assign new entry to entries dictionary
            entriesCBS[numRows, 1] = Entry(FrameCBS)
            
            #pack new label/entry
            entriesCBS[numRows, 0].pack(anchor = W)
            entriesCBS[numRows, 1].pack(anchor = W)
            
    #now that the new entries/labels are added to the dictionary, shuffle the 
    #rows to match the order defined by the user
    for row in range(1, len(bevDict) + 1):
        #means row is not at right position
        if bevDict[row] != entriesCBS[row, 0].cget("text"):
            #rowPos defines the correct position to move row
            rowPos = row + 1
            
            #iterate until the row's good position is found
            while bevDict[row] != entriesCBS[rowPos, 0].cget("text"):
                rowPos += 1 
            
            #switch the labels of the rows with a temporary variable
            auxLabel = bevDict[row]
            
            entriesCBS[rowPos, 0].config(text = entriesCBS[row, 0].cget("text"))
            entriesCBS[row, 0].config(text = auxLabel)
            
            #and switch the entries
            entriesCBS[rowPos, 1].delete(0, END)
            entriesCBS[rowPos, 1].insert(0, entriesCBS[row, 1].get())
            entriesCBS[row, 1].delete(0, END)