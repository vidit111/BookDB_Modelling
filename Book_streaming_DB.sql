create database IF NOT EXISTS testing1;

use testing1;

DROP TABLE IF EXISTS user;
CREATE TABLE IF NOT EXISTS user (
    u_id INT PRIMARY KEY,
    b_read INT,
    verification TINYINT(1)
);



CREATE TABLE IF NOT EXISTS author (
    author_id INT PRIMARY KEY,
    b_published INT,
    author_name VARCHAR(255) UNIQUE
);

CREATE TABLE IF NOT EXISTS books (
    B_id INT PRIMARY KEY,
    B_name VARCHAR(255),
    B_sales INT,
    author_id INT,
    FOREIGN KEY (author_id) REFERENCES author(author_id)
);


CREATE TABLE IF NOT EXISTS user_Books (
    U_id INT,
    B_id INT,
    PRIMARY KEY (U_id, B_id),
    FOREIGN KEY (U_id) REFERENCES User(U_id),
    FOREIGN KEY (B_id) REFERENCES Books(B_id)
);

CREATE TABLE IF NOT EXISTS genre (
    G_id INT AUTO_INCREMENT PRIMARY KEY,
    Genre VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS book_genre (
    B_id INT,
    G_id INT,
    PRIMARY KEY (B_id, G_id),
    FOREIGN KEY (B_id) REFERENCES books(B_id),
    FOREIGN KEY (G_id) REFERENCES genre(G_id)
);

CREATE TABLE IF NOT EXISTS book_ranking (
    B_id INT NOT NULL,
    Ranking INT DEFAULT 0,
    PRIMARY KEY (B_id),
    FOREIGN KEY (B_id) REFERENCES Books(B_id)
);

DELIMITER //

CREATE PROCEDURE UpdateBookRanking()
BEGIN
    -- Create a temporary table to store the sorted data
    CREATE TEMPORARY TABLE IF NOT EXISTS TempBookRanking AS
        SELECT B_id, COUNT(U_id) AS read_count
        FROM User_books
        GROUP BY B_id
        ORDER BY read_count DESC;

    -- Update the book_ranking table with the sorted data
    DELETE FROM book_ranking;

    INSERT INTO book_ranking (B_id, Ranking)
        SELECT B_id, ROW_NUMBER() OVER () AS Ranking
        FROM TempBookRanking;

    -- Drop the temporary table
    DROP TEMPORARY TABLE IF EXISTS TempBookRanking;
END //

DELIMITER ;


DELIMITER //

CREATE TRIGGER after_user_books_insert
AFTER INSERT ON User_books
FOR EACH ROW
BEGIN
    -- Call the stored procedure to update book rankings
    CALL UpdateBookRanking();
END //

DELIMITER ;

CREATE TABLE IF NOT EXISTS book_cover (
    c_id INT AUTO_INCREMENT PRIMARY KEY,
    b_id INT,
    c_image MEDIUMBLOB,
    FOREIGN KEY (b_id) REFERENCES books(b_id)
);

show tables;