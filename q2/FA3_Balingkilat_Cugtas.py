'''
Cugtas, Jairo Vincent M.
9 - Balingkilat
12/11/26
FA3 CS3 Q2
'''

from abc import ABC, abstractmethod #importing ABC and abstract method

class Sensor(ABC):
    @abstractmethod #defines the method as an abstract method
    def get_reading(self): #abstract method that will be used by the other 2 classes
        pass

class TempSensor(Sensor):
    def get_reading(self):
        return "24.5°C"

class PHSensor(Sensor):
    def get_reading(self):
        return "7.2 pH"

#Tasks 1-4 (The Success Run):
my_phsensor = PHSensor()
my_tempsensor = TempSensor()

print("--- Lab Inventory System ---")
print(f"[pH Sensor] Reading: {my_phsensor.get_reading()} (Neutral)")
print(f"[Temperature Sensor] Reading: {my_tempsensor.get_reading()}")
print("\n----------------------------")

#Task 5 (The "Break it" Test):
#my_sensor = Sensor() 
