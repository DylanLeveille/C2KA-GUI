from tkinter import*
import vertSuperscroll 

#function to extract the number of stims in the entry box
def get_num_stims(numStims):
 #test to see if more than one word in the entry box
 if len(numStims.split()) > 1:
   #call a function to pop up
   print('please try again')
    
 #test to see if it is a number only
 elif numStims.replace(' ', '').isdigit() != True:
   #call a function to pop up
   print('please try again')   
   
 else:
   print('yay, you win!')
   return int(numStims.replace(' ', ''))

#function to create specified number of stimuli entry boxes
def delete_all_stim(main, stimList, numStims):
 print('Hello, world!')

#Function to add new stimuli 
def add_stim(main, stimList, entryWords):
 #make a new frame capable of scrolling to the new entry box
 stimScrollingArea = vertSuperscroll.Scrolling_Area(main)
 stimScrollingArea.pack(expand = 1, fill=BOTH)
 
 stimTitle = Label(stimScrollingArea.innerframe, text='Please Enter The Stimuli')
 stimTitle.pack(side = TOP) 
     
 for i in range(len(entryWords)):
  stimEntry = Entry(stimScrollingArea.innerframe)
  stimEntry.insert(0, entryWords[i])    
  stimList[i] = stimEntry
  stimEntry.pack(side = TOP, pady=10)
 
 stimEntry = Entry(stimScrollingArea.innerframe)    
 stimEntry.pack(side = TOP, pady=10)     
 
 stimList.append(stimEntry)
 
 return stimScrollingArea
    
#Function to remove stimuli 
def remove_stim(main, stimList, entryWords):
 #make a new frame capable of scrolling to the new entry box
 stimScrollingArea = vertSuperscroll.Scrolling_Area(main)
 stimScrollingArea.pack(expand = 1, fill=BOTH)
 
 stimTitle = Label(stimScrollingArea.innerframe, text='Please Enter The Stimuli')
 stimTitle.pack(side = TOP) 
     
 for i in range(len(entryWords)):
  stimEntry = Entry(stimScrollingArea.innerframe)
  stimEntry.insert(0, entryWords[i])    
  stimList[i] = stimEntry
  stimEntry.pack(side = TOP, pady=10) 
 
 stimList[len(stimList) - 1].destroy()
 del stimList[len(stimList) - 1]
 
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