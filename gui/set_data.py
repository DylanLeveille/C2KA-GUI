from tkinter import *
from create_table import *
import superscroll ##Module containing the widget allowing a vertical and horizontal scrollbar.

def set_table_data(window, allBevDict, stimDict, allCircleTableBoxes, 
                   allLambdaTableBoxes, circleScrollingArea, 
                   lambdaScrollingArea, allCircleGridFrame, allLambdaGridFrame, 
                   generatedTable, boxIndex):
  if generatedTable == False:
    ##Creating scrolling areas and frames for both the circle and lambda tables.
      ##Also creating the labels in the upper corner of each table.
      circleScrollingArea = [superscroll.Scrolling_Area(window, width=1, height=1)]
      circleScrollingArea[0].pack(expand=1, fill = BOTH)     
    
      circleGridFrame = Frame(circleScrollingArea[0].innerframe) 
      circleTableLabel = Label(circleGridFrame, text = 'o')   
      circleTableLabel.grid(row = 0, column = 0)
    
      lambdaScrollingArea = [superscroll.Scrolling_Area(window, width=1, height=1)]
      lambdaScrollingArea[0].pack(expand=1, fill = BOTH)      
    
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
    
      generatedTable = True ##Table is now generated.
  
    
      ##Keep track of table's current lenght and width
      ##in one of the dictionaries at coordinate (0, 0),
      ##since that key is not in use.
      allCircleTableBoxes[boxIndex + 1][0, 0] = len(allBevDict[1]), len(stimDict)
      
      return allCircleTableBoxes, allLambdaTableBoxes, circleScrollingArea, lambdaScrollingArea, allCircleGridFrame, allLambdaGridFrame
      
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
    
    ##Destroy old scrolling areas and frames.
    circleScrollingArea.destroy()
    circleGridFrame.destroy()
    lambdaScrollingArea.destroy()
    lambdaGridFrame.destroy()
         
    ##Pack the new scrolling areas and frames.
    circleScrollingAreaTemp.pack(side=TOP, anchor = NW)
    circleGridFrameTemp.pack(side=TOP, anchor = NW)
    lambdaScrollingAreaTemp.pack(side=TOP, anchor = SW)
    lambdaGridFrameTemp.pack(side=TOP, anchor = SW)
    
    ##Assign the old scrolling areas and frames to the new ones.
    circleScrollingArea = circleScrollingAreaTemp
    circleGridFrame = circleGridFrameTemp
    lambdaScrollingArea = lambdaScrollingAreaTemp
    lambdaGridFrame = lambdaGridFrameTemp        