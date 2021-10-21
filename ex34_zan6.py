
service = 'ssh' # глобална променлива

def show(title, a=100, *args, **kwargs):
    print(f'title = {title}')

    print('optional params')
    print(f'a={a}')

    print('args:')
    for v in args:
        print(f'arg={v}')

    print('kwargs:')
    if 'version' in kwargs:
        print(f'version:{kwargs["version"]}')

    if 'path' in kwargs:
        print(f'path={kwargs["path"]}')

if __name__ == '__main__':
    # 1.  
    # show('Text Editor')

    # 2.
    # show('Text Editor', 10)

    # 3.
    # show('Text Editor', 10, 1, 2, 3, 4)

    # 4.
    # show('Text Editor', 10, 1, 2, 3, 4, path='/usr/local', version='1.2.3')
    app = {
        'path':'/usr/local/share', 
        'version':'1.4.3',
        'max_mem':4096,
        'port':3306,
        'is_running':False
    }

    show('Text Editor', 10, 1, 2, 3, 4, **app)
    

    print('---')