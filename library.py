#imports
import helper, api, manager

#load app state
#this will load the current state(app data)
#and fills the books dictionary
manager.load_state()

#main-loop
while True:
    helper.clear()
    print("1. Add a book")
    print("2. Update a book’s author")
    print("3. Update a book’s publication year")
    print("4. Search for a book by title")
    print("5. Delete a book")
    print("6. Display all books (sorted by title)")
    print("7. Exit")
    print()
    
    #reads user-input
    user_input = input("Enter a selection: ")
    #valdiation
    _input  = helper.validate_input(user_input)
    
    #if or if-not valid 
    match _input:
        case 7: api.quit_application()
        case 1: api.add_book() 
        case 2: api.update_author() 
        case 3: api.update_publication() 
        case 4: api.search_title()
        case 5: api.delete_title()
        case 6: api.display_all_books()
        case 0:
                print("!!Invalid input please try again with a number between 1-7")
                print()
                continue
        
