
service = 'ssh' # глобална променлива

def show(title, *, a=100 ):
    print(f'title = {title}')

    print('keyword only params')
    print(f'a={a}')

    
    

if __name__ == '__main__':
    
    show('Python')

   
    show('Python', a=1)


    print('---')