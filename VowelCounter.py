from flask import Flask,request,render_template

app = Flask(__name__)
@app.route('/', methods = ['POST','GET'])
def vowel_count():
    count = 0
    if(request.method == 'POST'):
     str = request.form.get('str')
     li = ['a','e','i','o','u']
     for i in str.lower():
        if(i in li):
            count += 1
    return render_template('VowelCounter.html', count = count)
if __name__ == '__main__':
    app.run(debug = True)
