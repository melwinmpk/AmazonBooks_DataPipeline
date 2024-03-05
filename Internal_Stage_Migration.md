
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

Once Completed remove 
REMOVE @amazone_books_stage;


CREATE SCHEMA config;

CREATE TABLE dag_config(
  dag_id INT NOT NULL AUTO_INCREMENT,
  dag_name TEXT,
  last_extract_date Date
);

</pre>  


<img width="1210" alt="image" src="https://github.com/melwinmpk/AmazonBooks_DataPipeline/assets/25386607/f14d9492-fdc6-4670-b56b-75303751392e">
<img width="945" alt="image" src="https://github.com/melwinmpk/AmazonBooks_DataPipeline/assets/25386607/88cf3b74-3387-4e1e-9309-c550ee13d487">
<img width="361" alt="image" src="https://github.com/melwinmpk/AmazonBooks_DataPipeline/assets/25386607/51e9538e-0cd2-4c24-b5a2-45337524460d">
<img width="780" alt="image" src="https://github.com/melwinmpk/AmazonBooks_DataPipeline/assets/25386607/241fe857-f986-487b-98f1-e9a378b5b426">
<img width="782" alt="image" src="https://github.com/melwinmpk/AmazonBooks_DataPipeline/assets/25386607/71688582-4fc7-47ce-b646-c25e0c373463">
<img width="982" alt="image" src="https://github.com/melwinmpk/AmazonBooks_DataPipeline/assets/25386607/9db6ff6a-e755-4c33-97c2-bf9854b7b8ba">
