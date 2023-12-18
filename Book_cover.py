import os
import mysql.connector
from config import mysql_config  # Import MySQL configuration from config.py


# Connect to MySQL
connection = mysql.connector.connect(**mysql_config)
cursor = connection.cursor()

# Folder path containing cover images
folder_path = r'C:\Users\Vidit\Desktop\Streaming\data\covers'

# Get a list of image files in the folder
image_files = [f for f in os.listdir(folder_path) if f.endswith('.jpg')]

# Insert images into the book_cover table
for image_file in image_files:
    b_id = os.path.splitext(image_file)[0]  # Use filename (excluding extension) as b_id and c_id

    # Read image binary data
    with open(os.path.join(folder_path, image_file), 'rb') as f:
        c_image = f.read()

    # Insert into the book_cover table
    insert_query = "INSERT INTO book_cover (b_id, c_id, c_image) VALUES (%s, %s, %s)"
    cursor.execute(insert_query, (b_id, b_id, c_image))
    connection.commit()
    print(f"Inserted cover image for b_id/c_id {b_id}")

# Close MySQL connection
cursor.close()
connection.close()
