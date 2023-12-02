# SwiftSpot-Parking
## Overview
This University Project consists in a number of sensors connected to a microcontroller that collect data about the status of a parking spot that then sends to an MQTT broker, the Mosquitto Test Server by default. It also features an MQTT server that subscribes to multiple topics related to a parking lot, collecting parameters such as availability, temperature, and humidity for each spot, displaying them in a simple webserver available to the public and one intended for administrators. The project can be configured to connect to any MQTT broker.

## Requirements
- Python 3.x
- Paho MQTT library
- Flask
  
Install the required libraries using the following command:

```bash
pip install -r python_requirements.txt
```
## Arduino Setup
![Arduino Setup](./arduino/Arduino%20Setup.jpg)

There are two sensors in use:
- A DHT11 CNT5 temperature and moisture sensor
- A HC-SR04 ultrasonic sensor

The microcontroller used was an Arduino MKR1000. Open the code contained in arduino\arduino_sketch in the Arduino IDE, change the necessary configuration variables (SSID, network password, pins) and upload it to the microcontroller. 

## Server Usage
Clone the repository:
```bash
git clone https://github.com/LD-11/mqtt-parking-lot-server.git

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

The inner server will connect to the test Mosquitto broker and subscribe to topics for three parking spots. Received messages will be sent to the web servers depending on their nature: 
- The private web server will handle the availability, temperature and humidity. 
- The public web server will only handle the availability of each parking spot.

## Testing
Test the server using the following example commands(Replace with your chosen MQTT server):

Publish availability data:
```bash
mosquitto_pub -h test.mosquitto.org -t "ICC452-1/swiftspot/spot1/availability" -m "0"
```
Subscribe to availability data:
```bash
mosquitto_sub -h test.mosquitto.org -t "ICC452-1/swiftspot/spot1/availability"
```
Adjust the topic and message as needed for testing different parameters and parking spots.


## Contributors
- Lorenzo Devia ( [LD-111](https://github.com/LD-111) )
- Kianush Atighi-Moghaddam ( [kianush00](https://github.com/kianush00) )

## License
This project is licensed under the MIT License - see the LICENSE file for details.
