

if __name__ == '__main__':
    pow2 = lambda x,y: x ** y

    print(f'2 ** 3 = {pow2(2,3)}')

    items = [('A', 5, 7), ('D', 2,  6), ('B', 4, 8), ('D', 2, 5)]

    # 1.
    # items.sort()

    # 2.
    # items.sort(key=lambda el: el[1])
    items.sort(key= lambda el: (el[1],el[0],el[2]) )

    print(f'sorted items:{items}')


    values = [2, 4, 3, 5]

    for v in map(lambda e: e ** 2, values):
        print(v)

    print('---')