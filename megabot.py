import wikipedia
import pyttsx3

wikipedia.set_lang('ru')
eng = pyttsx3.init()

while True:
    Theme = input('что найти?: ')
    wiki = wikipedia.summary(Theme, sentences = 3)
    print(wiki)
    eng.say(wiki)
    eng.runAndWait()
