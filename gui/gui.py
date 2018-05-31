from tkinter import*
from get_word_list import*
from fix_grids import*
from create_text import*
from check_if_good import*
import vertSuperscroll 
import superscroll

main = Tk()
main.title("C2KA GUI")
main.resizable(width=False, height=False)

windowSize = 500

screenWidth = main.winfo_screenwidth() 
screenHeight = main.winfo_screenheight()

positionRight = screenWidth/2 - windowSize/2
positionDown = screenHeight/2 - windowSize/2

main.geometry('%dx%d+%d+%d' % (windowSize, windowSize, positionRight, 
                               positionDown))

#Note: some global variables will be used due to the button functions
#being unable to contain parameters.
 
#button function to fill lambda table with neutral stimulus
def fill_n(bevDict, stimDict, circleTableBoxes, lambdaTableBoxes):
 for i in range(1, len(bevDict) + 1): #Rows
   for j in range(1, len(stimDict) + 1): #Columns
     #checking if empty in lambda table
     if lambdaTableBoxes[i, j].get() == ' ' * len(lambdaTableBoxes[i, j].get()):
       #if empty, put neutral stimulus
       lambdaTableBoxes[i, j].delete(0, END) 
       lambdaTableBoxes[i, j].insert(0, 'N')

#function to return to the tables after the pop-up 
def return_to_tables():
 main.update()
 main.deiconify()
 invalidEntryPop.destroy()

#Function to add new stimuli (page 1 exclusive)
def add_stim(): 
 global stimList #list containing every entry box
 global stimScrollingArea #area for the scrolling/stimuli
 
 #the scrolling area must be reset every time
 stimScrollingArea.pack_forget()

 stimScrollingArea = vertSuperscroll.Scrolling_Area(main)
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
 
 stimList.append(stimEntry)
    
#Function to remove stimuli (page 1 exclusive) 
def remove_stim():
 global stimScrollingArea #area for the scrolling/stimuli
 if len(stimList) > 0: #must be greater than 0 to be able to remove a stimulus
   entryToDelete = stimList[len(stimList) - 1]
   del stimList[len(stimList) - 1] 
   entryToDelete.destroy()
   
   #the scrolling area must be reset every time
   stimScrollingArea.pack_forget()
  
   stimScrollingArea = vertSuperscroll.Scrolling_Area(main)
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
    stimDict = build_stim_dict(stimList) #behaviour dictionary
       
    if stimDict == None or len(stimDict) == 0: #user must imput at least one valid stimulus
     #stay on current page
     incorrect_stims(main)
     pageNum -= 1     
     
    else:
     #set new page 
     stimScrollingArea.pack_forget()
     addStim.pack_forget()
     delButton.pack_forget()
     prevButton.pack(in_=buttonsFrame, side = LEFT)
     nextButton.config(width = 35)
     agentLabel.pack(side = TOP, anchor = W)
     agentEntry.pack(side = TOP, anchor = W)
     agentBevLabel.pack(side = TOP, anchor = W)
     agentBevEntry.pack(side = TOP, anchor = W)   
  
  #PAGE 2 to PAGE 3
  if pageNum ==2:
   
   bevDict = build_bev_dict(agentBevEntry.get()) #behaviour dictionary
   
   if bevDict == None or len(bevDict) == 0: #user must imput at least one valid behaviour
    #stay on current page
    incorrect_bevs(main)
    pageNum -= 1
    
   else:  
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
   #set new page 
   TitleCBS.pack_forget()
   LabelCBS.pack_forget()
   TextCBS.pack_forget()
   nextButton.config(width = 23)
   prevButton.config(width = 23)
   fillN.pack(in_=buttonsFrame, side = BOTTOM)
   
   if generated == False:
    #Frame for the tables and corner label
    circleScrollingArea = superscroll.Scrolling_Area(main, width=1, height=1)
    circleScrollingArea.pack(expand=1, fill = BOTH)   
    
    circleGridFrame = Frame(circleScrollingArea.innerframe) 
    circleTableLabel = Label(circleGridFrame, text = 'o')   
    circleTableLabel.grid(row = 0, column = 0)
    
    lambdaScrollingArea = superscroll.Scrolling_Area(main, width=1, height=1)
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
    #calling fix_grids() to check if modifications are necessary to the grids
    fix_grids(bevDict, stimDict, circleTableBoxes, lambdaTableBoxes,
              circleGridFrame, lambdaGridFrame) 
    
    #recreating the table
    circleScrollingArea.pack_forget()
    circleScrollingArea = superscroll.Scrolling_Area(main, width=1, height=1)
    circleScrollingArea.pack(expand=1, fill = BOTH)   
    
    circleGridFrame.pack_forget()
    circleGridFrame = Frame(circleScrollingArea.innerframe) 
    circleTableLabel = Label(circleGridFrame, text = 'o')   
    circleTableLabel.grid(row = 0, column = 0)
    
    lambdaScrollingArea.pack_forget()
    lambdaScrollingArea = superscroll.Scrolling_Area(main, width=1, height=1)
    lambdaScrollingArea.pack(expand=1, fill = BOTH)      
    
    lambdaGridFrame.pack_forget()
    lambdaGridFrame = Frame(lambdaScrollingArea.innerframe) 
    lambdaTableLabel = Label(lambdaGridFrame, text = b'\xce\xbb'.decode('utf-8'))   
    lambdaTableLabel.grid(row = 0, column = 0)           

    #Generate labels for the behaviours
    for i in range(1, len(bevDict) + 1): #Rows
     bevLabel = Label(circleGridFrame, text = bevDict[i])
     bevLabel.grid(row = i, column = 0)
     bevLabel = Label(lambdaGridFrame, text = bevDict[i])
     bevLabel.grid(row = i, column = 0)  

    #Generate labels for the stimuli
    for j in range(1, len(stimDict) + 1): #Columns
     stimLabel = Label(circleGridFrame, text = stimDict[j])
     stimLabel.grid(row = 0, column = j)  
     stimLabel = Label(lambdaGridFrame, text = stimDict[j])
     stimLabel.grid(row = 0, column = j)     
    
    #re-generate the table with the modifications brought by fix_grids()
    for i in range(1, len(bevDict) + 1): #Rows
      for j in range(1, len(stimDict) + 1): #Columns
         circleTableEntry = Entry(circleGridFrame)
         lambdaTableEntry = Entry(lambdaGridFrame)

         circleTableEntry.grid(row=i, column=j)
         lambdaTableEntry.grid(row=i, column=j)
         
         circleTableEntry.insert(0, circleTableBoxes[i, j].get())
         lambdaTableEntry.insert(0, lambdaTableBoxes[i, j].get())
           
         circleTableBoxes[i, j] = circleTableEntry
         lambdaTableBoxes[i, j] = lambdaTableEntry
         
    circleGridFrame.pack(side=TOP, anchor = NW) 
    lambdaGridFrame.pack(side=TOP, anchor = SW)         
    
  #PAGE 4 to PAGE 5
  if pageNum == 4:
   #create dictionary to hold values from tables
   circleTableValues = {}
   lambdaTableValues = {}
   
   #first table
   for key in circleTableBoxes.keys():
    a, b = key #extract corrdinate
    if a!= 0 and b != 0: #we are not interested in labels
     circleTableValues[key] = (circleTableBoxes[key].get()).replace(" ", "").upper()
     
   #second table  
   for key in lambdaTableBoxes.keys():
    a, b = key #extract corrdinate
    if a!= 0 and b != 0: #we are not interested in labels
     lambdaTableValues[key] = (lambdaTableBoxes[key].get()).replace(" ", "").upper()
 
   #calling check_if_good() to assure all the inputs are valid
   isGood, numInvalid = check_if_good(bevDict, stimDict, circleTableBoxes, 
                                      lambdaTableBoxes, circleTableValues, 
                                      lambdaTableValues)
   if isGood:
    circleScrollingArea.pack_forget()
    lambdaScrollingArea.pack_forget()
    
    circleGridFrame.pack_forget()
    lambdaGridFrame.pack_forget()
    
    fillN.pack_forget()
    nextButton.pack_forget()
    
    prevButton.config(width = 70)
    
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
  nextButton.config(width = 23)
  delButton.pack(in_=buttonsFrame, side = LEFT)
  addStim.pack(in_=buttonsFrame, side = TOP)
 
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
  
  fillN.pack_forget()
  
  nextButton.config(width = 35)
  prevButton.config(width = 35)  
  
  TitleCBS.pack(side = TOP)
  LabelCBS.pack(side = TOP, anchor = W)
  TextCBS.pack(side = TOP, fill = X)  
 
 
 if pageNum == 5:
   circleGridFrame.pack(side=TOP, anchor = NW) 
   lambdaGridFrame.pack(side=TOP, anchor = SW)  

 #PAGE 5 to PAGE 4
 if pageNum == 5:
  prevButton.config(width = 23) 
  
  circleScrollingArea.pack(expand=1, fill = BOTH)   
  lambdaScrollingArea.pack(expand=1, fill = BOTH)   
  
  circleGridFrame.pack(side=TOP, anchor = NW) 
  lambdaGridFrame.pack(side=TOP, anchor = SW) 
  
  nextButton.pack(in_=buttonsFrame, side = RIGHT)
  fillN.pack(in_=buttonsFrame, side = BOTTOM)
  
 pageNum -= 1
 
#Initializing the page number variable and the stimuli list
stimList = []
pageNum = 1

#No tables generated yet
generated = False

#Frame for the main buttons
buttonsFrame = Frame(main)
buttonsFrame.pack(side = BOTTOM, anchor = S, expand = True)

#
#Defining Buttons available on each page
#

#Test Button
#testButton = Button(main, text ='Test', command = test)
#testButton.pack(side = BOTTOM, fill = X)

#Next Button
nextButton = Button(main, text = 'Next', command = next_page, width = 23)
nextButton.pack(in_=buttonsFrame, side = RIGHT)

#Prev Button (will not be availible on page 1)
prevButton = Button(main, text = 'Prev', command = prev_page, width = 35)

#
#Label and Buttons exclusive to page 1
#
stimScrollingArea = vertSuperscroll.Scrolling_Area(main)
stimScrollingArea.pack(expand = 1, fill = BOTH)

stimTitle = Label(stimScrollingArea.innerframe, text='Please Enter The Stimuli')
stimTitle.pack(side = TOP)

#Delete previous entry Button
delButton = Button(main, text = 'Delete Previous', command = remove_stim, width = 23)
delButton.pack(in_=buttonsFrame, side = LEFT)

#Add stimulus Button
addStim = Button(main, text = 'Add new stimulus', command = add_stim, width = 23)
addStim.pack(in_=buttonsFrame, side = TOP)

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

#
#Labels and Entries exclusive for page 3
#

fillN = Button(main, text = 'Fill with neutral stimulus', 
               command = lambda: fill_n(bevDict, stimDict, 
                                        circleTableBoxes, lambdaTableBoxes), width = 23)

main.mainloop()
