# importing libraries
import os
import pyttsx3

print("Welcome to Text To Speech Converter")

#  initializes the pyttsx3 engine
reply = pyttsx3.init()
while True:
    user_input = input("Hey, type the sentence/sentences you want to pronounce: ")
    if user_input == 'q':
        break
    # If you want to change the voice from male to female
    #voice = reply.getProperty('voices')
    #reply.setProperty('voice', voice[1].id)

    reply.say(user_input)
    reply.runAndWait()

