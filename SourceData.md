Source Data Perpration 

Webscraping few pages of Books in Amazone website using Scrapy Liberary
Loading it into Mysql Database
Important Note: In this project very few pages are scraped for learning purposes

Developed 2 webspiders in single Project 
1) booklist : to fetch list of books in a page till the n number of pages
    Info that are fetched from webpage
        -> book_title
        -> book_amount
        -> book_author
        -> book_rating
        -> book_link
2) bookreview: to fetch top reviews of each books which is stored in my sql
    Info that are fetched from the webpage
        -> reviewer_name
        -> rating
        -> review_title
        -> review_content
        -> reviewed_on

