from flask import Flask, render_template, request

app = Flask(__name__)

# Initialize parking spot availability data
parking_spot_data = {
    "spot1-availability": True,
    "spot1-temperature(C°)": 0.0,
    "spot1-humidity(%)": 0.0,
    "spot2-availability": True,
    "spot2-temperature(C°)": 0.0,
    "spot2-humidity(%)": 0.0,
    "spot3-availability": True,
    "spot3-temperature(C°)": 0.0,
    "spot3-humidity(%)": 0.0,
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
        
    parking_spot_data[spot_name+"-availability"] = availability
    print(f"Updated availability for {spot_name}: {availability}")
    return 'OK'

@app.route('/update_temperature', methods=['POST'])
def update_temp():
    data = request.get_json()
    print(data)
    spot_name = data['spot_name']
    temperature = data['temperature']
    parking_spot_data[spot_name+"-temperature(C°)"] = temperature
    print(f"Updated param for {spot_name}: {temperature}")
    return 'OK'

@app.route('/update_humidity', methods=['POST'])
def update_humid():
    data = request.get_json()
    print(data)
    spot_name = data['spot_name']
    humidity = data['humidity']
    parking_spot_data[spot_name+"-humidity(%)"] = humidity
    print(parking_spot_data)
    print(f"Updated param for {spot_name}: {humidity}")
    return 'OK'

if __name__ == '__main__':
    app.run(port=8000, debug=True)