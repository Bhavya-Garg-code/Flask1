from flask import Flask, render_template, request
from datetime import datetime
app = Flask(__name__)
@app.route('/')

def home():
    return render_template('index.html')
@app.route('/calculate', methods = ['POST'])

def calculate():
   try:
    inp = int(request.form.get('birth_year'))
    current = datetime.now().year

    if(inp > current):
        return render_template('index.html', error = 'Please enter a valid value')
    
    age = current - inp
    return render_template('index.html', age = age)
   
   except ValueError:
      return render_template('index.html', error = 'Enter valid data')

if __name__ == '__main__':
    app.run(debug = True)
