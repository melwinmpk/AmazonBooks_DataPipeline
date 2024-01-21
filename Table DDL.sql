create database amazonebooks;

drop table if exists amazone_books;
create table amazone_books (
    book_id int NOT NULL AUTO_INCREMENT
    ,book_title text
    ,book_amount float
    ,book_author text
    ,book_rating float
    ,book_link   text
    ,PRIMARY KEY (book_id)
);