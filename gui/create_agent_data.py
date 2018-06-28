def create_agent_data():
  ##A swap list to hold agents swapped.
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
      del allTitleCBS[i - agentsDeleted]
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
  
  ##Set False to the tables generated based on if new agents were added.
  for i in range(len(oldAgentNames) - agentsDeleted, len(agentNames)):
    generatedCBS.append(False)
    generatedTables.append(False)    
    
    ##Append None to create a new size to each of the lists.
    allEditButtons.append((None, False))
    allAgentWindows.append(None)
    allTitleCBS.append(None)
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
  
  for i in range(len(oldAgentNames)):
    if oldAgentNames[i] != agentNames[i - agentsDeleted] and oldAgentNames[i] not in swapList: ##Means some agents have swapped places. We do not swap if it was already done.   
      ##Find position of where the agent name belongs.
      for j in range(i - agentsDeleted + 1, len(agentNames)): ##Postion to switch found if True.
        if agentNames[j] == oldAgentNames[i]:
          indexSwitch = j 
          
      ##Begin to switch the data for the dictionaries. If none of the agents had dictionaries, then there is no dictionary to shift.
      if allEditButtons[i - agentsDeleted][1] == True and allEditButtons[indexSwitch][1] == True: ##Both agents had keys associated with them.
        allCircleTableBoxes[i - agentsDeleted + 1], allCircleTableBoxes[indexSwitch + 1] = allCircleTableBoxes[indexSwitch + 1], allCircleTableBoxes[i - agentsDeleted + 1]
        allLambdaTableBoxes[i - agentsDeleted + 1], allLambdaTableBoxes[indexSwitch + 1] = allLambdaTableBoxes[indexSwitch + 1], allLambdaTableBoxes[i - agentsDeleted + 1]
      
      elif allEditButtons[i - agentsDeleted][1] == True: ##Only one agent had a key associated with them (first one).
        allCircleTableBoxes[indexSwitch + 1] = allCircleTableBoxes[i - agentsDeleted + 1]
        allLambdaTableBoxes[indexSwitch + 1] = allLambdaTableBoxes[i - agentsDeleted + 1]
        
        del allCircleTableBoxes[i - agentsDeleted + 1]
        del allLambdaTableBoxes[i - agentsDeleted + 1]
      
      elif allEditButtons[indexSwitch][1] == True: ##Only one agent had a key associated with them (second one).
        allCircleTableBoxes[i - agentsDeleted + 1] = allCircleTableBoxes[indexSwitch + 1]
        allLambdaTableBoxes[i - agentsDeleted + 1] = allLambdaTableBoxes[indexSwitch + 1] 
        
        del allCircleTableBoxes[indexSwitch + 1]
        del allLambdaTableBoxes[indexSwitch + 1] 
  
      ##Switch all the remaining data using tupple assignment.
      allAgentCBS[i - agentsDeleted], allAgentCBS[indexSwitch] = allAgentCBS[indexSwitch], allAgentCBS[i - agentsDeleted]
      allTitleCBS[i - agentsDeleted], allTitleCBS[indexSwitch] = allTitleCBS[indexSwitch], allTitleCBS[i - agentsDeleted]
      
      allFormatCBS[i - agentsDeleted], allFormatCBS[indexSwitch] = allFormatCBS[indexSwitch], allFormatCBS[i - agentsDeleted]
      allRadioButtons[i - agentsDeleted], allRadioButtons[indexSwitch] = allRadioButtons[indexSwitch], allRadioButtons[i - agentsDeleted]
      
      allTextBoxCBSFrame[i - agentsDeleted], allTextBoxCBSFrame[indexSwitch] = allTextBoxCBSFrame[indexSwitch], allTextBoxCBSFrame[i - agentsDeleted]
      allTextBoxCBS[i - agentsDeleted], allTextBoxCBS[indexSwitch] = allTextBoxCBS[indexSwitch], allTextBoxCBS[i - agentsDeleted]
      
      allConcreteScrollingArea[i - agentsDeleted], allConcreteScrollingArea[indexSwitch] = allConcreteScrollingArea[indexSwitch], allConcreteScrollingArea[i - agentsDeleted]      
      allEntriesCBS[i - agentsDeleted], allEntriesCBS[indexSwitch] = allEntriesCBS[indexSwitch], allEntriesCBS[i - agentsDeleted]    
      
      allFillButtons[i - agentsDeleted], allFillButtons[indexSwitch] = allFillButtons[indexSwitch], allFillButtons[i - agentsDeleted]
      
      allCircleScrollingArea[i - agentsDeleted], allCircleScrollingArea[indexSwitch] = allCircleScrollingArea[indexSwitch], allCircleScrollingArea[i - agentsDeleted]
      allCircleGridFrame[i - agentsDeleted], allCircleGridFrame[indexSwitch] = allCircleGridFrame[indexSwitch], allCircleGridFrame[i - agentsDeleted]
      
      allLambdaScrollingArea[i - agentsDeleted], allLambdaScrollingArea[indexSwitch] = allLambdaScrollingArea[indexSwitch], allLambdaScrollingArea[i - agentsDeleted]
      allLambdaGridFrame[i - agentsDeleted], allLambdaGridFrame[indexSwitch] = allLambdaGridFrame[indexSwitch], allLambdaGridFrame[i - agentsDeleted]
      
      generatedCBS[i - agentsDeleted], generatedCBS[indexSwitch] = generatedCBS[indexSwitch], generatedCBS[i - agentsDeleted] 
      generatedTables[i - agentsDeleted], generatedTables[indexSwitch] = generatedTables[indexSwitch], generatedTables[i - agentsDeleted]  
      
      allIsGoodCBS[i - agentsDeleted], allIsGoodCBS[indexSwitch] = allIsGoodCBS[indexSwitch], allIsGoodCBS[i - agentsDeleted]
      allIsGoodTable[i - agentsDeleted], allIsGoodTable[indexSwitch] = allIsGoodTable[indexSwitch], allIsGoodTable[i - agentsDeleted]
      
      allCheckLabels[i - agentsDeleted], allCheckLabels[indexSwitch] = allCheckLabels[indexSwitch], allCheckLabels[i - agentsDeleted]   
      
      allEditButtons[i - agentsDeleted], allEditButtons[indexSwitch] = allEditButtons[indexSwitch], allEditButtons[i - agentsDeleted]
      allAgentWindows[i - agentsDeleted], allAgentWindows[indexSwitch] = allAgentWindows[indexSwitch], allAgentWindows[i - agentsDeleted]           
      
      allPreviewPops[i - agentsDeleted], allPreviewPops[indexSwitch] = allPreviewPops[indexSwitch], allPreviewPops[i - agentsDeleted]
  
      ##Append the agent that was swapped in the bigger index to the list, 
      ##this way, when we will itearte back to that agent, no swapping will
      ##occur.
      swapList.append(agentNames[i - agentsDeleted])      