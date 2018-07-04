"""Functions to order behaviours correctly."""

##A function that iterates to common looking words
def fix_dict_order(wordDict):
  """ (dict) -> (dict)
    
    Sorts the stimuli/behaviour dictionary with the intent of grouping similar
    words together. 
    
    For example, AVG1, K, AVG2 would get sorted to AVG1, AVG2, K.
    
    Or, AVG2, K, AVG1 would get sorted to AVG1, AVG2, K.
    
    The order of the stimuli/behaviours is based on which word was written
    first in the behaviour specification.
  
  """    
  for index in range(1, len(wordDict)): ##No need to visit very last behaviour, hence, not len(bevDict) + 1.
    word = ''.join([i for i in wordDict[index] if not i.isdigit()]) ##Remove digits in the name; example, AVG1 becomes AVG.
    
    nextKey = index + 1 ##Assume that the next key is subject to switching.
    
    while nextKey <= len(wordDict): ## nextKey must not be used to access a key outside the dictionary.
          
        currWord = ''.join([i for i in wordDict[nextKey] if not i.isdigit()]) ##Checking for what the current stimulus/behaviour at nextKey looks like without its digits.
          
        if word == currWord: ##If True, then both stimuli/behaviours are similar words.  
              
            if wordDict[index] > wordDict[nextKey]: ##ex: AVG2 comes before AVG1.  
                wordDict[index], wordDict[nextKey] = wordDict[nextKey], wordDict[index]                
              
            wordDict = sort_words(index, nextKey, wordDict) ##Call a function to properly sort the dictionary.
            
        nextKey += 1 ##Increment to the next key.   
          
  return wordDict      

##A function that swaps (similar to bubble sort) from the first index up
##to the last one in a dictionary.
def sort_words(initIndex, finalIndex, wordDict):
  """ (int, int, dict) -> (dict)
    
    Based on the intial and final indices, the stimuli/behaviour
    dictionary is swapped its values in a manner similar to bubble sort.
  
  """  
  auxWord = wordDict[finalIndex] ##Store stimulus/behaviour at last index.
  
  for i in range(finalIndex - initIndex): ##Iterate to swap values.
    wordDict[finalIndex - i] = wordDict[finalIndex - i - 1]
      
  wordDict[initIndex + 1] = auxWord ##Put the stored stimulus/behaviour next to the current key.   
  
  return wordDict