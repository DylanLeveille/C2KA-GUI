from tkinter import *
from string import *

def create_text(agentName, agentBehaviour, circleTableValues,
                lambdaTableValues, stimDict, bevDict, entriesCBS):
    #Create file if it does not exist
    file = open("agentspec.txt", "w+") 
    
    #text for agent
    file.write("begin AGENT where\n")
    # Printing agent name and behaviour
    file.write("    %s := %s\n" %(agentName, agentBehaviour)) 
    #END
    file.write("end\n")
    file.write("\n")
    
    #text for next behaviour
    file.write("begin NEXT_BEHAVIOUR where\n")
    #access each element in stimulus dictionary
    for i in range(1, len(stimDict)+1): 
        #access each element in behaviour dictionary
        for j in range(1, len(bevDict)+1): 
            #write stimulus and behaviour
            file.write("    (%s, %s)" %(stimDict[i], bevDict[j]))
            #finding total whitespace to align '=' sign
            whiteSpace = len(max(stimDict.values(), key=len)) + len(max(bevDict.values(), key=len))- len(stimDict[i]) - len(bevDict[j])
            for k in range(whiteSpace + 1):
                file.write(" ")
            #Access table values using row and columns
            file.write("= %s" %(circleTableValues[j, i])) 
            file.write("\n")
    #END
    file.write("end\n")
    file.write("\n")
    
    #text for next stimulus
    file.write("begin NEXT_STIMULUS where\n")
    #access each element in stimulus dictionary
    for i in range(1, len(stimDict)+1):
        #access each element in behaviour dictionary
        for j in range(1, len(bevDict)+1):
            #write stimulus and behaviour
            file.write("    (%s, %s)" %(stimDict[i], bevDict[j]))
            #finding total whitespace to align '=' sign
            whiteSpace = len(max(stimDict.values(), key=len)) + len(max(bevDict.values(), key=len)) - len(stimDict[i]) - len(bevDict[j])
            for k in range(whiteSpace + 1):
                file.write(" ")
            #Access table values using row and columns
            file.write("= %s" %(lambdaTableValues[j, i]))
            file.write("\n")
    #END
    file.write("end\n")
    file.write("\n")
    
    #text for concrete behaviours
    file.write("begin CONCRETE BEHAVIOUR where\n")
    #iterate through concrete behaviours
    for i in range(1, len(bevDict) +1):
        #write label for CBS
        file.write("    %s" %(entriesCBS[i, 0].cget("text")))
        #finding total whitespace to align '=>' sign
        whiteSpace = len(max(bevDict.values(), key=len)) - len(entriesCBS[i, 0].cget("text"))
        for j in range(whiteSpace + 1):
            file.write(" ")
        #write concrete behaviour entry for each label
        file.write("=> [ %s ]" %(entriesCBS[i, 1].get()))
        file.write("\n")
    #END
    file.write("end")    
    file.close()