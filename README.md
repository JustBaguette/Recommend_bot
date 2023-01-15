# Recommend_bot
Steps before running the model
In order to run this model open the pogchamp file
In there there will be a text file with a google drive link , download the 2 pickle files so that the rest of the program can work as intended
Steps for running the model 
Once downloaded place it in the root folder when running pog.py
when you run the code in pog.py it should give a https link which once used in a browser should lead you to the CreAItive library
There in the recommend tab you can use the recommendation model for books that are already in the dataset (which can be checked in the final_DB in the dataset_fixing folder)


The Dataset
We have used 4 datasets in total for both the popular books and The recommendation bot . 
books_1.Best_Books_Ever.csv (https://zenodo.org/record/4265096)
Users.csv (https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset)
Ratings.csv (https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset)
Books.csv (https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset)

For the Popular books dataset we have combined both Books and ratings together and then eliminated books that have less than 200 ratings (referring to the number of ratings)
And out of those we have chosen the top 12 highest books based on user ratings 

For the recommendation bot we have combined both Books dataset and the books_1.Best_Books_Ever as we needed both the image of the books as well as the genre for a content based recommender
After removing all unnecessary data we combined the names of authors , the description and the genre to create a column called tags which will be used for the comparison

Then we vectorize the data present in the tags using CountVectorizer 
so that they can be compared to each other and later the similarity will be judged based on the cosine similarity technique

Cosine similarity 
After comparing the books with each other based on the tags column we finally have a x dimentional space (where x is determined by the number of books)
Based on the angle between the different books from the point of origin We select the books that are closest to each other and at the end output that 
