import psutil
import time

# [|||||.....]

while True:
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory()

    time.sleep(5)

    count = int(ram.percent / 10) 

    # Рисуем: (палочка * кол-во) + (точка * (10 - кол-во))
    bar = f"[{'|' * count}{'.' * (10 - count)}]"

    print(f"{ram.percent}% {bar}")

    print(cpu)
#я лох 1234, коммит
#еще коммит, проверка
