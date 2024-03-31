# Assignment #4 – Send and receive messages via MQTT
# Date: April 01, 2024
# Group 3:
#  - Cong Lanh Hoang
#  - Einer Cupino
#  - Jasper Jan Tan
#  - Kwok Yuk Chui
#  - Wing Chi Lam

import json
import time
import paho.mqtt.client as mqtt

from group_1_util import TemperatureGenerator

class Subscriber:
  def __init__(self, broker_address, broker_port, topic):
    self.__broker_address = broker_address
    self.__broker_port = broker_port
    self.__topic = topic
    self.__client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
    self.__client.on_connect = self.__on_connect # Assign the on_connect delegate to the function defined below
    self.__client.on_message = self.__on_message # Assign the on_message delegate to the function defined below
    self.__temp_gen = TemperatureGenerator()
    self.__running = False
  
  # Define the function to be called when the client connects to the broker
  def __on_connect(self, client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe(self.__topic)

  # Define the function to be called when a message is received
  def __on_message(self, client, userdata, message):
    # Extract the payload (a JSON string) from the message
    payload = message.payload.decode()
    # Convert the JSON string to a dictionary
    data = json.loads(payload)
    # Print the dictionary in a human-readable format
    self.__temp_gen.print_data(data)
  
  # Create a client
  def connect(self):
    self.__client.connect(self.__broker_address, self.__broker_port)

  # Subscribe to the specified topic
  def subscribe(self):
    self.__client.subscribe(self.__topic)
    print(f"Client subscribed to {self.__topic}")
  
  # Start the client's loop to begin receiving messages
  def start(self):
    self.connect()
    self.subscribe()
    self.__running = True
    self.__client.loop_forever()
  
  # Stop the client's loop to stop receiving messages
  def stop(self):
    self.__running = False
    self.__client.loop_stop()

if __name__ == "__main__":
  # Define the MQTT broker address and port
  broker_address = "localhost"
  broker_port = 1883

  # Define the topic to which data will be published
  topic = "room_temperature_data"

  # Create a subscriber instance
  subscriber = Subscriber(broker_address, broker_port, topic)
  subscriber.start()
  
  try:
    while True:
      time.sleep(1)
  except KeyboardInterrupt:
    subscriber.stop()
    print("Subscriber stopped")
