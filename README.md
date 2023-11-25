# SwiftSpot-Parking
## Overview
This Python script sets up an MQTT server that subscribes to multiple topics related to a parking lot, collecting parameters such as availability, temperature, and humidity for each spot. The script uses the Paho MQTT library and can be configured to connect to any MQTT broker.

## Requirements
- Python 3.x
- Paho MQTT library
  
Install the required libraries using the following command:

```bash
pip install -r python_requirements.txt
```
## Usage
Clone the repository:
```bash
git clone https://github.com/yourusername/mqtt-parking-lot-server.git

cd mqtt-parking-lot-server
```
Update the MQTT broker details in server.py:

```python
# MQTT broker details
broker_address = 'example.com'
broker_port = your_server_port
```
Run the inner server:
```bash
cd '.\server'
python server.py
```
Run the private web server:
```bash
cd '.\server\private server\'
python web_server.py
```
Run the public web server:
```bash
cd '.\server\public server\'
python admin_server.py
```

The inner servers will connect to the test Mosquitto broker and subscribe to topics for three parking spots. Received messages will be sent to the web servers depending on their nature: 
- The private web server will handle the availability, temperature and humidity. 
- The public web server will only handle the availability of each parking spot.

## Testing
Test the server using the following example commands:

Publish humidity data:
```bash
mosquitto_pub -h test.mosquitto.org -t "ICC452-1/swiftspot/spot1/availability" -m "True"
```
Subscribe to temperature data:
```bash
mosquitto_sub -h test.mosquitto.org -t "ICC452-1/swiftspot/spot1/availability"
```
Adjust the topic and message as needed for testing different parameters and parking spots.


## Contributors
- Lorenzo Devia ( [LD-111](https://github.com/LD-111) )
- Kianush Atighi-Moghaddam ( [kianush00](https://github.com/kianush00) )

## License
This project is licensed under the MIT License - see the LICENSE file for details.
