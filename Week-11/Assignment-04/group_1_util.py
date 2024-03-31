# Assignment #4 – Send and receive messages via MQTT
# Date: April 01, 2024
# Group 3:
#  - Cong Lanh Hoang
#  - Einer Cupino
#  - Jasper Jan Tan
#  - Kwok Yuk Chui
#  - Wing Chi Lam

import random
import time

class TemperatureGenerator:
  def __init__(self, max_data_points = 500, low_temp=18.0, high_temp=21.0, seed=None):
    self.__max_data_points = max_data_points
    self.__low_temp = low_temp
    self.__high_temp = high_temp
    self.start_id = 111 # Start ID initially set to 111
    random.seed(seed)
  
  def __generate_normalized_values(self):
    return random.random()

  @property
  def temperature(self):
    return self.__low_temp + (self.__high_temp - self.__low_temp) * self.__generate_normalized_values()
  
  def generate_temperature(self):
    return [self.temperature for _ in range(self.__max_data_points)]
  
  def create_data(self):
    self.start_id += 1
    data = {
      "packet_id": self.start_id,
      "temperature": f"{round(self.temperature, 1)} °C",
      "created_at": time.asctime(),
    }

    return data

  def print_data(self, data):
    print(f"ID: {data['packet_id']}\nTemperature: {data['temperature']}\nCreated At: {data['created_at']}\n")