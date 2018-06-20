from tkinter import *
import superscroll
import vertSuperscroll ##Module containing the widget allowing a vertical scrollbar.
from create_table import *
from entry_mods import *
from check_if_good import *
from CBS_mods import *
from CBS_radio import *
from set_data import *


def create_agent_page(main, editScrollingArea, allBevDict, stimDict, agentNames, allCircleTableBoxes, allLambdaTableBoxes, allCircleScrollingArea, allLambdaScrollingArea, allCircleGridFrame, allLambdaGridFrame, allEntriesCBS, allAgentCBS, allTextBoxCBS, allRadioButtons, allConcreteScrollingArea, moreThanOneAgent, generatedTables, generatedCBS):
    editScrollingAreaTemp = vertSuperscroll.Scrolling_Area(main)
    editScrollingAreaTemp.pack(expand = 1, fill=BOTH)
    global allFrames
    global allButtons
    allFrames = {} ##Dictionary for all the pop-ups
    allButtons = {} ##Dictionary for all the edit buttons
    
    for i in range(len(agentNames)):
        editFrame = Frame(editScrollingAreaTemp.innerframe)
        editLabel = Label(editFrame, text = agentNames[i])
        #completeLabel = Label(editFrame, image = complete_icon)
        editButton = Button(editFrame, text = 'Edit', border = 1, 
                                  command = lambda boxIndex=i: edit_agent_specs(main, editScrollingArea, allBevDict, stimDict, agentNames, allCircleTableBoxes, allLambdaTableBoxes, allCircleScrollingArea, allLambdaScrollingArea, allCircleGridFrame, allLambdaGridFrame, allEntriesCBS, allAgentCBS, allTextBoxCBS, allRadioButtons, allConcreteScrollingArea, moreThanOneAgent, generatedTables, generatedCBS, boxIndex)) #generated booleans will always be false first time...use data structure and set them to false before calling.

        allButtons[i] = editButton
        editLabel.pack(side = LEFT, anchor = N)
        editButton.pack(anchor = N)
        #completeLabel.pack(side = RIGHT, anchor = N)
        editFrame.pack(anchor = W)


def edit_agent_specs(main, editScrollingArea, allBevDict, stimDict, agentNames, allCircleTableBoxes, allLambdaTableBoxes, allCircleScrollingArea, allLambdaScrollingArea, allCircleGridFrame, allLambdaGridFrame, allEntriesCBS, allAgentCBS, allTextBoxCBS, allRadioButtons, allConcreteScrollingArea, moreThanOneAgent, generatedTables, generatedCBS, boxIndex):
    global editAgent
    editAgent = Toplevel() ##Creating new window to edit agent specs
    editAgent.geometry('500x500')
    
    
    allFrames[boxIndex] = editAgent ##Store specific frame according to index
    
    allButtons[boxIndex].config(state = DISABLED)
    
    editButtonsFrame = Frame(editAgent) ##Making the save and cancel buttons
    saveButton = Button(editButtonsFrame, text = "Done", command = lambda boxIndex=boxIndex: close_edit(main, boxIndex, allEntriesCBS))
    saveButton.pack(side = RIGHT, anchor = S)
    cancelButton = Button(editButtonsFrame, text = "Clear")
    cancelButton.pack(side = LEFT, anchor = S)
    editButtonsFrame.pack(side = BOTTOM, fill = X)
    
    editTabs = ttk.Notebook(editAgent) ##Create Tabs to switch from tables to CBS
    CBSTab = Frame(editTabs)
    tableTab = Frame(editTabs)
    
    ##Add tabs to frame
    editTabs.add(CBSTab)
    editTabs.add(tableTab) 
    
    editTabs.pack(expand = 1, fill = BOTH)
    
    
    """CBS Editing"""
    
    set_CBS_data(CBSTab, agentNames, allBevDict, allAgentCBS, allRadioButtons, 
                 allConcreteScrollingArea, allEntriesCBS, allTextBoxCBS, generatedCBS, moreThanOneAgent, boxIndex)
    
    
    """Table Editing"""
    
    set_table_data(tableTab, allBevDict, stimDict, allCircleTableBoxes, 
                   allLambdaTableBoxes, allCircleScrollingArea, 
                   allLambdaScrollingArea, allCircleGridFrame, allLambdaGridFrame, 
                   generatedTables, boxIndex)
        
             
def close_edit(main, boxIndex, allEntriesCBS):
    """ (tkinter.Tk) -> (none)
      
      Destroys the editAgent window 
    
    """     
    allFrames[boxIndex].destroy()
    del allFrames[boxIndex]
    
    allButtons[boxIndex].config(state = NORMAL)
    print(allEntriesCBS)