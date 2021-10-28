

if __name__ == '__main__':
    with_exception = True

    actions = {
        '+': lambda a, b: a + b
    }

    try:
        value1 = float(input('first number:'))
        op = input('action: +:')
        value2 = float(input('second number:'))
        result = actions[op](value1, value2)

    except KeyError as e:
        print(f'invalid operation:{e}')
    except ValueError as e:
        print(f'invalid number:{e}')
    except Exception as e:
        print(f'unknown error: {e}')
    else:
        with_exception = False
        print(f'{value1} {op} {value2} = {result}')
        print('--- else ---')

    print('---')