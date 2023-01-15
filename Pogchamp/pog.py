from flask import Flask,render_template,request
import pickle

#import numpy as np

popular_df = pickle.load(open("pouplar.pkl", 'rb'))
vectors = pickle.load(open('vectors.pkl','rb'))
books = pickle.load(open('books.pkl','rb'))
similar= pickle.load(open('similar.pkl','rb'))



app = Flask(__name__)



@app.route('/')
def index():
    return render_template('Front_page.html',
                           book_name = list(popular_df['Book-Title'].values),
                           author=list(popular_df['Book-Author'].values),
                           image=list(popular_df['Image-URL-M'].values),
                           votes=list(popular_df['Book-Rating'].values),
                           )


@app.route('/recommend_content')
def recommend_ui():
    return render_template('Recommend.html')

@app.route('/recommend_books',methods=['post'])
def recommend():
    booke= request.form.get('user_input')
    book_index = books[books['Title'] == booke].index[0]
    dist = similar[book_index]
    book_list = sorted(list(enumerate(dist)),reverse = True, key = lambda x:x[1])[1:7]
    
    book = []
    for i in book_list:
        item = []
        temp = books[books['Title']== books.iloc[i[0]].Title]
        #print (temp)
        item.extend(list(temp['Title'].values))
        item.extend(list(temp['Book-Author'].values))
        item.extend(list(temp['Image-URL-M_x'].values))
        
        book.append(item)

    print(book)
    return render_template('recommend.html', book=book)


     



if __name__ == '__main__':
    app.run(debug=True)