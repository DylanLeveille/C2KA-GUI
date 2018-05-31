import string
from tkinter import*
from check_if_good import*

def build_bev_dict(line):
  hist = {}
  i = 1 #index
  
  # Split each line into a list of words.
  # The split method removes the whitespace from around each word.
  word_list = line.split()

  # For each word, remove any punctuation marks immediately
  # before and after the word.
  for word in word_list:
    word = word.upper()
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
      
      # Don't count any empty strings created when the punctuation marks
      # are removed. For example, if word is bound to a hyphen, '-',
      # word.strip(string.punctuation) yields the empty string, ''.
      if word not in hist:
        hist[i] = word 
        i += 1
      
  #will only return a histogram if tests are passed    
  return hist

def build_stim_dict(stimList):
  global symbolsList
  hist = {}
  i = 1 #index for the list
  index = 1 #index for the dictionary 

  for i in range (len(stimList)):
    #test to see if it is a number only
    try:
        float(stimList[i].get())
        return None
    #if not only a number, check to see if characters are valid  
    except ValueError:   
      #return if there is an invalid symbol inside the word
      for character in stimList[i].get():
        if character.upper() not in symbolsList:
          return None
      
      # Don't count any empty strings created when the punctuation marks
      # are removed. For example, if word is bound to a hyphen, '-',
      # word.strip(string.punctuation) yields the empty string, ''.
      if stimList[i].get() not in hist and stimList[i].get() != ' ' * len(stimList[i].get()):
        hist[index] = stimList[i].get()
        index += 1
  #will only return a histogram if tests are passed    
  return hist  

#long, but necessary to check valid characters
symbolsList = ['A', "B", 'C', 'D', 'E', 'F', 'G', 'H', "I", 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
