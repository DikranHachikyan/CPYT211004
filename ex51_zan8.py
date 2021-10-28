
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

    print(concat(*users))
    print(concat(*users, sep=' | '))


    print(concat.__original(*users, sep=' | '))
    print(concat(*values, sep=','))

    concat = concat.__original
    print(concat(*users))
    

    print('---')