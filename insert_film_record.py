# Importing necessary module for database connection
from film_db_connect import *

# Function to insert a new film record into the database
def insert_film_record():
    try:
        # Establishing database connection and obtaining cursor
        film_db_con, film_db_cursor = film_db_access()

        # Gathering film details from user input
        title = input('Enter film title: ')
        yearReleased = int(input('Enter year released: '))
        rating = input('Enter film rating: ')
        duration = int(input('Enter film duration in minutes: '))
        genre = input('Enter film genre: ')

        # Executing SQL query to insert the film record into the database
        film_db_cursor.execute('Insert into tblFilms values (NULL,?,?,?,?,?)', (title, yearReleased, rating, duration, genre)) 
    
        # Committing the transaction to save changes to the database
        film_db_con.commit() 
        print(f'{title} inserted in the films table')
    
    # Handling operational errors
    except sql.OperationalError as e: 
        print(f'Failed because: {e}')

    # Handling programming errors
    except sql.ProgrammingError as pe:
        print(f'Not working because {pe}')

    # Handling general errors
    except sql.error as er:
        print(f'This error: {er}')

# Main function to execute the film record insertion
if __name__ == "__main__":
    insert_film_record()