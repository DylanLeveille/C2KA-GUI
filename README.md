

GUI to Assist the C2KA TOOL

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

Behaviour:  SINCE1 ; SINCE2 ; SINCE3; SINCE4 ; READ ; ((AVG1 ; RESET1) + (AVG2 ; RESET2) + (AVG3 ; RESET3) + (AVG4 ; RESET4))

Table values:

  circle table: 
       |   ips    |    abor   |   allo   |   help  |   noop  |    
---------------------------------------------------------------------       
SINCE1 |  SINCE1  |   SINCE1  |  SINCE 1 |  SINCE1 |  SINCE1 |   
---------------------------------------------------------------------       
SINCE2 |  SINCE2  |   SINCE2  |  SINCE2  |  SINCE2 |  SINCE2 | 
---------------------------------------------------------------------       
SINCE3 |  SINCE3  |   SINCE3  |  SINCE3  |  SINCE3 |  SINCE3 | 
---------------------------------------------------------------------       
SINCE4 |  SINCE4  |   SINCE4  |  SINCE4  |  SINCE4 |  SINCE4 | 
---------------------------------------------------------------------       
READ   |   READ   |    READ   |   READ   |   READ  |   READ  | 
---------------------------------------------------------------------       
AVG1   |   AVG1   |    AVG1   |   AVG1   |   AVG1  |   AVG1  | 
---------------------------------------------------------------------       
AVG2   |   AVG2   |    AVG2   |   AVG2   |   AVG2  |   AVG2  | 
---------------------------------------------------------------------       
AVG3   |   AVG3   |    AVG3   |   AVG3   |   AVG3  |   AVG3  | 
---------------------------------------------------------------------       
AVG4   |   AVG4   |    AVG4   |   AVG4   |   AVG4  |   AVG4  | 
---------------------------------------------------------------------       
RESET1 |  RESET1  |   RESET1  |  RESET1  |  RESET1 |  RESET1 | 
---------------------------------------------------------------------       
RESET2 |  RESET2  |   RESET2  |  RESET2  |  RESET2 |  RESET2 | 
---------------------------------------------------------------------       
RESET3 |  RESET3  |   RESET3  |  RESET3  |  RESET3 | RESET3  | 
---------------------------------------------------------------------       
RESET4 |  RESET4  |   RESET4  |  RESET4  |  RESET4 | RESET4  | 
---------------------------------------------------------------------

    

Do note that there is no guarantee that the program won't crash if uncommon characters are inputted in the entry boxes. Characters which are found on the standard English keyboard should work fine and are usually .

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

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
