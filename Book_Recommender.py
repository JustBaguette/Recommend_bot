#imports required
import mysql.connector
from flask import Flask, render_template, request, url_for, redirect
from flask_mysqldb import MySQL
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import pymysql

#connect mysql to python - not necessary but dont remove this code
mydb = mysql.connector.connect(host="localhost", user="root",password="", database='library')

if mydb.is_connected():
    print("connection complete")

my_c = mydb.cursor()

# function to create connection using pymysql (connecting flask and msql database)
def sql_connection():
    conn = pymysql.connect(user='root', password='', db='library',host='localhost')
    c=conn.cursor()
    return conn, c

# initialize the flask application
app = Flask(__name__,  template_folder='templates')

#the user input details are stored in the mysql database

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method=='POST':
        name=request.form.get('name')
        username=request.form.get('username')
        password = request.form.get('password')
        conn, c = sql_connection()
        c.execute("INSERT INTO user_details(name, username, password) VALUES(%s,%s,%s)", (name,username,password))
        conn.commit()
        conn.close()
        c.close()
    return render_template("Signin.html")



@app.route('/Login', methods = ['GET', 'POST'])
def log_in():
    if request.method=='POST':
        print('success')
        username=request.form.get('username')
        password=request.form.get('password')
        print(username)
        conn, c = sql_connection()
        
        c.execute("select * from user_details where username=%s and password=%s", (username,password))
        c.fetchall()
        if(c.rowcount==0):
            pass #print a text in login page saying you are not a user
        else:
            print(c.rowcount)
            pass 
            #write the code to shift to the recommended book section--- remove pass afterwards
        conn.close()
        c.close()        
    return render_template("Login.html")        


if __name__ == '__main__':
    app.run(debug=True)



# recommending books by collaborative filtring

table = pd.read_csv(r'D:\project\FLC_PROJECT\cosine_similarity.csv')

table = pd.DataFrame(table)
similarity_score=cosine_similarity(table)

book_list=[]
def recommend(book_name):
    index = np.where(table.index == book_name)[0][0]
    similar_items = sorted(list(enumerate(similarity_score[index])),key=lambda a:a[1],reverse=True)[1:6]
    for i in similar_items:
        book_list.append(table.index[i[0]])
    return book_list    
 
