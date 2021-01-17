import psycopg2 as pg2
import pandas as pd
from scraper import Scraper

conn = pg2.connect(database='postgres', user='postgres',password='password')
cur = conn.cursor()

class SQLOperations:

	def __init__(self):
		self.not_empty = []
		pass

	def create_table(self):
		query = '''
		CREATE TABLE gpu_info(
			gpu_id SERIAL PRIMARY KEY NOT NULL,
			name VARCHAR(500),
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
		cur.execute("SELECT * FROM gpu_info")
		for gpu in cur.fetchall():
			print(gpu[1])
			print(gpu[2:])
			print('\n')

	def clear_table(self):
		cur.execute("DROP TABLE gpu_info")
		conn.commit()


	def showPriceRange(self, lower_bound, higher_bound):
		cur.execute('SELECT * FROM gpu_info WHERE price BETWEEN {} AND {};'.format(lower_bound,higher_bound))
		for gpu in cur.fetchall():
			print(gpu[1])
			print(gpu[2:])
			print('\n')


link = 'https://www.newegg.com/gigabyte-geforce-rtx-3070-gv-n3070eagle-8gd/p/N82E16814932344?Description=rtx 3070&cm_re=rtx_3070-_-14-932-344-_-Product'
df = pd.DataFrame(columns=('Name','Price','Memory','Speed'))
add_to_df = pd.DataFrame([list(Scraper().scraperProductInfo(link))], columns=('Name','Price','Memory','Speed'))
add_to_df1 = pd.DataFrame([list(Scraper().scraperProductInfo(link))], columns=('Name','Price','Memory','Speed'))
add_to_df2 = pd.DataFrame([list(Scraper().scraperProductInfo(link))], columns=('Name','Price','Memory','Speed'))
df = df.append(add_to_df,ignore_index=True)
df = df.append(add_to_df1,ignore_index=True)
df = df.append(add_to_df2,ignore_index=True)

# print(df)

# print(df.iloc[0])
# SQLOperations().create_table()
SQLOperations().pass_into_table(df.iloc[0])
SQLOperations().pass_into_table(df.iloc[1])
SQLOperations().pass_into_table(df.iloc[2])
# SQLOperations().show_table()

# SQLOperations().clear_table()
SQLOperations().showPriceRange(100,800)
# SQLOperations().show_table()