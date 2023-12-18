import mysql.connector
import pandas as pd
from config import mysql_config
import time

# Establish a connection to your MySQL database
connection = mysql.connector.connect(**mysql_config)
cursor = connection.cursor()

# Main loop for continuous matrix update
while True:
    # Fetch data from user_books table
    cursor.execute("SELECT * FROM user_books")
    user_books_data = cursor.fetchall()

    # Fetch data from book_genre table
    cursor.execute("SELECT * FROM book_genre")
    book_genre_data = cursor.fetchall()

    # Create DataFrames for user_books and book_genre
    user_books_df = pd.DataFrame(user_books_data, columns=['U_id', 'B_id'])
    book_genre_df = pd.DataFrame(book_genre_data, columns=['B_id', 'G_id'])

    # Create a list of unique User IDs and Genre IDs
    unique_users = user_books_df['U_id'].unique()
    unique_genres = book_genre_df['G_id'].unique()

    # Create an empty matrix
    user_genre_matrix = pd.DataFrame(index=unique_users, columns=unique_genres).fillna(0)

    # Populate the matrix based on user preferences
    for index, row in user_books_df.iterrows():
        user_id = row['U_id']
        book_id = row['B_id']

        # Get the genres for the book
        book_genres = book_genre_df[book_genre_df['B_id'] == book_id]['G_id'].tolist()

        # Update the matrix based on the user's reading
        for genre in book_genres:
            user_genre_matrix.at[user_id, genre] += 1

    # Display the user_genre_matrix
    print("User Genre Matrix:")
    print(user_genre_matrix)

    # Insert data into the user_genre table
    for user_id, row in user_genre_matrix.iterrows():
        # Specify the columns in the INSERT statement
        columns = ', '.join(f'genre_{genre}' for genre in row.index)
        values = ', '.join(map(str, row.values))
    
        # Specify the ON DUPLICATE KEY UPDATE part
        update_values = ', '.join(f'genre_{genre} = genre_{genre} + VALUES(genre_{genre})' for genre in row.index)

        insert_data_query = f"INSERT INTO user_genre (U_id, {columns}) VALUES ({user_id}, {values}) ON DUPLICATE KEY UPDATE {update_values};"
        cursor.execute(insert_data_query)

    # Commit the changes
    connection.commit()

    # Wait for 120 seconds before the next update
    time.sleep(120)

# Close MySQL connection
cursor.close()
connection.close()