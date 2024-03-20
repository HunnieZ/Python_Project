# Importing necessary functions from the film_db_connect module
from film_db_connect import *

# Function to delete a film record from the database
def delete_film_record():
    try:
        # Establishing a connection to the film database and obtaining a cursor
        film_db_con, film_db_cursor = film_db_access()

        # Prompting the user to input the film title to be deleted
        title = input('Enter the film title to delete the record: ')

        # Executing a SQL query to select the record with the given title
        film_db_cursor.execute('select * from tblFilms where title = ?', (title,))
        
        # Fetching the first row from the query result
        row = film_db_cursor.fetchone()

        # Checking if the row is empty (i.e., no record found with the given title)
        if row == None:
            print(f'No record with title {title} in the films table!')
        else:
            # Deleting the record from the database
            film_db_cursor.execute('delete from tblFilms where title = ?', (title,))
            # Committing the transaction to apply changes
            film_db_con.commit()
            # Informing the user that the record has been successfully deleted
            print(f"Record {title} deleted from the films table")
    except sql.ProgrammingError as e:
        # Handling exceptions related to SQL errors
        print("Delete operation failed:", e)

# Entry point of the program
if __name__ == "__main__":
    # Calling the delete_film_record function when the script is executed
    delete_film_record()
