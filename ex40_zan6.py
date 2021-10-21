
def foo(a=[], b={}):
    print(f'a={a}')
    print(f'b={b}')
    print(' - ' * 20)
    n = len(a)
    a.append(n)
    b[n] = n

if __name__ == '__main__':
    
    foo()
    foo([4,1,6], {'x':11})
    foo()
    foo([41,12,61], {'x':11,'y':20})
    foo()
    print('---')