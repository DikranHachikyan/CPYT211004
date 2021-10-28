
from time import time, sleep
from functools import wraps

def to_uppercase(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.__original = func
        args = [ f'{v}'.upper()  for v in args]
        return func(*args, **kwargs)
    return wrapper


@to_uppercase
def concat(*args, **kwargs):
    '''concatenate list elements with sep'''
    sep = kwargs.get('sep', ';')
    return sep.join(args)


if __name__ == '__main__':
    users = ['anna', 'maria', 'markus', 'jane']
    values = [11, 12, 34, 6]

    print = to_uppercase(print)
    
    print('hello python', 'lorem ipsum')
    print(11,23, 'a', 40)

    print = print.__original
    print('hello python', 'lorem ipsum')

    
    print('---')