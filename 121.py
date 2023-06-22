import sqlite3

con = sqlite3.connect('info.db')
cur = con.cursor()

students = [
    {"name": "Arshia", "age": 18, "job": "Backend Developer"},
    {"name": "Ahmad", "age": 13, "job": "Frontend Developer"},
    {"name": "Ali", "age": 14, "job": "Security Engineer"},
    {"name": "Arad", "age": 16, "job": "Data Engineer"},
]

cur.execute("CREATE TABLE IF NOT EXISTS students(name, age, job);")


# for person in students:
#     cur.execute(f"INSERT INTO students(name,age,job) VALUES (?,?,?)",(person["name"], person["age"], person["job"]))


cur.execute("SELECT * FROM students;")
records = cur.fetchall()

# print(len(records))

for record in records:
    print(record)

con.commit()
con.close()
print('Done')
