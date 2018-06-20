from tkinter import *
from CBS_mods import * ##Functions which modify the concrete behaviours page.
from CBS_radio import *
from create_table import * ##Functions which modify the table page.
from fix_grids import * ##Functions which modifies the data currently stored in memory for the tables to match the data modified by the user.
import vertSuperscroll
import superscroll ##Module containing the widget allowing a vertical and horizontal scrollbar.

def set_CBS_data(window, agentNames, allBevDict, allAgentCBS, allRadioButtons, 
                 allConcreteScrollingArea, allEntriesCBS, allTextBoxCBS, generatedCBS, moreThanOneAgent, boxIndex):
    
  """Labels and Entries exclusive for CBS"""
  ##Title for the concrete behaviours.
  titleCBS = Label(window, text='Concrete Behaviours')
  
  ##Frame for the two radio buttons.
  formatCBS = Frame(window)
  
  ##Set a variable that the radio Buttons share to determine what happens when 
  ##one of them is pressed.
  allRadioButtons[boxIndex] = StringVar()
  allRadioButtons[boxIndex].set('Rows')  
  
  ##Create a frame for the text box.
  textBoxCBSFrame = Frame(window)
  
  ##Declaring x and y scrollbars for the CBS text box.
  xscrollbarCBS = Scrollbar(textBoxCBSFrame, orient=HORIZONTAL)
  xscrollbarCBS.grid(row=1, column=0, sticky=N+S+E+W)
  
  yscrollbarCBS = Scrollbar(textBoxCBSFrame)
  yscrollbarCBS.grid(row=0, column=1, sticky=N+S+E+W)
  
  content = StringVar()
  ##Create the text box widget for the CBS page.
  allTextBoxCBS[boxIndex] = Text(textBoxCBSFrame, wrap=NONE,
              xscrollcommand=xscrollbarCBS.set,
              yscrollcommand=yscrollbarCBS.set,
              width = 60)
  
  allTextBoxCBS[boxIndex].grid(row=0, column=0)
  
  xscrollbarCBS.config(command=allTextBoxCBS[boxIndex].xview)
  yscrollbarCBS.config(command=allTextBoxCBS[boxIndex].yview)    

  ##Radio button for the default style of entering concrete behaviours.
  radioRowsCBS = Radiobutton(window, text = 'CBS Rows', variable = allRadioButtons[boxIndex], value = 'Rows', 
                             state = 'disabled', command = lambda: change_CBS(radioRowsCBS, 
                             radioBoxCBS, allConcreteScrollingArea[boxIndex], textBoxCBSFrame, allRadioButtons[boxIndex]))
  radioRowsCBS.pack(in_=formatCBS, side = LEFT)
  
  ##Radio button for the alternate style of entering concrete behaviours.
  radioBoxCBS = Radiobutton(window, text = 'CBS Box', variable = allRadioButtons[boxIndex], value = 'Box', 
                            command = lambda: change_CBS(radioRowsCBS, radioBoxCBS, 
                            allConcreteScrollingArea[boxIndex], textBoxCBSFrame, allRadioButtons[boxIndex]))
  radioBoxCBS.pack(in_=formatCBS, side = RIGHT)            
 
  ##Pack frame for the radio Buttons
  formatCBS.pack(side = BOTTOM, anchor = S, expand = True)
  
  
  """Editing CBS"""
  ##If no concrete behaviours were yet generated for the behaviours,
  ##then we generate the rows for the CBS.
  if generatedCBS[boxIndex] == False: 
    ##Pack new labels for CBS.
    allAgentCBS.append(Label(window, text = agentNames[boxIndex] + ' =>'))
    titleCBS.pack(side = TOP) 
    allAgentCBS[boxIndex].pack(side = TOP, anchor = W)     
    
    ##Create a vertical scrolling area for the rows.
    allConcreteScrollingArea.append([vertSuperscroll.Scrolling_Area(window, width=1, height=1)])
    allConcreteScrollingArea[boxIndex][0].pack(expand=1, fill = BOTH)  
    
    ##Call create_CBS_entries() to create the rows in the CBS scrolling area.
    allEntriesCBS.append(create_CBS_entries(allBevDict[boxIndex + 1], allConcreteScrollingArea[boxIndex][0].innerframe))
    
    ##Save the number of CBS in the allBevDict dictionary at key (0, 0) since
    ##that coordinate is unused.
    allEntriesCBS[boxIndex][0, 0] = len(allBevDict[boxIndex + 1]) 
    
    ##Set generatedCBS to True.
    generatedCBS[boxIndex] = True 
  
  ##If concrete behaviours page was already generated, it must be modified 
  ##if necessary to adapt to changes made on previous pages.
  else:
    ##Re-pack labels.
    titleCBS.pack(side = TOP) 
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
    
    if whichRadio.get() == 'Rows': ##Repack the scrolling area if the user was previously using that display.     
      ##Pack the new scrolling area and the new frame for the CBS.
      concreteScrollingAreaTemp.pack(expand=1, fill = BOTH)
    
    else: ##Repack the text box. 
      textBoxCBSFrame.pack() 

def set_table_data(window, allBevDict, stimDict, allCircleTableBoxes, 
                   allLambdaTableBoxes, allCircleScrollingArea, 
                   allLambdaScrollingArea, allCircleGridFrame, allLambdaGridFrame, 
                   generatedTables, boxIndex):
  
  """Initialization of buttons"""
  buttonsFrame = Frame(window) ##Create frame for Fill buttons
  buttonsFrame.pack(side = BOTTOM, anchor = S, fill = X)
  
  ##Button to fill circle table with beahviour in each row.
  fillBev = Button(window, text = 'Fill with Behaviours', 
                 command = lambda: fill_bev(allBevDict[boxIndex + 1], stimDict, allCircleTableBoxes[boxIndex + 1]), 
                 width = 31)  
  fillBev.pack(in_=buttonsFrame, side = LEFT) 


  ##Button to fill lambda table with neutral stimulus.
  fillN = Button(window, text = 'Fill with neutral stimulus', 
                 command = lambda: fill_n(allBevDict[boxIndex + 1], stimDict, allLambdaTableBoxes[boxIndex + 1]), 
                 width = 31)
  fillN.pack(in_=buttonsFrame, side = RIGHT)   


  if generatedTables[boxIndex] == False: 
    ##Creating scrolling areas and frames for both the circle and lambda tables.
      ##Also creating the labels in the upper corner of each table.
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
      
      allCircleGridFrame.append(circleGridFrame)
      allLambdaGridFrame.append(lambdaGridFrame)
    
      generatedTables[boxIndex] = True ##Table is now generated.
      ##Keep track of table's current lenght and width
      ##in one of the dictionaries at coordinate (0, 0),
      ##since that key is not in use.
      allCircleTableBoxes[boxIndex + 1][0, 0] = len(allBevDict[1]), len(stimDict)
      
  else: ##Table was already generated.
    ##Calling fix_grids() to check if modifications are necessary to the grids.
    fix_grids(allBevDict[boxIndex + 1], stimDict, allCircleTableBoxes[boxIndex + 1], allLambdaTableBoxes[boxIndex + 1], 
              allCircleGridFrame[boxIndex], allLambdaGridFrame[boxIndex]) 
  
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
         
    ##Pack the new scrolling areas and frames.
    circleScrollingAreaTemp.pack(side=TOP, anchor = NW)
    circleGridFrameTemp.pack(side=TOP, anchor = NW)
    lambdaScrollingAreaTemp.pack(side=TOP, anchor = SW)
    lambdaGridFrameTemp.pack(side=TOP, anchor = SW)
    
    ##Assign the old scrolling areas and frames to the new ones.
    allCircleScrollingArea[boxIndex] = [circleScrollingAreaTemp]
    allCircleGridFrame[boxIndex] = circleGridFrameTemp
    allLambdaScrollingArea[boxIndex] = [lambdaScrollingAreaTemp]
    allLambdaGridFrame[boxIndex] = lambdaGridFrameTemp        