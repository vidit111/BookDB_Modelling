Book Streaming Database and Recommendation System: Data Modelling and DataBase planning

This project builds a complete Book Streaming Database system in MySQL and simulates a real-time recommendation engine.
It includes database creation, dynamic data insertion, fake user activity generation, cover image fetching, and a genre-based recommendation model — mimicking the backend operations of a real-world book streaming service.

*Learnt objectives such as:*
1)Build and structure complex relational databases with triggers, procedures, and constraints.

2)Work with Python-MySQL integration to perform CRUD operations.

3)Simulate real-time data ingestion and user activity.

4)Fetch and store external resources (like images) programmatically.

5)Build a simple recommendation system based on user reading habits.

6)Learn automation techniques for database operations and dynamic updates.


the following repository features a virtual library that i created to understand the data flow of a streaming service, the has a MySQL data base about books, it contains Book titles and other details, the Python codes generate fake users, user book reads, sql triggers and stored procedures make a book ranking table and a no ml recommendation engine

**File Descriptions**
Book_streaming_DB.sql:
Creates the entire database structure — tables, foreign keys, stored procedures, triggers, etc.
(Must run this first.)

config.py:
Contains SQL connection settings used by all other Python files.
(Edit your database credentials here.)

database.py:
Loads sample data from CSV files into the database tables.
(You can generate sample CSVs using ChatGPT.)

users.py:
Simulates fake user activity — generates users and reading records automatically every 15 seconds and inserts them into the database.

Cover_fetch.py and Book_cover.py:
Fetch book cover images based on book titles from the database and insert them into a new table for later retrieval.

Recommendation.py:
Builds a user-genre matrix to recommend the top 5 books a user is likely to enjoy.
(Automatically updates every 120 seconds.)

Sample CSV Files:
Provide example datasets to quickly populate the database for testing.

*Detailed descriptions:*
 1)Book_streaming_DB.sql: contains the sql queries to create the complete database, it creates every table, foreignkeys, stored procedures, Triggers etc. **It is necessary to first create the database to execute the other files.**
 2)config.py: this file contains the sql configurations that will be further used by other files, make sure to make chnages in it.
 3)database.py: this file inserts some table values that need to be inserted froma csv file, with chatgpt you can generate a csv file of the table format for sample values and insert into the mysql table by just mentioning the csv file path in this file.
4) users.py: this file generates fake users with fake reads and insert these records in your database in every 15 seconds.
5)Cover_fetch.py and Book_cover,py: fetch the book covers of the book names mentioned in the sql tbale books and insert into another table to be fetched in the future. 
6)Recommendation.py: Generates a matrix of the genres a user has read to determin the possible top 5 books that the user would like to read it updates in every 120 seconds.
7)Rest are sample csv files that contain a sample data that can be inserted through the database.py file by changing the csv file location.


