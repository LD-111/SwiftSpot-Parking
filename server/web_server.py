from flask import Flask, render_template, request

app = Flask(__name__)

# Store parking spot availability data
parking_spot_data = {}

@app.route('/')
def index():
    return render_template('index.html', parking_spots=parking_spot_data)

@app.route('/update_availability', methods=['POST'])
def update_availability():
    data = request.get_json()
    spot_name = data['spot_name']
    availability = data['availability']
    parking_spot_data[spot_name] = availability
    print(f"Updated availability for {spot_name}: {availability}")
    return 'OK'

if __name__ == '__main__':
    app.run(debug=True)