import sqlite3

con = sqlite3.connect('info.db')
cur = con.cursor()

# cur.execute("CREATE TABLE IF NOT EXISTS customers(name, age, phone);")

# cur.execute("INSERT INTO customers VALUES ('Taha','23','09334438725');")
# cur.execute("INSERT INTO customers VALUES ('Sara','24','09213378325');")
# cur.execute("INSERT INTO customers VALUES ('Ali','17','09363312320');")
# cur.execute("INSERT INTO customers VALUES ('Tina','13','09124428313');")

# cur.execute("DELETE FROM customers;")  # Deletes every record in table
# cur.execute("DELETE FROM customers WHERE age<'18';")

# cur.execute("DROP TABLE customers;") # Deletes table

cur.execute("SELECT * FROM customers;")
records = cur.fetchall()
for i in records:
    print(i[2])
# print(records)

con.commit()
con.close()
print('Done')