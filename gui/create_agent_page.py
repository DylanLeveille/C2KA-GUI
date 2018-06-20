from tkinter import *
import superscroll
import vertSuperscroll ##Module containing the widget allowing a vertical scrollbar.
from create_table import *
from entry_mods import *
from check_if_good import *
from CBS_mods import *
from CBS_radio import *


def create_agent_page(main, editScrollingArea, allBevDict, stimDict, agentNames, allCircleTableBoxes, allLambdaTableBoxes, allEntriesCBS, allTextBoxCBS, allRadioButtons):
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
                                  command = lambda boxIndex=i: edit_agent_specs(main, allBevDict, stimDict, agentNames, boxIndex, False, False, allCircleTableBoxes, allLambdaTableBoxes, allEntriesCBS, allTextBoxCBS, allRadioButtons)) #generated booleans will always be false first time...use data structure and set them to false before calling.

        allButtons[i] = editButton
        editLabel.pack(side = LEFT, anchor = N)
        editButton.pack(anchor = N)
        #completeLabel.pack(side = RIGHT, anchor = N)
        editFrame.pack(anchor = W)


def edit_agent_specs(main, allBevDict, stimDict, agentNames, boxIndex, generatedTable, generatedCBS, allCircleTableBoxes, allLambdaTableBoxes, allEntriesCBS, allTextBoxCBS, allRadioButtons):
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
    
    """Table Editing"""
    buttonsFrame = Frame(tableTab) ##Create frame for Fill buttons
    buttonsFrame.pack(side = BOTTOM, anchor = S, fill = X)
    
    ##Button to fill circle table with beahviour in each row.
    fillBev = Button(tableTab, text = 'Fill with Behaviours', 
                   command = lambda: fill_bev(allBevDict[boxIndex + 1], stimDict, allCircleTableBoxes[boxIndex + 1]), 
                   width = 31)  
    fillBev.pack(in_=buttonsFrame, side = LEFT) 


    ##Button to fill lambda table with neutral stimulus.
    fillN = Button(tableTab, text = 'Fill with neutral stimulus', 
                   command = lambda: fill_n(allBevDict[boxIndex + 1], stimDict, allLambdaTableBoxes[boxIndex + 1]), 
                   width = 31)
    fillN.pack(in_=buttonsFrame, side = RIGHT)    
    
    if generatedTable == False:
        ##Creating ccrolling areas and frames for both the circle and lambda tables.
        ##Also creating the labels in the upper corner of each table.
        circleScrollingArea = superscroll.Scrolling_Area(tableTab, width=1, height=1)
        circleScrollingArea.pack(expand=1, fill = BOTH)   
  
      
        circleGridFrame = Frame(circleScrollingArea.innerframe) 
        circleTableLabel = Label(circleGridFrame, text = 'o')   
        circleTableLabel.grid(row = 0, column = 0)
      
        lambdaScrollingArea = superscroll.Scrolling_Area(tableTab, width=1, height=1)
        lambdaScrollingArea.pack(expand=1, fill = BOTH)      
      
        lambdaGridFrame = Frame(lambdaScrollingArea.innerframe) 
        lambdaTableLabel = Label(lambdaGridFrame, text = b'\xce\xbb'.decode('utf-8')) ##Decoding the code yields the lambda string.  
        lambdaTableLabel.grid(row = 0, column = 0)   
      
        ##Create the data structures to hold the table entries and
        ##create the boxes within the frames.
        allCircleTableBoxes[boxIndex + 1], allLambdaTableBoxes[boxIndex + 1] = create_table(allBevDict[boxIndex + 1], stimDict,
                                                        circleGridFrame, 
                                                        lambdaGridFrame)
        ##pack the new table frames.   
        circleGridFrame.pack(side=TOP, anchor = NW) 
        lambdaGridFrame.pack(side=TOP, anchor = SW) 
      
        generatedTable = True ##Table is now generated.
  
      
        ##Keep track of table's current lenght and width
        ##in one of the dictionaries at coordinate (0, 0),
        ##since that key is not in use.
        allCircleTableBoxes[boxIndex + 1][0, 0] = len(allBevDict[1]), len(stimDict)
      
    else: ##Table was already generated.
        ##Calling fix_grids() to check if modifications are necessary to the grids.
        fix_grids(allBevDict[boxIndex], stimDict, allCircleTableBoxes[boxIndex + 1], allLambdaTableBoxes[boxIndex + 1],
                  circleGridFrame, lambdaGridFrame) 
      
        ##Recreating the table by using a technique similar to the one described
        ##on the CBS page (see PAGE 2 to PAGE 3).
        circleScrollingAreaTemp = superscroll.Scrolling_Area(tableTab, width=1, height=1)
        circleScrollingAreaTemp.pack(expand=1, fill = BOTH)   
      
        circleGridFrameTemp = Frame(circleScrollingAreaTemp.innerframe) 
        circleTableLabel = Label(circleGridFrameTemp, text = 'o')   
        circleTableLabel.grid(row = 0, column = 0)
      
        lambdaScrollingAreaTemp = superscroll.Scrolling_Area(tableTab, width=1, height=1)
        lambdaScrollingAreaTemp.pack(expand=1, fill = BOTH)      
      
        lambdaGridFrameTemp = Frame(lambdaScrollingAreaTemp.innerframe) 
        lambdaTableLabel = Label(lambdaGridFrameTemp, text = b'\xce\xbb'.decode('utf-8')) ##Decoding the code yields the lambda string.     
        lambdaTableLabel.grid(row = 0, column = 0) 
        
        ##Recreate the tables with the new data structures, and assing the data scructures
        ##to the newly created entry boxes.
        allCircleTableBoxes[boxIndex + 1], allLambdaTableBoxes[boxIndex + 1] = recreate_table(allBevDict[boxIndex], stimDict, allCircleTableBoxes[boxIndex + 1], 
                                                            allLambdaTableBoxes[boxIndex + 1], circleGridFrameTemp, 
                                                            lambdaGridFrameTemp)
        
        
        
    """CBS Editing"""
    """Labels and Entries exclusive for CBS"""
    ##Title for the concrete behaviours.
    titleCBS = Label(CBSTab, text='Concrete Behaviours')
    
    ##Frame for the two radio buttons.
    formatCBS = Frame(CBSTab)
    
    ##Set a variable that the radio Buttons share to determine what happens when 
    ##one of them is pressed.
    allRadioButtons[boxIndex + 1] = StringVar()
    allRadioButtons[boxIndex + 1].set('Rows')  
    
    ##Create a frame for the text box.
    textBoxCBSFrame = Frame(CBSTab)
    
    ##Declaring x and y scrollbars for the CBS text box.
    xscrollbarCBS = Scrollbar(textBoxCBSFrame, orient=HORIZONTAL)
    xscrollbarCBS.grid(row=1, column=0, sticky=N+S+E+W)
  
    yscrollbarCBS = Scrollbar(textBoxCBSFrame)
    yscrollbarCBS.grid(row=0, column=1, sticky=N+S+E+W)
  
    content = StringVar()
    ##Create the text box widget for the CBS page.
    allTextBoxCBS[boxIndex + 1] = Text(textBoxCBSFrame, wrap=NONE,
                xscrollcommand=xscrollbarCBS.set,
                yscrollcommand=yscrollbarCBS.set,
                width = 60)
    
    allTextBoxCBS[boxIndex + 1].grid(row=0, column=0)
  
    xscrollbarCBS.config(command=allTextBoxCBS[boxIndex + 1].xview)
    yscrollbarCBS.config(command=allTextBoxCBS[boxIndex + 1].yview)    
    
    ##Radio button for the default style of entering concrete behaviours.
    radioRowsCBS = Radiobutton(CBSTab, text = 'CBS Rows', variable = allRadioButtons[boxIndex + 1], value = 'Rows', 
                               state = 'disabled', command = lambda: change_CBS(radioRowsCBS, 
                               radioBoxCBS, concreteScrollingArea, frameCBS, textBoxCBSFrame, allRadioButtons[boxIndex + 1]))
    radioRowsCBS.pack(in_=formatCBS, side = LEFT)
    
    ##Radio button for the alternate style of entering concrete behaviours.
    radioBoxCBS = Radiobutton(CBSTab, text = 'CBS Box', variable = allRadioButtons[boxIndex + 1], value = 'Box', 
                              command = lambda: change_CBS(radioRowsCBS, radioBoxCBS, 
                              concreteScrollingArea, frameCBS, textBoxCBSFrame, allRadioButtons[boxIndex + 1]))
    radioBoxCBS.pack(in_=formatCBS, side = RIGHT)            
    
    
    if generatedCBS == False:   
        ##Create a vertical scrolling area for the rows.
        concreteScrollingArea = vertSuperscroll.Scrolling_Area(CBSTab, width=1, height=1)
        concreteScrollingArea.pack(expand=1, fill = BOTH)   
        ##create a frame for the rows within the scrolling area.
        frameCBS = Frame(concreteScrollingArea.innerframe)
        frameCBS.pack(anchor = W)
      
        ##Call create_CBS_entries() to create the rows in the CBS frame.
        allEntriesCBS[boxIndex + 1]= create_CBS_entries(allBevDict[boxIndex + 1], frameCBS)
      
        ##Save the number of CBS in the bevDict dictionary at key (0, 0) since
        ##that coordinate is unused.
        allEntriesCBS[boxIndex + 1][0, 0] = len(allBevDict[boxIndex + 1])
      
        ##Set generatedCBS to True.
        generatedCBS = True
        
        ##If concrete behaviours page was already generated, it must be modified 
        ##if necessary to adapt to changes made on previous pages.
    else:
        ##fix_CBS() function will modify the data scructures related to CBS.
        allEntriesCBS[boxIndex + 1]= fix_CBS(allBevDict[boxIndex + 1], frameCBS, allEntriesCBS[boxIndex + 1])
      
        ##Create a temporary scrolling area that will be later used as the main scrolling
        ##area. This is done in order to destroy the previous scrolling area
        ##at the end of the else statement once all the necessary widgets were
        ##saved from the old frame.
        concreteScrollingAreaTemp = vertSuperscroll.Scrolling_Area(CBSTab, width = 1, height = 1)
      
        ##Create a temporary frame to hold CBS (for the same reason described 
        ##in the temporary scrolling area).
        frameCBSTemp = Frame(concreteScrollingAreaTemp.innerframe)
      
        ##calling recreate_CBS_entries() to recreate the CBS rows in the new 
        ##temporary frame.
        allEntriesCBS[boxIndex + 1] = recreate_CBS_entries(allBevDict[boxIndex + 1], allEntriesCBS[boxIndex + 1], frameCBSTemp)
      
        ##Destroy the old scrolling area and the old frame for the CBS.
        concreteScrollingArea.destroy()
        frameCBS.destroy()            
      
        ##Assing the old scrolling area and the old frame to the new ones.
        concreteScrollingArea = concreteScrollingAreaTemp
        frameCBS = frameCBSTemp             
          
        if allRadioButtons[boxIndex + 1].get() == 'Rows': ##Repack the scrolling area if the user was previously using that display.     
            ##Pack the new scrolling area and the new frame for the CBS.
            concreteScrollingAreaTemp.pack(expand=1, fill = BOTH)
            frameCBSTemp.pack(anchor =  W)
          
        else: ##Repack the text box. 
            textBoxCBSFrame.pack()
          
    ##Pack frame for the radio Buttons
    formatCBS.pack(side = BOTTOM, anchor = S, expand = True)
    
def close_edit(main, boxIndex, allEntriesCBS):
    """ (tkinter.Tk) -> (none)
      
      Destroys the editAgent window 
    
    """     
    allFrames[boxIndex].destroy()
    del allFrames[boxIndex]
    
    allButtons[boxIndex].config(state = NORMAL)
    print(allEntriesCBS)