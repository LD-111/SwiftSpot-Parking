import paho.mqtt.client as mqtt

# MQTT broker details
broker_address = 'test.mosquitto.org'  # Replace with your MQTT broker's address
broker_port = 1883  # Replace with your MQTT broker's port

# Topics for three parking spots
ssspot1_availability_topic = 'ICC452-1/swiftspot/ssspot1/availability'
ssspot1_temperature_topic = 'ICC452-1/swiftspot/ssspot1/temperature'
ssspot1_humidity_topic = 'ICC452-1/swiftspot/ssspot1/humidity'

ssspot2_availability_topic = "ICC452-1/swiftspot/ssspot2/availability"
ssspot2_temperature_topic = "ICC452-1/swiftspot/ssspot2/temperature"
ssspot2_humidity_topic = "ICC452-1/swiftspot/ssspot2/humidity"

ssspot3_availability_topic = "ICC452-1/swiftspot/ssspot3/availability"
ssspot3_temperature_topic = "ICC452-1/swiftspot/ssspot3/temperature"
ssspot3_humidity_topic = "ICC452-1/swiftspot/ssspot3/humidity"

# Callback when the client connects to the broker
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    # Subscribe to topics upon successful connection
    topics = [
        (ssspot1_availability_topic, 0),
        (ssspot1_temperature_topic, 0),
        (ssspot1_humidity_topic, 0),
        (ssspot2_availability_topic, 0),
        (ssspot2_temperature_topic, 0),
        (ssspot2_humidity_topic, 0),
        (ssspot3_availability_topic, 0),
        (ssspot3_temperature_topic, 0),
        (ssspot3_humidity_topic, 0),
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