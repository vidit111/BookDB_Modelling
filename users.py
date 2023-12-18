import random
import mysql.connector
from config import mysql_config
import time

# Establish a connection to your MySQL database
conn = mysql.connector.connect(**mysql_config)

def generate_fake_reads():
    if conn.is_connected():
        cursor = conn.cursor()

        #fetch existing user ids
        cursor.execute("select u_id from user")
        user_ids=[row[0] for row in cursor.fetchall()]

        #step1: randomly choose 5 genres for every user
        genres = list(range(1,41))  #assuming you have 40 gendres
        for u_id in user_ids:
            chosen_genres = random.sample(genres, k =random.randint(5,40))

            #step2: for each chosen genre, randomly read books of that genre
            for genre_id in chosen_genres:
                #fetch books associated with the chosen genre
                cursor.execute("select B_id from book_genre where G_id = %s",(genre_id,))
                books_for_genre = cursor.fetchall()

                #randomly choose a book from the fetched books
                if books_for_genre:
                    chosen_book = random.choice(books_for_genre)[0]

                    #check if the entry already exists before inserting
                    cursor.execute("select count(*) from user_books where U_id = %s and B_id = %s", (u_id, chosen_book))
                    if cursor.fetchone()[0] == 0:
                        #insert values in user_book table
                        cursor.execute("INSERT into user_books (U_id, B_id) VAlues (%s,%s)", (u_id, chosen_book))

        #commit changes to the db
        conn.commit()

        #close the cursor
        cursor.close()

# Repeat the process every 5 seconds (adjust as needed)
while True:
    generate_fake_reads()
    print("Generated fake reads. Waiting for 15 seconds...")
    time.sleep(15)
