""" Internship Project.

GUI to Assist the C2KA TOOL.
"""

"""Imported modules."""
from tkinter import * ##Import the tkinter module to allow construction of the GUI interface.
from check_if_good import * ##Functions which validate most of the data in the program.
from entry_mods import * ##Functions which modify entry boxes.
from get_word_list import * ##Functions which parse an entry box and returns lists of words.
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
  global bevDict ##Dictionary to hold agent behaviours.
  
  global agentName ##Record entry for the name of the agent.
  global agentBehaviour ##Record entry for the behaviour of the agent.
  
  global frameCBS ##Frame to hold concrete behaviours.
  global agentCBS ##Label for the agent name on the concrete behaviours page.
  
  global concreteScrollingArea ##Scrolling area for the concrete behaviours (CBS).
  
  global entriesCBS ##Dict to hold concrete behaviour labels and entries.
  global concreteBehaviours ##Dict to hold parsed concrete behaviours
  
  global circleTableBoxes ##Dict to hold entry boxes and labels of circle table.
  global lambdaTableBoxes ##Dict to hold entry boxes and labels of lambda table.
  
  global circleTableValues ##Dict to hold values from circle table.
  global lambdaTableValues ##Dict to hold values from lambda table.   
  
  global circleScrollingArea ##Scrolling area for circle table.
  global lambdaScrollingArea ##Scrolling area for lambda table.
  
  global circleGridFrame ##Global frame for the circle table.
  global lambdaGridFrame ##Global frame for the lambda table.
  
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
      
      ##Pack new buttons and configure an appropriate size.
      prevButton.pack(in_=buttonsFrame, side = LEFT, anchor = S)
      
      ##Pack new labels/entries for the agent and its behaviours.
      agentLabel.pack(side = TOP, anchor = W)
      agentEntry.pack(side = TOP, anchor = W)
      agentBevLabel.pack(side = TOP, anchor = W)
      agentBevEntry.pack(side = TOP, anchor = W)   
  
  """PAGE 2 to PAGE 3."""
  if pageNum ==2: 
    agentName = get_agent(agentEntry.get()) ##The agent name is extracted from the entry.
    bevDict = build_bev_dict(agentBevEntry.get()) ##Behaviour dictionary for the agent.
   
    if agentName == None: ##User must input one valid agent to proceed.
      ##Change background colour of the agent entry to tomato-red to warn user.
      agentEntry.config(bg = 'tomato')
      ##Stay on current page by warning the user with a pop-up.
      incorrect_agent(main, return_arrow)
      ##Decrease pageNum to stay on current page.
      pageNum -= 1    
   
    elif bevDict == None or len(bevDict) == 0: ##User must imput at least one valid behaviour
      ##We can confirm that the agent entry is good since it passed the first if statement,
      ##therefore we set the background of the agent entry back to white. 
      agentEntry.config(bg = 'white')
      ##Change background colour of behaviour to tomato-red to warn user.
      agentBevEntry.config(bg = 'tomato')      
      
      ##Stay on current page by warning the user with a pop-up.
      incorrect_bevs(main, return_arrow)
      ##Decrease pageNum to stay on current page.
      pageNum -= 1  

    else: ##All good. 
      ##We can confirm that the agent entry and behaviour entry are good since 
      ##they passed the two first if statement,
      ##therefore we set the background back to white. 
      agentEntry.config(bg = 'white')      
      agentBevEntry.config(bg = 'white') 
      
      ##Before going to the next page, extract the full text describing 
      ##the agent behaviour (used when create the text file).
      agentBehaviour = agentBevEntry.get()        
      
      ##Set new page by unpacking entries/labels on page 2.
      agentLabel.pack_forget()
      agentEntry.pack_forget()
      agentBevLabel.pack_forget()
      agentBevEntry.pack_forget()
    
      ##Pack new labels for CBS.
      agentCBS = Label(main, text = agentName + ' =>')
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
        entriesCBS= create_CBS_entries(bevDict, frameCBS)
        
        ##Save the number of CBS in the bevDict dictionary at key (0, 0) since
        ##that coordinate is unused.
        entriesCBS[0, 0] = len(bevDict)
        
        ##Set generatedCBS to True.
        generatedCBS = True
 
      ##If concrete behaviours page was already generated, it must be modified 
      ##if necessary to adapt to changes made on previous pages.
      else:
        ##fix_CBS() function will modify the data scructures related to CBS.
        entriesCBS= fix_CBS(bevDict, frameCBS, entriesCBS)
        
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
        entriesCBS = recreate_CBS_entries(bevDict, entriesCBS, frameCBSTemp)
        
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
  if pageNum == 3:
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
     
      ##If no tables were yet generated, we create a new one.
      if generatedTable == False:
        ##Creating ccrolling areas and frames for both the circle and lambda tables.
        ##Also creating the labels in the upper corner of each table.
        circleScrollingArea = superscroll.Scrolling_Area(main, width=1, height=1)
        circleScrollingArea.pack(expand=1, fill = BOTH)   
  
      
        circleGridFrame = Frame(circleScrollingArea.innerframe) 
        circleTableLabel = Label(circleGridFrame, text = 'o')   
        circleTableLabel.grid(row = 0, column = 0)
      
        lambdaScrollingArea = superscroll.Scrolling_Area(main, width=1, height=1)
        lambdaScrollingArea.pack(expand=1, fill = BOTH)      
      
        lambdaGridFrame = Frame(lambdaScrollingArea.innerframe) 
        lambdaTableLabel = Label(lambdaGridFrame, text = b'\xce\xbb'.decode('utf-8')) ##Decoding the code yields the lambda string.  
        lambdaTableLabel.grid(row = 0, column = 0)   
      
        ##Create the data structures to hold the table entries and
        ##create the boxes within the frames.
        circleTableBoxes, lambdaTableBoxes = create_table(bevDict, stimDict,
                                                        circleGridFrame, 
                                                        lambdaGridFrame)
        ##pack the new table frames.   
        circleGridFrame.pack(side=TOP, anchor = NW) 
        lambdaGridFrame.pack(side=TOP, anchor = SW) 
      
        generatedTable = True ##Table is now generated.
  
      
        ##Keep track of table's current lenght and width
        ##in one of the dictionaries at coordinate (0, 0),
        ##since that key is not in use.
        circleTableBoxes[0, 0] = len(bevDict), len(stimDict)
      
      else: ##Table was already generated.
        ##Calling fix_grids() to check if modifications are necessary to the grids.
        fix_grids(bevDict, stimDict, circleTableBoxes, lambdaTableBoxes,
                  circleGridFrame, lambdaGridFrame) 
      
        ##Recreating the table by using a technique similar to the one described
        ##on the CBS page (see PAGE 2 to PAGE 3).
        circleScrollingAreaTemp = superscroll.Scrolling_Area(main, width=1, height=1)
        circleScrollingAreaTemp.pack(expand=1, fill = BOTH)   
      
        circleGridFrameTemp = Frame(circleScrollingAreaTemp.innerframe) 
        circleTableLabel = Label(circleGridFrameTemp, text = 'o')   
        circleTableLabel.grid(row = 0, column = 0)
      
        lambdaScrollingAreaTemp = superscroll.Scrolling_Area(main, width=1, height=1)
        lambdaScrollingAreaTemp.pack(expand=1, fill = BOTH)      
      
        lambdaGridFrameTemp = Frame(lambdaScrollingAreaTemp.innerframe) 
        lambdaTableLabel = Label(lambdaGridFrameTemp, text = b'\xce\xbb'.decode('utf-8')) ##Decoding the code yields the lambda string.     
        lambdaTableLabel.grid(row = 0, column = 0) 
        
        ##Recreate the tables with the new data structures, and assing the data scructures
        ##to the newly created entry boxes.
        circleTableBoxes, lambdaTableBoxes = recreate_table(bevDict, stimDict, circleTableBoxes, 
                                                            lambdaTableBoxes, circleGridFrameTemp, 
                                                            lambdaGridFrameTemp)     
        ##Destroy old scrolling areas and frames.
        circleScrollingArea.destroy()
        circleGridFrame.destroy()
        lambdaScrollingArea.destroy()
        lambdaGridFrame.destroy()
             
        ##Pack the new scrolling areas and frames.
        circleScrollingAreaTemp.pack(side=TOP, anchor = NW)
        circleGridFrameTemp.pack(side=TOP, anchor = NW)
        lambdaScrollingAreaTemp.pack(side=TOP, anchor = SW)
        lambdaGridFrameTemp.pack(side=TOP, anchor = SW)
        
        ##Assign the old scrolling areas and frames to the new ones.
        circleScrollingArea = circleScrollingAreaTemp
        circleGridFrame = circleGridFrameTemp
        lambdaScrollingArea = lambdaScrollingAreaTemp
        lambdaGridFrame = lambdaGridFrameTemp        
      
  """PAGE 4 to PAGE 5."""
  if pageNum == 4:
    ##Create dictionaries to hold the values from tables.
    circleTableValues = get_empty_dict()
    lambdaTableValues = get_empty_dict()
   
    ##Extract circle table values and lambda table values.
    circleTableValues, lambdaTableValues = get_table_values(circleTableBoxes, 
                                                         lambdaTableBoxes) 
   
    ##Calling check_if_good() to assure all the inputs are valid.
    isGood, numInvalid = check_if_good_table(bevDict, stimDict, circleTableBoxes, 
                                       lambdaTableBoxes, circleTableValues, 
                                       lambdaTableValues)
    ##If the table is good, proceed.
    if isGood:
      ##Forget table scrolling areas.
      circleScrollingArea.pack_forget()
      lambdaScrollingArea.pack_forget()
    
      ##Forget table frames.
      circleGridFrame.pack_forget()
      lambdaGridFrame.pack_forget()
    
      ##Forget next button, fillBev button and fillN button, since they are not
      ##needed on the last page of the program.
      fillBev.pack_forget()
      fillN.pack_forget()
      nextButton.pack_forget()
    
      ##Call create_text() to create the agentspec.txt file.
      create_text(agentName, agentBehaviour, concreteBehaviours, textBoxCBS, 
                  circleTableValues, lambdaTableValues, stimDict, bevDict, whichRadio)
      
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
   
    ##Set new page by unpacking agent related labels/entries.
    agentLabel.pack_forget()
    agentEntry.pack_forget()
    agentBevLabel.pack_forget()
    agentBevEntry.pack_forget()
    
    ##Unpack the previous button since it it not necessary on page 1.
    prevButton.pack_forget()
    
    ##Pack buttons for stimuli and frame to specify number of stimuli.
    stimFrame.pack(side = BOTTOM, anchor = S, expand = True, pady = 50)

    addStim.pack(in_=buttonsFrame, side = LEFT)

  """PAGE 3 to PAGE 2.""" 
  if pageNum == 3:
    ##Repack the agent related labels/entries.
    agentLabel.pack(side = TOP, anchor = W)
    agentEntry.pack(side = TOP, anchor = W)
    agentBevLabel.pack(side = TOP, anchor = W)
    agentBevEntry.pack(side = TOP, anchor = W)
    
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
  stimFrameList = []
  pageNum = 1
  
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
  ##Next Button (will not be availible on page 5).
  nextButton = Button(main, command = next_page, image = right_arrow, width = "25", height = "25", border = 0)
  nextButton.pack(in_=buttonsFrame, side = RIGHT, anchor = SE)

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
  

  enterStimButton = Button(main, image = check_mark, border = 0, command = lambda: specify_stim(main, stimList, stimFrameList, enterStimBox.get(), stimScrollingArea, remove_x, return_arrow))
  enterStimButton.pack(in_=stimFrame, side = RIGHT, anchor = N)
  
  enterStimBox = ttk.Entry(main, font = entry_font)
  enterStimBox.pack(in_=stimFrame, side = TOP)
  
  ##Add stimulus entry Button.
  addStim = Button(main, text = 'Add new stimulus', 
                   command = lambda: add_stim(main, stimList, stimFrameList, stimScrollingArea, remove_x, return_arrow), 
                   width = 23)
  
  addStim.pack(in_=buttonsFrame, side = LEFT)
  
  """Labels and Entries exclusive for page 2.""" 
  ##Agent Name Label and Entry.
  agentLabel = Label(main, text = 'Enter Agent Name:')
  agentEntry = Entry(main, width = 50)
  
  ##Agent Behaviour Label and Entry.
  agentBevLabel = Label(main, text = 'Enter Agent Behaviour:')
  agentBevEntry = Entry(main, width = 50)
  
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
                 command = lambda: fill_bev(bevDict, stimDict, circleTableBoxes), 
                 width = 31)  
  
  ##Button to fill lambda table with neutral stimulus.
  fillN = Button(main, text = 'Fill with neutral stimulus', 
                 command = lambda: fill_n(bevDict, stimDict, lambdaTableBoxes), 
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