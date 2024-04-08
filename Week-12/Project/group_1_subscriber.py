# Final Project
# Date: April 12, 2024
# Group 1:
#  - Cong Lanh Hoang
#  - Einer Cupino
#  - Jasper Jan Tan
#  - Kwok Yuk Chui
#  - Wing Chi Lam

import json
import time
import paho.mqtt.client as mqtt

from group_1_data_generator import TemperatureGenerator

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
    self.__log = []

  @property
  def running(self):
    return self.__running
  
  @property
  def log(self):
    return "\n".join(self.__log)
  
  # setter for log
  @log.setter
  def log(self, value):
    self.__log.append(value)
  
  # Define the function to be called when the client connects to the broker
  def __on_connect(self, client, userdata, flags, rc):
    print(f"[SUBSCRIBER] Connected with result code {rc}")
    self.log = f"[SUBSCRIBER] Connected with result code {rc}"
    client.subscribe(self.__topic)

  # Define the function to be called when a message is received
  def __on_message(self, client, userdata, message):
    # Extract the payload (a JSON string) from the message
    payload = message.payload.decode()
    # Detecting and handling missing data
    if not payload:
      print(f"[SUBSCRIBER] Missing data")
      self.log = f"[SUBSCRIBER] Missing data"
      return

    # Detecting and handling out of range data
    if self.is_out_of_range(payload):
      return

    # Convert the JSON string to a dictionary
    data = json.loads(payload)
    # Print the dictionary in a human-readable format
    self.__temp_gen.print_data(data)
    self.log = f"[SUBSCRIBER] Subscriber {id(self)} received data {payload}"
  
  # Create a client
  def connect(self):
    self.__client.connect(self.__broker_address, self.__broker_port)
    print(f"[SUBSCRIBER] Subscriber {id(self)} connected to {self.__broker_address}:{self.__broker_port}")
    self.log = f"[SUBSCRIBER] Subscriber {id(self)} connected to {self.__broker_address}:{self.__broker_port}"

  # Subscribe to the specified topic
  def subscribe(self):
    self.__client.subscribe(self.__topic)
    print(f"[SUBSCRIBER] Subscriber {id(self)} subscribed to {self.__topic}")
    self.log = f"[SUBSCRIBER] Subscriber {id(self)} subscribed to {self.__topic}"
  
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
  
  # Handle out of range data
  def is_out_of_range(self, payload):
    try:
      data = json.loads(payload)
      temperature = float(data["temperature"].split()[0])
      if temperature < 18.0 or temperature > 21.0:
        print(f"[SUBSCRIBER] Out of range data: {payload}")
        self.log = f"[SUBSCRIBER] Out of range data: {payload}"
        return True
    except Exception as e:
      print(f"[SUBSCRIBER] Error: {e}")
      self.log = f"[SUBSCRIBER] Error: {e}"
      return True
    
    return False
