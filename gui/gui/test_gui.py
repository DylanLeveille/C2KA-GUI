from tkinter import *
main = Tk()
main.geometry("500x500")

#Note: some global variables will be used due to the functions 
#being unable to conatain parameters. 

def new_entry():
  global stimNum #counter for the number of stimuli
  global stimList #list containing every entry box
  
  stim = Entry(main)
  stim.pack(side = TOP)
  stimNum += 1
  stimList.append(stim)
  
def remove_entry():
  global stimNum #counter for the number of stimuli
  global stimList #list containing every entry box
  
  entryToDelete = stimList[len(stimList) - 1]

  del stimList[len(stimList) - 1]
  
  entryToDelete.destroy()

def create_dict():
  global stimDict #dictionary to hold final entries of entered stimuli
  stimDict = {} #set dictionary empty every time create_dict() is called
  
  for i in range(len(stimList)):
    stimDict[i+1] = stimList[i].get()

def test():
  print(stimDict)

#Title related code 
stimTitle = Label(main, text='Please Enter The Stimuli')
stimTitle.pack(side = TOP)

#Initializing variables/data structures
stimNum = 1
stimList = []

#Add stimulus Button
addStim = Button(main, text = 'Add new stimulus', command = new_entry)
addStim.pack(side = BOTTOM)

#Next Button
nextButton = Button(main, text = 'Next', command = create_dict)
nextButton.pack(side = BOTTOM)

#Delete prev entry Button
delButton = Button(main, text = 'Delete Previous', command = remove_entry)
delButton.pack(side = BOTTOM)

#Test Button
#testButton = Button(main, text ='Test', command = test)
#testButton.grid(column = 100, row = 101)

main.mainloop()
