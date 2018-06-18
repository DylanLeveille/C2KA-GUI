"""Imported modules."""
from tkinter import * ##Import the tkinter module to allow construction of the GUI interface.
from string import * ##Module containing functions to modify strings.

"""Function which creates the product (text file)."""
def create_text(agentName, agentBehaviour, concreteBehaviours, textBoxCBS, 
                circleTableValues, lambdaTableValues, stimDict, bevDict, whichRadio):
  """ (str, str, str, dict, dict, dict, dict, StringVar) -> (none)
    
    Creates the text file for the agent specifications.
    File is saved in program's folder.
  
  """        
  ##Create file if it does not exist.
  file = open("agent_text_backup./agentspec.txt", "w+") 
    
  ##Text for the agent.
  file.write("begin AGENT where\n")
  ##Printing the agent name and behaviour.
  file.write("    %s := %s\n" %(agentName, agentBehaviour)) 
  ##END.
  file.write("end\n")
  file.write("\n")
  
  ##Text for the next behaviour.
  file.write("begin NEXT_BEHAVIOUR where\n")
  ##Access each element in stimulus dictionary.
  for i in range(1, len(stimDict)+1): 
      ##Access each element in behaviour dictionary.
      for j in range(1, len(bevDict)+1): 
          ##Write stimulus and behaviour.
          file.write("    (%s, %s)" %(stimDict[i], bevDict[j]))
          ##Finding total whitespace to align '=' sign.
          whiteSpace = len(max(stimDict.values(), key=len)) + len(max(bevDict.values(), key=len))- len(stimDict[i]) - len(bevDict[j])
          for k in range(whiteSpace + 1):
              file.write(" ")
          ##Access table values using row and columns.
          file.write("= %s" %(circleTableValues[j, i])) 
          file.write("\n")
  ##END.
  file.write("end\n")
  file.write("\n")
  
  ##Text for next stimulus.
  file.write("begin NEXT_STIMULUS where\n")
  ##Access each element in stimulus dictionary.
  for i in range(1, len(stimDict)+1):
      ##Access each element in behaviour dictionary.
      for j in range(1, len(bevDict)+1):
          ##Write stimulus and behaviour.
          file.write("    (%s, %s)" %(stimDict[i], bevDict[j]))
          ##Finding total whitespace to align '=' sign.
          whiteSpace = len(max(stimDict.values(), key=len)) + len(max(bevDict.values(), key=len)) - len(stimDict[i]) - len(bevDict[j])
          for k in range(whiteSpace + 1):
              file.write(" ")
          ##Access table values using row and columns.
          file.write("= %s" %(lambdaTableValues[j, i]))
          file.write("\n")
  ##END.
  file.write("end\n")
  file.write("\n")
  
  ##Text for concrete behaviours.
  file.write("begin CONCRETE BEHAVIOUR where\n")
  
  if whichRadio.get() == 'Rows': ##User used rows for concrete behaviours.
    ##Iterate through concrete behaviours.
    for i in range(1, len(bevDict) +1):
        ##Write label for CBS.
        file.write("    %s" %(bevDict[i]))
        ##Finding total whitespace to align '=>' sign.
        whiteSpace = len(max(bevDict.values(), key=len)) - len(bevDict[i])
        for j in range(whiteSpace + 1):
            file.write(" ")
        ##Write concrete behaviour entry for each label.
        file.write("=> [ %s ]" %(concreteBehaviours[i]))
        file.write("\n")
        
  else: ##User used the text box for the concrete behaviours
    ##Write agent name.
    file.write("    %s => [" %(agentName))
    whitespace = 9 + len(agentName) ##Used to align text.
    
    ##Write text Box entry.
    textBoxList = textBoxCBS.get("1.0", END).splitlines() ##Split each line in the text box.
    
    firstLineFound = False ##Boolean value to check if the first line has been found.
    
    for line in range(len(textBoxList)):##Iterate through each line.
      if len(textBoxList[line].split()) > 0: ##The line cannot be blank.
        
        if firstLineFound == False: ##Special syntax on first line.
          firstLineFound = True ##First line is found.    
          
        else: ##Not the first line.  
          file.write("\n%s" %(' ' * whitespace)) ##Allows alignment.
        
        for word in textBoxList[line].split():
          if word == '|': ##Means we must add a whitespace.
              file.write(" ")
                
          file.write(" %s" %(word)) ##Write the word.
      
    file.write(" ]\n") ##End with a closing bracket.
    
  ##END.
  file.write("end")    
  file.close()