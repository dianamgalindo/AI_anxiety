import tweepy
import config
from pyfirmata import Arduino, SERVO, util
#import pwmio

from time import sleep
port = 'COM9'
pin = 9
pin2 = 10
board= Arduino(port) #bind arduino to port

board.digital[pin].mode = SERVO
board.digital[pin2].mode = SERVO
initialServoState = board.digital[pin2].write(90) #initial state for the continuos servo

client = tweepy.Client(consumer_key=config.api_key,
                       consumer_secret=config.api_key_secret,
                       access_token=config.access_token,
                       access_token_secret=config.access_token_secret)

def rotateservo(pin, angle):
    board.digital[pin].write(angle)
    sleep(0.015)

def rotateContinuoServo(pin):
    # start_pos = 0
    # end_pos = 360
    # mapped_start = map(start_pos, 0, 360, 0, 180)
    # print(mapped_start)
    # mapped_end = map(end_pos, 0, 360, 0, 180)
    
    # board.digital[pin].write(mapped_start)
    # sleep(0.5)
    # board.digital[pin].write(mapped_end)
    # sleep(0.5)
    # board.digital[pin].write(mapped_start)

    #0 indicates rotation clockwise to a 360 rotation
    #180 indicates rotation anti-clockwise to a 360 rotation
    board.digital[pin].write(0) 
    sleep(0.5)
    board.digital[pin].write(90) #90 indicates stop

while True:
    x = input("input:")
    if x == "1":
        # response = client.create_tweet(text='i love me')
        # print(response)
        for i in range(0,180):
            rotateservo(pin, i)
           
        for i in range(180,1,-1):
            rotateservo(pin,i)
               
              
    elif x == "2":
        rotateContinuoServo(pin2)      
    elif x == "3":
        for i in range(0,360):
            rotateservo(pin2, i)                   