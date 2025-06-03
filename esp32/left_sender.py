import network
import espnow
import time
from machine import Pin

# 🔹 Step 1: Set up the button with an internal pull-up resistor
button = Pin(4, Pin.IN)  # D5 (Active LOW)
last_button_state = 1  # Assume button starts released (HIGH)
debounce_delay = 20  # Debounce time in ms
last_time = time.ticks_ms()  # Timestamp for debounce

# 🔹 Step 2: Initialize WLAN (required for ESP-NOW)
sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.disconnect()

# 🔹 Step 3: Initialize ESP-NOW
e = espnow.ESPNow()
e.active(True)

# 🔹 Step 4: Add a peer (Receiver's MAC Address)
peer = b'\x40\x22\xD8\xE8\xAD\x64'  # Replace with actual MAC address
e.add_peer(peer)  # No need for a check, just add it

print("Press the left button to send a signal")

# 🔹 Step 5: Main loop
while True:
    current_button_state = button.value()  # Read the button state
    current_time = time.ticks_ms()  # Get current time for debounce

    # Button Pressed (Active LOW)
    if current_button_state == 1 and last_button_state == 0:
        if time.ticks_diff(current_time, last_time) > debounce_delay:
            print("Button Pressed! Sending signal...")
            try:
                e.send(peer, 'LeftButtonPressed')  # Send message
            except OSError:
                print("Error: Failed to send ESP-NOW message.")
            last_time = current_time  # Update debounce timer

    # Button Released (Goes HIGH)
    elif current_button_state == 0 and last_button_state == 1:
        if time.ticks_diff(current_time, last_time) > debounce_delay:
            print("Button Released! Sending signal...")
            try:
                e.send(peer, 'LeftButtonReleased')
            except OSError:
                print("Error: Failed to send ESP-NOW message.")
            last_time = current_time  # Update debounce timer

    last_button_state = current_button_state  # Update button state
    time.sleep(0.01)  # Reduce CPU usage

