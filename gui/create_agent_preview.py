"""Imported modules."""
from tkinter import * ##Import the tkinter module to allow construction of the GUI interface.
from get_word_list import * ##Functions which parse an entry box and returns lists of words.
from create_text import * ##A module containing the function that creates the final product (text file).
from create_save_file import * ##A module that contains the function to allow the text file to be saved to a certain directory. 

"""Functions to implement the preview pop-ups for each agent."""
##Function which creates, or restores, the agent specification preview page.
def create_agent_preview(main, allEditButtons, allPreviewPops, agentNames, allEntriesCBS, 
                         agentBehaviours, allTextBoxCBS, allCircleTableValues, 
                         allLambdaTableValues, stimDict, allBevDict, allRadioButtons,
                         save_icon, return_arrow, moreThanOneAgent, boxIndex):
  """ 
  
    Creates the preview page for the text file(s).
  
  """      
  
  if moreThanOneAgent:
    allEditButtons[boxIndex][0].config(state = DISABLED)
  
    if allEditButtons[boxIndex][1] == False:
      allEditButtons[boxIndex] = allEditButtons[boxIndex][0], True ##Button is now clicked.
        
      agentSpecs = Toplevel() ##Creating new window to preview agent specs.
      agentSpecs.resizable(width = False, height = False) 
      allPreviewPops[boxIndex] = agentSpecs ##Store the window at the correct index.
      
      ##Collect screen (monitor) width and height to position the window in the center. 
      screenWidth = agentSpecs.winfo_screenwidth() 
      screenHeight = agentSpecs.winfo_screenheight()       
      
      windowSize = int(screenHeight/2.16) ##Dimension of the window is about half that of the screen height.
      
      agentSpecs.geometry('%dx%d' % (windowSize, windowSize))            

      agentSpecs.protocol("WM_DELETE_WINDOW", lambda: close_preview(allEditButtons, allPreviewPops, boxIndex))   
      
      previewAgent = Frame(agentSpecs) ##Making a frame on the preview page to hold the save and return buttons.
      
      saveButton = Button(previewAgent, image = save_icon, border = 0, command = lambda: create_save_file(textEntry.get(1.0, END)))
      saveButton.pack(side = RIGHT, anchor = S)
      
      returnButton = Button(previewAgent, image = return_arrow, border = 0, command = lambda: close_preview(allEditButtons, allPreviewPops, boxIndex))
      returnButton.pack(side = LEFT, anchor = S)
      
      previewAgent.pack(side = BOTTOM, fill = X)
      
      ##Text entry to give the user a preview of the text file.
      ##Create a frame for the text box.
      textEntryFrame = Frame(agentSpecs)
      
      ##Declaring x and y scrollbars for the text box.
      xscrollbarText = Scrollbar(textEntryFrame, orient=HORIZONTAL)
      xscrollbarText.grid(row=1, column=0, sticky=N+S+E+W)
    
      yscrollbarText = Scrollbar(textEntryFrame)
      yscrollbarText.grid(row=0, column=1, sticky=N+S+E+W)
    
      ##Create the text box widget for the preview page.
      textEntry = Text(textEntryFrame, wrap=NONE,
                  xscrollcommand=xscrollbarText.set,
                  yscrollcommand=yscrollbarText.set,
                  width = int(main.winfo_screenwidth()/32))
      
      textEntry.grid(row=0, column=0)
    
      xscrollbarText.config(command=textEntry.xview)
      yscrollbarText.config(command=textEntry.yview)            
      
      ##Extract concrete behaviour in a dictionary.
      concreteBehaviours = get_concrete_behaviours(allEntriesCBS[boxIndex])      

      ##Call create_text() to create the agentspec.txt file.
      create_text(agentNames[boxIndex], agentBehaviours[boxIndex + 1], concreteBehaviours, 
                  allTextBoxCBS[boxIndex], allCircleTableValues[boxIndex + 1], 
                  allLambdaTableValues[boxIndex + 1], stimDict, allBevDict[boxIndex + 1], 
                  allRadioButtons[boxIndex][2])
      
      ##Configure the text entry to be modifiable.
      textEntry.config(state = 'normal')
      ##Remove the previous text to insert new one.
      textEntry.delete(1.0, END)
      textEntry.insert(INSERT, open("agent_text_backup./agentspec.txt", "r").read())
      ##Configure the text entry so that it cannot be modified.
      textEntry.config(state="disabled")
      ##Pack the text entry frame to give a preview to the user.
      textEntryFrame.pack(expand = True)        
           
    else:
      allPreviewPops[boxIndex].deiconify() ##Bring back the withdrawn window.
 
  else: ##One Agent.
    ##Create the save button.
    saveButton = Button(main, image = save_icon, border = 0, command = lambda: create_save_file(textEntry.get(1.0, END)))      
    
    ##Text entry to give the user a preview of the text file.
    ##Create a frame for the text box.
    textEntryFrame = Frame(main)
    
    ##Declaring x and y scrollbars for the text box.
    xscrollbarText = Scrollbar(textEntryFrame, orient=HORIZONTAL)
    xscrollbarText.grid(row=1, column=0, sticky=N+S+E+W)
  
    yscrollbarText = Scrollbar(textEntryFrame)
    yscrollbarText.grid(row=0, column=1, sticky=N+S+E+W)
  
    ##Create the text box widget for the preview page.
    textEntry = Text(textEntryFrame, wrap=NONE,
                xscrollcommand=xscrollbarText.set,
                yscrollcommand=yscrollbarText.set,
                width = int(main.winfo_screenwidth()/32))
    
    textEntry.grid(row=0, column=0)
  
    xscrollbarText.config(command=textEntry.xview)
    yscrollbarText.config(command=textEntry.yview)          
    
    ##Extract concrete behaviour in a dictionary.
    concreteBehaviours = get_concrete_behaviours(allEntriesCBS[boxIndex])            

    ##Call create_text() to create the agentspec.txt file.
    create_text(agentNames[boxIndex], agentBehaviours[boxIndex + 1], concreteBehaviours, 
                allTextBoxCBS[boxIndex], allCircleTableValues[boxIndex + 1], 
                allLambdaTableValues[boxIndex + 1], stimDict, allBevDict[boxIndex + 1], 
                allRadioButtons[boxIndex][2])
    
    ##Configure the text entry to be modifiable.
    textEntry.config(state = 'normal')
    ##Remove the previous text to insert new one.
    textEntry.delete(1.0, END)
    textEntry.insert(INSERT, open("agent_text_backup./agentspec.txt", "r").read())
    ##Configure the text entry so that it cannot be modified.
    textEntry.config(state="disabled")
    ##Pack the text entry frame to give a preview to the user.
    textEntryFrame.pack(expand = True)
    
    ##Pack the button allowing the user to save the file if satisfied
    ##with the result.
    saveButton.pack(anchor = S)       
    
    ##Widgets must be returned to be unpacked later.
    return textEntryFrame, saveButton
    
##Function to close the preview page for the agent specification. 
def close_preview(allEditButtons, allPreviewPops, boxIndex):
  """ (tkinter.Button, tkinter.Toplevel, int) -> (none)
    
    Destroys the editAgent window 
  
  """

  allPreviewPops[boxIndex].withdraw() ##Hides, but does not destroy the window.

  allEditButtons[boxIndex][0].config(state = NORMAL) ##Re-enable the preview button.