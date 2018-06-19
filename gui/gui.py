""" Internship Project.

GUI to Assist the C2KA TOOL.
"""

"""Imported modules."""
from tkinter import * ##Import the tkinter module to allow construction of the GUI interface.
from check_if_good import * ##Functions which validate most of the data in the program.
from entry_mods import * ##Functions which modify entry boxes.
from get_word_list import * ##Functions which parse an entry box and returns lists of words.
from create_agent_page import *
from set_data import *
from CBS_radio import * ##Functions that set the CBS page depending on which radio button is clicked.
from CBS_mods import * ##Functions which modify the concrete behaviours page.
from create_table import * ##Functions which create/recreate the tables.
from fix_grids import * ##Functions which modifies the data currently stored in memory for the tables to match the data modified by the user.
from create_text import * ##A module containing the function that creates the final product (text file).
from create_save_file import * ##A module that contains the function to allow the text file to be saved to a certain directory. 
import vertSuperscroll ##Module containing the widget allowing a vertical scrollbar.
import superscroll ##Module containing the widget allowing a vertical and horizontal scrollbar.

"""Next and previous button functions."""
##Note: some global variables will be used due to the button functions
##being unable to contain parameters.
   
##Function to go to the next page.
def next_page():
  """ (none) -> (none)
    
    Allows the configuration of the next page 
    in the program depending on the current
    pageNum. Saves the collected entries (data)
    in global data structures.
  
  """
  global pageNum ##Keeps track of the page number.
  
  global stimDict ##Dictionary to hold final entries of entered stimuli.
  global allBevDict ##Dictionary to hold agent behaviours.
  
  global agentNames ##Record entries for the name of the agents.
  global agentBehaviours ##Record entries for the behaviour of the agents.
  
  global frameCBS ##Frame to hold concrete behaviours.
  global agentCBS ##Label for the agent name on the concrete behaviours page.
  
  global concreteScrollingArea ##Scrolling area for the concrete behaviours (CBS).
  
  global allEntriesCBS ##Dict to hold concrete behaviour labels and entries.
  global allRadioButtons
  global allTextCBS
  global concreteBehaviours ##Dict to hold parsed concrete behaviours
  
  global allCircleTableBoxes ##Dict to hold entry boxes and labels of circle table for all agents.
  global allLambdaTableBoxes ##Dict to hold entry boxes and labels of lambda table for all agents.
  
 # global circleTableValues ##Dict to hold values from circle table.   #Might not need this...
 # global lambdaTableValues ##Dict to hold values from lambda table.   #Might not need this...
  
  global circleScrollingArea ##Scrolling area for circle table.
  global lambdaScrollingArea ##Scrolling area for lambda table.
  
  global allCircleGridFrame ##Global frame for the circle table.
  global allLambdaGridFrame ##Global frame for the lambda table.
  
  global moreThanOneAgent
  global generatedTable ##Bool variable to check if tables were generated.
  global generatedCBS ##Bool variable to check if CBS were generated.
  
  ##Note: dictionaries are set empty when swithing to a next page
  ##(depending on pageNum) in order to update the data.
  
  """PAGE 1 to PAGE 2."""
  if pageNum == 1:
    stimDict = get_empty_dict() ##Stimuli dictionary set empty.
    stimDict = build_stim_dict(stimList) ##Stimuli dictionary is created usign the list of stim entries.
    
    if stimDict == None or len(stimDict) == 0: ##User must imput at least one valid stimulus.
      ##Stay on current page.
      incorrect_stims(main, return_arrow) ##Calls function for pop-up.
      pageNum -= 1 ##Decrease pageNum by one to stay on current page.    
     
    else: ##User inputted valid stimuli.
      ##Set new page by unpacking widgets on page 1.
      stimScrollingArea[0].pack_forget()
      addStim.pack_forget()
      stimFrame.pack_forget()
      
      ##Pack the new previous button.
      prevButton.pack(in_=buttonsFrame, side = LEFT, anchor = S)
      
      ##Pack new scrolling area for the agent and its behaviours,
      ##and pack the button to add an agent.
      agentScrollingArea[0].pack(expand = 1, fill = BOTH, pady = (0, 80))  
      
      addAgent.pack(in_=buttonsFrame, side = TOP)
  
  """PAGE 2 to PAGE 3."""
  if pageNum == 2: 
    agentsGood = True 
    
    agentNames = get_agents(agentFrames['agentNames']) ##The agent names are extracted from the entries in a list.
    allBevDict = build_bev_dict(agentFrames['agentBev']) ##Creates a behaviour dictionary for each agent.
    allEntriesCBS = {}
    for i in range(len(agentNames)):
      if agentNames[i] == None or agentNames[i] == '': ##User must input one valid agent to proceed.
        ##Change background colour of the agent entry to tomato-red to warn user.
        agentFrames['agentNames'][i].config(bg = 'tomato')
        ##Stay on current page by warning the user with a pop-up.
        
        if pageNum == 2: ##Only decrease pageNum once.
          ##Decrease pageNum to stay on current page.
          agentsGood = False
          incorrect_agent(main, return_arrow)        
          pageNum -= 1    
       
      else: ##Entry is good.
        agentFrames['agentNames'][i].config(bg = 'white')
        
    for i in range(len(allBevDict)):
      if allBevDict[i + 1] == None or len(allBevDict[i + 1]) == 0: ##User must input one valid agent to proceed.
        ##Change background colour of the agent entry to tomato-red to warn user.
        agentFrames['agentBev'][i].config(bg = 'tomato')
        ##Stay on current page by warning the user with a pop-up.
        
        if pageNum == 2: ##Only decrease pageNum once.
          ##Decrease pageNum to stay on current page.
          agentsGood = False
          incorrect_bevs(main, return_arrow)        
          pageNum -= 1    
       
      else: ##Entry is good.
        agentFrames['agentBev'][i].config(bg = 'white')
   
    if agentsGood:
      ##Before going to the next page, extract the full text describing 
      ##the agents' behaviour (used when create the text file).
      agentBehaviours = extract_full_behaviour(agentFrames['agentBev'])
      
      ##Set new page by unpacking scrolling area on page 2 and the add agent button.
      agentScrollingArea[0].pack_forget()      
      addAgent.pack_forget()
      
      if len(agentFrames['agentNames']) > 1: ##More than one agent calls for a diffrent layout.
        moreThanOneAgent = True
        create_agent_page(main, editScrollingArea, allBevDict, stimDict, agentNames, allCircleTableBoxes, allLambdaTableBoxes, allEntriesCBS)
        pageNum += 1 ##Add one to pageNum because we are skipping page 4.
      
      else: ##Only one agent.            
        
        ##Pack new labels for CBS.
        agentCBS = Label(main, text = agentNames[0] + ' =>')
        titleCBS.pack(side = TOP)
        agentCBS.pack(side = TOP, anchor = W)
  
        ##If no concrete behaviours were yet generated for the behaviours,
        ##then we generate the rows for the CBS.
        if generatedCBS == False:   
          ##Create a vertical scrolling area for the rows.
          concreteScrollingArea = vertSuperscroll.Scrolling_Area(main, width=1, height=1)
          concreteScrollingArea.pack(expand=1, fill = BOTH)   
          ##create a frame for the rows within the scrolling area.
          frameCBS = Frame(concreteScrollingArea.innerframe)
          frameCBS.pack(anchor = W)
          
          ##Call create_CBS_entries() to create the rows in the CBS frame.
          entriesCBS= create_CBS_entries(allBevDict[1], frameCBS)
          
          ##Save the number of CBS in the allBevDict[1] dictionary at key (0, 0) since
          ##that coordinate is unused.
          entriesCBS[0, 0] = len(allBevDict[1])
          
          ##Set generatedCBS to True.
          generatedCBS = True
   
        ##If concrete behaviours page was already generated, it must be modified 
        ##if necessary to adapt to changes made on previous pages.
        else:
          ##fix_CBS() function will modify the data scructures related to CBS.
          entriesCBS= fix_CBS(allBevDict[1], frameCBS, entriesCBS)
          
          ##Create a temporary scrolling area that will be later used as the main scrolling
          ##area. This is done in order to destroy the previous scrolling area
          ##at the end of the else statement once all the necessary widgets were
          ##saved from the old frame.
          concreteScrollingAreaTemp = vertSuperscroll.Scrolling_Area(main, width = 1, height = 1)
          
          ##Create a temporary frame to hold CBS (for the same reason described 
          ##in the temporary scrolling area).
          frameCBSTemp = Frame(concreteScrollingAreaTemp.innerframe)
          
          ##calling recreate_CBS_entries() to recreate the CBS rows in the new 
          ##temporary frame.
          entriesCBS = recreate_CBS_entries(allBevDict[1], entriesCBS, frameCBSTemp)
          
          ##Destroy the old scrolling area and the old frame for the CBS.
          concreteScrollingArea.destroy()
          frameCBS.destroy()        
          
          ##Assing the old scrolling area and the old frame to the new ones.
          concreteScrollingArea = concreteScrollingAreaTemp
          frameCBS = frameCBSTemp         
          
          if whichRadio.get() == 'Rows': ##Repack the scrolling area if the user was previously using that display.     
            ##Pack the new scrolling area and the new frame for the CBS.
            concreteScrollingAreaTemp.pack(expand=1, fill = BOTH)
            frameCBSTemp.pack(anchor =  W)
          
          else: ##Repack the text box. 
            textBoxCBSFrame.pack()
          
        ##Pack frame for the radio Buttons
        formatCBS.pack(side = BOTTOM, anchor = S, expand = True)      
  
  """PAGE 3 to PAGE 4."""
  if pageNum == 3 and moreThanOneAgent == False:
    ##Boolean variable for validity of entries.

    isGoodCBS = check_if_good_CBS(main, entriesCBS, whichRadio, textBoxCBS)

    ##If there are invalid entries, create popup.
    if isGoodCBS == False:
      incorrect_CBS(main, return_arrow) ##Calls function for pop-up.

      pageNum -= 1 ##Decrease pageNum by one to stay on current page. 

    else: ##Entries are good.    
      ##Extract concrete behaviour in a dictionary.
      concreteBehaviours = get_concrete_behaviours(entriesCBS)
      
      ##Set new page by forgetting the CBS related frames and entries.
      if whichRadio.get() == 'Rows': ##User was using rowsCBS.
        frameCBS.pack_forget()
        concreteScrollingArea.pack_forget()
        
      else: ##User was using boxCBS.
        textBoxCBSFrame.pack_forget()
      
      ##Unpack widgets available to both radio buttons.  
      titleCBS.pack_forget()
      agentCBS.pack_forget()
      formatCBS.pack_forget()
      
      ##Pack the fillBev button which fills the circle table with the 
      ##behaviour found on each row.
      fillBev.pack(in_=buttonsFrame, side = LEFT)         
      
      ##Pack the fillN button which fills the lambda table with the 
      ##neutral stimulus.
      fillN.pack(in_=buttonsFrame, side = RIGHT)   
     
      allCircleTableBoxes, allLambdaTableBoxes, circleScrollingArea, lambdaScrollingArea, allCircleGridFrame, allLambdaGridFrame = set_table_data(main, allBevDict, stimDict, allCircleTableBoxes, 
                                                                                                        allLambdaTableBoxes, circleScrollingArea, 
                                                                                                        lambdaScrollingArea, allCircleGridFrame, 
                                                                                                        allLambdaGridFrame, generatedTable,  0)
      generatedTable = True
     
  """PAGE 4 to PAGE 5."""
  if pageNum == 4:
    ##Create dictionaries to hold the values from tables.
    allCircleTableValues = get_empty_dict()
    allLambdaTableValues = get_empty_dict()
   
    ##Extract circle table values and lambda table values for each agent.
    for i in range(len(agentNames)):
      allCircleTableValues[i + 1], allLambdaTableValues[i + 1] = get_table_values(allCircleTableBoxes[i + 1], 
                                                                                  allLambdaTableBoxes[i + 1]) 
     
      ##Calling check_if_good() to assure all the inputs are valid.
      isGood, numInvalid = check_if_good_table(allBevDict[i + 1], stimDict, allCircleTableBoxes[i + 1], 
                                         allLambdaTableBoxes[i + 1], allCircleTableValues[i + 1], 
                                         allLambdaTableValues[i + 1])
    ##If the table is good, proceed.
    if isGood:
      ##Forget table scrolling areas.
      circleScrollingArea[0].pack_forget()
      lambdaScrollingArea[0].pack_forget()
    
      ##Forget table frames.
      allCircleGridFrame[0].pack_forget()
      allLambdaGridFrame[0].pack_forget()
    
      ##Forget next button, fillBev button and fillN button, since they are not
      ##needed on the last page of the program.
      fillBev.pack_forget()
      fillN.pack_forget()
      nextButton.pack_forget()
    
      ##Call create_text() to create the agentspec.txt file.
      create_text(agentNames[0], agentBehaviours[1], concreteBehaviours, textBoxCBS, 
                  allCircleTableValues[1], allLambdaTableValues[1], stimDict, allBevDict[1], whichRadio)
      
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
      saveButton.pack(in_=buttonsFrame)
    
    ##Table is not good.
    else:
      ##Deliver a pop-up to the user to warn of invalid entries in the table.
      incorrect_table(main, numInvalid, return_arrow)
      ##Decrease pageNum to stay on current page.
      pageNum -= 1
  
  ##Add one to pageNum everytime the next button is clicked.
  pageNum += 1

##Function to return to the previous page.
def prev_page():
  """ (none) -> (none)
    
    Allows the configuration of the previous page 
    in the program depending on the current
    pageNum. Unpacks newer widgets and packs older ones.
  
  """  
  global pageNum ##Keeps track of the page number.
 
  """PAGE 2 to PAGE 1."""
  if pageNum == 2:
    ##Repack the scrolling area for the stimuli.
    stimScrollingArea[0].pack(expand=1, fill=BOTH)     
   
    ##Set new page by unpacking addAgent button and the scrolling area for the agents.
    agentScrollingArea[0].pack_forget()
    addAgent.pack_forget()
    
    ##Unpack the previous button since it it not necessary on page 1.
    prevButton.pack_forget()
    
    ##Pack buttons for stimuli and frame to specify number of stimuli.
    stimFrame.pack(side = BOTTOM, anchor = S, expand = True, pady = 50)

    addStim.pack(in_=buttonsFrame, side = LEFT)

  """PAGE 3 to PAGE 2.""" 
  if pageNum == 3:
    ##Repack the agent scrolling area and the add agent button.
    agentScrollingArea[0].pack(expand = 1, fill = BOTH)
    addAgent.pack(in_=buttonsFrame, side = TOP)
    
    ##Checking which widgets to unpack from the window.
    if (whichRadio.get() == 'Rows'): ##Radio button was on rowsCBS.
      ##Forget the scrolling area for the CBS.
      concreteScrollingArea.pack_forget()
      frameCBS.pack_forget()
      
    else:##Radio button was on boxCBS.
      ##Forget the text box frame.
      textBoxCBSFrame.pack_forget()
      
    ##Forget the title and radio button frame regardless of which radio button was pressed.  
    titleCBS.pack_forget()
    agentCBS.pack_forget()      
    formatCBS.pack_forget()
  
  """PAGE 4 to PAGE 3."""
  if pageNum == 4:
    
    ##Forget scrolling areas and frames for the tables.
    circleScrollingArea.pack_forget()
    lambdaScrollingArea.pack_forget()
  
    circleGridFrame.pack_forget()
    lambdaGridFrame.pack_forget()
  
    ##Forget the fillBev and fillN button.
    fillBev.pack_forget()
    fillN.pack_forget()
 
    ##Pack widgets related to CBS page.
    titleCBS.pack(side = TOP)
    agentCBS.pack(side = TOP, anchor = W)  
    
    if whichRadio.get() == 'Rows': ##User was using rowsCBS.
      frameCBS.pack(anchor = W)
      concreteScrollingArea.pack(expand =1, fill = BOTH)
    
    else: ##User was using boxCBS.
      textBoxCBSFrame.pack()  
    
    ##Pack frame for the radio Buttons
    formatCBS.pack(side = BOTTOM, anchor = S, expand = True)    

  """PAGE 5 to PAGE 4."""
  if pageNum == 5:
    ##Forget text preview box and save button.
    textEntryFrame.pack_forget()
    saveButton.pack_forget()
  
    ##Repack table scrolling areas.
    circleScrollingArea.pack(expand=1, fill = BOTH)   
    lambdaScrollingArea.pack(expand=1, fill = BOTH)   
  
    ##Repack table frames.
    circleGridFrame.pack(side=TOP, anchor = NW) 
    lambdaGridFrame.pack(side=TOP, anchor = SW) 
  
    ##Repack the next button, fillBev button and fillN button.
    nextButton.pack(in_=buttonsFrame, side = RIGHT)
    fillBev.pack(in_=buttonsFrame, side = LEFT)
    fillN.pack(in_=buttonsFrame, side = RIGHT)
  
  ##Decrease pageNum every time the previous button is clicked.
  pageNum -= 1

if __name__ == '__main__': ##only start program when running gui.py
  
  """Code related to the main program's window."""
  main = Tk() ##The main window for the program.
  main.title("C2KA GUI") ##Title for the main window.
  main.resizable(width = False, height = False) ##The main window is not resizeable.
  mainStyle = ttk.Style()
  mainStyle.theme_use("clam")
  
  windowSize = 500 ##500 is the dimension that will be used for the window (500 x 500).
  
  ##Collect screen (monitor) width and height to position the program's main window in the center. 
  screenWidth = main.winfo_screenwidth() 
  screenHeight = main.winfo_screenheight()
  
  ##Calculate the center position.
  positionRight = screenWidth/2 - windowSize/2
  positionDown = screenHeight/2 - windowSize/2
  
  ##Set the window size using the geometry() method.
  main.geometry('%dx%d+%d+%d' % (windowSize, windowSize, positionRight, 
                                 positionDown))
  
  """Code to load initial data/widgets in the main window.""" 
  ##Initializing the page number variable and the stimuli list.
  stimList = []
  pageNum = 1
  
  ##Initializing the lists to hold the data for each agent.
  agentFrames = {} ##Stores the entry boxes for each agent name and the entry boxes for each agent behaviour.
  agentFrames['agentNames'] = []
  agentFrames['agentBev'] = []
  
  circleScrollingArea, lambdaScrollingArea = [], [] ##Bind these to empty lists to allow them to be passed as arguments.
  
  ##Dictionaries to hold all circle grid frames and lambda grid frames
  allCircleGridFrame = []
  allLambdaGridFrame = []
  
  ##Dictionaries to hold all circle table boxes and lambda table boxes
  allCircleTableBoxes = {}
  allLambdaTableBoxes = {}
  
  ##Assuming there will be only one agent.
  moreThanOneAgent = False
  
  ##No concrete behaviours generated yet.
  generatedCBS = False
  
  ##No tables generated yet.
  generatedTable = False
  
  ##Frame to hold the main buttons
  buttonsFrame = Frame(main)
  buttonsFrame.pack(side = BOTTOM, anchor = S, fill = X)
  
  ##Frame for the stim number Label, button and entry box (to specify
  ##a number of stimuli to be generated).
  stimFrame = Frame(main)
  stimFrame.pack(side = BOTTOM, anchor = S, expand = True, pady = 50)
  
  """Pictures and Fonts used for Buttons and Entries"""
  check_mark = PhotoImage(file = "images./check_mark.png")
  right_arrow = PhotoImage(file="images./right_arrow.png")
  left_arrow = PhotoImage(file="images./left_arrow.png")
  return_arrow = PhotoImage(file = "images./return_arrow.png")
  remove_x = PhotoImage(file = "images./remove_x.png")
  save_icon = PhotoImage(file = "images./save_icon.png")
  entry_font = ('Comic Sans MS', 11)

  """Defining Buttons available on each page.""" 
  ##Next Button (will not be available on page 5).
  nextButton = Button(main, command = next_page, image = right_arrow, width = "25", height = "25", border = 0)
  nextButton.pack(in_=buttonsFrame, side = RIGHT, anchor = E)

  ##Prev Button (will not be availible on page 1).
  prevButton = Button(main, command = prev_page, image = left_arrow, width = "25", height = "25", border = 0)
  
  """Label and Buttons exclusive to page 1."""  
  ##The scrolling area is at index zero of the stimScrollingArea list, this way, 
  ##the scrolling area can be passed by reference and be modified by other functions.
  stimScrollingArea = [vertSuperscroll.Scrolling_Area(main)]
  stimScrollingArea[0].pack(expand = 1, fill = BOTH)

  ##Title for the stimuli on page 1.
  stimTitle = Label(stimScrollingArea[0].innerframe, text='Please Enter The Stimuli')
  stimTitle.pack(side = TOP)
  
  ##Label, button and entry box to generate specified number of stimuli.
  enterStimLabel = Label(main, text = 'Enter # of stimuli : ')
  enterStimLabel.pack(in_=stimFrame, side = LEFT)
  
  enterStimButton = Button(main, image = check_mark, border = 0, command = lambda: specify_stim(main, stimList, enterStimBox.get(), stimScrollingArea, remove_x, return_arrow))
  enterStimButton.pack(in_=stimFrame, side = RIGHT, anchor = N)
  
  enterStimBox = ttk.Entry(main, font = entry_font)
  enterStimBox.pack(in_=stimFrame, side = TOP)
  
  ##Add stimulus entry Button.
  addStim = Button(main, text = 'Add new stimulus', 
                   command = lambda: add_stim(main, stimList, stimScrollingArea, remove_x), 
                   width = 23)
  
  addStim.pack(in_=buttonsFrame, side = LEFT)
  
  """Labels and Entries exclusive for page 2.""" 
  ##The scrolling area is at index zero of the bevScrollingArea list, this way, 
  ##the scrolling area can be passed by reference and be modified by other functions.
  agentScrollingArea = [vertSuperscroll.Scrolling_Area(main)]
  
  ##Add agent entry Button.
  addAgent = Button(main, text = 'Add new agent', 
                   command = lambda: add_agent(main, agentFrames, agentScrollingArea, remove_x), 
                   width = 23)  
  
  """For edit page"""
  editScrollingArea = [vertSuperscroll.Scrolling_Area(main)]
  
  """Labels and Entries exclusive for page 3."""
  ##Title for the concrete behaviours.
  titleCBS = Label(main, text='Concrete Behaviours')
  
  ##Frame for the two radio buttons.
  formatCBS = Frame(main)
  
  ##Set a variable that the radio Buttons share to determine what happens when 
  ##one of them is pressed.
  whichRadio = StringVar()
  whichRadio.set('Rows')  
  
  ##Create a frame for the text box.
  textBoxCBSFrame = Frame(main)
  
  ##Declaring x and y scrollbars for the CBS text box.
  xscrollbarCBS = Scrollbar(textBoxCBSFrame, orient=HORIZONTAL)
  xscrollbarCBS.grid(row=1, column=0, sticky=N+S+E+W)

  yscrollbarCBS = Scrollbar(textBoxCBSFrame)
  yscrollbarCBS.grid(row=0, column=1, sticky=N+S+E+W)

  content = StringVar()
  ##Create the text box widget for the CBS page.
  textBoxCBS = Text(textBoxCBSFrame, wrap=NONE,
              xscrollcommand=xscrollbarCBS.set,
              yscrollcommand=yscrollbarCBS.set,
              width = 60)
  
  textBoxCBS.grid(row=0, column=0)

  xscrollbarCBS.config(command=textBoxCBS.xview)
  yscrollbarCBS.config(command=textBoxCBS.yview)    
  
  ##Radio button for the default style of entering concrete behaviours.
  radioRowsCBS = Radiobutton(main, text = 'CBS Rows', variable = whichRadio, value = 'Rows', 
                             state = 'disabled', command = lambda: change_CBS(radioRowsCBS, 
                             radioBoxCBS, concreteScrollingArea, frameCBS, textBoxCBSFrame, whichRadio))
  radioRowsCBS.pack(in_=formatCBS, side = LEFT)
  
  ##Radio button for the alternate style of entering concrete behaviours.
  radioBoxCBS = Radiobutton(main, text = 'CBS Box', variable = whichRadio, value = 'Box', 
                            command = lambda: change_CBS(radioRowsCBS, radioBoxCBS, 
                            concreteScrollingArea, frameCBS, textBoxCBSFrame, whichRadio))
  radioBoxCBS.pack(in_=formatCBS, side = RIGHT)

  """Labels and Entries exclusive for page 4."""
  ##Button to fill circle table with beahviour in each row.
  fillBev = Button(main, text = 'Fill with Behaviours', 
                 command = lambda: fill_bev(allBevDict[1], stimDict, circleTableBoxes), 
                 width = 31)  
  
  ##Button to fill lambda table with neutral stimulus.
  fillN = Button(main, text = 'Fill with neutral stimulus', 
                 command = lambda: fill_n(allBevDict[1], stimDict, lambdaTableBoxes), 
                 width = 31)
  
  """Labels and Entries exclusive for page 5."""
  ##Text entry to give the user a preview of the text file.
  ##Create a frame for the text box.
  textEntryFrame = Frame(main)
  textEntry = Text(textEntryFrame)
  
  ##Declaring x and y scrollbars for the text box.
  xscrollbarText = Scrollbar(textEntryFrame, orient=HORIZONTAL)
  xscrollbarText.grid(row=1, column=0, sticky=N+S+E+W)

  yscrollbarText = Scrollbar(textEntryFrame)
  yscrollbarText.grid(row=0, column=1, sticky=N+S+E+W)

  ##Create the text box widget for the preview page.
  textEntry = Text(textEntryFrame, wrap=NONE,
              xscrollcommand=xscrollbarText.set,
              yscrollcommand=yscrollbarText.set,
              width = 60)
  
  textEntry.grid(row=0, column=0)

  xscrollbarText.config(command=textEntry.xview)
  yscrollbarText.config(command=textEntry.yview)    
  
  ##Save button to have the user save the text file.
  saveButton = Button(main, image = save_icon, border = 0, command = create_save_file)
  
  """Loop the main window."""
  main.mainloop()