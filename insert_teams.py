import sqlite3

conn = sqlite3.connect('playoffs.db')
cursor = conn.cursor()


query = '''
    INSERT INTO teams (City,Name)
    VALUES
    ('Denver', 'Broncos'),
    ('New_England', 'Patriots'),
    ('Houston', 'Texans'),
    ('Buffalo', 'Bills'),
    ('Seattle', 'Seahawks'),
    ('Chicago', 'Bears'),
    ('Los_Angeles', 'Rams'),
    ('San_Franciso', '49ers');
'''




cursor.execute(query)

conn.commit()
conn.close()