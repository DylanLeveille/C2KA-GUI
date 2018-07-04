""" Internship Project.

GUI to Assist the C2KA TOOL.
"""

"""Imported modules."""
from tkinter import * ##Import the tkinter module to allow construction of the GUI interface.
from check_if_good import * ##Functions which validate most of the data in the program.
from entry_mods import * ##Functions which modify entry boxes.
from get_word_list import * ##Functions which parse an entry box and returns lists of words.
from fix_dict_order import *
from create_agent_data import *
from create_agent_page import *
from create_agent_preview import *
from set_data import *
from CBS_radio import * ##Functions that set the CBS page depending on which radio button is clicked.
from create_text import * ##A module containing the function that creates the final product (text file).
from create_save_file import * ##A module that contains the function to allow the text file to be saved to a certain directory. 
import vertSuperscroll ##Module containing the widget allowing a vertical scrollbar.
import superscroll ##Module containing the widget allowing a vertical and horizontal scrollbar.

"""Next and previous button functions."""
##Note: some global variables will be used due to the button functions
##being unable to contain parameters.
   
##Function to go to the next page.
def next_page():
  """ (none) -> (none)
    
    Allows the configuration of the next page 
    in the program depending on the current
    pageNum. Saves the collected entries (data)
    in global data structures.
  
  """
  global pageNum ##Keeps track of the page number.
  
  global saveButton
  global textEntryFrame
  
  global stimDict ##Dictionary to hold final entries of entered stimuli.
  global allBevDict ##Dictionary to hold agent behaviours.
  
  global oldAgentNames ##Record the names of the agents previously stored in the program.
  global agentNames ##Record entries for the name of the agents.
  global agentBehaviours ##Record entries for the behaviour of the agents.
  
  global allConcreteScrollingArea ##Scrolling area for the concrete behaviours (CBS).
  
  global allEntriesCBS ##Dict to hold concrete behaviour labels and entries.
  global allTextBoxCBS ##Dict to hold textbox text for concrete behaviours
  
  global allRadioButtons
  global concreteBehaviours ##Dict to hold parsed concrete behaviours
  
  global allFormatCBS
  
  global allFillButtons
  
  global allAgentWindows
  global allCBSTabContents
  global allTableTabContents
  global allEditButtons
  
  global allCircleTableBoxes ##Dict to hold entry boxes and labels of circle table for all agents.
  
  global allCircleScrollingArea ##Scrolling area for circle table.
  global allLambdaScrollingArea ##Scrolling area for lambda table.
  
  global allCircleGridFrame ##Global frame for the circle table.
  global allLambdaGridFrame ##Global frame for the lambda table.
  
  global moreThanOneAgent ##Boolean to keep track of if there is more than one agent inputted.
  
  global allIsGoodCBS 
  global allIsGoodTable
  
  global allPreviewPops ##List to hold the pop-up windows for each agent specification

  global generatedTables ##List to keep track of tables that were already generated for each agent.
  global generatedCBS ##List to keep track of Bool variables to check if CBS were generated.
  
  ##Note: dictionaries are set empty when swithing to a next page
  ##(depending on pageNum) in order to update the data.
  
  """PAGE 1 to PAGE 2."""
  if pageNum == 1:
    stimDict = get_empty_dict() ##Stimuli dictionary set empty.
    stimDict = build_stim_dict(stimList) ##Stimuli dictionary is created usign the list of stim entries.
    
    if stimDict == None or len(stimDict) == 0: ##User must imput at least one valid stimulus.
      ##Stay on current page.
      incorrect_stims(main, return_arrow) ##Calls function for pop-up.
      pageNum -= 1 ##Decrease pageNum by one to stay on current page.    
     
    else: ##User inputted valid stimuli.
      ##Get a logical order for the stimul; ex: AVG2 AVG1 becomes AVG1 AVG2
      stimDict = fix_dict_order(stimDict)
      
      ##Set new page by unpacking widgets on page 1.
      stimScrollingArea[0].pack_forget()
      addStim.pack_forget()
      stimTitle.pack_forget()
      stimFrame.pack_forget()
      
      ##Pack the new previous button.
      prevButton.pack(in_=buttonsFrame, side = LEFT, anchor = S)
      
      ##Pack new scrolling area for the agent and its behaviours,
      ##and pack the button to add an agent.
      agentTitle.pack()
      agentScrollingArea[0].pack(expand = 1, fill = BOTH, pady = (0, 80))        
      
      addAgent.pack(in_=buttonsFrame, side = TOP)
      
      ##Store a copy of the old agent names to check if there are any similar agents
      ##before going to page 2.  
      oldAgentNames = agentNames.copy() 
  
  """PAGE 2 to PAGE 3."""
  if pageNum == 2: 
    agentsGood = True ##Assuming the agent entries are good.
    
    agentNames = get_agents(agentFrames['agentNames']) ##The agent names are extracted from the entries in a list.
    allBevDict = build_bev_dict(agentFrames['agentBev']) ##Creates a behaviour dictionary for each agent.
    
    for i in range(len(agentNames)):
      if agentNames[i] == None or agentNames[i] == '': ##User must input one valid agent to proceed.
        ##Change background colour of the agent entry to tomato-red to warn user.
        agentFrames['agentNames'][i].config(bg = 'tomato')
        ##Stay on current page by warning the user with a pop-up.
        
        if pageNum == 2: ##Only decrease pageNum once.
          ##Decrease pageNum to stay on current page.
          agentsGood = False
          incorrect_agent(main, return_arrow)        
          pageNum -= 1    
       
      else: ##Entry is good.
        agentFrames['agentNames'][i].config(bg = 'white')
        
    for i in range(len(allBevDict)):
      if allBevDict[i + 1] == None or len(allBevDict[i + 1]) == 0: ##User must input one valid agent to proceed.
        ##Change background colour of the agent entry to tomato-red to warn user.
        agentFrames['agentBev'][i].config(bg = 'tomato')
        ##Stay on current page by warning the user with a pop-up.
        
        if pageNum == 2: ##Only decrease pageNum once.
          ##Decrease pageNum to stay on current page.
          agentsGood = False
          incorrect_bevs(main, return_arrow)        
          pageNum -= 1    
       
      else: ##Entry is good.
        ##Get a logical order for the stimul; ex: AVG2 AVG1 becomes AVG1 AVG2
        allBevDict[i + 1] = fix_dict_order(allBevDict[i + 1])        
        
        ##Change entry box volour back to white.
        agentFrames['agentBev'][i].config(bg = 'white')
        
    if agentsGood:  ##If there is still no error
      if not check_if_good_agents(agentNames, agentFrames['agentNames']):
        agentsGood = False
        same_agent(main, return_arrow)
        pageNum-=1      
      
      elif len(agentNames) == 0: ##Means there are absolutely no agents.
        agentsGood = False
        incorrect_agent(main, return_arrow)
        pageNum-=1
   
    if agentsGood:
      ##Before going to the next page, extract the full text describing 
      ##the agents' behaviour (used hen create the text file).
      agentBehaviours = extract_full_behaviour(agentFrames['agentBev'])
      
      ##Set new page by unpacking scrolling area on page 2 and the add agent button.
      agentTitle.pack_forget()
      agentScrollingArea[0].pack_forget()      
      addAgent.pack_forget()
         
      ##Create and modify all of the agents data based on the entered information and their order.
      moreThanOneAgent, pageNum = create_agent_data(main, pageNum, agentFrames, buttonsFrame, allEditButtons,
                                                    allCheckLabels, allAgentWindows, editScrollingArea, allBevDict, 
                                                    stimDict, allFillButtons, oldAgentNames, agentNames, allCircleTableBoxes, 
                                                    allLambdaTableBoxes, allCircleScrollingArea, allLambdaScrollingArea, 
                                                    allCircleGridFrame, allLambdaGridFrame, allTextBoxCBSFrame,
                                                    allFormatCBS, allEntriesCBS, allAgentCBS, allTextBoxCBS, 
                                                    allRadioButtons, allConcreteScrollingArea, generatedTables, 
                                                    generatedCBS, allIsGoodCBS, allIsGoodTable, allCBSTabContents, 
                                                    allTableTabContents, allPreviewPops, edit_icon, filled_icon, editTitle)
        
      ##Save agents in old agents in case user returns to page 2 WITHOUT going to page 1.
      oldAgentNames = agentNames.copy()  
      
  """PAGE 3 to PAGE 4."""
  if pageNum == 3 and moreThanOneAgent == False: ##Only true when one agent only.
   
    ##Boolean variable for validity of entries.
    isGoodCBS = check_if_good_CBS(main, allEntriesCBS, allRadioButtons, allTextBoxCBS, allIsGoodCBS)
   
    ##If there are invalid entries, create popup.
    if isGoodCBS == False:
      incorrect_CBS(main, moreThanOneAgent, allIsGoodCBS, return_arrow, 0) ##Calls function for pop-up.

      pageNum -= 1 ##Decrease pageNum by one to stay on current page. 

    else: ##Entries are good.        
      whichRadio = allRadioButtons[0][2]
   
      ##Set new page by forgetting the CBS related frames and entries.
      if whichRadio.get() == 'Rows': ##User was using rowsCBS.
        allConcreteScrollingArea[0][0].pack_forget()
        
      else: ##User was using boxCBS.
        allTextBoxCBSFrame[0].pack_forget()
      
      ##Unpack widgets available to both radio buttons.  
      allAgentCBS[0].pack_forget()
      allFormatCBS[0].pack_forget()
      editTitle.config(text = "Agent Specifications: Tables") 
      set_table_data(main, allBevDict, stimDict, allFillButtons, allCircleTableBoxes,
                     allLambdaTableBoxes, allCircleScrollingArea, allLambdaScrollingArea, 
                     allCircleGridFrame, allLambdaGridFrame, generatedTables, 
                     moreThanOneAgent, 0, allTableTabContents)
    
  """PAGE 4 to PAGE 5."""
  if pageNum == 4:
    
    ##Create dictionaries to hold the values from tables.
    allCircleTableValues = get_empty_dict()
    allLambdaTableValues = get_empty_dict()
    
    isPageGood = True ##Assume entire page is good.
    wrongAgents = 0 ##Assume no agents are wrong (to be used in a pop-up to tell user how many are wrong if any).
    
    if moreThanOneAgent:
      buttonsClicked = 0
      for i in range(len(agentNames)):
        if allEditButtons[i][1] == True:
          
          buttonsClicked += 1
      
      if buttonsClicked == len(agentNames):

        
        check_if_good_CBS(main, allEntriesCBS, allRadioButtons, allTextBoxCBS, allIsGoodCBS) ##Note, return value not saved since it is only used for single agent CBS check.

        ##Create dictionaries to hold the values from tables.
        allCircleTableValues = get_empty_dict()
        allLambdaTableValues = get_empty_dict()
       
        ##Extract circle table values and lambda table values for each agent.
        for i in range(len(agentNames)):
          allCircleTableValues[i + 1], allLambdaTableValues[i + 1] = get_table_values(allCircleTableBoxes[i + 1], 
                                                                                      allLambdaTableBoxes[i + 1]) 

         
        ##Calling check_if_good() to assure all the inputs are valid.
        isGoodTable, numInvalid = check_if_good_table(allBevDict, stimDict, allCircleTableBoxes, 
                                          allLambdaTableBoxes, allCircleTableValues, 
                                          allLambdaTableValues, allIsGoodTable)

        for j in range(len(agentNames)):
          if allIsGoodCBS[j] == False or allIsGoodTable[j] == False:
            allCheckLabels[j].config(image = incorrect_icon)
            isPageGood = False
            wrongAgents += 1
                    
          else:
            allCheckLabels[j].config(image = correct_icon)
        
        
        if isPageGood:
          editTitle.config(text = "Agent Text Preview")
          ##Iterate through each edit button to change their text and command functions.
          for i in range(len(allEditButtons)):
            allEditButtons[i][0].config(image = view_icon, command = lambda boxIndex = i:create_agent_preview(main, allEditButtons, allPreviewPops, agentNames, allEntriesCBS, 
                                                                                                             agentBehaviours, allTextBoxCBS, allCircleTableValues, 
                                                                                                             allLambdaTableValues, stimDict, allBevDict, allRadioButtons,
                                                                                                             save_icon, return_arrow, moreThanOneAgent, boxIndex))
            allCheckLabels[i].pack_forget() ##Forget the check marks.
            allEditButtons[i] = allEditButtons[i][0], False ##Change clicked to False for each button.
            
            nextButton.pack_forget() ##Forget the next button since we are at the last page.
          
        else:
          incorrect_CBS(main, moreThanOneAgent, allIsGoodCBS, return_arrow, wrongAgents)
          pageNum -= 1
      
      else:
        button_not_clicked(main, return_arrow)
        pageNum -= 1

    elif not moreThanOneAgent: ##Only check tables.
      
      ##Extract circle table values and lambda table values for each agent.
      for i in range(len(agentNames)):
        allCircleTableValues[i + 1], allLambdaTableValues[i + 1] = get_table_values(allCircleTableBoxes[i + 1], 
                                                                                    allLambdaTableBoxes[i + 1])       
      ##Calling check_if_good() to assure all the inputs are valid.
      isGoodTable, numInvalid = check_if_good_table(allBevDict, stimDict, allCircleTableBoxes, 
                                        allLambdaTableBoxes, allCircleTableValues, 
                                        allLambdaTableValues, allIsGoodTable)      
      ##If the table is good, proceed.
      if isGoodTable:
        editTitle.config(text = "Agent Text Preview")
        ##Forget table scrolling areas.
        allCircleScrollingArea[0][0].pack_forget()
        allLambdaScrollingArea[0][0].pack_forget()
      
        ##Forget table frames.
        allCircleGridFrame[0].pack_forget()
        allLambdaGridFrame[0].pack_forget()
      
        ##Forget next button, fillBev button and fillN button, since they are not
        ##needed on the last page of the program.
        allFillButtons[0][0].pack_forget()
        allFillButtons[0][1].pack_forget()
        nextButton.pack_forget()
        
        ##Call create_text() to create the agentspec.txt file.
        textEntryFrame, saveButton = create_agent_preview(main, allEditButtons, allPreviewPops, agentNames, allEntriesCBS, 
                                                                     agentBehaviours, allTextBoxCBS, allCircleTableValues, 
                                                                     allLambdaTableValues, stimDict, allBevDict, allRadioButtons,
                                                                     save_icon, return_arrow, moreThanOneAgent, 0)
      
      ##Table is not good.
      else:
        ##Deliver a pop-up to the user to warn of invalid entries in the table.
        incorrect_table(main, numInvalid, return_arrow)
        ##Decrease pageNum to stay on current page.
        pageNum -= 1
  
  ##Add one to pageNum everytime the next button is clicked.
  pageNum += 1

##Function to return to the previous page.
def prev_page():
  """ (none) -> (none)
    
    Allows the configuration of the previous page 
    in the program depending on the current
    pageNum. Unpacks newer widgets and packs older ones.
  
  """  
  global pageNum ##Keeps track of the page number.
 
  """PAGE 2 to PAGE 1."""
  if pageNum == 2:
    ##Repack the scrolling area for the stimuli.
    stimTitle.pack()
    stimScrollingArea[0].pack(expand=1, fill=BOTH)     
   
    ##Set new page by unpacking addAgent button and the scrolling area for the agents.
    agentScrollingArea[0].pack_forget()
    addAgent.pack_forget()
    agentTitle.pack_forget()
    ##Unpack the previous button since it it not necessary on page 1.
    prevButton.pack_forget()
    

    ##Pack buttons for stimuli and frame to specify number of stimuli.
    stimFrame.pack(side = BOTTOM, anchor = S, expand = True, pady = 50)

    addStim.pack(in_=buttonsFrame, side = LEFT)

  """PAGE 3 to PAGE 2.""" 
  if pageNum == 3: ##Only True when one agent only.
    ##Repack the agent scrolling area and the add agent button.
    agentTitle.pack()
    agentScrollingArea[0].pack(expand = 1, fill = BOTH, pady = (0, 80))
    addAgent.pack(in_=buttonsFrame, side = TOP)
    
    ##Checking which widgets to unpack from the window.
    if (allRadioButtons[0][2].get() == 'Rows'): ##Radio button was on rowsCBS.
      ##Forget the scrolling area for the CBS.
      allConcreteScrollingArea[0][0].pack_forget()
      
    else:##Radio button was on boxCBS.
      ##Forget the text box frame.
      allTextBoxCBSFrame[0].pack_forget()
   
    ##Forget the title and radio button frame regardless of which radio button was pressed.
    editTitle.pack_forget()
    allAgentCBS[0].pack_forget()      
    allFormatCBS[0].pack_forget()
  
  stayOnPage = False ##Boolean variable to check if any pop-ups are open.
  
  """PAGE 4 to PAGE 3."""
  if pageNum == 4:
    if moreThanOneAgent: ##Back to page 2 if True, not page 3.
      
      for button in allEditButtons:
        if button[0].cget("state") == DISABLED: ##If the button is disabled, then that means a pop-up is open.
          if stayOnPage == False:
            stayOnPage = True
      
      if stayOnPage == True:
        ##Deliver a pop-up to the user to warn of closing the pop-ups first.
        dont_go_back(main, return_arrow)
        
        pageNum += 1
      
      else:  
        print('well...do what you gotta do') ##Easter egg.
        editScrollingArea[0].pack_forget() 
        editTitle.pack_forget()
        ##Repack the agent scrolling area and the add agent button.       
        agentScrollingArea[0].pack(expand = 1, fill = BOTH, pady = (0, 80))  
        addAgent.pack(in_=buttonsFrame, side = TOP)      
        
        pageNum -= 1
    
    else: ##One agent only.
      ##Forget scrolling areas and frames for the tables.
      allCircleScrollingArea[0][0].pack_forget()
      allLambdaScrollingArea[0][0].pack_forget()
 
      allCircleGridFrame[0].pack_forget()
      allLambdaGridFrame[0].pack_forget()
    
      ##Forget the fillBev and fillN button.
      allFillButtons[0][0].pack_forget()
      allFillButtons[0][1].pack_forget()
      
      editTitle.config(text = "Agent Specifications: Concrete Behaviours") 
   
      ##Pack widgets related to CBS page.
      allAgentCBS[0].pack(side = TOP, anchor = W)  

      if allRadioButtons[0][2].get() == 'Rows': ##User was using rowsCBS.
        allConcreteScrollingArea[0][0].pack(expand = 1, fill = BOTH)
      
      else: ##User was using boxCBS.
        allTextBoxCBSFrame[0].pack()  
      
      ##Pack frame for the radio Buttons
      allFormatCBS[0].pack(side = BOTTOM, anchor = S, expand = True)    

  """PAGE 5 to PAGE 4."""
  if pageNum == 5 and stayOnPage == False: ##stayOnPage must be false in case it was turned True by previous if statement.
    if moreThanOneAgent:
      
      for button in allEditButtons:
        if button[0].cget("state") == DISABLED: ##If the button is disabled, then that means a pop-up is open.
          if stayOnPage == False:
            stayOnPage = True
      
      if stayOnPage == True:
        ##Deliver a pop-up to the user to warn of closing the pop-ups first.
        dont_go_back(main, return_arrow)
        
        pageNum += 1   
      
      else:
        editTitle.config(text = "Agent Specifications")
        ##Iterate through each edit button to change their text and command functions.
        for i in range(len(allEditButtons)):
          allEditButtons[i][0].config(image = edit_icon, command = lambda boxIndex = i:edit_agent_specs(main, allEditButtons, editScrollingArea, allBevDict, stimDict, 
                                                                                                    allFillButtons, agentNames, allCircleTableBoxes, allLambdaTableBoxes, 
                                                                                                    allCircleScrollingArea, allLambdaScrollingArea, allCircleGridFrame, 
                                                                                                    allLambdaGridFrame, allTextBoxCBSFrame, allFormatCBS, allEntriesCBS, 
                                                                                                    allAgentCBS, allAgentWindows, allTextBoxCBS, allRadioButtons, allConcreteScrollingArea, 
                                                                                                    moreThanOneAgent, generatedTables, generatedCBS, boxIndex, 
                                                                                                    allCBSTabContents, allTableTabContents, allCheckLabels, filled_icon))
          allCheckLabels[i].pack(side = RIGHT, anchor = N)
          allEditButtons[i] = allEditButtons[i][0], True ##Change clicked to True for each button.      
          
        ##Repack the next button.
        nextButton.pack(in_=buttonsFrame, side = RIGHT)          
      
    else: ##One agent only.    
      ##Forget text preview box and save button.
      editTitle.config(text = "Agent Specifications: Tables")
      textEntryFrame.pack_forget()
      saveButton.pack_forget()
    
      ##Repack table scrolling areas.
      allCircleScrollingArea[0][0].pack(expand=1, fill = BOTH)   
      allLambdaScrollingArea[0][0].pack(expand=1, fill = BOTH)   
    
      ##Repack table frames.
      allCircleGridFrame[0].pack(side=TOP, anchor = NW) 
      allLambdaGridFrame[0].pack(side=TOP, anchor = SW) 
    
      ##Repack the next button, and the fillBev and fillN buttons.
      allFillButtons[0][0].pack(in_=buttonsFrame, side = LEFT)
      nextButton.pack(in_=buttonsFrame, side = RIGHT) 
      allFillButtons[0][1].pack(in_=buttonsFrame, side = RIGHT)
  
  ##Decrease pageNum every time the previous button is clicked.
  pageNum -= 1

if __name__ == '__main__': ##only start program when running gui.py
  
  """Code related to the main program's window."""
  main = Tk() ##The main window for the program.
  main.title("C2KA GUI") ##Title for the main window.
  main.resizable(width = False, height = False) ##The main window is not resizeable.
  mainStyle = ttk.Style()
  mainStyle.theme_use("clam")
  
  ##Collect screen (monitor) width and height to position the program's main window in the center. 
  screenWidth = main.winfo_screenwidth() 
  screenHeight = main.winfo_screenheight()  
  
  windowSize = int(screenHeight/2.16) ##Dimension of the window is about half that of the screen height.
  
  ##Calculate the center position.
  positionRight = screenWidth/2 - windowSize/2
  positionDown = screenHeight/2 - windowSize/2
  
  ##Set the window size using the geometry() method.
  main.geometry('%dx%d+%d+%d' % (windowSize, windowSize, positionRight, 
                                 positionDown))
  
  """Code to load initial data/widgets in the main window.""" 
  ##Initializing the page number variable.
  pageNum = 1
  
  ##Initialize the stimuli list.
  stimList = []
  
  ##Initializing a list top hold the agent names.
  agentNames = []
  
  ##Initializing the lists to hold the data for each agent.
  agentFrames = {} ##Stores the entry boxes for each agent name and the entry boxes for each agent behaviour.
  agentFrames['agentNames'] = []
  agentFrames['agentBev'] = []  
  
  ##List to hold CBS labels for the agent name.
  allAgentCBS = []
  
  ##List to keep track of Bool variables to check if CBS were generated.
  generatedCBS = []
  
  ##Dictionary containing the values of each radio button for CBS
  allRadioButtons = [] 
  
  ##List to keep track of all CBS scrolling areas.
  allConcreteScrollingArea = []
  
  ##List containing the CBS entry boxes and labels.
  allEntriesCBS = []
  
  ##List containing the CBS textboxes and a list containing the textBox frames.
  allTextBoxCBS = []
  allTextBoxCBSFrame = []
  
  ##List to hold the frame for the CBS radio buttons.
  allFormatCBS = []
  
  ##Initialize lists to hold the fill with behaviour and fill with neutral stimuli buttons and the frames for them.
  allFillButtons = []
  
  allAgentWindows = [] ##Dictionary for all the pop-ups
  allCBSTabContents = {} ##Dictionary for everything inside CBSTab
  allTableTabContents = {} ##Dictionary for everything inside tableTab
  allEditButtons = [] ##Dictionary for all the edit buttons    
  
  ##Bind these to empty lists to allow them to be passed as arguments.
  allCircleScrollingArea = []
  allLambdaScrollingArea = [] 
  
  ##Dictionaries to hold all circle grid frames and lambda grid frames
  allCircleGridFrame = []
  allLambdaGridFrame = []
  
  ##Dictionaries to hold all circle table boxes and lambda table boxes
  allCircleTableBoxes = {}
  allLambdaTableBoxes = {}
  
  ##List to check if the table was generated.
  generatedTables = []
  
  ##List to hold the preview pop-ups for the text files (for multiple agents).
  allPreviewPops = []
   
  allIsGoodCBS = [] 
   
  allIsGoodTable = [] 
  
  allCheckLabels = []
    
  ##Frame to hold the main buttons
  buttonsFrame = Frame(main)
  buttonsFrame.pack(side = BOTTOM, anchor = S, fill = X, pady = (5, 0))
  
  ##Frame for the stim number Label, button and entry box (to specify
  ##a number of stimuli to be generated).
  stimFrame = Frame(main)
  stimFrame.pack(side = BOTTOM, anchor = S, expand = True, pady = 50)
  
  """Pictures and Fonts used for Buttons and Entries"""
  check_mark = PhotoImage(file = "images/check_mark.png")
  right_arrow = PhotoImage(file="images/right_arrow.png")
  left_arrow = PhotoImage(file="images/left_arrow.png")
  return_arrow = PhotoImage(file = "images/return_arrow.png")
  remove_x = PhotoImage(file = "images/remove_x.png")
  edit_icon = PhotoImage(file = "images/edit_icon.png")
  filled_icon = PhotoImage(file = "images/filled_icon.png")
  view_icon = PhotoImage(file = "images/view_icon.png")
  save_icon = PhotoImage(file = "images/save_icon.png")
  incorrect_icon = PhotoImage(file = "images/incorrect_icon.png")
  correct_icon = PhotoImage(file = "images/correct_icon.png")
  entry_font = ('Calibri', 11)

  """Defining Buttons available on each page.""" 
  ##Next Button (will not be available on page 5).
  nextButton = Button(main, command = next_page, image = right_arrow, width = int(screenWidth/76.8), height = int(screenWidth/76.8), border = 0, highlightthickness = 0)
  nextButton.pack(in_=buttonsFrame, side = RIGHT, anchor = E)

  ##Prev Button (will not be availible on page 1).
  prevButton = Button(main, command = prev_page, image = left_arrow, width = int(screenWidth/76.8), height = int(screenWidth/76.8), border = 0, highlightthickness = 0)
  
  """Label and Buttons exclusive to page 1."""  
  
  ##Title for the stimuli on page 1.
  stimTitle = Label(main, text='Please Enter The Stimuli', font = 'Calibri')
  stimTitle.pack(side = TOP, padx = (0, int(screenWidth/240)))
  
  ##The scrolling area is at index zero of the stimScrollingArea list, this way, 
  ##the scrolling area can be passed by reference and be modified by other functions.
  stimScrollingArea = [vertSuperscroll.Scrolling_Area(main)]
  stimScrollingArea[0].pack(expand = 1, fill = BOTH)


  
  ##Label, button and entry box to generate specified number of stimuli.
  enterStimLabel = Label(main, text = 'Enter # of stimuli : ', font = "Calibri")
  enterStimLabel.pack(in_=stimFrame, side = LEFT)
  
  enterStimButton = Button(main, image = check_mark, border = 0, width = int(screenWidth/76.8), height = int(screenWidth/76.8), 
                           command = lambda: specify_stim(main, stimList, enterStimBox.get(), stimScrollingArea, remove_x, return_arrow), 
                           highlightthickness = 0)
  enterStimButton.pack(in_=stimFrame, side = RIGHT, anchor = N)
  
  enterStimBox = ttk.Entry(main, font = entry_font)
  enterStimBox.pack(in_=stimFrame, side = TOP, padx = (0, 10))
  
  ##Add stimulus entry Button.
  addStim = Button(main, text = 'Add new stimulus', 
                   command = lambda: add_stim(main, stimList, stimScrollingArea, remove_x), 
                   width = int(screenWidth/83.47826), highlightthickness = 0)
  
  addStim.pack(in_=buttonsFrame, side = LEFT)
  
  """Labels and Entries exclusive for page 2.""" 
  ##The scrolling area is at index zero of the bevScrollingArea list, this way, 
  ##the scrolling area can be passed by reference and be modified by other functions.
  agentScrollingArea = [vertSuperscroll.Scrolling_Area(main)]
  
  ##Add agent entry Button.
  addAgent = Button(main, text = 'Add new agent',
                   command = lambda: add_agent(main, agentFrames, agentScrollingArea, remove_x), 
                   width = 23, highlightthickness = 0)  
  
  ##Make a title for the frame.
  agentTitle = Label(main, text='Please Enter The Agents', font = "Calibri")

  
  """Scrolling area for the edit page of multiple agents."""
  editScrollingArea = [vertSuperscroll.Scrolling_Area(main)]
  
  ##Make a title for the frame.
  editTitle = Label(main, text='Agent Specifications', font = "Calibri")

  
  """Loop the main window."""
  main.mainloop()