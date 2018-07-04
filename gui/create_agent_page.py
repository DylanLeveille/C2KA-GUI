"""Imported modules."""
from tkinter import * ##Import the tkinter module to allow construction of the GUI interface.
from create_table import * ##Functions that create or recreate the tables for each agent.
from entry_mods import * ##Functions that modify user entries.
from check_if_good import * ##Functions which validate most of the data in the program.
from CBS_mods import * ##Function to modify the concrte behaviours based on user changes. 
from CBS_radio import * ##Function to set the correct layout for the CBS based on which radio button the user is on.
from set_data import * ##Functions to set the CBS and table data for the agents.
import vertSuperscroll ##Module containing the widget allowing a vertical scrollbar.
import superscroll ##Module containing the widget allowing a vertical and horizontal scrollbar.

"""Functions that work with the multiple agents page."""
##Creates the agent page. 
def create_agent_page(main, allEditButtons, allCheckLabels, allAgentWindows, editScrollingArea, allBevDict, 
                      stimDict, allFillButtons, oldAgentNames, agentNames, allCircleTableBoxes, 
                      allLambdaTableBoxes, allCircleScrollingArea, allLambdaScrollingArea, 
                      allCircleGridFrame, allLambdaGridFrame, allTextBoxCBSFrame, 
                      allFormatCBS,allEntriesCBS, allAgentCBS, allTextBoxCBS, 
                      allRadioButtons, allConcreteScrollingArea, moreThanOneAgent, 
                      generatedTables, generatedCBS, edit_icon, filled_icon):
  """ 
  
    Creates the multiple agents page.
  
  """      
  ##Create a temporary scrolling area so as to not delete the previous one immediately.
  editScrollingAreaTemp = superscroll.Scrolling_Area(main)
  editScrollingAreaTemp.pack(expand = 1, fill=BOTH, pady = (0, 80))

  ##Iterate through the agents to create a frame to hold their name labels, completion status labels and edit buttons.
  for i in range(len(agentNames)):
    editFrame = Frame(editScrollingAreaTemp.innerframe, pady = 20, highlightbackground = "black", highlightcolor = "black", highlightthickness = 1)
    editLabel = Label(editFrame, text = agentNames[i], justify = LEFT, font = ("Times", 16), padx = 15)
    completeLabel = Label(editFrame, padx = 15)
    editButton = Button(editFrame, image = edit_icon, border = 0, highlightthickness = 0,
                        command = lambda boxIndex=i: edit_agent_specs(main, allEditButtons, editScrollingArea, allBevDict, stimDict, 
                                                                      allFillButtons, agentNames, allCircleTableBoxes, allLambdaTableBoxes, 
                                                                      allCircleScrollingArea, allLambdaScrollingArea, allCircleGridFrame, 
                                                                      allLambdaGridFrame, allTextBoxCBSFrame, allFormatCBS, 
                                                                      allEntriesCBS, allAgentCBS, allAgentWindows, allTextBoxCBS, allRadioButtons,
                                                                      allConcreteScrollingArea, moreThanOneAgent, generatedTables, generatedCBS, 
                                                                      boxIndex, allCheckLabels, filled_icon)) 
    
    ##Assigning the new button to the list.
    allEditButtons[i] = editButton, allEditButtons[i][1]

    if allEditButtons[i][1] == True: ##If True, that means the agent was already existant.
      completeLabel.config(image = allCheckLabels[i].cget("image")) ##Put in the image that was there previously.
    
    ##New status label is saved in memory.       
    allCheckLabels[i] = completeLabel
    
    ##Pack new labels, buttons and scrolling area.
    editLabel.pack(side = LEFT, anchor = N)
    editButton.pack(side = RIGHT, anchor = N, padx = 20)
    completeLabel.pack(side = RIGHT, anchor = N)
    editFrame.pack(anchor = W, fill = X)
    editScrollingArea[0] = editScrollingAreaTemp ##By garbage collection, if there was an old scrolling area present, it no longer exists.

##Function to allow editting of each agent.    
def edit_agent_specs(main, allEditButtons, editScrollingArea, allBevDict, stimDict, 
                     allFillButtons, agentNames, allCircleTableBoxes, allLambdaTableBoxes, 
                     allCircleScrollingArea, allLambdaScrollingArea, allCircleGridFrame, 
                     allLambdaGridFrame, allTextBoxCBSFrame, allFormatCBS, allEntriesCBS, 
                     allAgentCBS, allAgentWindows, allTextBoxCBS, allRadioButtons, 
                     allConcreteScrollingArea, moreThanOneAgent, generatedTables,
                     generatedCBS, boxIndex, allCheckLabels, filled_icon):
  """ 
  
    Function called when the user whishes to edit an agent.
    Allows the creation of a pop-up window to edit the 
    desired agent.
  
  """              
  ##Disable the edit button on the multiple agent page so that it cannot be clicked twice.
  allEditButtons[boxIndex][0].config(state = DISABLED)
  
  if generatedCBS[boxIndex] == False: ##This means not only that the pop-up isn't generated, but the CBS and tables as well. 
    editAgent = Toplevel() ##Creating new window to edit agent specs
    editAgent.resizable(width = False, height = False) 
    allAgentWindows[boxIndex] = editAgent ##Store specific frame according to index.
    
    ##Collect screen (monitor) width and height to position the window in the center. 
    screenWidth = editAgent.winfo_screenwidth() 
    screenHeight = editAgent.winfo_screenheight()       
    
    windowSize = int(screenHeight/2.16) ##Dimension of the window is about half that of the screen height.
    
    editAgent.geometry('%dx%d' % (windowSize, windowSize))

    editAgent.protocol("WM_DELETE_WINDOW", lambda: close_edit(boxIndex, allEditButtons, allAgentWindows, allCheckLabels, filled_icon)) ##Give a command to the X button of the window.
    
    editButtonsFrame = Frame(editAgent) ##Frame to hold the done button.
    
    saveButton = Button(editButtonsFrame, text = "Done", command = lambda: close_edit(boxIndex, allEditButtons, allAgentWindows, allCheckLabels, filled_icon), highlightthickness = 0) ##Button to close the agent when done.

    ##Pack the done button and frame to hold it.
    saveButton.pack(side = RIGHT, anchor = S)
    editButtonsFrame.pack(side = BOTTOM, fill = X)
    
    editTabs = ttk.Notebook(editAgent) ##Create Tabs to switch from CBS to tables.
    CBSTab = Frame(editTabs)
    tableTab = Frame(editTabs)
    
    ##Add tabs to frame
    editTabs.add(CBSTab, text = "Concrete Behaviours")
    editTabs.add(tableTab, text = "Tables") 
    
    ##Pack the tabs.
    editTabs.pack(expand = 1, fill = BOTH)    
    
    ##Set True to allEditButtons to indicate that it was clicked.
    allEditButtons[boxIndex] = allEditButtons[boxIndex][0], True
    
  else:
    ##Extract the agent window and tab info that was created for it previously.
    editAgent = allAgentWindows[boxIndex]
    editAgent.deiconify()
    editAgent.protocol("WM_DELETE_WINDOW", lambda: close_edit(boxIndex, allEditButtons, allAgentWindows, allCheckLabels, filled_icon))
    
    allAgentWindows[boxIndex].winfo_children()[0].winfo_children()[0].config(command = lambda: close_edit(boxIndex, allEditButtons, allAgentWindows, allCheckLabels, filled_icon))
    
    CBSTab = allAgentWindows[boxIndex].winfo_children()[1].winfo_children()[0]
    tableTab = allAgentWindows[boxIndex].winfo_children()[1].winfo_children()[1]

  ##Modify data for the CBS for the agent.
  set_CBS_data(CBSTab, agentNames, allBevDict, allAgentCBS, allTextBoxCBSFrame, 
               allFormatCBS, allRadioButtons, 
               allConcreteScrollingArea, allEntriesCBS, allTextBoxCBS, 
               generatedCBS, moreThanOneAgent, boxIndex)
  
  ##Modify data for the table for the agent.
  set_table_data(tableTab, allBevDict, stimDict, allFillButtons, allCircleTableBoxes, 
                 allLambdaTableBoxes, allCircleScrollingArea, 
                 allLambdaScrollingArea, allCircleGridFrame, allLambdaGridFrame, 
                 generatedTables, moreThanOneAgent, boxIndex)  

##Function to close the edit page.
def close_edit(boxIndex, allEditButtons, allAgentWindows, allCheckLabels, filled_icon):
  """ (int, list, list, list, image) -> (none)
    
    Hides the editAgent window without destroying it. 
  
  """
  allAgentWindows[boxIndex].withdraw()
  allCheckLabels[boxIndex].config(image = filled_icon)
  allEditButtons[boxIndex][0].config(state = NORMAL)