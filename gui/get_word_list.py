import string

def build_histogram(line):
  hist = []
  
  # Split each line into a list of words.
  # The split method removes the whitespace from around each word.
  word_list = line.split()
  

  # For each word, remove any punctuation marks immediately
  # before and after the word.
  for word in word_list:
    word = word.strip(string.punctuation)
    
  # Don't count any empty strings created when the punctuation marks
  # are removed. For example, if word is bound to a hyphen, '-',
  # word.strip(string.punctuation) yields the empty string, ''.
  
    if word != '' and word not in hist:
      hist.append(word)

  return hist

