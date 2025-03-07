from flask import Flask, request, render_template
import mysql.connector
app = Flask(__name__)
@app.route('/login')
def login():
    msg = ''
    if(request.method == 'POST' and 'username' in username and 'password' in password):
        username = request.form.get('username')
        password = request.form.get('password')
        db = mysql.connector.connect(
            host = 'sql12.freesqldatabase.com',
            password = 'Vf2fgLzunm',
            user = ' sql12766450',
            database = 'sql12766450'
        )
        cursor = db.cursor()
        cursor.execute('SELECT * FROM LoginData WHERE NAME = %s AND PASSWORD = %s',(username,password))
        account = mysql.fetchone()
        if(account):
            print('Logged In successfully')
            name = account[0]
            id = account[1]
            print('Log in done')
            msg = 'Logged In'
            return render_template('UserLogin.html', msg = msg, name= name, id= id)
        else:
            print('Wrong Details')
            msg = 'Log In Unsuccessful!!'
            return render_template('UserLogin.html', msg = msg)
    else:
        return render_template('UserLogin.html')

@app.route('/logout')
def logout():
    name = ''
    id = ''
    msg = 'Logged Out Successfully!'
    return render_template('UserLogin.html', msg = msg, name = name, id = id)