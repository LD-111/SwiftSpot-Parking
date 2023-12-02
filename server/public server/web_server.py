from flask import Flask, render_template, request

app = Flask(__name__)

# Initialize parking spot availability data
parking_spot_data = {
    "spot1": True,
    "spot2": True,
    "spot3": True,
}

@app.route('/')
def index():
    return render_template('index.html', parking_spots=parking_spot_data)

@app.route('/update_availability', methods=['POST'])
def update_availability():
    data = request.get_json()
    print(data)
    spot_name = data['spot_name']
    availability = data['availability']

    if availability == "1":
        availability = True
    elif availability == "0":
        availability = False
        
    parking_spot_data[spot_name] = availability
    print(f"Updated availability for {spot_name}: {availability}")
    return 'OK'

if __name__ == '__main__':
    app.run(debug=True)