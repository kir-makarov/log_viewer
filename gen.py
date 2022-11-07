import datetime
import sqlite3
import random
import time

conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

build_data = ("3.9.0", "3.8.0", "3.7.0")
db_data = ['tfact01', 'rfact01', 'tdb3']
author_data = ['Makarov Kirill Dmitrievich',
               'Ivanov Ivan Ivanovich']
task = ['FACT-01', 'FACT-02', 'FACT-03']
hash = 'asdasd123123123asdas12431241dadasdasdasd'
message = 'test test testtest test testtest test testtest test testtest test testtest test testtest test testtest test' \
          'test test testtest test testtest test testtest test testtest test testtest test testtest test test test'

filename = '/dfgdfgdfg/dfgdfgdfgdg/dfgdfg/привет.sql'

# cursor.execute("DELETE FROM maintable")
start = time.time()
a = cursor.execute("select * from maintable where build = '3.9.0'")
for i in a:
    print(i)
# for i in range(1000000):
#     cursor.execute(
#         "INSERT INTO maintable (build, task, database, hash, author, date, message, filename) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
#         (random.choices(build_data, k=1)[0], random.choices(task, k=1)[0], random.choices(db_data, k=1)[0], hash,
#          random.choices(author_data, k=1)[0], datetime.datetime.now(),
#          message, filename,))
#
# conn.commit()
conn.close()

print(time.time() - start)

# {"build": random.choices(build_data, k=1),
#                     'task': random.choices(task, k=1),
#                     'database': random.choices(db_data, k=1),
#                     'hash': hash,
#                     'author': random.choices(author_data, k=1),
#                     'date': datetime.datetime.now(),
#                     'message': message,
#                     'filename': filename
#                     }
