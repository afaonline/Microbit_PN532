from microbit import *
import music
import pn532

pn532.connect()
address = 36

display.show(Image.HOUSE)

while True:
    display.show(Image.HOUSE)
    card_id = pn532.wait_card(address)
    if card_id == '34dfab091b0276':
        display.show(Image.HAPPY)
        music.play(music.POWER_UP)        
    else:
        display.show(Image.SAD)
        music.play(music.JUMP_DOWN)
    sleep(400)
