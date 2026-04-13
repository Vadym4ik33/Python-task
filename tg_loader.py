import telebot
import yt_dlp as yt
import os

bot = telebot.TeleBot('8035162332:AAEq2mO_r6l8E_6VsBPkG32XGaD7ObPOYPo')

@bot.message_handler(content_types=['text'])

def get_video(message):
    try:

        vvod = message.text

        bot.send_message(message.chat.id, "Начинаю загрузку")

        options = {'outtmpl': 'video.mp4'}
       
        with yt.YoutubeDL(options) as ydl:
            ydl.download([vvod])

        file_info = os.stat('video.mp4')
        
        if file_info.st_size > 50 * 1024 * 1024:
            bot.send_message(message.chat.id, "😔 Видео слишком большое (>50 МБ). Телеграм не разрешает ботам кидать такие файлы.")
        else:
            with open('video.mp4', 'rb') as video:
                bot.send_video(message.chat.id, video, timeout=180)

        os.remove('video.mp4')

    except Exception as e:
        bot.send_message(message.chat.id, f'Анлак: {e}')

bot.polling(non_stop=True)
