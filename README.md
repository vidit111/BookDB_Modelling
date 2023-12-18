# Book

following is the ER diagram of the Database: ![image](https://github.com/vidit111/Book_streaming_sql/assets/140490594/2e6089f6-7660-48de-a79a-4f9585e1e9ed)

the following repository features a virtual library that i created to understand the data flow of a streaming service, the has a MySQL data base about books, it contains Book titles and other details, the Python codes generate fake users, user book reads, sql triggers and stored procedures make a book ranking table and a no ml recommendation engine

File descriptions:
 1)Book_streaming_DB.sql: contains the sql queries to create the complete database, it creates every table, foreignkeys, stored procedures, Triggers etc. **It is necessary to first create the database to execute the other files.**
 2)config.py: this file contains the sql configurations that will be further used by other files, make sure to make chnages in it.
 3)database.py: this file inserts some table values that need to be inserted froma csv file, with chatgpt you can generate a csv file of the table format for sample values and insert into the mysql table by just mentioning the csv file path in this file.
4) users.py: this file generates fake users with fake reads and insert these records in your database in every 15 seconds.
5)Cover_fetch.py and Book_cover,py: fetch the book covers of the book names mentioned in the sql tbale books and insert into another table to be fetched in the future. 
6)Recommendation.py: Generates a matrix of the genres a user has read to determin the possible top 5 books that the user would like to read it updates in every 120 seconds.
7)Rest are sample csv files that contain a sample data that can be inserted through the database.py file by changing the csv file location.
