create database amazonebooks;

drop table if exists amazone_books;
create table amazone_books (
    book_id int NOT NULL AUTO_INCREMENT
    ,book_title text
    ,book_amount float
    ,book_author text
    ,book_rating float
    ,book_link   text
    ,business_date DATE DEFAULT (CURRENT_DATE)
    ,PRIMARY KEY (book_id)
);

create table amazonebook_reviews (
    book_id int NOT NULL
    ,reviewer_name text
    ,rating float
    ,review_title text
    ,review_content text
    ,reviewed_on date
);