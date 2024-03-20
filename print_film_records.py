
# Importing necessary module for database connection
from film_db_connect import *

# Function to print all film records from the database
def print_film_records():
    try:
        # Establishing database connection and obtaining cursor
        film_db_con, film_db_cursor = film_db_access()
        
        # Executing SQL query to select all records from tblFilms table
        film_db_cursor.execute('select * from tblFilms')
        all_records = film_db_cursor.fetchall() 
        
        # Displaying records if any exist
        if all_records:
            print(f'filmID{"": <3}|Title{"": <25}|YearReleased{"": <8}|Rating{"": <9}|Duration{"": <7}|Genre{"": <16}')
            print('*' * 100)

            # Iterating through each record and printing its details
            for aRecord in all_records:
                print(f'{aRecord[0]: <9}|{aRecord[1]: <30}|{aRecord[2]: <20}|{aRecord[3]: <15}|{aRecord[4]: <15}|{aRecord[5]: <15}')
                print('*' * 100)

    # Handling operational errors
    except sql.OperationalError as e:
        print(f'Failed because: {e}')

# Main function to execute printing of film records
if __name__ == "__main__":
    print_film_records()

