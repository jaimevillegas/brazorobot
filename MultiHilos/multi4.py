import threading
import time

numero = 0


def incrementar():
    global numero
    numero += 1
    print(' ', numero)
    time.sleep(.5)


def restar():
    global numero
    if numero > 10:
        numero -= 5
        time.sleep(1)

threads = list()

while True:
    t = threading.Thread(target=incrementar())
    threads.append(t)
    t.start()

    a = threading.Thread(target=restar())
    threads.append(a)
    a.start()
