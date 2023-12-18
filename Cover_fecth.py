import requests
import os

# Function to get book cover image URL
def get_book_cover_image(title):
    base_url = 'https://www.googleapis.com/books/v1/volumes'
    params = {'q': f'intitle:{title}'}

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        items = data.get('items', [])

        if items:
            # Get the first item (assuming it's the most relevant)
            volume_info = items[0].get('volumeInfo', {})
            image_links = volume_info.get('imageLinks', {})

            # Get the thumbnail image link
            thumbnail_link = image_links.get('thumbnail')

            return thumbnail_link

    return None

import os

import os

# Function to download and save the image
def download_and_save_image(url, b_id):
    # Specify the folder location
    folder_location = r'C:\Users\Vidit\Desktop\Streaming\data\covers'

    # Check if the image file already exists
    image_filename = os.path.join(folder_location, f'{b_id}.jpg')
    if os.path.exists(image_filename):
        print(f'Cover image for b_id {b_id} already exists.')
        return

    response = requests.get(url)

    if response.status_code == 200:
        # Save the image with the book's b_id as the filename in the specified folder
        with open(image_filename, 'wb') as f:
            f.write(response.content)
        print(f'Saved cover image for b_id {b_id} as {image_filename}')
    else:
        print(f'Failed to download cover image for b_id {b_id}')


# Book data with b_id and b_name
book_data = [
    (1, 'The Great Gatsby'),
    (2, 'To Kill a Mockingbird'),
    (3, "Harry Potter and the Sorcerer's Stone"),
    (4, '1984'),
    (5, 'Pride and Prejudice'),
    (6, 'The Catcher in the Rye'),
    (7, 'The Hobbit'),
    (8, 'The Lord of the Rings: The Fellowship of the Ring'),
    (9, 'One Hundred Years of Solitude'),
    (10, 'Brave New World'),
    (11, 'The Grapes of Wrath'),
    (12, 'Crime and Punishment'),
    (13, 'The Chronicles of Narnia: The Lion, the Witch and the Wardrobe'),
    (14, 'The Alchemist'),
    (15, 'The Picture of Dorian Gray'),
    (16, 'Jane Eyre'),
    (17, 'Anna Karenina'),
    (18, 'The Count of Monte Cristo'),
    (19, 'The Little Prince'),
    (20, 'A Tale of Two Cities'),
    (21, 'The Brothers Karamazov'),
    (22, 'The Old Man and the Sea'),
    (23, 'Gone with the Wind'),
    (24, 'The Scarlet Letter'),
    (25, 'The Iliad'),
    (26, 'Les Misérables'),
    (27, 'The Road Less Traveled'),
    (28, 'The Stand'),
    (29, 'Fahrenheit 451'),
    (30, "The Hitchhiker's Guide to the Galaxy"),
    (31, 'The Art of War'),
    (32, 'The Secret Garden'),
    (33, 'The Shining'),
    (34, 'The Outsiders'),
    (35, 'East of Eden'),
    (36, 'A Clockwork Orange'),
    (37, 'The Princess Bride'),
    (38, 'The Girl with the Dragon Tattoo'),
    (39, 'The Help'),
    (40, 'Dracula'),
    (41, 'The Fault in Our Stars'),
    (42, 'The Martian'),
    (43, 'Dune'),
    (44, 'The Sun Also Rises'),
    (45, 'The Color Purple'),
    (46, 'The Bell Jar'),
    (47, 'The Immortal Life of Henrietta Lacks'),
    (48, 'The Road to Serfdom'),
    (49, 'A Man Called Ove'),
    (50, 'Where the Crawdads Sing')
]


# Fetch cover images and save them
for b_id, b_name in book_data:
    cover_image_url = get_book_cover_image(b_name)

    if cover_image_url:
        download_and_save_image(cover_image_url, b_id)
    else:
        print(f'Cover image not found for b_id {b_id} ({b_name})')
