# Importing the sqlite3 library under the alias 'sql'
import sqlite3 as sql

# Function to establish a connection to the film database
def film_db_access():
    try:
        # Attempting to connect to the 'filmflix 2.db' database
        with sql.connect('filmflix 2.db') as film_db_con:
            # Creating a cursor object to execute SQL commands
            film_db_cursor = film_db_con.cursor()
            # Returning the connection and cursor objects
            return film_db_con, film_db_cursor
        
    except sql.OperationalError as e:
        # Handling exceptions related to database connection errors
        print(f'Connection failed: {e}')

# Entry point of the program
if __name__== "__main__":
    # Calling the film_db_access function when the script is executed
    film_db_access()






        
