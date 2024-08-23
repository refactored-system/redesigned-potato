import numpy as np
import matplotlib.pyplot as plt


class DataGenerator:
    # Initialize the class with the number of values to generate
    def __init__(self, num_value):
        self.num_value = num_value
        self.value = {
            "base": 10,
            "delta": 0.15,
        }

    # Private method to generate random data points
    def __generateDataPoints(self):
        return np.random.random(self.num_value)

    # Public method to get a temperature sensor dataset
    def getTemperatureSensorDataset(self, min, max):

        # Generate the random data points
        x = self.__generateDataPoints()

        # Calculate the range of the temperature values
        m = max - min

        # Minimum temperature value
        c = min

        # Scale and shift the random values to fit within the min and max range
        y = m * x + c

        # Return the value
        return y
