import requests
from bs4 import BeautifulSoup

# response = requests.get('https://www.google.com')
# soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.title.text)

# print(response.status_code)
# print(response.text[:200])

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
}
#делаем вид что я человек

response = requests.get('https://yummyanime.tv/index-2', headers=headers)


soup = BeautifulSoup(response.text, 'html.parser') 
titles = soup.find_all('div', class_='movie-item__title')# сначала идет класс, всегда спереди, а потом класс = ***


# for title in titles:
#     print(title.text.strip())#title, text - убирает всякие теги и другой калл, strip()- убирает пробелы невидимые переносы и тд

# Вместо одного поиска по названию, попробуй найти весь "каркас" карточки
items = soup.find_all('div', class_='movie-item__inner')

for item in items:
    # Ищем название ВНУТРИ карточки
    title = item.find('div', class_='movie-item__title').text.strip()
    
    # Ищем ссылку ВНУТРИ карточки и достаем атрибут 'href'
    link = item.find('a', class_='movie-item__link')['href']
    
    print(f"Название: {title}")
    print(f"Ссылка: https://yummyanime.tv{link}")
    print("-" * 20)

    
