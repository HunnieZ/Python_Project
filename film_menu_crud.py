# Importing necessary modules
import insert_film_record, print_film_records, update_film_record,delete_film_record, film_report

# Function to read the content of a file
def read_file(file_path):
    try:
        # Opening the file specified by the file_path
        with open(file_path) as open_file:
            # Reading the content of the file
            rf = open_file.read()
        return rf
    except FileNotFoundError as nf:
        # Handling file not found error
        print(f"File not found: {nf}")

# Function to display films menu and prompt user for choice
def films_menu():
    try:
        option = 0 
        optionsList = ["1","2","3","4","5","6"]  # Valid options for the menu
        # Reading menu choices from a file
        menu_choices = read_file("film_menu_crud.txt")
        while option not in optionsList:
            print(menu_choices)
            option = input("Select option number 1-6: ")  # Prompting user for input
            if option not in optionsList:
                print(f"{option} is invalid")
        return option
    except FileNotFoundError as e:
        # Handling file not found error for the menu file
        print(f"Add error: {e}")

# Main program loop
mainProgram = True 
while mainProgram: 
    main_menu = films_menu()  # Displaying films menu and getting user choice
    if main_menu == "1":
        insert_film_record.insert_film_record()  # Calling function to insert a film record
    elif main_menu == "2":
        delete_film_record.delete_film_record()  # Calling function to delete a film record
    elif main_menu == "3":
        update_film_record.update_film_record()  # Calling function to update a film record
    elif main_menu == "4":
        print_film_records.print_film_records()  # Calling function to print film records
    elif main_menu == "5":
        film_report.search_film_report()  # Calling function to search film records
    else:
        mainProgram = False  # Exiting the program if an invalid option is chosen

# Waiting for user to press Enter before exiting
input("Press Enter to exit....")
