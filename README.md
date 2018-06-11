#GUI to Assist the C2KA TOOL

This project consists of a graphical user interface (GUI) to assist the C2KA tool (developed by Dr. Jason Jaskolka). With simple entries, the GUI can generate a text file describing an agent’s specification.  

## Getting Started
1.	Download the entire project folder (found at https://github.com/DylanLeveille/C2KA-GUI). 
2.	Open a python IDE (using a version of Python 3.6).
3.	Run the main program by compiling the gui.py file in the IDE.

Note: Steps 2 and 3 may be skipped by starting the executable found in the project folder (Not yet implemented). 

### Prerequisites *(ideas borrowed from Dr. Bailey's course outline for SYSC 1005)

All the software used in this project is free. Here's what you need to install this software on your own computer:

● Python 3.6.2 can be downloaded from: python.org/downloads/release/python-362. For Windows platforms, download the Windows x86-64 executable installer: python-3.6.2-amd64.exe. 

● Wing 101 v. 6.0.7-1 can be downloaded from: wingware.com. Please ensure that you download and install Wing 101, not Wing Professional. The latter IDE has a free 30-day trial license, after which a license must be purchased. Wing 101 is free, and does not require you to purchase a license. For Windows platforms, download the 32-bit/64-bit installer (wingide-101-6.0.7-1.exe). 


Note: as of Version 6.0, Wing Personal is free. This IDE has more features than Wing 101, but fewer than Wing Professional.

### Installing

To install the software correctly, install python, followed by Wing 101. 

Please note there are known issues with OS X, Python's Tkinter module and the third-party Tcl/Tk GUI toolkit on which it depends (these issues are documented at python.org). This should, however, not be an issue for this project.

## Running tests

No automated tests available due to the nature of this project. 

However, we recommend testing out the project with various different text entries and taking advantage of the scrollbars to facilitate entries.

Example:

Inserting the following information should generate the preview shown below.

Stimuli: ips, abor, allo, help, noop.

Agent Name: R

Behaviour:  
    SINCE1 ; SINCE2 ; SINCE3; SINCE4 ; READ ; ((AVG1 ; RESET1) + (AVG2 ; RESET2) + (AVG3 ; RESET3) + (AVG4 ; RESET4))

Concrete behaviour (with text radio button active): 

    since1 := since1 + delta;
    since2 := since2 + delta;
    since3 := since3 + delta;
    since4 := since4 + delta;
    n := cmd;
    if n = 1 -> avg1 := since1 / num1; since1 := 0
     | n = 2 -> avg2 := since2 / num2; since2 := 0
     | n = 3 -> avg3 := since3 / num3; since3 := 0
     | n = 4 -> avg4 := since4 / num4; since4 := 0
    fi

Table values:
For circle table, please insert each row (behaviour) name along the row.
For lambda Table, fill with Neutral stimuli (N), except bottom right corner, in which is entered the deactivation stimulus (D).

Product:
begin AGENT where
    R := SINCE1 ; SINCE2 ; SINCE3; SINCE4 ; READ ; ((AVG1 ; RESET1) + (AVG2 ; RESET2) + (AVG3 ; RESET3) + (AVG4 ; RESET4))
end

begin NEXT_BEHAVIOUR where

    (ips, SINCE1)  = SINCE1
    
    (ips, SINCE2)  = SINCE2
    
    (ips, SINCE3)  = SINCE3
    
    (ips, SINCE4)  = SINCE4
    
    (ips, READ)    = READ
    
    (ips, AVG1)    = AVG1
    
    (ips, RESET1)  = RESET1
    
    (ips, AVG2)    = AVG2
    
    (ips, RESET2)  = RESET2
    
    (ips, AVG3)    = AVG3
    
    (ips, RESET3)  = RESET3
    
    (ips, AVG4)    = AVG4
    
    (ips, RESET4)  = RESET4
    
    (abor, SINCE1) = SINCE1
    
    (abor, SINCE2) = SINCE2
    
    (abor, SINCE3) = SINCE3
    
    (abor, SINCE4) = SINCE4
    
    (abor, READ)   = READ
    
    (abor, AVG1)   = AVG1
    
    (abor, RESET1) = RESET1
    
    (abor, AVG2)   = AVG2
    
    (abor, RESET2) = RESET2
    
    (abor, AVG3)   = AVG3
    
    (abor, RESET3) = RESET3
    
    (abor, AVG4)   = AVG4
    
    (abor, RESET4) = RESET4
    
    (allo, SINCE1) = SINCE1
    
    (allo, SINCE2) = SINCE2
    
    (allo, SINCE3) = SINCE3
    
    (allo, SINCE4) = SINCE4
    
    (allo, READ)   = READ
    
    (allo, AVG1)   = AVG1
    
    (allo, RESET1) = RESET1
    
    (allo, AVG2)   = AVG2
    
    (allo, RESET2) = RESET2
    
    (allo, AVG3)   = AVG3
    
    (allo, RESET3) = RESET3
    
    (allo, AVG4)   = AVG4
    
    (allo, RESET4) = RESET4
    
    (help, SINCE1) = SINCE1
    
    (help, SINCE2) = SINCE2
    
    (help, SINCE3) = SINCE3
    
    (help, SINCE4) = SINCE4
    
    (help, READ)   = READ
    
    (help, AVG1)   = AVG1
    
    (help, RESET1) = RESET1
    
    (help, AVG2)   = AVG2
    
    (help, RESET2) = RESET2
    
    (help, AVG3)   = AVG3
    
    (help, RESET3) = RESET3
    
    (help, AVG4)   = AVG4
    
    (help, RESET4) = RESET4
    
    (noop, SINCE1) = SINCE1
    
    (noop, SINCE2) = SINCE2
    
    (noop, SINCE3) = SINCE3
    
    (noop, SINCE4) = SINCE4
    
    (noop, READ)   = READ
    
    (noop, AVG1)   = AVG1
    
    (noop, RESET1) = RESET1
    
    (noop, AVG2)   = AVG2
    
    (noop, RESET2) = RESET2
    
    (noop, AVG3)   = AVG3
    
    (noop, RESET3) = RESET3
    
    (noop, AVG4)   = AVG4
    
    (noop, RESET4) = RESET4
end

begin NEXT_STIMULUS where

    (ips, SINCE1)  = N
    
    (ips, SINCE2)  = N
    
    (ips, SINCE3)  = N
    
    (ips, SINCE4)  = N
    
    (ips, READ)    = N
    
    (ips, AVG1)    = N
    
    (ips, RESET1)  = N
    
    (ips, AVG2)    = N
    
    (ips, RESET2)  = N
    
    (ips, AVG3)    = N
    
    (ips, RESET3)  = N
    
    (ips, AVG4)    = N
    
    (ips, RESET4)  = N
    
    (abor, SINCE1) = N
    
    (abor, SINCE2) = N
    
    (abor, SINCE3) = N
    
    (abor, SINCE4) = N
    
    (abor, READ)   = N
    
    (abor, AVG1)   = N
    
    (abor, RESET1) = N
    
    (abor, AVG2)   = N
    
    (abor, RESET2) = N
    
    (abor, AVG3)   = N
    
    (abor, RESET3) = N
    
    (abor, AVG4)   = N
    
    (abor, RESET4) = N
    
    (allo, SINCE1) = N
    
    (allo, SINCE2) = N
    
    (allo, SINCE3) = N
    
    (allo, SINCE4) = N
    
    (allo, READ)   = N
    
    (allo, AVG1)   = N
    
    (allo, RESET1) = N
    
    (allo, AVG2)   = N
    
    (allo, RESET2) = N
    
    (allo, AVG3)   = N
    
    (allo, RESET3) = N
    
    (allo, AVG4)   = N
    
    (allo, RESET4) = N
    
    (help, SINCE1) = N
    
    (help, SINCE2) = N
    
    (help, SINCE3) = N
    
    (help, SINCE4) = N
    
    (help, READ)   = N
    
    (help, AVG1)   = N
    
    (help, RESET1) = N
    
    (help, AVG2)   = N
    
    (help, RESET2) = N
    
    (help, AVG3)   = N
    
    (help, RESET3) = N
    
    (help, AVG4)   = N
    
    (help, RESET4) = N
    
    (noop, SINCE1) = N
    
    (noop, SINCE2) = N
    
    (noop, SINCE3) = N
    
    (noop, SINCE4) = N
    
    (noop, READ)   = N
    
    (noop, AVG1)   = N
    

(noop, RESET1) = N
    
    (noop, AVG2)   = N
    
    (noop, RESET2) = N
    
    (noop, AVG3)   = N
    
    (noop, RESET3) = N
    
    (noop, AVG4)   = N
    
    (noop, RESET4) = D
end

begin CONCRETE BEHAVIOUR where

    R => [ since1 := since1 + delta;
           since2 := since2 + delta;
           since3 := since3 + delta;
           since4 := since4 + delta;
           n := cmd;
           if n = 1 -> avg1 := since1 / num1; since1 := 0
            | n = 2 -> avg2 := since2 / num2; since2 := 0
            | n = 3 -> avg3 := since3 / num3; since3 := 0
            | n = 4 -> avg4 := since4 / num4; since4 := 0
           fi  ]
end

### Things to be aware of

Do note that there is no guarantee that the program won't crash if uncommon characters are inputted in the entry boxes. Characters which are found on the standard English keyboard should work fine and are usually.

Also, since we decided that the behaviours would be stored based on the order they appeared, the stimulis-behaiour order in the text file is somewhat disorganized to maintain that order. This will NOT disrupt the functionality of the text file.

## Built With

* [Python](https://www.python.org/) - The programming language used
* [Tkinter](https://wiki.python.org/moin/TkInter) - Python's de-facto standard GUI package

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments


* Hat tip to anyone whose code was used
* Inspiration
* etc
