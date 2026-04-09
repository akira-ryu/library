import helper, data, manager

#1. add-fucntion (to add a book to the dicts)
def add_book():
   helper.clear()
   print('ADD A BOOK TO THE LIBRARY')
   print()
   while True:
    print()
    _title = input("Enter title: ")
    _author = input("Enter author name: ")
    _year = input("Enter year of publication: ")
    _isbn = input("Enter ISBN: ")

    is_valid_tile = helper.validate_string(_title)
    is_valid_author = helper.validate_string(_author)
   
    #checks if the author and the title is valid then adds 
    #to the global library
    if (is_valid_author and is_valid_tile and helper.validate_year(_year) and helper.validate_ISBN(_isbn)):
        #title must not already exist in the dictionary
       if helper.book_exsits_in(data.books, _title):
           print()
           print('the given title already exists in the library')
           print('try a diffrent title')
           continue
           
       #dicts inside dicts 
       book = { "author" : _author, "year" : int(_year), "isbn" : int(_isbn)}
       data.books[_title] = book
       print()
       print("book added successfully")
       break
    else:
       print()
       print("Invalid input please enter a valid book data")
       print("A valid book data has an author, title, valid year")
       print('and valid ISBN number with 10 digits numbers')
       print('..please try again..')
       print()
       continue
   
   print()
   input('press any key to continue..')
   return
   
def update_author():
    print()
    if not data.books.items(): 
        print('no books in library')
        print('please add books to furthur view')
        return
    
    helper.clear()
    print("UPDATE A BOOKS AUTHOR")
    print()
    while True:
        print()
        _title = input("Enter title: ")
        if helper.book_exsits_in(data.books, _title):
            while True:
             print(f"Current author name is {data.books[_title]['author']}")  
             _author = input("Enter new author: ")
             if helper.validate_string(_author):
                data.books[_title]["author"] = _author
                
                print('authors name was updated successfully')
                break
             else:
                 print()
                 print("Invlaid : author cannot be empty")
                 print("please try again")
                 continue
            break
        else:
            print()
            print("Given title was not found in the library")
            print('please try a diffrent title')
            continue
    
    print()
    input('press any key to continue..')
    return


def update_publication():
    print()
    if not data.books.items(): 
        print('no books in library')
        print('please add books to furthur view')
        return
    
    helper.clear()
    print("UPDATE PUBLICATION YEAR OF A BOOK")
    print()
    while True:
        print()
        _title = input("Enter title: ")
        if helper.book_exsits_in(data.books, _title):
            while True:
             print(f"Current publication year is {data.books[_title]['year']}")  
             _year = input("Enter new publication year: ")
             
             if helper.validate_year(_year):
                data.books[_title]["year"] = _year
                
                print('publication year was updated successfully')
                break
             else:
                 print()
                 print("Invlaid : year should be a number greater than 1000 less than next year")
                 print("please try again")
                 continue
            break
        else:
            print()
            print("Given title was not found in the library")
            print('please try a diffrent title')
            continue
    
    print()
    input('press any key to continue..')
    return
    

def display_all_books():
    #todo - format all the values to print
    print()
    if not data.books.items(): 
        print('no books in library')
        print('please add books to furthur view')
        print()
        input('press any key to continue..')
        return
    
    helper.clear()
    print('ALL THE BOOKS AVAILABLE IN LIBRARY(sorted by title)')
    print('++++++++++++++++++++++++++++++')
    data.books = dict(sorted(data.books.items()))
    #for key, value in key-value pair print {key} {value[get-valueOfKey'auhtor']]}
    for title, details in data.books.items():
       print()
       print(f"Title: {title}")
       print(f"Author: {details['author']}")
       print(f"Year: {details['year']}")
       print(f"ISBN: {details['isbn']}")
       print()
       print('++++++++++++++++++++++++++++++')   
    
    print()
    input('press any key to continue..')
    return       
     
def search_title():
    helper.clear()
    print('SEARCH A BOOK IN LIBRARY')
    print()
    
    if not data.books.items(): 
        print('no books in library')
        print('please add books to furthur view')
        print()
        input('press any key to continue..')
        return
    
    _title = input('Enter a title to search: ')
    
    if helper.validate_string(_title):
        
        if helper.book_exsits_in(data.books, _title):
            
            book = data.books[_title]
           
            print()
            print(f"Title: {_title}")
            print(f"Author: {book['author']}")
            print(f"Year: {book['year']}")
            print(f"ISBN: {book['isbn']}")
            print()
        else:
            print('Given title was not found')
            print('Try again a diffrent title')
    else:
        print('please enter a valid title')
        print('a valid title cannot be empty')
    
    print()
    input('press any key to continue..')
    return
        

def delete_title():
    helper.clear()
    print('DELETE A BOOK FROM LIBRARY')
    print()
    
    if not data.books.items(): 
        print('no books in library')
        print('please add books to furthur view')
        print()
        input('press any key to continue..')
        return    

    _title = input('Enter a title to remove: ')
    if helper.validate_string(_title):
        
        if helper.book_exsits_in(data.books, _title):
          _char = input('Are you sure you want to delete this book? (Y/N):')
          
          if _char == 'y' or _char == 'Y':
              #remove the book
              del data.books[_title]
              print()
              print('The given book was successfully removed.')    
          else: 
              print()
              print('Operation was cancelled')
              input('press any key to continue..')
              return       
        else:
            print()
            print('Given title was not found')
            print('Try again a diffrent title')
    else:
        print()
        print('please enter a valid title')
        print('a valid title cannot be empty')
    
    print()
    input('press any key to continue..')
    return
           

def quit_application():
    print()
    _char = input('Are you sure you want to exit? (Y/N):')
    
    if _char == 'y' or _char == 'Y':
        manager.update_state()
        print()
        print('Thank you for using the library....')
        print()
        quit()
    else:
        return
        