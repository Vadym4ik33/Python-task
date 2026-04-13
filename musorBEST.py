import os
import shutil

print('вставь путь уборки')
target_path = input().strip('"')

try:
    os.chdir(target_path)
except:
    print('путь не найден.')
    exit()

for f in os.listdir():
    if f == os.path.basename(__file__):
        continue
        
    if os.path.isdir(f):
        continue
    # ... дальше твой код

# Словарь: "Расширение": "Папка"
extensions = {
    '.png': 'Images',
    '.jpg': 'Images',
    '.jpeg': 'Images',
    '.txt': 'Text',
    '.docx': 'Text',
    '.pdf': 'Text',
    '.exe': 'Installers',
    '.mp4': 'Video'
}

# ... создание папок ...

for f in os.listdir():
    if os.path.isdir(f) or f == os.path.basename(__file__):
        continue

    # Получаем расширение файла (в нижний регистр, чтобы .PNG и .png было одно и то же)
    ext = os.path.splitext(f)[1].lower()

    # Проверяем, есть ли такое расширение в нашем словаре
    if ext in extensions:
        folder_name = extensions[ext]
        shutil.move(f, folder_name)
        print(f'✅ {f} улетел в {folder_name}')
    else:
        # Если расширения нет в списке — в мусорку (или папку Other)
        shutil.move(f, 'Trash')
        print(f'🗑 {f} улетел в помойку')