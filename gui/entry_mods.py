from tkinter import*
import vertSuperscroll 

#Function to add new stimuli 
def add_stim(main, stimList): 

 stimScrollingArea = vertSuperscroll.Scrolling_Area(main)
 stimScrollingArea.pack(expand = 1, fill=BOTH)
 
 stimTitle = Label(stimScrollingArea.innerframe, text='Please Enter The Stimuli')
 stimTitle.pack(side = TOP)        
     
 for i in range(len(stimList)):
  stimEntry = Entry(stimScrollingArea.innerframe)
  stimEntry.insert(0, stimList[i].get())    
  stimList[i] = stimEntry
  stimEntry.pack(side = TOP, pady=10)
 
 stimEntry = Entry(stimScrollingArea.innerframe)    
 stimEntry.pack(side = TOP, pady=10)     
 
 stimList.append(stimEntry)
 
 return stimScrollingArea
    
#Function to remove stimuli 
def remove_stim(main, stimList):
  entryToDelete = stimList[len(stimList) - 1]
  del stimList[len(stimList) - 1] 
  entryToDelete.destroy()
 
  stimScrollingArea = vertSuperscroll.Scrolling_Area(main)
  stimScrollingArea.pack(expand = 1, fill=BOTH)   
  
  stimTitle = Label(stimScrollingArea.innerframe, text='Please Enter The Stimuli')
  stimTitle.pack(side = TOP)    
  
  for i in range(len(stimList)):   
   stimEntry = Entry(stimScrollingArea.innerframe)
   stimEntry.insert(0, stimList[i].get())
   stimList[i] = stimEntry
   stimEntry.pack(side = TOP)    
   
  return stimScrollingArea 
 
#button function to fill lambda table with neutral stimulus
def fill_n(bevDict, stimDict, circleTableBoxes, lambdaTableBoxes):
 for i in range(1, len(bevDict) + 1): #Rows
   for j in range(1, len(stimDict) + 1): #Columns
     #checking if empty in lambda table
     if lambdaTableBoxes[i, j].get() == ' ' * len(lambdaTableBoxes[i, j].get()):
       #if empty, put neutral stimulus
       lambdaTableBoxes[i, j].delete(0, END) 
       lambdaTableBoxes[i, j].insert(0, 'N')