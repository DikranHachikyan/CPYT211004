def print_key(key, **kwargs):
    try:
        print(f'{key} => {kwargs[key]}')
    except KeyError as e:
        # 3. opt
        raise
        # 2. може да има:
        # pass
        
        # 1. не е добра идея
        # print(f'invalid key:{key}')


if __name__ == '__main__':

    conn = {
        'host':'localhost',
        'port':1521,
        'service':'oracle'
    }

    try:
        print_key('host', **conn)
        print_key('ip', **conn)
        print_key('service', **conn)
    except KeyError as e:
        # pass
        print('invalid key')

    print('---')