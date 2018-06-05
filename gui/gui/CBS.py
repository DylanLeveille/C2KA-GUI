from tkinter import*
from delete_CBS import *
from add_CBS import*


def create_CBS_entries(bevDict, FrameCBS, rowNum):
    Entries = {}
    Labels = {}
    for i in range(1, len(bevDict)+1):
        LabelCBS = Label(FrameCBS, text = bevDict[i])
        EntryCBS = Entry(FrameCBS)
        LabelCBS.pack(anchor = W)
        EntryCBS.pack(anchor = W)
        Labels[i] = LabelCBS
        Entries[i] = EntryCBS
        rowNum+=1

    return Entries, Labels, rowNum

def fix_CBS(bevDict, Entries, Labels, FrameCBS, rowNum):
    currRow = 1
    count = 0
    count = delete_CBS(rowNum, currRow, count, bevDict, Entries, Labels)
    newRowNum = rowNum - count
    while count>0:
        
        del Labels[rowNum - count+1]
        del Entries[rowNum - count+1]
        count-=1
    
    
    rowNum = add_CBS(newRowNum, currRow, count, bevDict, Entries, Labels, FrameCBS)
    return rowNum, Entries, Labels
    

    
        

