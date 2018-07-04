from create_agent_page import *

def create_agent_data(main, pageNum, agentFrames, buttonsFrame, allEditButtons, 
                      allCheckLabels, allAgentWindows, editScrollingArea, allBevDict, 
                      stimDict, allFillButtons, oldAgentNames, agentNames, allCircleTableBoxes, 
                      allLambdaTableBoxes, allCircleScrollingArea, allLambdaScrollingArea, 
                      allCircleGridFrame, allLambdaGridFrame, allTextBoxCBSFrame, 
                      allFormatCBS,allEntriesCBS, allAgentCBS, allTextBoxCBS, 
                      allRadioButtons, allConcreteScrollingArea, generatedTables, 
                      generatedCBS, allIsGoodCBS, allIsGoodTable, allCBSTabContents, 
                      allTableTabContents, allPreviewPops, edit_icon, filled_icon, editTitle):
  
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
  
  ##Make a copy of the swap list to represent how data is distributed in the computer's memory for swapping.
  dataSwap = swapList.copy()    
  
  ##Set False to the tables generated based on if new agents were added.
  for i in range(len(oldAgentNames) - agentsDeleted, len(agentNames)):
    generatedCBS.append(False)
    generatedTables.append(False)    
    
    ##Append None to create a new size to each of the lists.
    allEditButtons.append((None, False))
    allAgentWindows.append(None)
    
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
    
    dataSwap.append(None) ##Appending None to dataSwap to indicate the 'new' agents and their data.
    
  for i in range(len(swapList)):
    if swapList[i] != agentNames[i]: ##Means some agents have swapped places. We do not swap if it was already done.   
      ##Find position of where the agent name belongs in the data.
      indexSwitch = agentNames.index(swapList[i])
      i = dataSwap.index(swapList[i])
          
      ##Begin to switch the data for the dictionaries. If none of the agents had dictionaries, then there is no dictionary to shift.
      if allEditButtons[i][1] == True and allEditButtons[indexSwitch][1] == True: ##Both agents had keys associated with them.
        allCircleTableBoxes[i + 1], allCircleTableBoxes[indexSwitch + 1] = allCircleTableBoxes[indexSwitch + 1], allCircleTableBoxes[i + 1]
        allLambdaTableBoxes[i + 1], allLambdaTableBoxes[indexSwitch + 1] = allLambdaTableBoxes[indexSwitch + 1], allLambdaTableBoxes[i + 1]
      
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
      
      dataSwap[i], dataSwap[indexSwitch] = dataSwap[indexSwitch], dataSwap[i]
      
  if len(agentFrames['agentNames']) > 1: ##More than one agent calls for a different layout.
    moreThanOneAgent = True        
    
    if len(oldAgentNames) == 1 and oldAgentNames[0] in agentNames: ##If agent was single but now multiple, we need to remake the UI for that agent in the multiple agent page.
      newIndex = agentNames.index(oldAgentNames[0])
      generatedTables[newIndex] = False
      generatedCBS[newIndex] = False
    editTitle.config(text = "Agent Specifications") 
    editTitle.pack()   
    ##Special UI when more than one agent is entered.
    create_agent_page(main, allEditButtons, allCheckLabels, allAgentWindows, editScrollingArea, allBevDict, 
                      stimDict, allFillButtons, oldAgentNames, agentNames, allCircleTableBoxes, 
                      allLambdaTableBoxes, allCircleScrollingArea, allLambdaScrollingArea, 
                      allCircleGridFrame, allLambdaGridFrame, allTextBoxCBSFrame, 
                      allFormatCBS,allEntriesCBS, allAgentCBS, allTextBoxCBS, 
                      allRadioButtons, allConcreteScrollingArea, moreThanOneAgent, 
                      generatedTables, generatedCBS, allCBSTabContents, allTableTabContents, edit_icon, filled_icon) 
    
    pageNum += 1 ##Add one to pageNum because we are skipping page 4.
  
  else: ##Only one agent.            
    moreThanOneAgent = False
    if len(oldAgentNames) > 1 and agentNames[0] in oldAgentNames: ##If agent was in multiple agents but now single, we need to remake the UI for that agent in the single agent page.
      generatedTables[0] = False
      generatedCBS[0] = False
      allFillButtons[0] = (None, None, buttonsFrame)
     
    editTitle.config(text = "Agent Specifications: Concrete Behaviours")   
    editTitle.pack()   
    set_CBS_data(main, agentNames, allBevDict, allAgentCBS, allTextBoxCBSFrame,  
                 allFormatCBS, allRadioButtons, allConcreteScrollingArea, 
                 allEntriesCBS, allTextBoxCBS, generatedCBS, moreThanOneAgent, 0, allCBSTabContents)
  
  return moreThanOneAgent, pageNum