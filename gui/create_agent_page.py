from tkinter import *
import vertSuperscroll ##Module containing the widget allowing a vertical scrollbar.
from entry_mods import *
from check_if_good import *


def create_agent_page(editScrollingArea, allBevDict, stimDict, agentNames, complete_icon):
    editScrollingAreaTemp = vertSuperscroll.Scrolling_Area(main)
    editScrollingAreaTemp.pack(expand = 1, fill=BOTH)
    
    for i in range(len(agentNames)):
        editFrame = Frame(editScrollingAreaTemp.innerframe)
        editLabel = Label(editFrame, text = agentNames[i])
        completeLabel = Label(editFrame, image = complete_icon)
        editButton = Button(editFrame, text = 'Edit', border = 1, 
                                  command = lambda boxIndex=i: edit_agent_specs(main, allBevDict, stimDict, agentNames, boxIndex))

        editLabel.pack(side = LEFT, anchor = N)
        editButton.pack(anchor = N)
        completeLabel.pack(side = RIGHT, anchor = N)
        editFrame.pack(anchor = W)


def edit_agent_specs(main, allBevDict, stimDict, agentNames, boxIndex, generatedTable, generatedCBS):
    editAgent = Toplevel() ##Creating new window to edit agent specs
    
    editTabs = Notebook() ##Create Tabs to switch from tables to CBS
    tableTab = Frame(editTabs)
    CBSTab = Frame(editTabs)
    
    editTabs.add(tableTab) ##Add tabs to frame
    editTabs.add(CBSTab)
    
    """Table Editing"""
    buttonsFrame = Frame(tableTab) ##Create frame for Fill buttons
    buttonsFrame.pack(side = BOTTOM, anchor = S, fill = X)
    
    ##Button to fill circle table with beahviour in each row.
    fillBev = Button(tableTab, text = 'Fill with Behaviours', 
                   command = lambda: fill_bev(bevDict, stimDict, circleTableBoxes), 
                   width = 31)  
    fillBev.pack(in_=buttonsFrame, side = LEFT) 


    ##Button to fill lambda table with neutral stimulus.
    fillN = Button(tableTab, text = 'Fill with neutral stimulus', 
                   command = lambda: fill_n(bevDict, stimDict, lambdaTableBoxes), 
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
        circleTableBoxes, lambdaTableBoxes = create_table(allBevDict[boxIndex], stimDict,
                                                        circleGridFrame, 
                                                        lambdaGridFrame)
        ##pack the new table frames.   
        circleGridFrame.pack(side=TOP, anchor = NW) 
        lambdaGridFrame.pack(side=TOP, anchor = SW) 
      
        generatedTable = True ##Table is now generated.
  
      
        ##Keep track of table's current lenght and width
        ##in one of the dictionaries at coordinate (0, 0),
        ##since that key is not in use.
        circleTableBoxes[0, 0] = len(bevDict), len(stimDict)
      
    else: ##Table was already generated.
        ##Calling fix_grids() to check if modifications are necessary to the grids.
        fix_grids(allBevDict[boxIndex], stimDict, circleTableBoxes, lambdaTableBoxes,
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
        circleTableBoxes, lambdaTableBoxes = recreate_table(allBevDict[boxIndex], stimDict, circleTableBoxes, 
                                                            lambdaTableBoxes, circleGridFrameTemp, 
                                                            lambdaGridFrameTemp)
        
        
        
        """CBS Editing"""
        
        if generatedCBS == False:   
            ##Create a vertical scrolling area for the rows.
            concreteScrollingArea = vertSuperscroll.Scrolling_Area(CBSTab, width=1, height=1)
            concreteScrollingArea.pack(expand=1, fill = BOTH)   
            ##create a frame for the rows within the scrolling area.
            frameCBS = Frame(concreteScrollingArea.innerframe)
            frameCBS.pack(anchor = W)
          
            ##Call create_CBS_entries() to create the rows in the CBS frame.
            entriesCBS= create_CBS_entries(allBevDict[boxIndex], frameCBS)
          
            ##Save the number of CBS in the bevDict dictionary at key (0, 0) since
            ##that coordinate is unused.
            entriesCBS[0, 0] = len(allBevDict[boxIndex])
          
            ##Set generatedCBS to True.
            generatedCBS = True
            
            ##If concrete behaviours page was already generated, it must be modified 
            ##if necessary to adapt to changes made on previous pages.
        else:
            ##fix_CBS() function will modify the data scructures related to CBS.
            entriesCBS= fix_CBS(allBevDict[boxIndex], frameCBS, entriesCBS)
          
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
            entriesCBS = recreate_CBS_entries(allBevDict[boxIndex], entriesCBS, frameCBSTemp)
          
            ##Destroy the old scrolling area and the old frame for the CBS.
            concreteScrollingArea.destroy()
            frameCBS.destroy()            
          
            ##Assing the old scrolling area and the old frame to the new ones.
            concreteScrollingArea = concreteScrollingAreaTemp
            frameCBS = frameCBSTemp             
          
        if whichRadio.get() == 'Rows': ##Repack the scrolling area if the user was previously using that display.     
            ##Pack the new scrolling area and the new frame for the CBS.
            concreteScrollingAreaTemp.pack(expand=1, fill = BOTH)
            frameCBSTemp.pack(anchor =  W)
          
        else: ##Repack the text box. 
            textBoxCBSFrame.pack()
          
        ##Pack frame for the radio Buttons
        formatCBS.pack(side = BOTTOM, anchor = S, expand = True)
        
        """Labels and Entries exclusive for CBS"""
        ##Title for the concrete behaviours.
        titleCBS = Label(main, text='Concrete Behaviours')
        
        ##Frame for the two radio buttons.
        formatCBS = Frame(main)
        
        ##Set a variable that the radio Buttons share to determine what happens when 
        ##one of them is pressed.
        whichRadio = StringVar()
        whichRadio.set('Rows')  
        
        ##Create a frame for the text box.
        textBoxCBSFrame = Frame(main)
        
        ##Declaring x and y scrollbars for the CBS text box.
        xscrollbarCBS = Scrollbar(textBoxCBSFrame, orient=HORIZONTAL)
        xscrollbarCBS.grid(row=1, column=0, sticky=N+S+E+W)
      
        yscrollbarCBS = Scrollbar(textBoxCBSFrame)
        yscrollbarCBS.grid(row=0, column=1, sticky=N+S+E+W)
      
        content = StringVar()
        ##Create the text box widget for the CBS page.
        textBoxCBS = Text(textBoxCBSFrame, wrap=NONE,
                    xscrollcommand=xscrollbarCBS.set,
                    yscrollcommand=yscrollbarCBS.set,
                    width = 60)
        
        textBoxCBS.grid(row=0, column=0)
      
        xscrollbarCBS.config(command=textBoxCBS.xview)
        yscrollbarCBS.config(command=textBoxCBS.yview)    
        
        ##Radio button for the default style of entering concrete behaviours.
        radioRowsCBS = Radiobutton(main, text = 'CBS Rows', variable = whichRadio, value = 'Rows', 
                                   state = 'disabled', command = lambda: change_CBS(radioRowsCBS, 
                                   radioBoxCBS, concreteScrollingArea, frameCBS, textBoxCBSFrame, whichRadio))
        radioRowsCBS.pack(in_=formatCBS, side = LEFT)
        
        ##Radio button for the alternate style of entering concrete behaviours.
        radioBoxCBS = Radiobutton(main, text = 'CBS Box', variable = whichRadio, value = 'Box', 
                                  command = lambda: change_CBS(radioRowsCBS, radioBoxCBS, 
                                  concreteScrollingArea, frameCBS, textBoxCBSFrame, whichRadio))
        radioBoxCBS.pack(in_=formatCBS, side = RIGHT)        