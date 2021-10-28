

if __name__ == '__main__':
    
    actions = {
        '+': lambda a, b: a + b
    }

    try:
        value1 = float(input('first number:'))
        op = input('action: +:')
        value2 = float(input('second number:'))

        print(f'{value1} {op} {value2} = {actions[op](value1, value2)}')
    except KeyError as e:
        print(f'invalid operation:{e}')
    except ValueError as e:
        print(f'invalid number:{e}')
    except Exception as e:
        print(f'unknown error: {e}')


    print('---')