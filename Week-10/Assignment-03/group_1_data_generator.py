# Assignment #3 – Data Generator
# Date: March 22, 2024
# Group 3:
#  - Cong Lanh Hoang
#  - Einer Cupino
#  - Jasper Jan Tan
#  - Kwok Yuk Chui
#  - Wing Chi Lam

import random
import matplotlib.pyplot as plt

class TemperatureGenerator:
  def __init__(self, max_data_points = 500, low_temp=18.0, high_temp=21.0, seed=None):
    self.__max_data_points = max_data_points
    self.__low_temp = low_temp
    self.__high_temp = high_temp
    random.seed(seed)
  
  def __generate_normalized_values(self):
    return random.random()

  @property
  def temperature(self):
    return self.__low_temp + (self.__high_temp - self.__low_temp) * self.__generate_normalized_values()
  
  def generate_temperature(self):
    return [self.temperature for _ in range(self.__max_data_points)]

  def plot_temperature(self):
    plt.plot(self.generate_temperature())
    plt.xlabel("Time")
    plt.ylabel("Temperature")
    plt.title("Temperature Data")
    plt.show()


if __name__ == "__main__":
  temperature_generator = TemperatureGenerator()
  temperature_generator.plot_temperature()