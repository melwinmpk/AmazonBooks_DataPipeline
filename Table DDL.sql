CREATE DATABASE amazonebooks;

CREATE TABLE amazone_books (
    book_id INT NOT NULL AUTO_INCREMENT
    ,book_title TEXT
    ,book_amount FLOAT
    ,book_author TEXT
    ,book_rating FLOAT
    ,book_link TEXT
    ,business_date DATE DEFAULT(CURRENT_DATE)
    ,PRIMARY KEY (book_id)
);

CREATE TABLE amazonebook_reviews (
    book_id INT NOT NULL
    ,reviewer_name TEXT
    ,rating FLOAT
    ,review_title TEXT
    ,review_content TEXT
    ,reviewed_on DATE
    ,business_date DATE DEFAULT(CURRENT_DATE)
);