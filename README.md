# Speech Light Controller

This Python project enables voice-controlled light management using speech recognition and Arduino. The system utilizes the `speech_recognition`, `pyttsx3`, and `serial` libraries in Python to capture spoken commands, convert them to text, and send them to an Arduino board through a serial connection.

## Setup and Dependencies
1. Install the required Python libraries using the following:
   ```bash
   pip install speech_recognition pyttsx3
   ```

2. Connect your Arduino board to your computer and adjust the `arduino_port` variable in the Python script (`speech_light_controller.py`) to match the port your Arduino is connected to (`COM3` is used as an example).

3. Upload the provided Arduino code (`arduino_light_control.ino`) to your Arduino board.

## Usage
1. Run the Python script (`speech_light_controller.py`).
   ```bash
   python speech_light_controller.py
   ```

2. Once the script is running, speak commands into the microphone. The recognized text will be printed, and the corresponding command will be sent to the Arduino.

3. The Arduino code reads incoming serial data and controls the LED connected to pin 12 based on the received command. In the provided example, saying "lights on" will turn the LED on for 0.5 seconds and then off for 0.5 seconds.

## Notes
- Adjust the Arduino code or Python script as needed for your specific hardware setup.
- Make sure to handle the microphone and Arduino port configurations according to your system.

Feel free to explore and customize this project to suit your requirements!
