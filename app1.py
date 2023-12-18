from flask import Flask, render_template, request
import mysql.connector
import pandas as pd
from recommendations import recommend_books_for_users
from book_covers import get_book_covers
import os

# Establish a connection to your MySQL database
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="vidit.1234",
    database="streaming_service"
)
cursor = connection.cursor()


app = Flask(__name__)

# Function to recommend books for each user
def recommend_books_for_users(user_genre_matrix, book_genre_df, user_books_df):
    recommendations = {}

    for user_id, row in user_genre_matrix.iterrows():
        # Sort genres in descending order and select top 5
        top_genres = row.sort_values(ascending=False).index[:5]
        
        # Retrieve books from the top genres that the user hasn't read
        user_books = user_books_df[user_books_df['U_id'] == user_id]['B_id'].tolist()
        recommended_books = set()

        for genre in top_genres:
            books_in_genre = book_genre_df[book_genre_df['G_id'] == genre]['B_id'].tolist()
            recommended_books.update(set(books_in_genre) - set(user_books))

        recommendations[user_id] = list(recommended_books)[:5]  # Select top 5 recommendations

    return recommendations

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

# Function to fetch book covers
def get_book_covers(book_ids):
    covers = {}
    cursor = None  # Declare cursor outside the try block

    try:
        # Re-establish the cursor inside the function
        cursor = connection.cursor()

        for book_id in book_ids:
            file_path = f"C:\\Users\\Vidit\\Desktop\\Streaming\\data\\covers\\{book_id}.png"

            if os.path.exists(file_path):
                covers[book_id] = file_path
            else:
                print(f"No cover available for Book ID {book_id}")
    except mysql.connector.Error as err:
        print(f"Error fetching book cover: {err}")
    finally:
        # Close the cursor inside the function, checking if it's not None
        if cursor:
            cursor.close()

    return covers

# Close MySQL connection
cursor.close()
connection.close()

# Route for the homepage
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle form submission
@app.route('/recommendations', methods=['POST'])
def recommendations():
    user_id = int(request.form['user_id'])
    
    # Get book recommendations for the specified user
    user_recommendations = recommend_books_for_users(user_genre_matrix, book_genre_df, user_books_df).get(user_id, [])

    # Get book covers for the recommended books
    covers = get_book_covers(user_recommendations)

    return render_template('recommendations.html', user_id=user_id, recommendations=user_recommendations, covers=covers)

if __name__ == '__main__':
    app.run(debug=True)
