import speech_recognition
import pyttsx3
import serial
import time

recognizer= speech_recognition.Recognizer()

while True:
    try:
        with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio =recognizer.listen(mic)

            text=recognizer.recognize_google(audio)
            text=text.lower()
            print(f"Recognized {text}")
            arduino_port = 'COM3'  

            # Open a serial connection to the Arduino
            ser = serial.Serial(arduino_port, 9600, timeout=2)

            try:
                while True:
                    ser.write(text.encode('utf-8') + b'\n')  # Send the command to Arduino with a newline
                    time.sleep(0.1)
            except KeyboardInterrupt:
                print("Exiting...")
                ser.close()
            
    
    except speech_recognition.UnknownValueError():
        recognizer=speech_recognition.Recognizer()
        continue
