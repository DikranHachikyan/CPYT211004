# 1.
# import time
# print(time.time())

# 1.1
# import time as tm
# print(tm.time())

# 2.
from time import time
# print(time())

# 2.1
# from time import time as get_time
# print(get_time())

if __name__ == '__main__':
    N = 5000
    values = []

    # for
    t = time()
    for v in range(1,N):
        for s in range(1, N):
            values.append( divmod(v,s))
    print(f'nested loops:{time() - t:.4f}')

    # for expr
    t = time()
    values2 = [ divmod(v,s)  for v in range(1,N) for s in range(1,N)]
    print(f'for expr:{time() - t:.4f}')


    # generators
    t = time()
    gen = ( divmod(v,s)  for v in range(1,N) for s in range(1,N) )
    values3 =  list(gen)
    print(f'generators:{time() - t:.4f}')

    print('---')