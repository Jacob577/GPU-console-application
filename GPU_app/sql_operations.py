import psycopg2 as pg2

conn = pg2.connect(database='postgres', user='postgres',password='password')
cur = conn.cursor()

class SQLOperations:

	def __init__(self):
		self.not_empty = []
		pass

	def create_table(self):
		'''
		This method recreates the base table, use when reset table or create from scratch.

		'''
		query = '''
		CREATE TABLE gpu_info(
			gpu_id SERIAL PRIMARY KEY NOT NULL,
			name VARCHAR(100),
			price FLOAT(2),
			speed VARCHAR(50),
			memory VARCHAR(10)
		);
		'''
		cur.execute(query)

	def pass_into_table(self,input_values):

		cur.execute('''INSERT INTO gpu_info(
			name,
			price,
			speed,
			memory
			)
			VALUES(%s,%s,%s,%s)''', 
		input_values)
		conn.commit()

	def show_table(self):
		cur.execute("SELECT * FROM gpu_info;")
		print(cur.fetchall())

	def clear_table(self):
		cur.execute("DROP TABLE gpu_info")
		conn.commit()

