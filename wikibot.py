import wikipedia
wikipedia.set_lang('ru')

while True:
    x = input('что ищем?: ')
    wiki = wikipedia.summary(x, sentences = 5)
    print(wiki)
