from datetime import datetime
from flask import Flask, request, render_template

app  = Flask(__name__)
@app.route('/', methods = ['GET','POST'])


def difference():
    diff = None
    if(request.method == 'POST'):
        date1 = request.form.get('date1')
        date2 = request.form.get('date2')
        
        if(date1 and date2):
            format = '%Y-%m-%d'
            diff_date1 = datetime.strptime(date1,format)
            diff_date2 = datetime.strptime(date2,format)
            diff = abs((diff_date1 - diff_date2).days)
    return render_template('DateDiff.html', dif = diff)

if __name__ == '__main__':
    app.run(debug = True)
