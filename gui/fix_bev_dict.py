"""Functions to order behaviours correctly."""

##A function that iterates to common looking words
def fix_bev_dict(bevDict):
  """ (dict) -> (dict)
    
    Sorts the behaviour dictionary with the intent of grouping similar
    words together. 
    
    For example, AVG1, K, AVG2 would get sorted to AVG1, AVG2, K.
    
    Or, AVG2, K, AVG1 would get sorted to AVG1, AVG2, K.
    
    The order of the behaviours is based on which word was written
    first in the behaviour specification.
  
  """    
  for index in range(1, len(bevDict)): ##No need to visit very last behaviour, hence, not len(bevDict) + 1.
    bev = ''.join([i for i in bevDict[index] if not i.isdigit()]) ##Remove digits in the name; example, AVG1 becomes AVG.
    
    nextKey = index + 1 ##Assume that the next key is subject to switching.
    
    while nextKey <= len(bevDict): ## nextKey must not be used to access a key outside the dictionary.
          
        currBev = ''.join([i for i in bevDict[nextKey] if not i.isdigit()]) ##Checking for what the current behaviour at nextKey looks like without its digits.
          
        if bev == currBev: ##If True, then both behaviours are similar words.  
              
            if bevDict[index] > bevDict[nextKey]: ##ex: AVG2 comes before AVG1.  
                bevDict[index], bevDict[nextKey] = bevDict[nextKey], bevDict[index]                
              
            bevDict = sort_bev(index, nextKey, bevDict) ##Call a function to properly sort the dictionary.
            
        nextKey += 1 ##Increment to the next key.   
          
  return bevDict      

##A function that swaps (similar to bubble sort) from the first index up
##to the last one in a dictionary.
def sort_bev(initIndex, finalIndex, bevDict):
  """ (int, int, dict) -> (dict)
    
    Based on the intial and final indices, the behaviour
    dictionary is swapped its values in a manner similar to bubble sort.
  
  """  
  auxBev = bevDict[finalIndex] ##Store behaviour at last index.
  
  for i in range(finalIndex - initIndex): ##Iterate to swap values.
    bevDict[finalIndex - i] = bevDict[finalIndex - i - 1]
      
  bevDict[initIndex + 1] = auxBev ##Put the stored behaviour next to the current key.   
  
  return bevDict