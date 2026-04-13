import os
import shutil

print('вставь путь уборки')
target_path = input().strip('"')

try:
    os.chdir(target_path)
except:
    print('путь не найден.')
    exit()

os.makedirs('Images', exist_ok=True)
os.makedirs('Text', exist_ok=True)
os.makedirs('Trash', exist_ok=True)
os.listdir()

for f in os.listdir():

    if os.path.isdir(f):
        continue

    if f.endswith('.png'):
        shutil.move(f, 'Images')
        print(f'картинка {f} съебалась в Images')

    elif f.endswith('.txt'):
        shutil.move(f, 'Text')
        print(f'текстовик {f} съебался в Text')
    
    else:
        shutil.move(f, 'Trash')
        print(f'хуйня какая то: {f} перемещена в Trash')
