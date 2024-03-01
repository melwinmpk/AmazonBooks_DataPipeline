
<img width="1052" alt="image" src="https://github.com/melwinmpk/AmazonBooks_DataPipeline/assets/25386607/a3b2c949-2e49-4418-a7e2-bfede2356fc9">

<pre>

CREATE DATABASE amazonebooks;

USE DATABASE amazonebooks;
USE SCHEMA public;

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

CREATE OR REPLACE STAGE amazone_books_stage
FILE_FORMAT = (TYPE= csv FIELD_DELIMITER = ',' FIELD_OPTIONALLY_ENCLOSED_BY = '"' SKIP_HEADER = 1);

-- We Can Use Put command only in SnowSQL
USE DATABASE amazonebooks;
PUT 'file:///<PATH>/amazonebooks.csv' @amazone_books_stage; 

COPY INTO amazone_books FROM @amazone_books_stage;

CREATE SCHEMA config;

CREATE TABLE dag_config(
  dag_id INT NOT NULL AUTO_INCREMENT,
  dag_name TEXT,
  last_extract_date Date
);

</pre>  
