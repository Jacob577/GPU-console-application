import psycopg2 as pg2
from sql_operations import SQLOperations
from scraper import Scraper

conn = pg2.connect(database='postgres', user='postgres',password='password')
cur = conn.cursor()

# SQLOperations().create_table()
# SQLOperations().pass_into_table(('http1g','AMD','MSI','2060',150.5,'1800 MHz','6 gb'))
# SQLOperations().show_table()

# SQLOperations().clear_table()
answers = Scraper().scraperUpdate()