from flask import Flask,request, render_template

app = Flask(__name__)
@app.route('/', methods = ['GET','POST'])

def leapyear():
    ans = None
    year_inp = request.form.get('year')
    if(year_inp):
        if(int(year_inp)%4 == 0):
            ans = "Yes, it is a leap year"
        else:
            ans = "No, it is not a leap year"
    return render_template('LeapYear.html',ans = ans)

if __name__ == '__main__':
    app.run(debug = True)
