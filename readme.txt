run the library.py to run the application make sure other files are in the same folder
    in order for successfull run

    Reffrence's and Matireals
[imported subproccess] https://www.w3schools.com/python/ref_module_subprocess.asp
#usage : to clear clutterd screens when moving in between loops

[match aka switch] https://www.w3schools.com/python/python_match.asp
#usage : to avoid if-else hell in mainloop 

[module and FS] 
https://www.w3schools.com/python/python_modules.asp
https://docs.python.org/3/tutorial/modules.html
https://www.learnpython.org/en/Modules_and_Packages
#usage : to seprate the application into 3 layes with a helper class
       : also to avoid 1000's of line in single source file

[DictReader](using both DictRead and DictWrite)
#usage : an Object based way of serializing the data from a local saved
       : used to read from the csv and store it in books library
https://docs.python.org/3/library/csv.html#csv.QUOTE_NONNUMERIC:~:text=class%20csv.-,DictReader,-(f%2C
https://docs.python.org/3/library/csv.html#csv.DictWriter:~:text=class%20csv.-,DictWriter,-(f%2C

    FS(File structure explained)
Library.py : 
    handle's the main loop and main switch's callback's
Helper.py :
    provides helper functions like validations, doesExist and Clear
Data.py :
    holds the global dictionary called called books
    to avoid Circular Import (Circular Dependency)
Api.py :
    handles endpoint void functions
    auto handels consoleUI
    actuall endpoint of 3 layer lazy architecture
