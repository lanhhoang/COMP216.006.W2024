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

class Publisher:
  def __init__(self, broker_address, broker_port, topic):
    self.__broker_address = broker_address
    self.__broker_port = broker_port
    self.__topic = topic
    self.__client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
    self.__temp_gen = TemperatureGenerator()
    self.__running = False

  # Create a dictionary containing sample data
  def generate_data(self):
    data = self.__temp_gen.create_data()
    return json.dumps(data)

  # Create a client
  def connect(self):
    self.__client.connect(self.__broker_address, self.__broker_port)

  # Publish the JSON string to the specified topic
  def publish(self, payload):
    self.__client.publish(self.__topic, payload)

  # Disconnect from the MQTT broker
  def disconnect(self):
    self.__client.disconnect()

  # Publish multiple payloads
  def publish_data(self):
    while self.__running:
      payload = self.generate_data()
      self.publish(payload)
      print(f"Data {payload} published to {topic}")
      time.sleep(5)
  
  # Start the client and begin publishing data
  def start(self):
    self.connect()
    self.__running = True
    self.publish_data()
  
  # Stop publishing data and disconnect from the broker
  def stop(self):
    self.__running = False
    self.disconnect()

if __name__ == "__main__":
  # Define the MQTT broker address and port
  broker_address = "localhost"
  broker_port = 1883

  # Define the topic to which data will be published
  topic = "room_temperature_data"

  # Create a Publisher instance
  publisher = Publisher(broker_address, broker_port, topic)
  publisher.start()

  try:
    while True:
      time.sleep(1)
  except KeyboardInterrupt:
    publisher.stop()
    print("Publisher stopped")