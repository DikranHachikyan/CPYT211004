
service = 'ssh' # глобална променлива

# 1. дефиниция на функция

def sum_numbers(a, b):
    # c - локална променлива
    c = a + b
    return c

if __name__ == '__main__':
    # 2. извикване на функцията
    s1 = sum_numbers(5,6)

    print(f's1 = {s1}')

    x, y = 12,15

    s1 = sum_numbers(x, y)
    print(f'{x} + {y} = {s1}')
    
    print('---')