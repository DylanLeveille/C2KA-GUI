""" Internship Project.

GUI to Assist the C2KA TOOL.
"""

"""Imported modules."""
from tkinter import * ##Import the tkinter module to allow construction of the GUI interface.
from check_if_good import * ##Functions which validate most of the data in the program.
from entry_mods import * ##Functions which modify entry boxes.
from get_word_list import * ##Functions which parse an entry box and returns lists of words.
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
  
  global allTitleCBS
  global allFormatCBS
  
  global allFillButtons
  
  global allAgentWindows
  global allCBSTabContents
  global allTableTabContents
  global allEditButtons
  
  global allCircleTableBoxes ##Dict to hold entry boxes and labels of circle table for all agents.
  global allLambdaTableBoxes ##Dict to hold entry boxes and labels of lambda table for all agents.
  
 # global circleTableValues ##Dict to hold values from circle table.   #Might not need this...
 # global lambdaTableValues ##Dict to hold values from lambda table.   #Might not need this...
  
  global allCircleScrollingArea ##Scrolling area for circle table.
  global allLambdaScrollingArea ##Scrolling area for lambda table.
  
  global allCircleGridFrame ##Global frame for the circle table.
  global allLambdaGridFrame ##Global frame for the lambda table.
  
  global moreThanOneAgent ##Boolean to keep track of if there is more than one agent inputted.
  
 # global wrongAgents ##Count for the number of incorrect agents (only if multiple)
  
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
      ##Set new page by unpacking widgets on page 1.
      stimScrollingArea[0].pack_forget()
      addStim.pack_forget()
      stimFrame.pack_forget()
      
      ##Pack the new previous button.
      prevButton.pack(in_=buttonsFrame, side = LEFT, anchor = S)
      
      ##Pack new scrolling area for the agent and its behaviours,
      ##and pack the button to add an agent.
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
      ##the agents' behaviour (used when create the text file).
      agentBehaviours = extract_full_behaviour(agentFrames['agentBev'])
      
      ##Set new page by unpacking scrolling area on page 2 and the add agent button.
      agentScrollingArea[0].pack_forget()      
      addAgent.pack_forget()
      
      ##A swap list to hold agents that may need swapping.
      swapList = []
      
      ##Keep track of agents deleted.
      agentsDeleted = 0
      ##Remove generated tables and CBS based on if agents were removed. Since we used lists, the indices will shift automatically.
      for i in range(len(oldAgentNames)):
        if oldAgentNames[i] not in agentNames: ##Checks if any agents were removed.
          
          if allEditButtons[i - agentsDeleted][1] == True: ##Means dictionaries were made for that agent.
            del allCircleTableBoxes[i - agentsDeleted + 1]
            del allLambdaTableBoxes[i - agentsDeleted + 1]          
          
          del allAgentCBS[i - agentsDeleted]
          del allTitleCBS[i - agentsDeleted]
          del allFormatCBS[i - agentsDeleted]     
          del allRadioButtons[i - agentsDeleted]
          del allTextBoxCBSFrame[i - agentsDeleted]
          del allTextBoxCBS[i - agentsDeleted]
          del allConcreteScrollingArea[i - agentsDeleted]      
          del allEntriesCBS[i - agentsDeleted]      
          del allFillButtons[i - agentsDeleted]
          del allCircleScrollingArea[i - agentsDeleted] 
          del allCircleGridFrame[i - agentsDeleted]
          del allLambdaScrollingArea[i - agentsDeleted] 
          del allLambdaGridFrame[i - agentsDeleted] 
          del generatedCBS[i - agentsDeleted] 
          del generatedTables[i - agentsDeleted]          
          del allIsGoodCBS[i - agentsDeleted]
          del allIsGoodTable[i - agentsDeleted]
          del allCheckLabels[i - agentsDeleted]
          del allPreviewPops[i - agentsDeleted]  
          del allEditButtons[i - agentsDeleted]
          del allAgentWindows[i - agentsDeleted]          
          
          for j in range(i - agentsDeleted + 1, len(oldAgentNames) - agentsDeleted): ##Shift all the keys down by 1.
            key = j + 1
            if key in allCircleTableBoxes.keys():
              allCircleTableBoxes[key - 1] = allCircleTableBoxes[key]
              del allCircleTableBoxes[key]
              
              allLambdaTableBoxes[key - 1] = allLambdaTableBoxes[key]
              del allLambdaTableBoxes[key]              
              
          agentsDeleted += 1
        
        else: ##The agent is still present (but may be shifted).
          swapList.append(oldAgentNames[i])
      
      ##Set False to the tables generated based on if new agents were added.
      for i in range(len(oldAgentNames) - agentsDeleted, len(agentNames)):
        generatedCBS.append(False)
        generatedTables.append(False)    
        
        ##Append None to create a new size to each of the lists.
        allEditButtons.append((None, False))
        allAgentWindows.append(None)
        
        allTitleCBS.append(None)
        allFormatCBS.append(None)        
        allRadioButtons.append(None)
        allConcreteScrollingArea.append(None)   
        allEntriesCBS.append(None)    
        allTextBoxCBSFrame.append(None)
        allTextBoxCBS.append(None) 
        allAgentCBS.append(None) 
        allFillButtons.append((None, None, buttonsFrame))
        allCircleScrollingArea.append(None)
        allLambdaScrollingArea.append(None)
        allCircleGridFrame.append(None) 
        allLambdaGridFrame.append(None) 
        allIsGoodCBS.append(True) 
        allIsGoodTable.append(True)
        allCheckLabels.append(None)
        allPreviewPops.append(None)
      
      for i in range(len(swapList)):
        if swapList[i] != agentNames[i]: ##Means some agents have swapped places. We do not swap if it was already done.   
          ##Find position of where the agent name belongs.
          for j in range(i + 1, len(agentNames)): ##Postion to switch found if True.
            if agentNames[j] == swapList[i]:
              indexSwitch = j 
              
          ##Begin to switch the data for the dictionaries. If none of the agents had dictionaries, then there is no dictionary to shift.
          if allEditButtons[i][1] == True and allEditButtons[indexSwitch][1] == True: ##Both agents had keys associated with them.
            allCircleTableBoxes[i + 1], allCircleTableBoxes[indexSwitch + 1] = allCircleTableBoxes[indexSwitch + 1], allCircleTableBoxes[i + 1]
            allLambdaTableBoxes[i + 1], allLambdaTableBoxes[indexSwitch + 1] = allLambdaTableBoxes[indexSwitch + 1], allLambdaTableBoxes[i+ 1]
          
          elif allEditButtons[i][1] == True: ##Only one agent had a key associated with them (first one).
            allCircleTableBoxes[indexSwitch + 1] = allCircleTableBoxes[i  + 1]
            allLambdaTableBoxes[indexSwitch + 1] = allLambdaTableBoxes[i  + 1]
            
            del allCircleTableBoxes[i  + 1]
            del allLambdaTableBoxes[i  + 1]
          
          elif allEditButtons[indexSwitch][1] == True: ##Only one agent had a key associated with them (second one).
            allCircleTableBoxes[i  + 1] = allCircleTableBoxes[indexSwitch + 1]
            allLambdaTableBoxes[i  + 1] = allLambdaTableBoxes[indexSwitch + 1] 
            
            del allCircleTableBoxes[indexSwitch + 1]
            del allLambdaTableBoxes[indexSwitch + 1] 
    
          ##Switch all the remaining data (lists) using tupple assignment.
          allAgentCBS[i], allAgentCBS[indexSwitch] = allAgentCBS[indexSwitch], allAgentCBS[i]
          allTitleCBS[i], allTitleCBS[indexSwitch] = allTitleCBS[indexSwitch], allTitleCBS[i]
          
          allFormatCBS[i], allFormatCBS[indexSwitch] = allFormatCBS[indexSwitch], allFormatCBS[i]
          allRadioButtons[i], allRadioButtons[indexSwitch] = allRadioButtons[indexSwitch], allRadioButtons[i]
          
          allTextBoxCBSFrame[i], allTextBoxCBSFrame[indexSwitch] = allTextBoxCBSFrame[indexSwitch], allTextBoxCBSFrame[i]
          allTextBoxCBS[i], allTextBoxCBS[indexSwitch] = allTextBoxCBS[indexSwitch], allTextBoxCBS[i]
          
          allConcreteScrollingArea[i], allConcreteScrollingArea[indexSwitch] = allConcreteScrollingArea[indexSwitch], allConcreteScrollingArea[i]      
          allEntriesCBS[i], allEntriesCBS[indexSwitch] = allEntriesCBS[indexSwitch], allEntriesCBS[i]    
          
          allFillButtons[i], allFillButtons[indexSwitch] = allFillButtons[indexSwitch], allFillButtons[i]
          
          allCircleScrollingArea[i], allCircleScrollingArea[indexSwitch] = allCircleScrollingArea[indexSwitch], allCircleScrollingArea[i]
          allCircleGridFrame[i], allCircleGridFrame[indexSwitch] = allCircleGridFrame[indexSwitch], allCircleGridFrame[i]
          
          allLambdaScrollingArea[i], allLambdaScrollingArea[indexSwitch] = allLambdaScrollingArea[indexSwitch], allLambdaScrollingArea[i]
          allLambdaGridFrame[i], allLambdaGridFrame[indexSwitch] = allLambdaGridFrame[indexSwitch], allLambdaGridFrame[i]
          
          generatedCBS[i], generatedCBS[indexSwitch] = generatedCBS[indexSwitch], generatedCBS[i] 
          generatedTables[i], generatedTables[indexSwitch] = generatedTables[indexSwitch], generatedTables[i]  
          
          allIsGoodCBS[i], allIsGoodCBS[indexSwitch] = allIsGoodCBS[indexSwitch], allIsGoodCBS[i]
          allIsGoodTable[i], allIsGoodTable[indexSwitch] = allIsGoodTable[indexSwitch], allIsGoodTable[i]
          
          allCheckLabels[i], allCheckLabels[indexSwitch] = allCheckLabels[indexSwitch], allCheckLabels[i]   
          
          allEditButtons[i], allEditButtons[indexSwitch] = allEditButtons[indexSwitch], allEditButtons[i]
          allAgentWindows[i], allAgentWindows[indexSwitch] = allAgentWindows[indexSwitch], allAgentWindows[i]           
          
          allPreviewPops[i], allPreviewPops[indexSwitch] = allPreviewPops[indexSwitch], allPreviewPops[i]
          
      if len(agentFrames['agentNames']) > 1: ##More than one agent calls for a different layout.
        moreThanOneAgent = True        
        
        if len(oldAgentNames) == 1 and oldAgentNames[0] in agentNames: ##If agent was single but now multiple, we need to remake the UI for that agent in the multiple agent page.
          newIndex = agentNames.index(oldAgentNames[0])
          generatedTables[newIndex] = False
          generatedCBS[newIndex] = False
          
        
        ##Special UI when more than one agent is entered.
        create_agent_page(main, allEditButtons, allCheckLabels, allAgentWindows, editScrollingArea, allBevDict, stimDict, allFillButtons, agentNames, allCircleTableBoxes, 
                          allLambdaTableBoxes, allCircleScrollingArea, allLambdaScrollingArea, allCircleGridFrame, allLambdaGridFrame, allTextBoxCBSFrame, 
                          allTitleCBS, allFormatCBS, allEntriesCBS, allAgentCBS, allTextBoxCBS, allRadioButtons, allConcreteScrollingArea, moreThanOneAgent, 
                          generatedTables, generatedCBS, allCBSTabContents, allTableTabContents, edit_icon, filled_icon) 
        
        pageNum += 1 ##Add one to pageNum because we are skipping page 4.

      else: ##Only one agent.            
        moreThanOneAgent = False
     
        if len(oldAgentNames) > 1 and agentNames[0] in oldAgentNames: ##If agent was in multiple agents but now single, we need to remake the UI for that agent in the single agent page.
          generatedTables[0] = False
          generatedCBS[0] = False        
          allFillButtons[0] = (None, None, buttonsFrame)

        set_CBS_data(main, agentNames, allBevDict, allAgentCBS, allTextBoxCBSFrame, allAgentWindows,  
                     allTitleCBS, allFormatCBS, allRadioButtons, allConcreteScrollingArea, 
                     allEntriesCBS, allTextBoxCBS, generatedCBS, moreThanOneAgent, 0, allCBSTabContents)
        
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
      allTitleCBS[0].pack_forget()
      allAgentCBS[0].pack_forget()
      allFormatCBS[0].pack_forget()

      set_table_data(main, allBevDict, stimDict, allFillButtons, allCircleTableBoxes,
                     allLambdaTableBoxes, allCircleScrollingArea, allLambdaScrollingArea, 
                     allCircleGridFrame, allLambdaGridFrame, generatedTables, 
                     moreThanOneAgent, 0, allTableTabContents)
    
  """PAGE 4 to PAGE 5."""
  if pageNum == 4:
    
    ##Create dictionaries to hold the values from tables.
    allCircleTableValues = get_empty_dict()
    allLambdaTableValues = get_empty_dict()
    isPageGood = True 
    wrongAgents = 0
    
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
    stimScrollingArea[0].pack(expand=1, fill=BOTH)     
   
    ##Set new page by unpacking addAgent button and the scrolling area for the agents.
    agentScrollingArea[0].pack_forget()
    addAgent.pack_forget()
    
    ##Unpack the previous button since it it not necessary on page 1.
    prevButton.pack_forget()
    
    ##Pack buttons for stimuli and frame to specify number of stimuli.
    stimFrame.pack(side = BOTTOM, anchor = S, expand = True, pady = 50)

    addStim.pack(in_=buttonsFrame, side = LEFT)

  """PAGE 3 to PAGE 2.""" 
  if pageNum == 3: ##Only True when one agent only.
    ##Repack the agent scrolling area and the add agent button.
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
    allTitleCBS[0].pack_forget()
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
        print('well...do what you gotta do')
        editScrollingArea[0].pack_forget() 

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
   
      ##Pack widgets related to CBS page.
      allTitleCBS[0].pack(side = TOP)
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
        ##Iterate through each edit button to change their text and command functions.
        for i in range(len(allEditButtons)):
          allEditButtons[i][0].config(image = edit_icon, command = lambda boxIndex = i:edit_agent_specs(main, allEditButtons, editScrollingArea, allBevDict, stimDict, 
                                                                                                    allFillButtons, agentNames, allCircleTableBoxes, allLambdaTableBoxes, 
                                                                                                    allCircleScrollingArea, allLambdaScrollingArea, allCircleGridFrame, 
                                                                                                    allLambdaGridFrame, allTextBoxCBSFrame, allTitleCBS, allFormatCBS, allEntriesCBS, 
                                                                                                    allAgentCBS, allAgentWindows, allTextBoxCBS, allRadioButtons, allConcreteScrollingArea, 
                                                                                                    moreThanOneAgent, generatedTables, generatedCBS, boxIndex, 
                                                                                                    allCBSTabContents, allTableTabContents, allCheckLabels))
          allCheckLabels[i].pack(side = LEFT, anchor = N)
          allEditButtons[i] = allEditButtons[i][0], True ##Change clicked to True for each button.      
          
          ##Repack the next button.
          nextButton.pack(in_=buttonsFrame, side = RIGHT)          
      
    else: ##One agent only.    
      ##Forget text preview box and save button.
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
  
  ##List to hold the labels for the CBS titles.
  allTitleCBS = []
  
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
  entry_font = ('Comic Sans MS', 11)

  """Defining Buttons available on each page.""" 
  ##Next Button (will not be available on page 5).
  nextButton = Button(main, command = next_page, image = right_arrow, width = int(screenWidth/76.8), height = int(screenWidth/76.8), border = 0, highlightthickness = 0)
  nextButton.pack(in_=buttonsFrame, side = RIGHT, anchor = E)

  ##Prev Button (will not be availible on page 1).
  prevButton = Button(main, command = prev_page, image = left_arrow, width = int(screenWidth/76.8), height = int(screenWidth/76.8), border = 0, highlightthickness = 0)
  
  """Label and Buttons exclusive to page 1."""  
  ##The scrolling area is at index zero of the stimScrollingArea list, this way, 
  ##the scrolling area can be passed by reference and be modified by other functions.
  stimScrollingArea = [vertSuperscroll.Scrolling_Area(main)]
  stimScrollingArea[0].pack(expand = 1, fill = BOTH)

  ##Title for the stimuli on page 1.
  stimTitle = Label(stimScrollingArea[0].innerframe, text='Please Enter The Stimuli')
  stimTitle.pack(side = TOP)
  
  ##Label, button and entry box to generate specified number of stimuli.
  enterStimLabel = Label(main, text = 'Enter # of stimuli : ')
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
  agentTitle = Label(agentScrollingArea[0].innerframe, text='Please Enter The Agents')
  agentTitle.pack()
  
  """Scrolling area for the edit page of multiple agents."""
  editScrollingArea = [vertSuperscroll.Scrolling_Area(main)]
  
  ##Make a title for the frame.
  editTitle = Label(editScrollingArea[0].innerframe, text='Please Edit The Agents')  #Not working...
  editTitle.pack()
  
  """Loop the main window."""
  main.mainloop()