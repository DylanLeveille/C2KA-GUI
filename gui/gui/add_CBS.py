from tkinter import*

def add_CBS(rowNum, currRow, count, bevDict, Entries, Labels, FrameCBS):

    #Creating a list of the current Labels 
    listofLabels = []

    
    for row in range(1, rowNum+1):
        listofLabels.append(Labels[row].cget("text"))
    #Check behaviour dictionary to see if new behaviour was added    
    for j in range(1, len(bevDict)+1):
        currLabel = bevDict[j]
        #New behaviour added, create a new row with new behaviour
        if currLabel not in listofLabels:
            
            rowNum+=1
            
            Labels[rowNum] = Label(FrameCBS, text = currLabel)
            Entries[rowNum] = Entry(FrameCBS)
            Labels[rowNum].pack(anchor =W)
            Entries[rowNum].pack(anchor =W)

    for row in range(1, len(bevDict)+1):
        if bevDict[row] != Labels[row].cget("text"):
            rowPos = row + 1
            while bevDict[row] != Labels[rowPos].cget("text"):
                rowPos += 1 
            
            tempLabel = bevDict[row]
            
            Labels[rowPos].config(text = Labels[row].cget("text"))
            Labels[row].config(text = tempLabel)
            
            Entries[rowPos].delete(0, END)
            Entries[rowPos].insert(0, Entries[row].get())
            Entries[row].delete(0, END)
    return rowNum


            
    