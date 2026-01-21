import sqlite3
import pandas as pd

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

df = pd.DataFrame(result, columns=['id', 'City', 'Name'])
print(df)
print(df['City'])

cityList = []
for item in result:
    cityList.append(item[1])
print(cityList)

cityLengthList = []
for item in result:
    cityLengthList.append(len(item[1]))
print(cityLengthList)


teamLengthList = []
for item in result:
    teamLengthList.append((len(item[1]), len(item[2])))
print(teamLengthList)