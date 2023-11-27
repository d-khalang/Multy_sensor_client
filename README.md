# Multy_sensor_client

This project facilitates communication between IoT devices using the MQTT protocol. It simulates a building named "IoT project" with five floors, each containing three rooms, each equipped with a sensor.

## Files

- **sensor.py:** Contains the "Sensor" class, where each object simulates a temperature and humidity sensor.

- **sensorClient:** Allows users to receive sensor data based on the specified topic, whether it's the entire building, a specific floor, or a room. Users can dynamically change the topic during runtime.

- **MyMQTT:** Provides handy methods for Paho-Mqtt.

- **simplePublisher:** A typical publisher for the project.

- **simpleSubscriber:** A typical subscriber for the project.

- **settings.json:** Contains essential information about the broker and the main topic.

## Usage

To get started, run **sensor.py** and **sensorClient**
    and ensure to input the same name for both programs.



Feel free to adjust the structure and content according to your preferences and the specific details of your project.

