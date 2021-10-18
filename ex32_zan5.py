
service = 'ssh' # глобална променлива

# 1. дефиниция на функция

def sum_numbers(a, b, d=None):
    # c - локална променлива
    c = a + b + d if d  else a + b 
    return c

if __name__ == '__main__':
    # 2. извикване на функцията
    s1 = sum_numbers(5,6)

    print(f's1 = {s1}')

    x, y, z = 12,15, 4

    s1 = sum_numbers(x, y, z)
    print(f'{x} + {y} + {z} = {s1}')
    
    print('---')