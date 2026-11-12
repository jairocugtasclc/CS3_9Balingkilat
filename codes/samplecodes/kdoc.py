from abc import ABC, abstractmethod

class Sensor(ABC):
    @abstractmethod
    def get_data(self):
        pass

class TempSensor(Sensor):
    def get_data(self):
        return "22 K"
    def __str__(self):
        return "24 K"

sensor = TempSensor()
print(sensor.get_data())
print(sensor)
