import string
from tkinter import*
from check_if_good import*

def get_empty_dict():
  return {}

def build_stim_dict(stimList):
  global symbolsList
  hist = {}
  i = 1 #index for the list
  index = 1 #index for the dictionary 
  
  #Bollean to check if there is at least one bad entry
  oneBad = False

  for i in range (len(stimList)):
    #Boolean to check if bad
    isBad = False    
    #test to see if more than one word in each entry box
    stimEntryList = stimList[i].get().split()
    if len(stimEntryList) > 1:
      isBad = True

    #test to see if it is a number only
    try:
        float(stimList[i].get())
        if isBad == False:
          isBad = True

    #if not only a number, check to see if characters are valid  
    except ValueError:   
      #return if there is an invalid symbol inside the word
      for character in stimList[i].get():
        if character.upper() not in symbolsList:
          if isBad == False:
            isBad = True
  
    #background configured to red since it is a bad entry
    if isBad:
      if oneBad == False:
        oneBad = True
      #change background to color red to indicate error
      stimList[i].config(bg = 'red')
    
    else:  
      #background configured to white since it is a good entry
      stimList[i].config(bg = 'white')
      #make sure entry is not empty
      if stimList[i].get() not in hist and stimList[i].get() != ' ' * len(stimList[i].get()):
        hist[index] = stimList[i].get().replace(' ', '')
        index += 1
          
  #will only return a histogram if tests are passed 
  if oneBad:
    return None
  else:
    return hist

def get_agent(agentEntry):
  #test to see if more than one word in the entry box
  if len(agentEntry.split()) > 1:
    return None
  #test to see if it is a number only
  try:
      float(agentEntry)
      return None
  #if not only a number, check to see if characters are valid  
  except ValueError:   
    #return if there is an invalid symbol inside the word
    for character in agentEntry:
      if character.upper() not in symbolsList:
        return None
    #return agent without any whitespace
    if agentEntry != ' ' * len(agentEntry):
      return agentEntry.replace(' ', '')

def build_bev_dict(line):
  hist = {}
  i = 1 #index
  
  # Split each line into a list of words.
  # The split method removes the whitespace from around each word.
  wordList = line.split()

  # For each word, remove any punctuation marks immediately
  # before and after the word.
  for word in wordList:
    word = word.upper().strip(string.punctuation)
    #test to see if it is a number only
    try:
        float(word)
        return None
    #if not only a number, check to see if characters are valid  
    except ValueError:   
      #return if there is an invalid symbol inside the word
      for character in word:
        if character not in symbolsList:
          return None
      
      #make sure netry isn't the enmpty string
      if word not in hist and word != '':
        hist[i] = word 
        i += 1
      
  #will only return a histogram if tests are passed    
  return hist  

def getTableValues(circleTableBoxes, lambdaTableBoxes):
  #create dictionary to hold values from tables
  circleTableValues = {}
  lambdaTableValues = {}  
  
  for key in circleTableBoxes.keys():
    a, b = key #extract corrdinate
    if a!= 0 and b != 0: #we are not interested in labels
      circleTableValues[key] = (circleTableBoxes[key].get()).replace(" ", "").upper()
    
  for key in lambdaTableBoxes.keys():
    a, b = key #extract corrdinate
    if a!= 0 and b != 0: #we are not interested in labels
      lambdaTableValues[key] = (lambdaTableBoxes[key].get()).replace(" ", "")
  return circleTableValues, lambdaTableValues

#long, but necessary to check valid characters
symbolsList = ['A', "B", 'C', 'D', 'E', 'F', 'G', 'H', "I", 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ']
