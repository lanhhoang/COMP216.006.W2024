#author: Narendra
#filename: wk03d1_threading.py

#calling a method synchronously

#import time
from time import perf_counter, sleep
from random import randint

def sleeper(n: int, name: str) -> None:
    print(f'{name} is going to sleep for {n} seconds')
    sleep(n)
    print(f'{name} is done sleeping')


def do_five() -> None:
    start = perf_counter()
    for x in 'Amir Ashley Palk Sumi Tale'.split():
        sleeper(randint(4, 8), x) #runs the method synchronously
    end = perf_counter()
    print(f'Finished in {round(end-start, 2)} seconds')

do_five()

