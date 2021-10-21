
port = 3306 # глобана променлива

def show():
    global port
    port = 22 # локална променлива
    print(f'port:{port}')
    

    
    

if __name__ == '__main__':
    
    print(f'before:{port}')
    show()
    print(f'after:{port}')

    print('---')