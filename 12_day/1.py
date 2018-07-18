from threading import Thread
import time
from threading import Thread

def multy(a, *args):
    print(*(a * i for i in args))

time1 = time.time()
print(time1)
p = Thread(target=multy, args=(2, 10, 20, 30, 40, 50))
p.start()
p.join()
print(time.time() - time1)

def diva(a, *args):
    print(*(i // a for i in args))
print("---------------- ------- - - - - - -")
time2 = time.time()
print(time2)
p2 = Thread(target=diva, args=(2, 10, 20, 30, 40, 50))
p2.start()
p2.join()
print(time.time() - time2)
