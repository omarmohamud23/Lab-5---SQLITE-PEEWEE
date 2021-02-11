import sqlite3 

conn = sqlite3.connect('first_db.sqlite')

conn.execute('CREATE  TABLE IF NOT EXISTS products (id int, name text)')

##conn.execute('INSERT INTO products values (1000, "hat")')
##conn.execute('INSERT INTO products values (1001, "jacket")')

conn.commit()

results  = conn.execute('SELECT * FROM products')


for row in results:
    print(row [1])


results = conn.execute('SELECT * FROM products WHERE name like "jacket"')
first_row = results.fetchone()
print(first_row)


new_id = int(input('Enter new id: '))
new_name = input('enter new product: ')

conn.execute(f'INSERT INTO products VALUES (?, ?)', (new_id, new_name) )
conn.commit()



conn.close()