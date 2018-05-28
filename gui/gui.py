from tkinter import*
from get_word_list import*
from fix_grids import*
from create_text import*
from superscroll import*
from check_if_good import*

main = Tk()
main.title("C2KA GUI")

windowSize = 500

screenWidth = main.winfo_screenwidth() 
screenHeight = main.winfo_screenheight()

positionRight = screenWidth/2 - windowSize/2
positionDown = screenHeight/2 - windowSize/2

main.geometry('%dx%d+%d+%d' % (windowSize, windowSize, positionRight, 
                               positionDown))

#Note: some global variables will be used due to the button functions
#being unable to contain parameters.

#function to return to the stimuli entry page after the pop-up 
def return_to_stims():
 main.update()
 main.deiconify()
 noStims.destroy() 
 
 #regenerate the stim boxes that were un-packed
 for i in range(len(stimList)):   
  stimList[i].pack(side = TOP) 
 
#function to return to the behaviour entry page after the pop-up 
def return_to_bevs():
 main.update()
 main.deiconify()
 noBevs.destroy() 

#function to return to the tables after the pop-up 
def return_to_tables():
 main.update()
 main.deiconify()
 invalidEntryPop.destroy()

#Function to add new stimuli (page 1 exclusive)
def new_entry(): 
 global stimList #list containing every entry box
 global stimScrollingArea #area for the scrolling/stimuli
 
 #the scrolling area must be reset every time
 stimScrollingArea.pack_forget()

 stimScrollingArea = Scrolling_Area(main)
 stimScrollingArea.pack(expand = 1, fill=BOTH)
 
 stimTitle = Label(stimScrollingArea.innerframe, text='Please Enter The Stimuli')
 stimTitle.pack(side = TOP)        
     
 for i in range(len(stimList)):
  stimEntry = Entry(stimScrollingArea.innerframe)
  stimEntry.insert(0, stimList[i].get())    
  stimList[i] = stimEntry
  stimEntry.pack(side = TOP)
 
 stimEntry = Entry(stimScrollingArea.innerframe)        
 stimEntry.pack(side = TOP)     
 #stimScrollingArea.innerframe.yview_moveto( 1 )
 #stimEntry.configure(yscrollcommand = stimScrollingArea.set)
 
 stimList.append(stimEntry)
    
#Function to remove stimuli (page 1 exclusive) 
def remove_entry():
 global stimScrollingArea #area for the scrolling/stimuli
 if len(stimList) > 0: #must be greater than 0 to be able to remove a stimulus
   entryToDelete = stimList[len(stimList) - 1]
   del stimList[len(stimList) - 1] 
   entryToDelete.destroy()
   
   #the scrolling area must be reset every time
   stimScrollingArea.pack_forget()
  
   stimScrollingArea = Scrolling_Area(main)
   stimScrollingArea.pack(expand = 1, fill=BOTH)   
   
   stimTitle = Label(stimScrollingArea.innerframe, text='Please Enter The Stimuli')
   stimTitle.pack(side = TOP)    
   
   for i in range(len(stimList)):   
    stimEntry = Entry(stimScrollingArea.innerframe)
    stimEntry.insert(0, stimList[i].get())
    stimList[i] = stimEntry
    stimEntry.pack(side = TOP)    
   
#Function to go to next page
def next_page():
  global pageNum #keep track of page number
  
  global stimDict #dictionary to hold final entries of entered stimuli
  global bevDict #dictionary to hold agent behaviours
  
  global agentName #Record Entries for name and behaviour of agent
  global agentBehaviour 
  
  global circleTableBoxes #dict to hold entry boxes and labels of circle table
  global lambdaTableBoxes #dict to hold entry boxes and labels of lambda table 
  
  global circleTableValues #dict to hold values from circle table
  global lambdaTableValues #dict to hold values from lambda table   
  
  global circleScrollingArea #scrolling area for circle table
  global lambdaScrollingArea #scrolling area for circle table
  
  global circleGridFrame #global frame for the circle table
  global lambdaGridFrame #global frame for the circle table
  
  global generated #bool variable to check if tables were generated
  
  global noStims #pop-up window for no stims inputted
  global invalidEntryPop #pop-up window for invalid table entries
  
  global LabelCBS
  
  #Note: dictionaries are set empty when swithing to a next page
  #(depending on pageNum) in order to update the data
  
  #PAGE 1 to PAGE 2
  if pageNum == 1:
    stimDict = {} #stimuli dictionary
    index = 0 #necessary for good indices in the dictionary
    
    for i in range(len(stimList)):
     #we don't want the empty string
     if stimList[i].get() != '': 
      stimDict[index + 1] = stimList[i].get()
      index +=  1
      
     stimList[i].pack_forget() 
    
    if len(stimDict) == 0: #user must imput at least one stimulus
     pageNum -= 1
     #generate pop-up to prompt user to enter at least one stimulus   
     noStims = Toplevel()
     
     windowSize = 300
     
     screenWidth = noStims.winfo_screenwidth() 
     screenHeight = noStims.winfo_screenheight()
     
     positionRight = screenWidth/2 - windowSize/2
     positionDown = screenHeight/2 - windowSize/2
     
     noStims.geometry('%dx%d+%d+%d' % (windowSize, windowSize, 
                                       positionRight, positionDown)) 
     
     noStims.resizable(width = False, height = False) 
 
     noStims.wm_title("No stimuli")
     noStims.overrideredirect(1)
     
     Label(noStims, text = 'Please enter at least one stimuli').pack(side = TOP)
     
     pressToClose = Button(noStims, text = "Return", 
                           command = return_to_stims)
     pressToClose.pack(side = BOTTOM)
     
     main.withdraw()     
     
    else:
     #set new page 
     stimScrollingArea.pack_forget()
     addStim.pack_forget()
     delButton.pack_forget()
     prevButton.pack(side = BOTTOM, fill = X)
     agentLabel.pack(side = TOP, anchor = W)
     agentEntry.pack(side = TOP, anchor = W)
     agentBevLabel.pack(side = TOP, anchor = W)
     agentBevEntry.pack(side = TOP, anchor = W)   
  
  #PAGE 2 to PAGE 3
  if pageNum ==2:
   #set new page
   agentLabel.pack_forget()
   agentEntry.pack_forget()
   agentBevLabel.pack_forget()
   agentBevEntry.pack_forget()
   LabelCBS = Label(main, text = agentEntry.get())
   TitleCBS.pack(side = TOP)
   LabelCBS.pack(side = TOP, anchor = W)
   TextCBS.pack(side = TOP, fill = X)
   agentName = agentEntry.get()
   agentBehaviour = agentBevEntry.get()   
  
  #PAGE 3 to PAGE 4
  if pageNum == 3:
   bevDict = {} #behaviour dictionary
   bevList = build_histogram(agentBevEntry.get()) #behaviour words
   for i in range(len(bevList)):
     bevDict[i + 1] = bevList[i]
     
   #set new page 
   TitleCBS.pack_forget()
   LabelCBS.pack_forget()
   TextCBS.pack_forget()
   
   if generated == False:
    #Frame for the tables and corner label
    circleScrollingArea = Scrolling_Area(main, width=1, height=1)
    circleScrollingArea.pack(expand=1, fill = BOTH)   
    
    circleGridFrame = Frame(circleScrollingArea.innerframe) 
    circleTableLabel = Label(circleGridFrame, text = 'o')   
    circleTableLabel.grid(row = 0, column = 0)
    
    lambdaScrollingArea = Scrolling_Area(main, width=1, height=1)
    lambdaScrollingArea.pack(expand=1, fill = BOTH)      
    
    lambdaGridFrame = Frame(lambdaScrollingArea.innerframe) 
    lambdaTableLabel = Label(lambdaGridFrame, text = b'\xce\xbb'.decode('utf-8'))   
    lambdaTableLabel.grid(row = 0, column = 0)   
    
    #Generate data collection for the table boxes
    circleTableBoxes = {}
    lambdaTableBoxes = {}    
    
    #Generate labels for the behaviours
    for i in range(1, len(bevDict) + 1): #Rows
     bevLabel = Label(circleGridFrame, text = bevDict[i])
     bevLabel.grid(row = i, column = 0)
     circleTableBoxes[i, 0] = bevLabel
     bevLabel = Label(lambdaGridFrame, text = bevDict[i])
     bevLabel.grid(row = i, column = 0)  
     lambdaTableBoxes[i, 0] = bevLabel
    
    #Generate labels for the stimuli
    for j in range(1, len(stimDict) + 1): #Columns
     stimLabel = Label(circleGridFrame, text = stimDict[j])
     stimLabel.grid(row = 0, column = j)  
     circleTableBoxes[0, j] = stimLabel
     stimLabel = Label(lambdaGridFrame, text = stimDict[j])
     stimLabel.grid(row = 0, column = j)   
     lambdaTableBoxes[0, j] = stimLabel
    
    #generate the entry boxes
    for i in range(1, len(bevDict) + 1): #Rows
      for j in range(1, len(stimDict) + 1): #Columns
         circleTableEntry = Entry(circleGridFrame)
         lambdaTableEntry = Entry(lambdaGridFrame)
         circleTableEntry.grid(row=i, column=j)
         lambdaTableEntry.grid(row=i, column=j)
         circleTableBoxes[i, j] = circleTableEntry
         lambdaTableBoxes[i, j] = lambdaTableEntry
         
    circleGridFrame.pack(side=TOP, anchor = NW) 
    lambdaGridFrame.pack(side=TOP, anchor = SW) 
    
    generated = True
    
    #keep track of table's current lenght and width
    #only necessary to save this in one of the dictionaries
    #will be saved at coordinate (0, 0) since not in use
    circleTableBoxes[0, 0] = len(bevDict), len(stimDict)
    
   else: #Table was already generated
    circleScrollingArea.pack(expand=1, fill = BOTH)
    lambdaScrollingArea.pack(expand=1, fill = BOTH)
    
    circleGridFrame.pack(side=TOP, anchor = NW) 
    lambdaGridFrame.pack(side=TOP, anchor = SW)
    
    #calling fix_grids() to check if modifications are necessary to the grids
    fix_grids(bevDict, stimDict, circleTableBoxes, lambdaTableBoxes,
              circleGridFrame, lambdaGridFrame) 
    
  #PAGE 4 to PAGE 5
  if pageNum == 4:
   #create dictionary to hold values from tables
   circleTableValues = {}
   lambdaTableValues = {}
   
   #first table
   for key in circleTableBoxes.keys():
    a, b = key #extract corrdinate
    if a!= 0 and b != 0: #we are not interested in labels
     circleTableValues[key] = circleTableBoxes[key].get()
     
   #second table  
   for key in lambdaTableBoxes.keys():
    a, b = key #extract corrdinate
    if a!= 0 and b != 0: #we are not interested in labels
     lambdaTableValues[key] = lambdaTableBoxes[key].get()
    
   #calling check_if_good() to assure all the inputs are valid
   isGood, numInvalid = check_if_good(bevDict, stimDict, circleTableBoxes, 
                                      lambdaTableBoxes, circleTableValues, 
                                      lambdaTableValues)
   if isGood:
    circleGridFrame.pack_forget()
    lambdaGridFrame.pack_forget()
    create_text(agentName, agentBehaviour, circleTableBoxes, 
                lambdaTableBoxes, stimDict, bevDict)
   else:
    pageNum -= 1
    invalidEntryPop = Toplevel()
    
    windowSize = 300
    
    screenWidth = invalidEntryPop.winfo_screenwidth() 
    screenHeight = invalidEntryPop.winfo_screenheight()
    
    positionRight = screenWidth/2 - windowSize/2
    positionDown = screenHeight/2 - windowSize/2
    
    invalidEntryPop.geometry('%dx%d+%d+%d' % (windowSize, windowSize, 
                                              positionRight, positionDown))    
    invalidEntryPop.resizable(width = False, height = False) 

    invalidEntryPop.wm_title("INVALID ENTRIES!")
    invalidEntryPop.overrideredirect(1)
    
    Label(invalidEntryPop, text = 'Invalid Entries:').pack(side = TOP)
    invalidEntriesLabel = Label(invalidEntryPop, text = str(numInvalid) + 
                                ' entries to fix')
    invalidEntriesLabel.pack(side = TOP)
    
    pressToClose = Button(invalidEntryPop, text = "Return", 
                          command = return_to_tables)
    pressToClose.pack(side = BOTTOM)
    
    main.withdraw()
  pageNum += 1

#Function to return to previous page
def prev_page():
 global pageNum #keep track of page number
 
 #PAGE 2 to PAGE 1
 if pageNum == 2:
  stimScrollingArea.pack(expand=1, fill=BOTH)     
     
  for i in range(len(stimList)):   
   stimList[i].pack(side = TOP)
   
  #set new page 
  agentLabel.pack_forget()
  agentEntry.pack_forget()
  agentBevLabel.pack_forget()
  agentBevEntry.pack_forget()
  prevButton.pack_forget()
  delButton.pack(side = BOTTOM, fill = X)
  addStim.pack(side = BOTTOM, fill = X)
 
 #PAGE 3 to PAGE 2 
 if pageNum == 3:
  agentLabel.pack(side = TOP, anchor = W)
  agentEntry.pack(side = TOP, anchor = W)
  agentBevLabel.pack(side = TOP, anchor = W)
  agentBevEntry.pack(side = TOP, anchor = W)
  TitleCBS.pack_forget()
  LabelCBS.pack_forget()
  TextCBS.pack_forget()
  
  
 #PAGE 4 to PAGE 3
 if pageNum == 4:
    
  #set new page 
  circleScrollingArea.pack_forget()
  lambdaScrollingArea.pack_forget()
  
  circleGridFrame.pack_forget()
  lambdaGridFrame.pack_forget()
  
  TitleCBS.pack(side = TOP)
  LabelCBS.pack(side = TOP, anchor = W)
  TextCBS.pack(side = TOP, fill = X)  
 
 
 if pageNum == 5:
   circleGridFrame.pack(side=TOP, anchor = NW) 
   lambdaGridFrame.pack(side=TOP, anchor = SW)  
  
 pageNum -= 1
 
#Initializing the page number variable and the stimuli list
stimList = []
pageNum = 1

#No tables generated yet
generated = False

#
#Label exclusive to page 1
#
stimScrollingArea = Scrolling_Area(main)
stimScrollingArea.pack(expand=1, fill=BOTH)

stimTitle = Label(stimScrollingArea.innerframe, text='Please Enter The Stimuli')
stimTitle.pack(side = TOP)
#
#Defining Buttons available on each page
#

#Test Button
#testButton = Button(main, text ='Test', command = test)
#testButton.pack(side = BOTTOM, fill = X)

#Next Button
nextButton = Button(main, text = 'Next', command = next_page)
nextButton.pack(side = BOTTOM, fill = X)

#Prev Button (will not be availible on page 1)
prevButton = Button(main, text = 'Prev', command = prev_page)

#
#Buttons exclusive for page 1
#

#Delete previous entry Button
delButton = Button(main, text = 'Delete Previous', command = remove_entry)
delButton.pack(side = BOTTOM, fill = X)

#Add stimulus Button
addStim = Button(main, text = 'Add new stimulus', command = new_entry)
addStim.pack(side = BOTTOM, fill = X)

#
#Labels and Entries exclusive for page 2
#

#Agent Name Label and Entry
agentLabel = Label(main, text = 'Enter Agent Name:')
agentEntry = Entry(main, width = 50)

#Agent Behaviour Label and Entry
agentBevLabel = Label(main, text = 'Enter Agent Behaviour:')
agentBevEntry = Entry(main, width = 50)

#
#Labels and Entries exclusive for page 3
#

TitleCBS = Label(main, text='Concrete Behaviours')
TextCBS = Text(main, height = 10)

main.mainloop()
