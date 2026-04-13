import asyncio
import requests
import datetime
from bs4 import BeautifulSoup

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

# --- ТВОИ ДАННЫЕ (ВСТАВЛЕНЫ) ---
BOT_TOKEN = "8035162332:AAEq2mO_r6l8E_6VsBPkG32XGaD7ObPOYPo"
USER_LOGIN = "vadimkaa33@yandex.ru"
USER_PASSWORD = "Baksikcat2!&21"

bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()
session = requests.Session()

def login_to_synergy():
    """Максимально реалистичный вход"""
    base_url = "https://lms.synergy.ru/login"
    login_handler = "https://lms.synergy.ru/user/login/login"
    switch_role_url = "https://lms.synergy.ru/misc/accset/student/1" 
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    }
    
    try:
        # 1. Получаем начальные куки
        session.get(base_url, headers=headers, timeout=15)
        
        # 2. Логинимся
        payload = {"login": USER_LOGIN, "password": USER_PASSWORD}
        res = session.post(login_handler, data=payload, headers=headers, timeout=15)
        
        # Проверка: ищем признаки того, что мы внутри
        page_content = res.text.lower()
        if res.status_code == 200 and ("logout" in page_content or "userlogged = '1'" in page_content):
            # 3. Переключаемся на нужную подгруппу
            session.get(switch_role_url, timeout=10)
            print("✅ Авторизация и выбор группы ДКИП-202 успешны!")
            return True
        else:
            print("❌ Сайт отклонил вход. Проверь пароль еще раз!")
            return False
    except Exception as e:
        print(f"❌ Ошибка сети: {e}")
        return False

def get_synergy_schedule(target_date_str):
    """Парсит расписание"""
    url = "https://lms.synergy.ru/schedule/academ"
    try:
        response = session.get(url, timeout=15)
        
        if "login" in response.url or "dictionaryTable" not in response.text:
            if not login_to_synergy():
                return "❌ Не удалось войти в аккаунт Синергии."
            response = session.get(url, timeout=15)

        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('tbody', id='dictionaryTable')
        
        if not table:
            return f"❌ Таблица не найдена. На {target_date_str} пар может не быть."

        schedule_message = f"🎓 <b>Расписание на {target_date_str}:</b>\n\n"
        is_target_day = False 
        lessons_found = False
        
        for row in table.find_all('tr'):
            date_header = row.find('th')
            if date_header:
                is_target_day = target_date_str in date_header.text.strip()
                continue 
            
            if is_target_day:
                cols = row.find_all('td')
                if len(cols) >= 5:
                    time = " ".join(cols[0].text.split())
                    subject = " ".join(cols[1].text.split())
                    place = " ".join(cols[2].text.split())
                    lesson_type = " ".join(cols[3].text.split())
                    teacher = " ".join(cols[4].text.split())
                    
                    if not time: continue
                    lessons_found = True
                    schedule_message += (
                        f"⏰ {time} | 📝 <i>{lesson_type}</i>\n"
                        f"📚 <b>{subject}</b>\n"
                        f"🏫 {place} | 👨‍🏫 {teacher}\n"
                        f"➖➖➖➖➖➖➖➖➖➖\n"
                    )
        
        if not lessons_found:
            return f"🎉 На {target_date_str} пар нет!"
        return schedule_message
    except Exception as e:
        return f"❌ Ошибка: {e}"

# --- КОМАНДЫ ---

@dp.message(Command("today"))
async def cmd_today(message: types.Message):
    await message.answer("⏳ Собираю инфу на сегодня...")
    date_str = datetime.datetime.now().strftime("%d.%m.%y")
    await message.answer(get_synergy_schedule(date_str))

@dp.message(Command("tomorrow"))
async def cmd_tomorrow(message: types.Message):
    await message.answer("⏳ Гляну на завтра...")
    date_str = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%d.%m.%y")
    await message.answer(get_synergy_schedule(date_str))

async def main():
    login_to_synergy()
    print("Бот запущен! Жду /today или /tomorrow...")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("Бот выключен.")