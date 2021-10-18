
service = 'ssh' # глобална променлива

# 1. дефиниция на функция

def sum_numbers(a, b, *args):
    # c - локална променлива
    c = a + b
    print(f'args:{args}')
    for v in args:
        c += v
    return c

if __name__ == '__main__':
    # 2. извикване на функцията
    s1 = sum_numbers(5,6)

    print(f's1 = {s1}')

    x, y, z, m, n, t = 12, 15, 4, 11, 34, 56

    s1 = sum_numbers(x, y, z, m, n, t)
    print(f'{x} + {y} + {z} + {m} + {n} + {t} = {s1}')
    
    values = [ i for i in range(4,13)]
    s1 = sum_numbers(x, y, *values)
    print(f'{x} + {y} + ' + ' + '.join(map(str, values)) + f' = {s1}')
    print('---')