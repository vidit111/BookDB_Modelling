import pandas as pd
import mysql.connector
from config import mysql_config  # Import MySQL configuration from config.py

def insert_csv_to_mysql(csv_file_path, db_config, table_name):
    # Read the CSV file using pandas
    df = pd.read_csv(csv_file_path)

    # Connect to MySQL
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Create the INSERT query
        insert_query = f"INSERT IGNORE INTO {table_name} ({', '.join(df.columns)}) VALUES ({', '.join(['%s']*len(df.columns))})"

        # Insert the data row by row
        for _, row in df.iterrows():
            cursor.execute(insert_query, tuple(row))

        # Commit the changes
        connection.commit()
        print("Data inserted successfully!")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Close the connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

# Example usage:
insert_csv_to_mysql('C:/Users/Vidit/Desktop/Streaming/data/author.csv', mysql_config, 'author')
#Second file books
insert_csv_to_mysql('C:/Users/Vidit/Desktop/Streaming/data/books.csv', mysql_config, 'books')
#third file genre
insert_csv_to_mysql('C:/Users/Vidit/Desktop/Streaming/data/genre.csv', mysql_config, 'genre')
#fourth file book_genre
insert_csv_to_mysql('C:/Users/Vidit/Desktop/Streaming/data/Book_genre.csv', mysql_config, 'book_genre')
#fifth file user
insert_csv_to_mysql('C:/Users/Vidit/Desktop/Streaming/data/user.csv', mysql_config, 'user')
