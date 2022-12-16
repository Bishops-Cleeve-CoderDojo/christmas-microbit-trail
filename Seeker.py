from microbit import *
import radio

# Start the radio on channel 1
channel = 1
radio.config(group=channel)
radio.on()
display.show(channel)
sleep(600)

while True:

    #################################################################
    # Add code below to send a message using the radio, when 
    # button B is pressed. 
    # 
    # Start by sending "Santa" to the micro:bit on channel 1 (stick person)
    # then, send the response to the micro:bit using channel 2.
    # Do the same for the micro:bits on channels 3 and 4, then come 
    # and tell me the answer to the final riddle!
    #
    #################################################################



    
      
    ####### Don't change the code below this line #######

    # Change the channel when button A is pressed
    if button_a.was_pressed():
        channel += 1
        if channel == 5: channel = 1

        radio.config(group=channel)
        display.show(channel)
        sleep(600) 

    # Check the strength of any received messages
    received_messages = []
    received = None
    while True:
        received = radio.receive_full()
        if not received:
            break
        received_messages.append(received)

    # Check if we recieved any messages
    if len(received_messages) == 0:
            display.show(Image('00000:'
                               '00000:'
                               '00000:'
                               '00000:'
                               '99999'))
    else:
        # Find the average signal strength of all the messages
        average_rssi = sum([m[1] for m in received_messages]) / len(received_messages)
        
        if average_rssi > -55:
            display.show(Image('99999:'
                               '99999:'
                               '99999:'
                               '99999:'
                               '99999'))
        elif average_rssi > -65:
            display.show(Image('00000:'
                               '99999:'
                               '99999:'
                               '99999:'
                               '99999'))
        elif average_rssi > -80:
            display.show(Image('00000:'
                               '00000:'
                               '99999:'
                               '99999:'
                               '99999'))
        else:
            display.show(Image('00000:'
                               '00000:'
                               '00000:'
                               '99999:'
                               '99999'))

    sleep(700)
    display.clear()
    sleep(300)
