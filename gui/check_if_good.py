from tkinter import*

def check_if_good(bevDict, stimDict, circleTableBoxes, lambdaTableBoxes, 
                  circleTableValues, lambdaTableValues):
  invalidEntries = 0 #a counter for invalid entries
  
  firstFlag = True
  secondFlag = True
  
  found = False
  #search for incorrect value in circleTableValues 
  for key in circleTableValues.keys():
    if circleTableValues[key] not in bevDict.values():
      if found == False:
        firstFlag = False 
        found = True
      circleTableBoxes[key].config(bg = 'red')
      invalidEntries += 1
    #change background to white (normal) if the value is now valid  
    else:
      circleTableBoxes[key].config(bg = 'white')    
  
  found = False    
  #search for incorrect value in lambdaTableValues     
  for key in lambdaTableValues.keys():
    if lambdaTableValues[key] not in stimDict.values() and lambdaTableValues[key] != 'N' and lambdaTableValues[key] != 'D':
      if found == False:
        secondFlag = False 
        found = True
      lambdaTableBoxes[key].config(bg = 'red') 
      invalidEntries += 1
    #change background to white (normal) if the value is now valid  
    else: 
      lambdaTableBoxes[key].config(bg = 'white')
  
  #if both tables contain valid values, return True; else return False    
  if firstFlag == True and secondFlag == True:
    return True, invalidEntries
  else:
    return False, invalidEntries
