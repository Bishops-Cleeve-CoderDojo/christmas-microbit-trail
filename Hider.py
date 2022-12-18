from microbit import *
import radio

CHANNEL_ICONS = {
    1: Image.STICKFIGURE,
    2: Image.HEART,
    3: Image.GIRAFFE,
    4: Image.HAPPY,
}

SEND_INTERVAL = 300

choosing_channel = True
channel = 1
display.show(CHANNEL_ICONS[channel])

while choosing_channel:
    if button_a.was_pressed():
        channel += 1
        if channel == 5: channel = 1
        display.show(CHANNEL_ICONS[channel])
    if button_b.was_pressed():
        choosing_channel = False

display.show(CHANNEL_ICONS[channel])

radio.config(group=channel, power = 6)
radio.on()

while True:
    radio.send('hello')
 
    received = None
    while True:
        received = radio.receive()
        if not received:
            break
        if channel == 1 and received.lower() == 'santa':
            display.scroll('Rudolph')
        if channel == 2 and received.lower() == 'rudolph':
            display.scroll('Snowman')
        if channel == 3 and received.lower() == 'snowman':
            display.scroll('Turkey')
        if channel == 4 and received.lower() == 'turkey':
            display.scroll('What falls in winter but never gets hurt?')
        display.show(CHANNEL_ICONS[channel])
    
    sleep(SEND_INTERVAL)
