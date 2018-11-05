# Microbit_PN532
Simple PN532 NFC reader library for Micro:bit MicroPython. 
Based on https://github.com/otlich/pn532

# Installation and function reference
Copy pn532.py to your Micro:bit filesystem. Use `import pn532` in your main module to access functions:

    pn532.connect()
    
Initialize i2c interface

    pn532.scan_i2c()
    
Scan for devices on i2c bus. Returns an array of bytes, each byte is an address of i2c device. Please note that built-in magnetometer and accelerometer share the same bus (their addresses are 0x0E and 0x1D). Most likely your PN532 will have address 0x24 (decimal 36).

    pn532.get_version(addr)
    
Returns an array of bytes which contains module version informations

    pn532.wait_card(addr)
    
Waits for a NFC card to be read. Returns an identificator of the card in hex string

# Wiring and other notes
Connect your PN532 module to Micro:bit

PN532 pin | Micro:bit pin
----------|--------------
SDA|SDA (20)
SCL|SCL (19)
VCC|3.3V
GND|GND

Please note that PN532 will most likely not work when Micro:bit is powered by two AAA batteries. PN532 requires at least 3.3 volts so two batteries are not enough. Use Micro-USB or other external source to power your project.
