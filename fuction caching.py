import time
from functools import lru_cache


@lru_cache()
def some_work(n):
    time.sleep(n)
    return n

if __name__ == '__main__':
    take_time = eval(input('Input time you want to delay for:'))
    lru_input = eval(input('Enter the value for LRU cach:'))
    lru_cache(lru_input)
    print('Running function.. ')
    some_work(take_time)
    print('Done. Running again..')
    some_work(2)
    print('Done. Running again..(2)')
    some_work(take_time)
    print('Done. Running again..(3)')
    some_work(2)
    print('Done. Running again..(4)')
    some_work(4)
    print('Done. Running again..(5)')
    some_work(2)
    print('Done. Running again..(6)')
    some_work(9)
    print('Stop.')