import customtkinter
import pyttsx3

customtkinter.set_appearance_mode("dark")
app = customtkinter.CTk()
app.geometry("400x240")
app.title("Моя Говорилка")

def click_button():
    text = entry.get()
    eng = pyttsx3.init()
    eng.say(text)
    eng.runAndWait()

entry = customtkinter.CTkEntry(app, placeholder_text="Введи текст...")
entry.pack(pady=20)
btn = customtkinter.CTkButton(app, text="Озвучить", command=click_button)
btn.pack(pady=20)

app.mainloop()