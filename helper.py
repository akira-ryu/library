#helper functions
import subprocess # modern system call can also use system.os
from datetime import date
#UI-functions
clear = lambda : subprocess.run('cls', shell = True)

#validaton-fucntion
def validate_input(_input):
    if _input.isdigit():
        x = int(_input)
        if (x<=7 and x>=1): return x
        else: return 0
    else : 
        return 0

def validate_string(_string):  
    if not _string : return False
    return True

def validate_year(_year):
    if not _year : return False
    if not _year.isdigit(): return False
       
    _year = int(_year)
    current_year = date.today().year
    if(_year > 1000 and _year < (current_year + 1)):
        return True
    return False
    
def validate_ISBN(_isbn):
    if len(_isbn) < 10 : return False
    return _isbn.isdigit()
    
    
def book_exsits_in(_books, _title):
    if _title in _books:
        return True
    else:
        return False
