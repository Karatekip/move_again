import network
import espnow
import time
import machine  # Import machine module for controlling GPIO
 
# Step 1: Initialize WLAN
sta = network.WLAN(network.STA_IF)
sta.active(True)
 
# Step 2: Initialize ESP-NOW
e = espnow.ESPNow()
e.active(True)
 
# Step 3: Initialize LED on GPIO 12
led1 = machine.Pin(12, machine.Pin.OUT)  # Set GPIO 12 as an output
 
print("listening")
 
n = 1
# Step 4: Main loop to receive ESP-NOW messages
while True:
    host, msg = e.recv()
    if msg:
        msg = msg.decode('utf-8')  # Decode bytes to string
        # Blink LED when a message is received


        if msg == "LeftButtonPressed":
            print("left_button_pressed")
            led1.value(1)  # Turn LED ON
        elif msg == "RightButtonPressed":
            print("right_button_pressed")
            led2.value(1)
        elif msg == "LeftButtonReleased":
            print("left_button_released")
            led1.value(0)  # Turn LED OFF
        elif msg == "RightButtonReleased":
            print("right_button_released")
            led2.value(0)
    n += 1
 
