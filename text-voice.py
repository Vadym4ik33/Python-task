import pyttsx3
eng = pyttsx3.init()

while True:
    text = input('fraza: ')
    pyttsx3.speak(text)
    eng.runAndWait()