# import gtts
# import playsound

# text = input("Enter your speech : ")
# sound = gtts.gTTS(text, lang="hi")
# sound.save("welcome.mp3")
# playsound.playsound("welcome.mp3")

import gtts
import playsound
import os

def text_to_speech(text, filename):
    sound = gtts.gTTS(text, lang="hi")
    sound.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

text = input("Enter your speech : ")
filename = "welcome.mp3"
text_to_speech(text, filename)