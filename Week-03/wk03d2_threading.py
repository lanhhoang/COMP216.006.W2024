#author: Narendra
#filename: wk03d2_threading.py

#calling a method asynchronously

from time import perf_counter, sleep
from random import randint
from threading import Thread

def sleeper(n: int, name: str) -> None:
    print(f'{name} is going to sleep for {n} seconds')
    sleep(n)
    print(f'{name} is done sleeping')

def do_five() -> None:
    start = perf_counter()
    threads = []
    for x in 'Angello Amir Ashley Palk Sidney Sahansan Shemar Sumi Tale'.split():
        t1 = Thread(
            target=sleeper,             #name of he method to run as a thread
            name=x,                     #optional name of the thread
            args=(randint(4, 8), x)     #arguments as a tuple
        )
        
        t1.start()                      #starts the thread
        threads.append(t1)              #adds it to the list
    
    for t in threads:
            t.join()                    #prevent the further execution until all the thread complete

    end = perf_counter()
    print(f'Finished in {round(end-start, 2)} seconds')

do_five()