import paho.mqtt.client as mqtt
import requests

# MQTT broker details
broker_address = "test.mosquitto.org"  # Replace with your MQTT broker's address
broker_port = 1883  # Replace with your MQTT broker's port

# Topics for three parking spots
sspot1_availability_topic = "ICC452-1/swiftspot/sspot1/availability"
sspot1_temperature_topic = "ICC452-1/swiftspot/sspot1/temperature"
sspot1_humidity_topic = "ICC452-1/swiftspot/sspot1/humidity"

sspot2_availability_topic = "ICC452-1/swiftspot/sspot2/availability"
sspot2_temperature_topic = "ICC452-1/swiftspot/sspot2/temperature"
sspot2_humidity_topic = "ICC452-1/swiftspot/sspot2/humidity"

sspot3_availability_topic = "ICC452-1/swiftspot/sspot3/availability"
sspot3_temperature_topic = "ICC452-1/swiftspot/sspot3/temperature"
sspot3_humidity_topic = "ICC452-1/swiftspot/sspot3/humidity"

# Callback when the client connects to the broker
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    # Subscribe to topics upon successful connection
    topics = [
        (sspot1_availability_topic, 0),
        (sspot1_temperature_topic, 0),
        (sspot1_humidity_topic, 0),
        (sspot2_availability_topic, 0),
        (sspot2_temperature_topic, 0),
        (sspot2_humidity_topic, 0),
        (sspot3_availability_topic, 0),
        (sspot3_temperature_topic, 0),
        (sspot3_humidity_topic, 0),
    ]
    for topic in topics:
        client.subscribe(topic)
        print("subscribed to "+topic[0])

# Callback when a message is received from the broker
def on_message(client, userdata, msg):
    print("message received")
    topic = msg.topic
    payload = msg.payload.decode("utf-8")

    print(f"Received message on topic '{topic}': {payload}")

    # Add your business logic here based on the received topic and payload

    # Update the web server with parking spot availability
    update_web_server(topic, payload)

def update_web_server(topic, payload):
    # Extract parking spot name from the topic
    spot_name = topic.split("/")[-1]

    # Define the URL of the web server
    web_server_url = "http://localhost:5000/update_availability"

    # Create JSON data
    data = {"spot_name": spot_name, "availability": payload}

    # Send a POST request to the web server
    try:
        response = requests.post(web_server_url, json=data)
        response.raise_for_status()
        print(f"Updated web server: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error updating web server: {e}")

# Create an MQTT client
client = mqtt.Client()

# Set up callback functions
client.on_connect = on_connect
client.on_message = on_message

# Connect to the broker
client.connect(broker_address, broker_port, 60)

# Start the MQTT loop
print("starting server...")
client.loop_forever()