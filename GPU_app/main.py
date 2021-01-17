import psycopg2 as pg2
from sql_operations import SQLOperations
from scraper import Scraper
import pandas as pd
from os import system, name 

df = pd.DataFrame(columns=('Name','Price','Memory','Speed'))
pd.set_option('display.width', 40)
# link = 'https://www.newegg.com/gigabyte-geforce-rtx-3070-gv-n3070eagle-8gd/p/N82E16814932344?Description=rtx 3070&cm_re=rtx_3070-_-14-932-344-_-Product'

conn = pg2.connect(database='postgres', user='postgres',password='password')
cur = conn.cursor()
# df = Scraper().scraperUpdate()

# add_to_df = pd.DataFrame([list(Scraper().scraperProductInfo(link))], columns=('Name','Price','Memory','Speed'))
# add_to_df1 = pd.DataFrame([list(Scraper().scraperProductInfo(link))], columns=('Name','Price','Memory','Speed'))
# add_to_df2 = pd.DataFrame([list(Scraper().scraperProductInfo(link))], columns=('Name','Price','Memory','Speed'))
# df = df.append(add_to_df,ignore_index=True)
# df = df.append(add_to_df1,ignore_index=True)
# df = df.append(add_to_df2,ignore_index=True)

# print(df)

# print(df.iloc[0])
# SQLOperations().create_table()
# SQLOperations().pass_into_table(df.iloc[0])
# SQLOperations().pass_into_table(df.iloc[1])
# SQLOperations().pass_into_table(df.iloc[2])
# SQLOperations().show_table()

# SQLOperations().clear_table()
# print(list((Scraper().scraperProductInfo('https://www.newegg.com/gigabyte-geforce-rtx-3070-gv-n3070eagle-8gd/p/N82E16814932344?Description=rtx 3070&cm_re=rtx_3070-_-14-932-344-_-Product'))))

running = True

while running:	
	_ = system('cls')
	print('Welcome to a GPU-application created by Jacob')
	print('Choose between the different alternatives bellow by entering the number in front of the alternative and press enter: \n')
	
	print('1. Update table')
	print('2. Show all gpu:s')
	print('3. Specify price range')
	print('4. Specify memory range')
	print('5. Specify speed range')
	print('6. Search within database')
	print('To exit application press any letter.\n')
	print('Enter your choice:\n')
	choice = input()

	try:
		choice = int(choice)
		if choice == 1:
			print('Wait a moment, this may take a while.')	
			try:
				SQLOperations().clear_table()
				print('table now cleared')
			except:
				pass

			try:
				SQLOperations().create_table()
				print('table now created')
			except:
				pass

			try:
				df = Scraper().scraperUpdate()
				for i in range(len(df.iloc[:])):
					try:
						SQLOperations().pass_into_table(df.iloc[i])
					except:
						pass
				wait = input('Update complete, press enter to return to the main menue')
			except:
				pass

		if choice == 2:
			_ = system('cls')
			try:
				print(df)
				SQLOperations().show_table()
				another = input('Press enter to return to the main menue')
			except:
				print('You need to update the table, option "1" in the main menue')
				another = input('Press enter to return to the main menue')
		if choice == 3:
			try:
				_ = system('cls')
				print('What is the lowes price you would like to pay for a GPU?')
				lower_bound = float(input('Lower bound: '))
				print('What is the lowest price you would like to pay for a GPU?')
				higher_bound = float(input('Higher bound: '))
				SQLOperations().showPriceRange(lower_bound,higher_bound)
				print('Press enter to return to main menue.')
				wait = input()
			except:
				print('Something went wrong, make sure to not include anything else than numbers or ","!')
				wait = input('Press enter to return to main menue.')

		if choice == 4:
			try:
				_ = system('cls')
				print('What is the lowes memory you would like your GPU to have?')
				lower_bound = float(input('Lower bound: '))
				print('What is the highest memory you would like your GPU to have?')
				higher_bound = float(input('Higher bound: '))
				SQLOperations().showMemoryRange(lower_bound,higher_bound)
				print('Press enter to return to main menue.')
				wait = input()
			except:
				print('Something went wrong, make sure to not include anything else than numbers or ","!')
				wait = input('Press enter to return to main menue.')

		if choice == 5:
			try:
				_ = system('cls')
				print('What is the lowes speed you would like your GPU to have?')
				lower_bound = float(input('Lower bound: '))
				print('What is the highest speed you would like your GPU to have?')
				higher_bound = float(input('Higher bound: '))
				SQLOperations().showSpeedRange(lower_bound,higher_bound)
				print('Press enter to return to main menue.')
				wait = input()
			except:
				print('Something went wrong, make sure to not include anything else than numbers or ","!')
				wait = input('Press enter to return to main menue.')

		if choice == 6:
			try:
				_ = system('cls')
				name_search = input('Search within database for GPU: ')
				SQLOperations().searchGPU(name_search) 
				print('Press enter to return to main menue.')
				wait = input()
			except:
				print('Something went wrong, feel free to try again or update database.')
				wait = input('Press enter to return to main menue.')
	except:
		running = False


