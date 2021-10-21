
service = 'ssh' # глобална променлива

def show(title, *args, a=100 ):
    print(f'title = {title}')

    print('args:')
    for v in args:
        print(f'arg={v}')

    print('keyword only params')
    print(f'a={a}')

    
    

if __name__ == '__main__':
    
    show('Python')

    t = (11,22,33,44)

    show('Python',  *t)


    show('Python',  *t, a=1)

    show('Python', a=1)


    print('---')