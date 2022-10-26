from threading import Lock
from concurrent.futures import ThreadPoolExecutor
num = 10

def add(lock):
    with lock:
        global num
        for _ in range(100000):
            num+=10

def sub(lock):
    with lock:
        global num
        for _ in range(100000):
            num-=10
lock = Lock()
with ThreadPoolExecutor(2) as executor:
    executor.submit(add,lock)
    executor.submit(sub,lock)

print(num)
