import gtts
import playsound

text = input("Enter your speech : ")
sound = gtts.gTTS(text, lang="en")
sound.save("welcome.mp3")
playsound.playsound("welcome.mp3")