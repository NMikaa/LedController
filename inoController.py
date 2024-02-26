import serial
import time

ser = serial.Serial('COM7', 9600)  # Update to your Arduino's COM port
time.sleep(2)  # Wait for connection to establish

def led(total):
    # Send the total number of fingers as a byte
    ser.write(str(total).encode())
