# Python Code for Monitoring a Room (Digital Twin Example)
import random
import time
import json


# Room class to simulate sensors and digital twin
class Room:
    def __init__(self, room_name):
        self.room_name = room_name
        self.temperature = random.uniform(20, 25)  # Celsius (comfortable room temperature)
        self.humidity = random.uniform(30, 60)  # Percentage
        self.co2_level = random.uniform(350, 800)  # CO2 level in ppm (parts per million)
        self.light_intensity = random.uniform(100, 1000)  # Lux (light level)

    def update_sensors(self):
        """Simulate updates to room sensors."""
        self.temperature = random.uniform(20, 25)  # Temperature between 20-25°C
        self.humidity = random.uniform(30, 60)  # Humidity between 30-60%
        self.co2_level = random.uniform(350, 800)  # CO2 level between 350-800 ppm
        self.light_intensity = random.uniform(100, 1000)  # Light intensity between 100-1000 lux

    def get_digital_twin(self):
        """Returns a dictionary representing the room's digital twin."""
        status = "Normal"

        # Defining thresholds for room conditions
        if self.temperature < 18 or self.temperature > 27:
            status = "Temperature out of range"
        elif self.co2_level > 1000:
            status = "High CO2 levels detected"
        elif self.humidity < 30 or self.humidity > 70:
            status = "Humidity out of range"

        return {
            "room_name": self.room_name,
            "temperature": self.temperature,
            "humidity": self.humidity,
            "co2_level": self.co2_level,
            "light_intensity": self.light_intensity,
            "status": status
        }


# Main program to simulate monitoring the room
def monitor_room():
    room = Room("University Classroom 101")

    while True:
        room.update_sensors()  # Simulate sensor updates every cycle
        digital_twin = room.get_digital_twin()  # Get the current state of the room

        # Print the digital twin data (in JSON format)
        print(json.dumps(digital_twin, indent=4))

        # Wait for 5 seconds before the next update
        time.sleep(5)


if __name__ == "__main__":
    monitor_room()
