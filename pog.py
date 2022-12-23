from flask import Flask, render_template, request
from flask_mysqldb import MySQL
#import yaml
app = Flask(__name__)
#configure db
#db = yaml.load(open('db.yaml'))
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '25101995'
app.config['MYSQL_DB'] = 'users'

mysql = MySQL(app)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        #FETCH FORM DATA
        userDetails = request.form
        name = userDetails['name']
        email = userDetails['Email']
        username = userDetails['username']
        password = userDetails['password']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO userdb(name, email, username, password) VALUES(%s,%s,%s,%s)", (name,email,username,password))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('Signin.html')

if __name__ == '__main__':
    app.run(debug=True)