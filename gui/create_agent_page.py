from tkinter import *
import superscroll
import vertSuperscroll ##Module containing the widget allowing a vertical scrollbar.
from create_table import *
from entry_mods import *
from check_if_good import *
from CBS_mods import *
from CBS_radio import *
from set_data import *


def create_agent_page(main, allButtons, allFrames, editScrollingArea, allBevDict, stimDict, allFillButtons, agentNames, allCircleTableBoxes, allLambdaTableBoxes, allCircleScrollingArea, allLambdaScrollingArea, allCircleGridFrame, allLambdaGridFrame, allTextBoxCBSFrame, allTitleCBS, allFormatCBS,allEntriesCBS, allAgentCBS, allTextBoxCBS, allRadioButtons, allConcreteScrollingArea, moreThanOneAgent, generatedTables, generatedCBS, allCBSTabContents, allTableTabContents):
    editScrollingAreaTemp = vertSuperscroll.Scrolling_Area(main)
    editScrollingAreaTemp.pack(expand = 1, fill=BOTH)

    
    for i in range(len(agentNames)):
        editFrame = Frame(editScrollingAreaTemp.innerframe)
        editLabel = Label(editFrame, text = agentNames[i])
        #completeLabel = Label(editFrame, image = complete_icon)
        editButton = Button(editFrame, text = 'Edit', border = 1, 
                                  command = lambda boxIndex=i: edit_agent_specs(main, allButtons, editScrollingArea, allBevDict, stimDict, allFillButtons, agentNames, allCircleTableBoxes, allLambdaTableBoxes, allCircleScrollingArea, allLambdaScrollingArea, allCircleGridFrame, allLambdaGridFrame, allTextBoxCBSFrame, allTitleCBS, allFormatCBS, allEntriesCBS, allAgentCBS, allFrames, allTextBoxCBS, allRadioButtons, allConcreteScrollingArea, moreThanOneAgent, generatedTables, generatedCBS, boxIndex, allCBSTabContents, allTableTabContents)) #generated booleans will always be false first time...use data structure and set them to false before calling.

        allButtons[i] = editButton
        editLabel.pack(side = LEFT, anchor = N)
        editButton.pack(anchor = N)
        #completeLabel.pack(side = RIGHT, anchor = N)
        editFrame.pack(anchor = W)
        
        editScrollingArea[0] = editScrollingAreaTemp         


def edit_agent_specs(main, allButtons, editScrollingArea, allBevDict, stimDict, allFillButtons, agentNames, allCircleTableBoxes, allLambdaTableBoxes, allCircleScrollingArea, allLambdaScrollingArea, allCircleGridFrame, allLambdaGridFrame, allTextBoxCBSFrame, allTitleCBS, allFormatCBS,allEntriesCBS, allAgentCBS, allFrames, allTextBoxCBS, allRadioButtons, allConcreteScrollingArea, moreThanOneAgent, generatedTables, generatedCBS, boxIndex, allCBSTabContents, allTableTabContents):
    global editAgent
    if generatedCBS[boxIndex] == False:
        editAgent = Toplevel() ##Creating new window to edit agent specs
        allFrames[boxIndex] = editAgent ##Store specific frame according to index
    
        editAgent.geometry('500x500')
        
        allButtons[boxIndex].config(state = DISABLED)
        
        editButtonsFrame = Frame(editAgent) ##Making the save and cancel buttons
        saveButton = Button(editButtonsFrame, text = "Done", command = lambda boxIndex=boxIndex: close_edit(main, boxIndex, allButtons, allFrames, allCircleTableBoxes))
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
    else:
        editAgent = allFrames[boxIndex]
        CBSTab = allFrames[boxIndex].winfo_children()[1].winfo_children()[0]
        tableTab = allFrames[boxIndex].winfo_children()[1].winfo_children()[1]
    

    
    
    """CBS Editing"""
    
    set_CBS_data(CBSTab, agentNames, allBevDict, allAgentCBS, allTextBoxCBSFrame, allFrames, allTitleCBS, allFormatCBS, allRadioButtons, 
                 allConcreteScrollingArea, allEntriesCBS, allTextBoxCBS, generatedCBS, moreThanOneAgent, boxIndex, allCBSTabContents)
    
    
    """Table Editing"""
    
    set_table_data(tableTab, allBevDict, stimDict, allFillButtons, allCircleTableBoxes, 
                   allLambdaTableBoxes, allCircleScrollingArea, 
                   allLambdaScrollingArea, allCircleGridFrame, allLambdaGridFrame, 
                   generatedTables, moreThanOneAgent, boxIndex, allTableTabContents)
        
             
def close_edit(main, boxIndex, allButtons, allFrames, allCircleTableBoxes):
    """ (tkinter.Tk) -> (none)
      
      Destroys the editAgent window 
    
    """     
    allFrames[boxIndex].withdraw()
    
    contents = allFrames[boxIndex].winfo_children()
    print(contents[1].winfo_children())
    allButtons[boxIndex].config(state = NORMAL)
