from tkinter import *
from string import *

def create_text(agentName, agentBehaviour, circleTableBoxes,
                lambdaTableBoxes, stimDict, bevDict):
    global a
    #Create file if it does not exist
    a = open("agentspec.txt", "w+") 
    a.write("begin AGENT where\n")
    # Printing agent name and behaviour
    a.write("    %s := %s\n" %(agentName, agentBehaviour)) 
    a.write("end\n")
    a.write("\n")
    a.write("begin NEXT_BEHAVIOUR where\n")
    #access each element in stimulus dictionary
    for i in range(1, len(stimDict)+1): 
        #access each element in behaviour dictionary
        for j in range(1, len(bevDict)+1): 
            #write stimulus and behaviour
            a.write("    (%s, %s)" %(stimDict[i], bevDict[j]))
            #finding total whitespace to align '=' sign
            whiteSpace = len(max(stimDict.values(), key=len)) + len(max(bevDict.values(), key=len))
            - len(stimDict[i]) - len(bevDict[j])
            for k in range(whiteSpace + 1):
                a.write(" ")
            #Access table box using row and columns
            a.write("= %s" %(circleTableBoxes[j, i].get())) 
            a.write("\n")
    
    a.write("end\n")
    a.write("\n")
    a.write("begin NEXT_STIMULUS where\n")
    for i in range(1, len(stimDict)+1):
        for j in range(1, len(bevDict)+1):
            a.write("    (%s, %s)" %(stimDict[i], bevDict[j]))
            whiteSpace = len(max(stimDict.values(), key=len)) + len(max(bevDict.values(), key=len)) - len(stimDict[i]) - len(bevDict[j])
            for k in range(whiteSpace + 1):
                a.write(" ")
            a.write("= %s" %(lambdaTableBoxes[j, i].get()))
            a.write("\n")
  
    a.write("end")    
    a.close()
    
    

    
    
 

    