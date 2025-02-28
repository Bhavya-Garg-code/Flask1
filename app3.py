from flask import Flask, request,jsonify, render_template

from geopy.geocoders import Nominatim

app = Flask(__name__)
geolocator = Nominatim(user_agent = 'district_locator')
@app.route('/')
def home():
    return render_template('Locator.html')
@app.route('/locate', methods = ['POST'])
def locate():
    dist = request.form.get('dist')
    if(not dist):
        return jsonify({'Error':'District is required'}),404
    location = geolocator.geocode(dist, exactly_one = True, addressdetails= True)
    if(dist and 'address' in location.raw):
        address = location.raw['address']
        return jsonify({
            'district':dist,
            'state':address.get('state','Unknown'),
            'country':address.get('country','Unknown')
        })
    return jsonify({'Error':'Location not found!'}),404

if __name__ == '__main__':
    app.run(debug = True)
