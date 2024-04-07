# Final Project
# Date: April 12, 2024
# Group 1:
#  - Cong Lanh Hoang
#  - Einer Cupino
#  - Jasper Jan Tan
#  - Kwok Yuk Chui
#  - Wing Chi Lam

import json
import random
import time
import paho.mqtt.client as mqtt

from group_1_data_generator import TemperatureGenerator

class Publisher:
  def __init__(self, broker_address, broker_port, topic):
    self.__broker_address = broker_address
    self.__broker_port = broker_port
    self.__topic = topic
    self.__client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
    self.__temp_gen = TemperatureGenerator()
    self.__running = False
    self.__log = []

  @property
  def running(self):
    return self.__running
  
  @property
  def log(self):
    return "\n".join(self.__log)

  @log.setter
  def log(self, value):
    self.__log.append(value)

  # Create a dictionary containing sample data
  def generate_data(self):
    data = self.__temp_gen.create_data()
    return json.dumps(data)

  def generate_error_data(self):
    data = self.__temp_gen.create_error_data()
    return json.dumps(data)

  # Create a client
  def connect(self):
    self.__client.connect(self.__broker_address, self.__broker_port)
    print(f"[PUBLISHER] Publisher {id(self)} connected to {self.__broker_address}:{self.__broker_port}")
    self.log = f"[PUBLISHER] Publisher {id(self)} connected to {self.__broker_address}:{self.__broker_port}"

  # Publish the JSON string to the specified topic
  def publish(self, payload):
    self.__client.publish(self.__topic, payload)
    print(f"[PUBLISHER] Publisher {id(self)} published data {payload} to {self.__topic}")
    self.log = f"[PUBLISHER] Publisher {id(self)} published data {payload} to {self.__topic}"
  
  def skip_publish(self):
    print(f"[PUBLISHER] Publisher {id(self)} published failed to {self.__topic}")
    self.log = f"[PUBLISHER] Publisher {id(self)} published failed to {self.__topic}"

  # Disconnect from the MQTT broker
  def disconnect(self):
    self.__client.disconnect()

  # Publish multiple payloads
  def publish_data(self):
    while self.__running:
      # Publish the data. With a frequency of about 1 in very 100 transmissions, transmit off the chart data 
      payload = self.generate_error_data() if random.randint(1, 100) == 1 else self.generate_data()
      self.publish(payload)
      time.sleep(2)
      # Simulate missed transmissions with a frequency of about 1 in very 100 transmissions
      if random.randint(1, 100) == 1:
        self.skip_publish()
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