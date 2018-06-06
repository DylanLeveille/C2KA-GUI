from tkinter import*
from entry_mods import*
from get_word_list import*
from CBS import *
from create_table import*
from fix_grids import*
from create_text import*
from check_if_good import*
from create_save_file import*
import vertSuperscroll
import superscroll

main = Tk()
main.title("C2KA GUI")
main.resizable(width = False, height = False)

windowSize = 500

screenWidth = main.winfo_screenwidth() 
screenHeight = main.winfo_screenheight()

positionRight = screenWidth/2 - windowSize/2
positionDown = screenHeight/2 - windowSize/2

main.geometry('%dx%d+%d+%d' % (windowSize, windowSize, positionRight, 
                               positionDown))

#Note: some global variables will be used due to the button functions
#being unable to contain parameters.
   
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
  
  global generatedTable #bool variable to check if tables were generated
  global generatedCBS #check to see if CBS was already generated
  
  global noStims #pop-up window for no stims inputted
  global invalidEntryPop #pop-up window for invalid table entries
  
  global FrameCBS
  global AgentCBS
  global EntriesCBS
  global LabelsCBS
  global rowNum
  
  #Note: dictionaries are set empty when swithing to a next page
  #(depending on pageNum) in order to update the data
  
  #PAGE 1 to PAGE 2
  if pageNum == 1:
    stimDict = get_empty_dict() #stimuli dictionary
    stimDict = build_stim_dict(stimList) #behaviour dictionary
    
    if stimDict == None or len(stimDict) == 0: #user must imput at least one valid stimulus
      #stay on current page
      incorrect_stims(main)
      pageNum -= 1     
     
    else:
      #set new page 
      stimScrollingArea[0].pack_forget()
      addStim.pack_forget()
      delButton.pack_forget()
      stimFrame.pack_forget()
      prevButton.pack(in_=buttonsFrame, side = LEFT)
      nextButton.config(width = 35)
      agentLabel.pack(side = TOP, anchor = W)
      agentEntry.pack(side = TOP, anchor = W)
      agentBevLabel.pack(side = TOP, anchor = W)
      agentBevEntry.pack(side = TOP, anchor = W)   
  
  #PAGE 2 to PAGE 3
  if pageNum ==2:
   
    agentName = get_agent(agentEntry.get()) #the agent name
    bevDict = build_bev_dict(agentBevEntry.get()) #behaviour dictionary
   
    if agentName == None: #need at least one agent
      #stay on current page
      incorrect_agent(main)
      pageNum -= 1    
   
    elif bevDict == None or len(bevDict) == 0: #user must imput at least one valid behaviour
      #stay on current page
      incorrect_bevs(main)
      pageNum -= 1
    

    else:  
      #set new page
      agentLabel.pack_forget()
      agentEntry.pack_forget()
      agentBevLabel.pack_forget()
      agentBevEntry.pack_forget()
    
      AgentCBS = Label(main, text = agentEntry.get())
      TitleCBS.pack(side = TOP)
      AgentCBS.pack(side = TOP, anchor = W)
      FrameCBS.pack(side = TOP, fill = BOTH)
    
      if generatedCBS == False:
        rowNum = 0
        EntriesCBS, LabelsCBS, rowNum = create_CBS_entries(bevDict, FrameCBS, rowNum)
        generatedCBS = True
 
      else:
        rowNum, EntriesCBS, LabelsCBS = fix_CBS(bevDict, EntriesCBS, LabelsCBS, FrameCBS, rowNum)
     
      agentName = agentEntry.get()    
      agentBehaviour = agentBevEntry.get()   
  
  #PAGE 3 to PAGE 4
  if pageNum == 3:
    #set new page 
    FrameCBS.pack_forget()
    TitleCBS.pack_forget()
    AgentCBS.pack_forget()
    nextButton.config(width = 23)
    prevButton.config(width = 23)
    fillN.pack(in_=buttonsFrame, side = BOTTOM)
   
    if generatedTable == False:
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
    
      #create the data structures to hold the table entries
      circleTableBoxes, lambdaTableBoxes = create_table(bevDict, stimDict,
                                                      circleGridFrame, 
                                                      lambdaGridFrame)
      #pack the new frames     
      circleGridFrame.pack(side=TOP, anchor = NW) 
      lambdaGridFrame.pack(side=TOP, anchor = SW) 
    
      generatedTable = True #table is now generated

    
      #keep track of table's current lenght and width
      #only necessary to save this in one of the dictionaries
      #will be saved at coordinate (0, 0) since not in use
      circleTableBoxes[0, 0] = len(bevDict), len(stimDict)
    
    else: #Table was already generated
      #calling fix_grids() to check if modifications are necessary to the grids
      fix_grids(bevDict, stimDict, circleTableBoxes, lambdaTableBoxes,
                circleGridFrame, lambdaGridFrame) 
    
      #recreating the table
      circleScrollingAreaTemp = superscroll.Scrolling_Area(main, width=1, height=1)
      circleScrollingAreaTemp.pack(expand=1, fill = BOTH)   
    
      circleGridFrameTemp = Frame(circleScrollingAreaTemp.innerframe) 
      circleTableLabel = Label(circleGridFrameTemp, text = 'o')   
      circleTableLabel.grid(row = 0, column = 0)
    
      lambdaScrollingAreaTemp = superscroll.Scrolling_Area(main, width=1, height=1)
      lambdaScrollingAreaTemp.pack(expand=1, fill = BOTH)      
    
      lambdaGridFrameTemp = Frame(lambdaScrollingAreaTemp.innerframe) 
      lambdaTableLabel = Label(lambdaGridFrameTemp, text = b'\xce\xbb'.decode('utf-8'))   
      lambdaTableLabel.grid(row = 0, column = 0)           

      circleTableBoxes, lambdaTableBoxes = recreate_table(bevDict, stimDict, circleTableBoxes, 
                                                          lambdaTableBoxes, circleGridFrameTemp, 
                                                          lambdaGridFrameTemp)     
      #destroy old frames
      circleScrollingArea.destroy()
      circleGridFrame.destroy()
      lambdaScrollingArea.destroy()
      lambdaGridFrame.destroy()
           
      #pack the new frames
      circleScrollingAreaTemp.pack(side=TOP, anchor = NW)
      circleGridFrameTemp.pack(side=TOP, anchor = NW)
      lambdaScrollingAreaTemp.pack(side=TOP, anchor = SW)
      lambdaGridFrameTemp.pack(side=TOP, anchor = SW)
      
      #assign to old frames to the new frames
      circleScrollingArea = circleScrollingAreaTemp
      circleGridFrame = circleGridFrameTemp
      lambdaScrollingArea = lambdaScrollingAreaTemp
      lambdaGridFrame = lambdaGridFrameTemp        
    
  #PAGE 4 to PAGE 5
  if pageNum == 4:
    #create dictionary to hold values from tables
    circleTableValues = get_empty_dict()
    lambdaTableValues = get_empty_dict()
   
    #first table values and second table values
    circleTableValues, lambdaTableValues = getTableValues(circleTableBoxes, 
                                                         lambdaTableBoxes) 
   
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
    
      prevButton.config(width = 35)
    
      create_text(agentName, agentBehaviour, circleTableValues, 
                  lambdaTableValues, stimDict, bevDict, LabelsCBS, EntriesCBS)
  
      textEntry.config(state = 'normal')
      textEntry.delete(1.0, END)
      textEntry.insert(INSERT, open("agentspec.txt", "r").read())
      textEntry.config(state="disabled")
      textEntry.pack(side = TOP)
      
      saveButton.pack(in_=buttonsFrame)

    else:
      incorrect_table(main, numInvalid)
      pageNum -= 1
  pageNum += 1

#Function to return to previous page
def prev_page():
  global pageNum #keep track of page number
 
  #PAGE 2 to PAGE 1
  if pageNum == 2:
    stimScrollingArea[0].pack(expand=1, fill=BOTH)     
     
    for i in range(len(stimList)):   
      stimList[i].pack(side = TOP)
   
    #set new page 
    agentLabel.pack_forget()
    agentEntry.pack_forget()
    agentBevLabel.pack_forget()
    agentBevEntry.pack_forget()
    prevButton.pack_forget()
    nextButton.config(width = 23)
    stimFrame.pack(side = BOTTOM, anchor = S, expand = True)
    delButton.pack(in_=buttonsFrame, side = LEFT)
    addStim.pack(in_=buttonsFrame, side = TOP)

 #PAGE 3 to PAGE 2 
  if pageNum == 3:
    agentLabel.pack(side = TOP, anchor = W)
    agentEntry.pack(side = TOP, anchor = W)
    agentBevLabel.pack(side = TOP, anchor = W)
    agentBevEntry.pack(side = TOP, anchor = W)
    FrameCBS.pack_forget()
    TitleCBS.pack_forget()
    AgentCBS.pack_forget()
  
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
    AgentCBS.pack(side = TOP, anchor = W)
    FrameCBS.pack(fill = BOTH) 

  #PAGE 5 to PAGE 4
  if pageNum == 5:
    textEntry.pack_forget()
    saveButton.pack_forget()
    
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
generatedTable = False
generatedCBS = False

#Frame for the main buttons
buttonsFrame = Frame(main)
buttonsFrame.pack(side = BOTTOM, anchor = S, expand = True)

#Frame for the stim # Label, button and entry box
stimFrame = Frame(main)
stimFrame.pack(side = BOTTOM, anchor = S, expand = True)

#
#Defining Buttons available on each page
#

#Next Button
nextButton = Button(main, text = 'Next', command = next_page, width = 23)
nextButton.pack(in_=buttonsFrame, side = RIGHT)

#Prev Button (will not be availible on page 1)
prevButton = Button(main, text = 'Prev', command = prev_page, width = 35)

#
#Label and Buttons exclusive to page 1
#

#stimScrollingArea is at index zero of the list, this way, the scrolling area
#can be passed by reference and modified by other functions
stimScrollingArea = [vertSuperscroll.Scrolling_Area(main)]
stimScrollingArea[0].pack(expand = 1, fill = BOTH)

stimTitle = Label(stimScrollingArea[0].innerframe, text='Please Enter The Stimuli')
stimTitle.pack(side = TOP)

#label, button and entry box to generate specified number of stimuli
enterStimLabel = Label(main, text = 'enter # of stims')
enterStimLabel.pack(in_=stimFrame, side = LEFT)

enterStimButton = Button(main, text = 'OK', command = lambda: specify_stim(main, stimList, enterStimBox.get(), stimScrollingArea))
enterStimButton.pack(in_=stimFrame, side = RIGHT)

enterStimBox = Entry(main)
enterStimBox.pack(in_=stimFrame, side = TOP)

#Delete previous entry Button
delButton = Button(main, text = 'Delete Previous', command = lambda: remove_stim(main, stimList, stimScrollingArea), 
                   width = 23)
delButton.pack(in_=buttonsFrame, side = LEFT)

#Add stimulus Button
addStim = Button(main, text = 'Add new stimulus', 
                 command = lambda: add_stim(main, stimList, stimScrollingArea), 
                 width = 23)

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

#Labels and Entries for page 3
FrameCBS = Frame(main)
TitleCBS = Label(main, text='Concrete Behaviours')

#
#Labels and Entries exclusive for page 4
#

fillN = Button(main, text = 'Fill with neutral stimulus', 
               command = lambda: fill_n(bevDict, stimDict, 
                                        circleTableBoxes, lambdaTableBoxes), width = 23)

#
#Labels and Entries exclusive for page 5
#
textEntry = Text(main)

saveButton = Button(main, text = 'Save File', command = create_save_file, width = 35)

main.mainloop()