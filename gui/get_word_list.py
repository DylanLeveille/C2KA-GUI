"""Imported modules."""
from tkinter import * ##Import the tkinter module to allow construction of the GUI interface.
#from check_if_good import* ##Functions which validate most of the data in the program.
import string ##Module containing functions to modify strings.

"""Functions that extract entries."""
##Returns an empty dictionary.
def get_empty_dict():
  """ (none) -> (dict)
    
    Returns an empty dictionary.
  
  """  
  return {}

##Extracts all enetred stimuli
def build_stim_dict(stimList):
  """ (dict) -> (dict)
    
    Creates the dictionary of all stimuli entries and
    checks for any invalid stimuli.
  
  """  
  global symbolsList
  hist = {}
  i = 1 ##Index for the list.
  index = 1 ##Index for the dictionary. 
  
  ##Bollean to check if there is at least one bad entry.
  oneBad = False

  for i in range (len(stimList)):
    ##Boolean to check if that particular entry is bad.
    isBad = False    
    ##Test to see if more than one word in each entry box.
    stimEntryList = stimList[i].get().split()
    if len(stimEntryList) > 1:
      isBad = True
      
    elif stimList[i].get() in hist: ##Means it's in the dictionary already.  
      if isBad == False:
        isBad = True
        
    ##Test to see if it is a number only.
    try:
        float(stimList[i].get())
        if isBad == False:
          isBad = True

    ##If not only a number, check to see if characters are valid.  
    except ValueError:   
      ##Return if there is an invalid symbol inside the word.
      for character in stimList[i].get():
        if character.upper() not in symbolsList:
          if isBad == False:
            isBad = True
  
    ##Background configured to tomato-red since it is a bad entry.
    if isBad:
      if oneBad == False:
        oneBad = True
      ##Change background to color tomato-red to indicate error.
      stimList[i].config(bg = 'tomato')
    
    else:  
      ##Background configured to white since it is a good entry.
      stimList[i].config(bg = 'white')
      ##Make sure entry is not empty.
      if stimList[i].get() != ' ' * len(stimList[i].get()):
        hist[index] = stimList[i].get().replace(' ', '')
        index += 1
          
  ##Will only return a histogram if tests are passed. 
  if oneBad:
    return None
  else:
    return hist

##Function to extract the agent name.
def get_agents(agentNames):
  """ (list) -> (list)
    
    Takes the agent entries and extracts the agent names out of
    them. The function also checks if an entry is invalid.
  
  """  
  agentNames = agentNames.copy() ##Make a copy to prevent modifying the original list (due to it being passed by reference).
  
  for i in range(len(agentNames)):
    agentEntry = agentNames[i].get() ##Get the entry.
    badEntry = False ##Assume it is not a bad entry.
    
    ##Test to see if more than one word in the entry box.
    if len(agentEntry.split()) > 1:
      badEntry = True

    ##Test to see if it is a number only.
    try:
        float(agentEntry)
        
        if badEntry == False:
          badEntry = True

    ##If not only a number, check to see if characters are valid.  
    except ValueError:   
      ##Return if there is an invalid symbol inside the word.
      for character in agentEntry:
        if character.upper() not in symbolsList:
          badEntry = True
          
      ##Save agent without any whitespace.
      agentNames[i] = agentEntry.replace(' ', '')
    
    if badEntry:
      agentNames[i] = None
  
  return agentNames    

def build_bev_dict(agentBevs):
  """ (list) -> (dict)
    
    Takes the agent behaviour entries, and extracts all
    behaviours into a dictionary for each agent. The function also validates
    the entry.
  
  """  
  allBevDict = {}
  
  for i in range(len(agentBevs)):
    isBad = False ##Assume entry is good.
    bevEntry = agentBevs[i]
    line = bevEntry.get() ##Get the line in each entry.
    
    hist = {}
    index = 1 ##Index.
    
    ##Split each line into a list of words.
    ##The split method removes the whitespace from around each word.
    wordList = line.split()
  
    ##For each word, remove any punctuation marks immediately
    ##before and after the word.
    for word in wordList:
      word = word.upper().strip(string.punctuation)
      ##Test to see if it is a number only.
      try:
        float(word)
        isBad = True
      ##If not only a number, check to see if characters are valid.  
      except ValueError:   
        ##Return if there is an invalid symbol inside the word.
        for character in word:
          if character not in symbolsList:
            isBad = True
        
        ##Make sure the entry isn't already in the dictionary.
        if word not in hist.values() and word != '':
          hist[index] = word 
          index += 1
    
    if isBad:
      allBevDict[i + 1] = None
    else: ##Only keep dictionary if good.
      allBevDict[i + 1] = hist
      
  return allBevDict  

##Function to correctly extract the agent behaviour.
def extract_full_behaviour(agentBevs): 
  """ (list) -> (dict)
    
    Takes the agent behaviour entries, and extracts the 
    behaviour into a string that contains the right amount
    of spacing.
  
  """   
  agentBehaviours = {} ##Dictionary to hold the full text describing the behaviour of each agent.
  index = 1 ##The index to keep track of the diffrent agents.
  
  for bevWords in agentBevs:
    bevWords = bevWords.get().split() ##Get every word in the entry, igoring whitespace.
    agentBehaviour = '' ##Set agent behaviour to the empty string.
    
    for i in range(len(bevWords)): ## Correctly append each word to the string.
      if i == len(bevWords) - 1: ##No whitespace if True.
        agentBehaviour += bevWords[i].upper()
      else:  
        agentBehaviour += bevWords[i].upper() + " " ##Add a whitespace to the end of each word for spacing.
    
    agentBehaviours[index] = agentBehaviour ##Put the behaviour text in the dictionary.
    index += 1

  return agentBehaviours  
    

##Function to get concrete behaviour entry.
def get_concrete_behaviours(entriesCBS):
  """ (dict) -> (dict)
    
    Parse the concrete behaviours to ignore any
    whitespace that may have been added unintentionally.
  
  """   
  ##Create the dictionary to hold the values.
  concreteBehaviours = {}
  
  ##Get the number of rows.
  numRows = entriesCBS[0, 0]
  
  for row in range(1, numRows + 1):
    line = entriesCBS[row, 1] ##Get the line of concrete behaviours.
    
    ##Split each concrete behaviour into a list of words.
    ##The split method removes the whitespace from around each word.  
    wordList = line.get().split()
    
    line = "" ##Set line to an empty string in order to store the correct concrete behaviour.
    
    ##Correctly append each word to the string.
    for i in range(len(wordList)): 
      if i == len(wordList) - 1: ##No whitespace if True.
        line += wordList[i]
      else:
        line += wordList[i] + " " ##Add a whitespace to the end of each word for spacing.
    
    ##Add the line to the dictionary at the appropriate key.
    concreteBehaviours[row] = line
  
  return concreteBehaviours      

##Function to get values form table.
def get_table_values(circleTableBoxes, lambdaTableBoxes):
  """ (dict, dict) -> (dict, dict)
    
    Extracts the table values from the table entries.
  
  """  
  ##Create dictionary to hold values from tables.
  circleTableValues = {}
  lambdaTableValues = {}  
  
  for key in circleTableBoxes.keys():
    a, b = key ##Extract corrdinate.
    if a!= 0 and b != 0: ##We are not interested in labels.
      circleTableValues[key] = (circleTableBoxes[key].get()).replace(" ", "").upper()
    
  for key in lambdaTableBoxes.keys():
    a, b = key ##Extract corrdinate.
    if a!= 0 and b != 0: ##We are not interested in labels.
      lambdaTableValues[key] = (lambdaTableBoxes[key].get()).replace(" ", "")
  return circleTableValues, lambdaTableValues

##Long, but necessary to check for valid characters.
symbolsList = ['A', "B", 'C', 'D', 'E', 'F', 'G', 'H', "I", 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ']
