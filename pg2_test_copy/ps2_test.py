import psycopg2 as pg2

conn = pg2.connect(database='postgres', user='postgres',password='password')
cur = conn.cursor()

query1 = '''
CREATE TABLE pay(
	pers_id SERIAL PRIMARY KEY UNIQUE NOT NULL, 
	payment SMALLINT NOT NULL
);
'''
query2 = '''
INSERT INTO pay(payment) 
VALUES (%s)
''',
(19)


cur.execute(query1)
cur.execute('''
INSERT INTO pay(payment)
 VALUES (10);
''')
# cur.commit()

cur.execute("SELECT * FROM pay;")
rese = cur.fetchall()

print(rese)

