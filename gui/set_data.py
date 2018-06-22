from tkinter import *
from CBS_mods import * ##Functions which modify the concrete behaviours page.
from CBS_radio import *
from create_table import * ##Functions which modify the table page.
from fix_grids import * ##Functions which modifies the data currently stored in memory for the tables to match the data modified by the user.
from check_if_good import *
from entry_mods import *
import vertSuperscroll
import superscroll ##Module containing the widget allowing a vertical and horizontal scrollbar.

def set_CBS_data(window, agentNames, allBevDict, allAgentCBS, allTextBoxCBSFrame, 
                 allFrames, allTitleCBS, allFormatCBS, allRadioButtons, 
                 allConcreteScrollingArea, allEntriesCBS, allTextBoxCBS, 
                 generatedCBS, moreThanOneAgent, boxIndex, allCBSTabContents):
  
  """Editing CBS"""
  ##If no concrete behaviours were yet generated for the behaviours,
  ##then we generate the rows for the CBS.
  if generatedCBS[boxIndex] == False: 
    
    """Labels and Entries exclusive for CBS"""
    ##Title for the concrete behaviours.
    allTitleCBS[boxIndex] = Label(window, text='Concrete Behaviours')
    
    ##Frame for the two radio buttons.
    allFormatCBS[boxIndex] = Frame(window)
    
    ##Create a frame for the text box.
    allTextBoxCBSFrame[boxIndex] = Frame(window)
    
    ##Declaring x and y scrollbars for the CBS text box.
    xscrollbarCBS = Scrollbar(allTextBoxCBSFrame[boxIndex], orient=HORIZONTAL)
    xscrollbarCBS.grid(row=1, column=0, sticky=N+S+E+W)
    
    yscrollbarCBS = Scrollbar(allTextBoxCBSFrame[boxIndex])
    yscrollbarCBS.grid(row=0, column=1, sticky=N+S+E+W)
    
    content = StringVar()
    ##Create the text box widget for the CBS page.
    allTextBoxCBS[boxIndex] = Text(allTextBoxCBSFrame[boxIndex], wrap=NONE,
                xscrollcommand=xscrollbarCBS.set,
                yscrollcommand=yscrollbarCBS.set,
                width = 60)
    
    allTextBoxCBS[boxIndex].grid(row=0, column=0)
    
    xscrollbarCBS.config(command=allTextBoxCBS[boxIndex].xview)
    yscrollbarCBS.config(command=allTextBoxCBS[boxIndex].yview)               
   
    ##Pack frame for the radio Buttons
    allFormatCBS[boxIndex].pack(side = BOTTOM, anchor = S, expand = True)
       
    ##Set a variable that the radio Buttons share to determine what happens when 
    ##one of them is pressed.
    whichRadio = StringVar()
    whichRadio.set('Rows')      
    
    
    radioRowsCBS = Radiobutton(window, text = 'CBS Rows', variable = whichRadio, value = 'Rows', 
                                 state = 'disabled', command = lambda: change_CBS(radioRowsCBS, 
                                 radioBoxCBS, allConcreteScrollingArea[boxIndex], allTextBoxCBSFrame[boxIndex], whichRadio))
    radioRowsCBS.pack(in_=allFormatCBS[boxIndex], side = LEFT)
      
    ##Radio button for the alternate style of entering concrete behaviours.
    radioBoxCBS = Radiobutton(window, text = 'CBS Box', variable = whichRadio, value = 'Box', 
                              command = lambda: change_CBS(radioRowsCBS, radioBoxCBS, 
                              allConcreteScrollingArea[boxIndex], allTextBoxCBSFrame[boxIndex], whichRadio))
    radioBoxCBS.pack(in_=allFormatCBS[boxIndex], side = RIGHT)    
    
    ##Pack the two radio buttons in allRadioButtons as a tupple, including whichRadio.
    allRadioButtons[boxIndex] = (radioRowsCBS, radioBoxCBS, whichRadio)     
    
    ##Pack new labels for CBS.
    allAgentCBS[boxIndex] = Label(window, text = agentNames[boxIndex] + ' =>')
    allTitleCBS[boxIndex].pack(side = TOP) 
    allAgentCBS[boxIndex].pack(side = TOP, anchor = W)     
    
    ##Create a vertical scrolling area for the rows.
    allConcreteScrollingArea[boxIndex] = [vertSuperscroll.Scrolling_Area(window, width=1, height=1)]
    allConcreteScrollingArea[boxIndex][0].pack(expand=1, fill = BOTH)  
    
    ##Call create_CBS_entries() to create the rows in the CBS scrolling area.
    allEntriesCBS[boxIndex]= create_CBS_entries(allBevDict[boxIndex + 1], allConcreteScrollingArea[boxIndex][0].innerframe)
    
    ##Save the number of CBS in the allBevDict dictionary at key (0, 0) since
    ##that coordinate is unused.
    allEntriesCBS[boxIndex][0, 0] = len(allBevDict[boxIndex + 1]) 
    
    ##Set generatedCBS to True.
    generatedCBS[boxIndex] = True 
    
    allCBSTabContents[boxIndex] = window.winfo_children()      
  
  ##If concrete behaviours page was already generated, it must be modified 
  ##if necessary to adapt to changes made on previous pages.
  else: #No need to do all that repacking stuff
    ##Re-pack labels.
    if not moreThanOneAgent:
      
      allTitleCBS[boxIndex].pack(side = TOP) 
      allAgentCBS[boxIndex].pack(side = TOP, anchor = W) 
      
      ##fix_CBS() function will modify the data scructures related to CBS.
      allEntriesCBS[boxIndex] = fix_CBS(allBevDict[boxIndex + 1], allConcreteScrollingArea[boxIndex][0].innerframe, allEntriesCBS[boxIndex]) 
      
      ##Create a temporary scrolling area that will be later used as the main scrolling
      ##area. This is done in order to destroy the previous scrolling area
      ##at the end of the else statement once all the necessary widgets were
      ##saved from the old frame.
      concreteScrollingAreaTemp = vertSuperscroll.Scrolling_Area(window, width = 1, height = 1)
      
      ##calling recreate_CBS_entries() to recreate the CBS rows in the new 
      ##temporary frame.
      allEntriesCBS[boxIndex] = recreate_CBS_entries(allBevDict[boxIndex + 1], allEntriesCBS[boxIndex], concreteScrollingAreaTemp.innerframe) 
      
      ##Destroy the old scrolling area for the CBS.
      allConcreteScrollingArea[boxIndex][0].destroy() 
      
      ##Asign to the new scrolling area.
      allConcreteScrollingArea[boxIndex] = [concreteScrollingAreaTemp]

      if allRadioButtons[boxIndex][2].get() == 'Rows': ##Repack the scrolling area if the user was previously using that display.     
        ##Pack the new scrolling area and the new frame for the CBS.
        concreteScrollingAreaTemp.pack(expand=1, fill = BOTH)
  
      
      else: ##Repack the text box. 
        allTextBoxCBSFrame[boxIndex].pack()
      
      allFormatCBS[boxIndex].pack(side = BOTTOM, anchor = S, expand = True)
      
    else:
      allFrames[boxIndex].deiconify()
      allFrames[boxIndex].iconify()
        

def set_table_data(window, allBevDict, stimDict, allFillButtons, allCircleTableBoxes, 
                   allLambdaTableBoxes, allCircleScrollingArea, 
                   allLambdaScrollingArea, allCircleGridFrame, allLambdaGridFrame, 
                   generatedTables, moreThanOneAgent, boxIndex, allTableTabContents):

  if generatedTables[boxIndex] == False: 
    ##Creating scrolling areas and frames for both the circle and lambda tables.
    ##Also creating the labels in the upper corner of each table.
    if moreThanOneAgent:
      buttonsFrame = Frame(window) ##Create frame for Fill buttons
      buttonsFrame.pack(side = BOTTOM, anchor = S, fill = X)
    
    else: ##One agent
      buttonsFrame = allFillButtons[boxIndex][2]
    
    ##Button to fill circle table with beahviour in each row and button to fill
    ##lambda table with neutral stimulis is initialized here in a tupple. The tupple
    ##also contains the buttons frame.
    allFillButtons[boxIndex] = (Button(window, text = 'Fill with Behaviours', 
                     command = lambda: fill_bev(allBevDict[boxIndex + 1], stimDict, allCircleTableBoxes[boxIndex + 1]), 
                     width = 31), Button(window, text = 'Fill with neutral stimulus', 
                     command = lambda: fill_n(allBevDict[boxIndex + 1], stimDict, allLambdaTableBoxes[boxIndex + 1]), 
                     width = 31), buttonsFrame)   
    
    ##Pack the fill buttons.
    allFillButtons[boxIndex][0].pack(in_=buttonsFrame, side = LEFT) 
    allFillButtons[boxIndex][1].pack(in_=buttonsFrame, side = RIGHT)
  
     
    circleScrollingArea = [superscroll.Scrolling_Area(window, width=1, height=1)]
    circleScrollingArea[0].pack(expand=1, fill = BOTH)    
    allCircleScrollingArea.append(circleScrollingArea)
  
    circleGridFrame = Frame(circleScrollingArea[0].innerframe) 
    circleTableLabel = Label(circleGridFrame, text = 'o')   
    circleTableLabel.grid(row = 0, column = 0)
  
    lambdaScrollingArea = [superscroll.Scrolling_Area(window, width=1, height=1)]
    lambdaScrollingArea[0].pack(expand=1, fill = BOTH)   
    allLambdaScrollingArea.append(lambdaScrollingArea)
  
    lambdaGridFrame = Frame(lambdaScrollingArea[0].innerframe) 
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
    
    allCircleGridFrame[boxIndex] = circleGridFrame
    allLambdaGridFrame[boxIndex] = lambdaGridFrame
  
    generatedTables[boxIndex] = True ##Table is now generated.
    ##Keep track of table's current lenght and width
    ##in one of the dictionaries at coordinate (0, 0),
    ##since that key is not in use.
    allCircleTableBoxes[boxIndex + 1][0, 0] = len(allBevDict[1]), len(stimDict)  
      
  else: ##Table was already generated.
    if not moreThanOneAgent:
      ##Pack the fill buttons. Already packed when only one agent.
      allFillButtons[boxIndex][0].pack(in_=allFillButtons[boxIndex][2], side = LEFT) 
      allFillButtons[boxIndex][1].pack(in_=allFillButtons[boxIndex][2], side = RIGHT)
    
    allFillButtons[boxIndex][0].config(command = lambda: fill_bev(allBevDict[boxIndex + 1], stimDict, allCircleTableBoxes[boxIndex + 1]))
    allFillButtons[boxIndex][1].config(command = lambda: fill_n(allBevDict[boxIndex + 1], stimDict, allLambdaTableBoxes[boxIndex + 1]))
    
    ##Store a copy of the old circleTableBoxes and lambdaTableBoxes to see if any changes were made after calling fix_grids.
    ##This way, if no changes were made, there is no neeed to recreate the tables.
    oldCircleTableBoxes = allCircleTableBoxes[boxIndex + 1].copy()
    oldLambdaTableBoxes = allLambdaTableBoxes[boxIndex + 1].copy()
    
    ##Calling fix_grids() to check if modifications are necessary to the grids.
    fix_grids(allBevDict[boxIndex + 1], stimDict, allCircleTableBoxes[boxIndex + 1], allLambdaTableBoxes[boxIndex + 1], 
              allCircleGridFrame[boxIndex], allLambdaGridFrame[boxIndex]) 
    
    if oldCircleTableBoxes != allCircleTableBoxes[boxIndex + 1] or oldLambdaTableBoxes != allLambdaTableBoxes[boxIndex + 1]: ##Means changes were made.
    
      ##Recreating the table by using a technique similar to the one described
      ##on the CBS page (see PAGE 2 to PAGE 3).
      circleScrollingAreaTemp = superscroll.Scrolling_Area(window, width=1, height=1)
      circleScrollingAreaTemp.pack(expand=1, fill = BOTH)   
    
      circleGridFrameTemp = Frame(circleScrollingAreaTemp.innerframe) 
      circleTableLabel = Label(circleGridFrameTemp, text = 'o')   
      circleTableLabel.grid(row = 0, column = 0)
    
      lambdaScrollingAreaTemp = superscroll.Scrolling_Area(window, width=1, height=1)
      lambdaScrollingAreaTemp.pack(expand=1, fill = BOTH)      
    
      lambdaGridFrameTemp = Frame(lambdaScrollingAreaTemp.innerframe) 
      lambdaTableLabel = Label(lambdaGridFrameTemp, text = b'\xce\xbb'.decode('utf-8')) ##Decoding the code yields the lambda string.     
      lambdaTableLabel.grid(row = 0, column = 0) 
      
      ##Recreate the tables with the new data structures, and assing the data scructures
      ##to the newly created entry boxes.
      allCircleTableBoxes[boxIndex + 1], allLambdaTableBoxes[boxIndex + 1] = recreate_table(allBevDict[boxIndex + 1], stimDict, allCircleTableBoxes[boxIndex + 1], 
                                                          allLambdaTableBoxes[boxIndex + 1], circleGridFrameTemp, 
                                                          lambdaGridFrameTemp)
      ##Destroy old scrolling areas and frames.
      allCircleScrollingArea[boxIndex][0].destroy()
      allCircleGridFrame[boxIndex].destroy()
      allLambdaScrollingArea[boxIndex][0].destroy()
      allLambdaGridFrame[boxIndex].destroy()
           
      ##Pack the new frames.
      circleGridFrameTemp.pack(side=TOP, anchor = NW)
      lambdaGridFrameTemp.pack(side=TOP, anchor = SW)
      
      ##Assign the old scrolling areas and frames to the new ones.
      allCircleScrollingArea[boxIndex] = [circleScrollingAreaTemp]
      allCircleGridFrame[boxIndex] = circleGridFrameTemp
      allLambdaScrollingArea[boxIndex] = [lambdaScrollingAreaTemp]
      allLambdaGridFrame[boxIndex] = lambdaGridFrameTemp        
  
    else: ##No changes to tables.    
      if not moreThanOneAgent: ##We must repack the tables for a single agent.
        allCircleScrollingArea[boxIndex][0].pack(expand=1, fill = BOTH)  
        allCircleGridFrame[boxIndex].pack(side=TOP, anchor = NW)
        allLambdaScrollingArea[boxIndex][0].pack(expand=1, fill = BOTH)  
        allLambdaGridFrame[boxIndex].pack(side=TOP, anchor = SW)        