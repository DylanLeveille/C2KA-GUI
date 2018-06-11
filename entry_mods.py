from tkinter import*
import vertSuperscroll 

#Function to add new stimuli 
def add_stim(main, stimList, stimScrollingArea):
 #make a new frame capable of scrolling to the new entry box
 stimScrollingAreaTemp = vertSuperscroll.Scrolling_Area(main)
 stimScrollingAreaTemp.pack(expand = 1, fill=BOTH)
 
 stimTitle = Label(stimScrollingAreaTemp.innerframe, text='Please Enter The Stimuli')
 stimTitle.pack(side = TOP) 
     
 for i in range(len(stimList)):
  stimEntry = Entry(stimScrollingAreaTemp.innerframe)
  stimEntry.insert(0, stimList[i].get())    
  stimList[i] = stimEntry
  stimEntry.pack(side = TOP, pady=10)
 
 stimEntry = Entry(stimScrollingAreaTemp.innerframe)    
 stimEntry.pack(side = TOP, pady=10)     
 
 #destroy old frame
 stimScrollingArea[0].destroy()
 
 #assign new frame
 stimScrollingArea[0] = stimScrollingAreaTemp
 
 #add new entryto the list
 stimList.append(stimEntry)
    
#Function to remove stimuli 
def remove_stim(main, stimList, stimScrollingArea):
 #we need at least one entry to be able to remove a stimulus
 if len(stimList) > 0:
  #make a new frame capable of scrolling to the new entry box
  stimScrollingAreaTemp = vertSuperscroll.Scrolling_Area(main)
  stimScrollingAreaTemp.pack(expand = 1, fill=BOTH)
  
  stimTitle = Label(stimScrollingAreaTemp.innerframe, text='Please Enter The Stimuli')
  stimTitle.pack(side = TOP) 
      
  for i in range(len(stimList) - 1):
   stimEntry = Entry(stimScrollingAreaTemp.innerframe)
   stimEntry.insert(0, stimList[i].get())    
   stimList[i] = stimEntry
   stimEntry.pack(side = TOP, pady=10)
  
  #remove last entry in list 
  stimList[len(stimList) - 1].destroy()
  del stimList[len(stimList) - 1]
  
  #destroy old frame
  stimScrollingArea[0].destroy()
  
  #assign new frame
  stimScrollingArea[0] = stimScrollingAreaTemp 
 
 
#button function to fill lambda table with neutral stimulus
def fill_n(bevDict, stimDict, circleTableBoxes, lambdaTableBoxes):
 for i in range(1, len(bevDict) + 1): #Rows
   for j in range(1, len(stimDict) + 1): #Columns
     #checking if empty in lambda table
     if lambdaTableBoxes[i, j].get() == ' ' * len(lambdaTableBoxes[i, j].get()):
       #if empty, put neutral stimulus
       lambdaTableBoxes[i, j].delete(0, END) 
       lambdaTableBoxes[i, j].insert(0, 'N')