# %%
conn = dict(
    host='localhost',
    port=1521,
    encoding='utf8',
    db='northwind',
    keepalive=True
)

conn
# %%
conn['db']
# %%
conn1 = ['localhost', 'northwind','utf8',1521]

conn1[1]

# %%

user = {
    'first_name':'Anna',
    'last_name':'Smith',
    'age':30,
    'mail':'anna@no.com'
}

user['last_name']
# %%
user.keys()
# %%
user.values()
# %%
user.items()
# %%
'age' in user
# %%
user['phone']
# %%
user.get('phone','000-00-00')
# %%
