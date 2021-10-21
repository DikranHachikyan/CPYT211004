# 1 + 2 + .... + 99 + 100 = 5050


def sum_numbers(n):
    print(f'n={n}')
    if n > 0:
        return n + sum_numbers(n - 1)
    return 0


if __name__ == '__main__':
    
    # res = sum_numbers(100)
    res = sum_numbers(5)
    print(f'res = {res}')
    print('---')