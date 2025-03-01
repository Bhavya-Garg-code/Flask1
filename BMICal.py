from flask import Flask, request, render_template

app = Flask(__name__)
@app.route('/', methods = ['GET', 'POST'])

def BMI():
   mess = None
   bmi = None
   if(request.method == 'POST'):
    try:
     height = float(request.form.get('height'))
     weight = float(request.form.get('weight'))
     if(height < 0 or weight < 0):
      mess = 'Height and Weight are not positives'
     else:
      bmi = weight/(height**2)

     if(bmi <= 18.5):
        mess = 'Underweight'

     elif(18.5 <= bmi <= 24.9):
        mess = 'Healthy Weight'

     elif(25 <= bmi <= 29.9):
        mess = 'Overweight'

     elif(30 <= bmi <= 39.9):
        mess = 'Obese'

     elif(bmi >= 40):
        mess = 'Severe Obesity'
    except ValueError :
       return 'Please enter valid numbers'

   return render_template('BMICal.html', mess = mess, bmi = bmi)

if __name__ == '__main__':
    app.run(debug= True)