import psycopg2 as pg2
from sql_operations import SQLOperations
from scraper import Scraper
import pandas as pd

pd.set_option('display.width', 40)
link = 'https://www.newegg.com/gigabyte-geforce-rtx-3070-gv-n3070eagle-8gd/p/N82E16814932344?Description=rtx 3070&cm_re=rtx_3070-_-14-932-344-_-Product'

conn = pg2.connect(database='postgres', user='postgres',password='password')
cur = conn.cursor()

# df = pd.DataFrame(columns=('name','price','ram','speed'))
# df2 = pd.DataFrame([list(Scraper().scraperProductInfo(link))], columns=('name','price','ram','speed'))
# df3 = pd.DataFrame([list(Scraper().scraperProductInfo(link))], columns=('name','price','ram','speed'))

# df = df.append(df2,ignore_index=True)
# df = df.append(df3,ignore_index=True)
df = Scraper().scraperUpdate()

print(df)

# SQLOperations().create_table()
# SQLOperations().pass_into_table(('http1g',15,'MSI','2060'))
# SQLOperations().show_table()

# SQLOperations().clear_table()
# print(list((Scraper().scraperProductInfo('https://www.newegg.com/gigabyte-geforce-rtx-3070-gv-n3070eagle-8gd/p/N82E16814932344?Description=rtx 3070&cm_re=rtx_3070-_-14-932-344-_-Product'))))
