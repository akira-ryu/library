#this file is used to manage the State of the app
#this file and its functions will be responsible for 
#reading and writing to the app state
import csv, data

def load_state():
    try:
        with open("state/books.csv", newline='') as csvfile:
            #DictReader refrenced in the readme.txt
            reader = csv.DictReader(csvfile)
            for row in reader:
                book = {"author" : row['Author'], "year" : int(row['Year']), "isbn": int(row['ISBN']) }
                data.books[row['Title']] = book
                #print(row['Title'], row['Author'])
    
        print(row)
    except FileNotFoundError:
        print("books.csv file was not found.")
        print("!!Please make sure the books.csv file is inside state folder!!")      
    except PermissionError:
        print("Error: Permission denied when accessing the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")  

            
def update_state():
    try:
        with open('state/books.csv', 'w', newline='') as csvfile:
            fieldnames = ['Title','Author','Year','ISBN']
            #use of this is mentioned in the readme.txt
            #were to and how to details are given in that file
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for title, details in data.books.items():
                writer.writerow({'Title': title, 'Author': details['author'], 
                                 'Year': details['year'], 'ISBN': details['isbn']})
    except Exception as ex:
        print(ex)

