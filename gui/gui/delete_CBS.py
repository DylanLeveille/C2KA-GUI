from tkinter import*

def delete_CBS(rowNum, currRow, count, bevDict, Entries, Labels):

    if currRow >rowNum:
        
        return count

    elif Labels[currRow].cget("text") not in bevDict.values():
        count+=1
        for i in range(currRow , rowNum):
            Labels[i].config(text = Labels[i+1].cget("text"))
            Entries[i].delete(0, END)
            Entries[i].insert(0, Entries[i+1].get())
            
        return delete_CBS(rowNum-1, currRow, count, bevDict, Entries, Labels)
    return delete_CBS(rowNum, currRow+1, count, bevDict, Entries, Labels)