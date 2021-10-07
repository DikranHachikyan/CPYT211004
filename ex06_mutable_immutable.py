# %%
a = 5

b = 5

id(a) == id(b)
# %%
print(id(a))

a = 10

print(id(a))


# %%
class Point:
    def __init__(self, x):
        self.x = x

# %%
p1 = Point(x = 10)
p2 = Point(x = 10)

id(p1) == id(p2)
# %%

p1.x = 10

id(p1) == id(p2)

# %%
id(p1.x) == id(p2.x)
# %%
s1 = 'hello' * 1300
s2 = 'hello' * 1300

id(s1) == id(s2)
# %%
