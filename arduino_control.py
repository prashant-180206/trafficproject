import serial
import time

arduino = None

def setup_arduino():
    global arduino
    try:
        arduino = serial.Serial('COM5', 9600, timeout=1)  # Add timeout for better handling
        time.sleep(2)  # Wait for Arduino to initialize
        print("Arduino connected.")
    except serial.SerialException as e:
        print(f"Failed to connect to Arduino: {e}")

counter = 1  # Initialize the counter

def activate_traffic_lights(state):
    """Send the state command to Arduino to activate traffic light sequence"""
    if arduino:
        try:
            print(f"Sending command: {state}")  # Debug print
            arduino.write(state.encode())
            time.sleep(0.1)  # Small delay to ensure Arduino processes the command
        except serial.SerialException as e:
            print(f"Error sending data to Arduino: {e}")
    else:
        print("Arduino is not connected.")

def change_counter(N, E, W, S):
    """Change the counter variable based on the current traffic light state"""
    global counter
    if N.state == "GREEN":
        counter = 1
    elif E.state == "GREEN":
        counter = 2
    elif S.state == "GREEN":
        counter = 3
    elif W.state == "GREEN":
        counter = 4
    else :
        counter = 5

def arduino_control(count, FPS, signallist):
    N = signallist[0]
    E = signallist[1]
    W = signallist[2]
    S = signallist[3]
    
    """Control the Arduino traffic lights based on the count variable"""
    if count % (FPS * 1) == 0:  # Every 1 second if running at 40 FPS
        change_counter(N, E, W, S)  # Update the counter based on current traffic light states
        activate_traffic_lights(str(counter))  # Send the updated state to Arduino

def close_arduino():
    global arduino
    if arduino:
        try:
            arduino.close()
            print("Arduino connection closed.")
        except serial.SerialException as e:
            print(f"Error closing Arduino connection: {e}")