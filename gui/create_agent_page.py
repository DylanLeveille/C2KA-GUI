from tkinter import *
import superscroll
import vertSuperscroll ##Module containing the widget allowing a vertical scrollbar.
from create_table import *
from entry_mods import *
from check_if_good import *
from CBS_mods import *
from CBS_radio import *
from set_data import *

def create_agent_page(main, allEditButtons, allFrames, editScrollingArea, allBevDict, 
                      stimDict, allFillButtons, agentNames, allCircleTableBoxes, 
                      allLambdaTableBoxes, allCircleScrollingArea, allLambdaScrollingArea, 
                      allCircleGridFrame, allLambdaGridFrame, allTextBoxCBSFrame, 
                      allTitleCBS, allFormatCBS,allEntriesCBS, allAgentCBS, allTextBoxCBS, 
                      allRadioButtons, allConcreteScrollingArea, moreThanOneAgent, 
                      generatedTables, generatedCBS, allCBSTabContents, allTableTabContents):
    
    editScrollingAreaTemp = vertSuperscroll.Scrolling_Area(main)
    editScrollingAreaTemp.pack(expand = 1, fill=BOTH)

    for i in range(len(agentNames)):
        editFrame = Frame(editScrollingAreaTemp.innerframe)
        editLabel = Label(editFrame, text = agentNames[i])
        #completeLabel = Label(editFrame, image = complete_icon)
        editButton = Button(editFrame, text = 'Edit', border = 1, 
                                  command = lambda boxIndex=i: edit_agent_specs(main, allEditButtons, editScrollingArea, allBevDict, stimDict, 
                                                                                allFillButtons, agentNames, allCircleTableBoxes, allLambdaTableBoxes, 
                                                                                allCircleScrollingArea, allLambdaScrollingArea, allCircleGridFrame, 
                                                                                allLambdaGridFrame, allTextBoxCBSFrame, allTitleCBS, allFormatCBS, 
                                                                                allEntriesCBS, allAgentCBS, allFrames, allTextBoxCBS, allRadioButtons,
                                                                                allConcreteScrollingArea, moreThanOneAgent, generatedTables, generatedCBS, 
                                                                                boxIndex, allCBSTabContents, allTableTabContents)) 


        allEditButtons[i] = editButton, False
        editLabel.pack(side = LEFT, anchor = N)
        editButton.pack(anchor = N)
        #completeLabel.pack(side = RIGHT, anchor = N)
        editFrame.pack(anchor = W)
        
        editScrollingArea[0] = editScrollingAreaTemp  
    

def edit_agent_specs(main, allEditButtons, editScrollingArea, allBevDict, stimDict, 
                     allFillButtons, agentNames, allCircleTableBoxes, allLambdaTableBoxes, 
                     allCircleScrollingArea, allLambdaScrollingArea, allCircleGridFrame, 
                     allLambdaGridFrame, allTextBoxCBSFrame, allTitleCBS, allFormatCBS, allEntriesCBS, 
                     allAgentCBS, allFrames, allTextBoxCBS, allRadioButtons, allConcreteScrollingArea, 
                     moreThanOneAgent, generatedTables, generatedCBS, boxIndex, 
                     allCBSTabContents, allTableTabContents):
    global editAgent      
   
    allEditButtons[boxIndex][0].config(state = DISABLED)
    allEditButtons[boxIndex] = allEditButtons[boxIndex][0], True 
    
    if generatedCBS[boxIndex] == False:
        editAgent = Toplevel() ##Creating new window to edit agent specs
        editAgent.resizable(width = False, height = False) 
        allFrames[boxIndex] = editAgent ##Store specific frame according to index.

        editAgent.protocol("WM_DELETE_WINDOW", lambda: close_edit(boxIndex, allEditButtons, allFrames))
        
        editAgent.geometry('500x500')
        
        
        editButtonsFrame = Frame(editAgent) ##Making the save and cancel button
        
        saveButton = Button(editButtonsFrame, text = "Done", command = lambda: close_edit(boxIndex, allEditButtons, allFrames))

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
        editAgent.protocol("WM_DELETE_WINDOW", lambda boxIndex = boxIndex: close_edit(boxIndex, allEditButtons, allFrames))
        allFrames[boxIndex].winfo_children()[0].winfo_children()[0].config(command = lambda: close_edit(boxIndex, allEditButtons, allFrames))
        
        CBSTab = allFrames[boxIndex].winfo_children()[1].winfo_children()[0]
        tableTab = allFrames[boxIndex].winfo_children()[1].winfo_children()[1]


    """CBS Editing"""
    
    set_CBS_data(CBSTab, agentNames, allBevDict, allAgentCBS, allTextBoxCBSFrame, 
                 allFrames, allTitleCBS, allFormatCBS, allRadioButtons, 
                 allConcreteScrollingArea, allEntriesCBS, allTextBoxCBS, 
                 generatedCBS, moreThanOneAgent, boxIndex, allCBSTabContents)
    
    
    """Table Editing"""

    set_table_data(tableTab, allBevDict, stimDict, allFillButtons, allCircleTableBoxes, 
                   allLambdaTableBoxes, allCircleScrollingArea, 
                   allLambdaScrollingArea, allCircleGridFrame, allLambdaGridFrame, 
                   generatedTables, moreThanOneAgent, boxIndex, allTableTabContents)  

def close_edit(boxIndex, allEditButtons, allFrames):
    """ (tkinter.Tk) -> (none)
      
      Destroys the editAgent window 
    
    """

    allFrames[boxIndex].withdraw()

    allEditButtons[boxIndex][0].config(state = NORMAL)


