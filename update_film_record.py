# Importing necessary module for database connection
from film_db_connect import *

# Function to update a film record in the database
def update_film_record():
    try:
        # Establishing database connection and obtaining cursor
        film_db_con, film_db_cursor = film_db_access()
        
        # Prompting user to enter the filmID to update a record
        filmID = int(input("Enter the filmID to update a record: "))
        film_db_cursor.execute("SELECT * FROM tblFilms WHERE filmID = ?", (filmID,))
        row = film_db_cursor.fetchone()

        # Checking if the filmID exists
        if row is None:
            print(f"No record with the filmID {filmID} exists ")
        else:
            # Prompting user to choose the field to update
            field_name = input("Would you like to update the filmID, title, yearReleased, rating, duration or genre? ").lower()
            
            # Validating the chosen field
            if field_name not in ["title", "yearreleased", "rating", "duration", "genre"]:
                print(f"Field {field_name} is not a field name in the table")
            else:
                # Prompting user to enter the new value for the chosen field
                field_value = input(f"Enter the {field_name}: ")
                
                # Executing SQL query to update the record
                film_db_cursor.execute(f"UPDATE tblFilms SET {field_name} = ? WHERE filmID = ? ", (field_value, filmID,))
                film_db_con.commit()
                print(f"Record {filmID} updated")            
    
    # Handling programming errors
    except sql.ProgrammingError as e:
        print(f"Update error: {e}")

# Main function to execute the film record update
if __name__ == "__main__":
    update_film_record()



