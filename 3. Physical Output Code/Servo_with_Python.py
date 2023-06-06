import tweepy
import config
from pyfirmata import Arduino, SERVO, util
#import pwmio

from time import sleep
port = 'COM11'
pin = 10
pin2 = 11
pin3 = 9 
pin4 = 12
board= Arduino(port) #bind arduino to port

board.digital[pin].mode = SERVO
board.digital[pin2].mode = SERVO
board.digital[pin3].mode = SERVO
board.digital[pin4].mode = SERVO

initialServoState = board.digital[pin].write(90) #initial state for the continuos servo
initialServoState = board.digital[pin2].write(90) #initial state for the continuos servo
initialServoState = board.digital[pin3].write(90) #initial state for the continuos servo
initialServoState = board.digital[pin4].write(90) #initial state for the continuos servo

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
         userInputFeeling = input("How do you feel about the future of AI in the workplace")
         finalTweet = ("~ Positive, Joy ~ {}".format(userInputFeeling))
         rotateContinuoServo(pin)
         response = client.create_tweet(text= finalTweet)
         print(response)   
    elif x == "2":
        userInputFeeling = input("How do you feel about the future of AI in the workplace?")
        finalTweet = ("~ Anticipation, Trust ~ {}".format(userInputFeeling))
        rotateContinuoServo(pin2)
        response = client.create_tweet(text= finalTweet)  
    elif x == "3":
        userInputFeeling = input("How do you feel about the future of AI in the workplace?")
        finalTweet = ("~ Negative, Fear ~ {}".format(userInputFeeling))
        rotateContinuoServo(pin3)
        response = client.create_tweet(text= finalTweet) 
        # for i in range(0,360):
        #     rotateservo(pin2, i)                   
    elif x == "4":
        userInputFeeling = input("How do you feel about the future of AI in the workplace?")
        finalTweet = ("~ Anger, Sadness ~ {}".format(userInputFeeling))
        rotateContinuoServo(pin4)
        response = client.create_tweet(text= finalTweet)     