# %%
s1 = 'Lorem ipsum dolor sit amet'

s2 = "Lorem ipsum dolor sit amet"
# %%
s3 = '''Lorem ipsum dolor sit amet, 
consectetur adipisicing elit, sed do 
eiusmodtempor incididunt ut labore et 
dolore magna aliqua.'''

print(s3)
# %%
def foo():
    '''Function foo()
    created:04.10.2021
    author:me
    '''
    print('Hello Foo')

# %%
foo()
# %%
print(foo.__doc__)
# %%
x = 5

print(f'value of {x} ** 2 is {x ** 2}')
# %%
s1[4]
# %%
s1[0:5]
# %%
s1[0:20:2]
# %%
s1[::2]
# %%
s1[::-1]
# %%
'HELLO'.lower()
# %%
