import sqlite3

conn = sqlite3.connect('playoffs.db')
cursor = conn.cursor()


query = '''
    SELECT *
    FROM teams;
'''



cursor.execute(query)

result = cursor.fetchall()

conn.close()

for item in result:
    print(item)