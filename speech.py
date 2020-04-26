import pyttsx3 as tts
from settings import Settings

sett = Settings()


def speak(text):
    engine = tts.init()
    vol = sett.getVolume()
    rate = sett.getRate()
    engine.setProperty('rate', rate)
    engine.setProperty('volume', vol)
    engine.say(text)
    engine.runAndWait()


def greet():
    speak("Hello!i'm Jarvis.")


def ch_rate(val):
    # get initial rate and increase as said
    if val:
        print("increase")
    else:
        print("dec")


def ch_vol(val):
    # get initial vol and increase as said
    if val:
        print("increase")
    else:
        print("dec")
