# Microbit_PN532
Simple PN532 NFC reader library for Micro:bit. 
Based on https://github.com/otlich/pn532

# Installation
Copy pn532.py to your Micro:bit filesystem. Use `import pn532` in your main module to access functions

# Wiring and other notes
Connect your PN532 module to Micro:bit

PN532 pin | Micro:bit pin
----------|--------------
SDA|SDA (20)
SCL|SCL (19)
VCC|3.3V
GND|GND

Please note that PN532 will most likely not work when Micro:bit is powered by two AAA batteries. PN532 requires at least 3.3 volts so two batteries is not enough. Use micro USB to power your project.
