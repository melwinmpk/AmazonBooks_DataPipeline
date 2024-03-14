# AmazonBookData_DataPipeline

</p>

<h2>Source Data Perpration</h2> 

<p>Scraping few pages of Books on the Amazone website using Scrapy Library. Automating the entire process using Airflow
Loading it into Mysql Database</p>
<p><b>Important Note:</b> In this project we are scraping a few pages for learning purposes Only.</p>

<img width="1009" alt="image" src="https://github.com/melwinmpk/AmazonBooks_DataPipeline/assets/25386607/8b987143-52b7-47db-a73e-3fa177791eca"><br>

<p>Developed 2 web spiders in a single Project</p> 
<ol>
    <li><b>booklist:</b>. to fetch a list of books on a page till the n number of pages <br>
        Info that is fetched from the webpage and loaded into the Table amazone_books in Mysql Database
    </li>
    <ul>
        <li>book_title</li>
        <li>book_amount</li>
        <li>book_author</li>
        <li>book_rating</li>
        <li>book_link</li>
    </ul>    
    <li><b>bookreview:</b> to fetch top reviews of each book which is stored in my SQL.<br>
    Info that is fetched from the webpage and loaded into the Table amazonebook_reviews in Mysql Database</li>
    <ul>
        <li>reviewer_name</li>
        <li>rating</li>
        <li>review_title</li>
        <li>review_content</li>
        <li>reviewed_on</li>
    </ul>    
</ol>

<p>DDL for MLSQL Data Base</p>

<pre>
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
	);
</pre>

<h3>Sample Output</h3>
<b>Dag Image</b>
<img width="1215" alt="image" src="https://github.com/melwinmpk/AmazonBooks_DataPipeline/assets/25386607/37f602b0-2324-4cb3-8cb6-d2f647a67e93">
<img width="787" alt="image" src="https://github.com/melwinmpk/AmazonBooks_DataPipeline/assets/25386607/7943baef-cd63-4ea7-8367-a81fbfa00916">
<img width="787" alt="image" src="https://github.com/melwinmpk/AmazonBooks_DataPipeline/assets/25386607/5a27619d-f820-4919-b64a-535c5c7a8b09">
<!-- <img width="787" alt="image" src="https://github.com/melwinmpk/AmazonBooks_DataPipeline/assets/25386607/c5efe69e-afea-446d-bfac-dd813778fc8e"> -->


