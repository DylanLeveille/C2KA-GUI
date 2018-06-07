"""Imported modules."""
from tkinter import filedialog ##Module which implements the file explorer. 

""""Function that prompts save location."""
def create_save_file():
  """ (none) -> (none)
    
    Extracts the user's desired save path for the text file,
    and saves the text file at that location.
  
  """   
  ##Extract path Name from file explorer.
  pathName =  filedialog.asksaveasfilename(initialdir = "/", title = "Save text file", filetypes = ((".txt","*.txt"), ("all files","*.*")), initialfile = 'agentspec.txt')

  if pathName!= '': ##PathName is '' when user closes file explorer (no selection).
      
      dst = open(pathName, "w+")
      src = open("agentspec.txt", "r")
      dst.write(src.read()) ##Copies text from the source to the destination.
      
      ##Close each file.
      dst.close()
      src.close()