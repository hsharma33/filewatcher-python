# Problem Statement:

>    Developers lack the ability to run the code/build by making changes in one or more than one files automatically. They are forced to manually save all the files and run the project as and when any changes are made until a working functinality is achieved. 

# Solution:

    Watchdog: It provides platform-independent architecture to solve the problem for Python projects. 

# Solution Approach:

- Watch the hash of data of each file
- If any hash changes, trigger user's action

### Features:

- User should be able to modify the Polling Interval via a config file. 
- User should be able to exclude certain files/directories. 

## Design And Architecture

### Naive Implementation: 
- Design Pattern: Observer Pattern

- Basic Design Document 

<img src="UML Diagram-FileWatcher.png"
     alt="uml_diagram"
     style="float: left; margin-right: 10px;" />
