import requests
from bs4 import BeautifulSoup
import pandas as pd
from os import system, name 

class Scraper:

	def __init__(self):
		self.product_links = []
		self.headers = {
			"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
		}
		self.df = pd.DataFrame(columns=('Name','price','Memory','Speed'))
	def scrapeLinks(self):

		URL = {
		'3070p1':'https://www.newegg.com/p/pl?d=rtx+3070&N=100007709&isdeptsrh=1',
		'3070p2':'https://www.newegg.com/p/pl?d=rtx+3070&N=100007709&isdeptsrh=2',
		'3080p1':'https://www.newegg.com/p/pl?d=rtx+3080&N=100007709&isdeptsrh=1',
		'3080p2':'https://www.newegg.com/p/pl?d=rtx+3080&N=100007709&isdeptsrh=2',
		'3090p1':'https://www.newegg.com/p/pl?d=rtx+3090&N=100007709&isdeptsrh=1',
		'3090p2':'https://www.newegg.com/p/pl?d=rtx+3090&N=100007709&isdeptsrh=2',
		}

		for link in list(URL.values()):
			try:
				page = requests.get(link, headers=self.headers)
				soup = BeautifulSoup(page.content, 'html.parser')

				for i in soup.find_all(class_="item-info"):
					for a in i.find_all('a', href=True): 
						if a.text:
							self.product_links.append(a['href'])
			except:
				print('Failed to get ' + str(link))
		return self.product_links

	def scraperProductInfo(self,URL):
		title = ''
		price = ''
		product_bullets = []
		ram = ''
		speed = ''

		try:
			if URL[-1] == 't': #This speeds up the proces significantly
				try:
					page = requests.get(URL, headers=self.headers)
					soup = BeautifulSoup(page.content, 'html.parser')

					title = soup.find(class_='product-title').get_text()
					price = str(soup.find(class_='price-current').get_text())

					try:
						price = price.replace(',','')
					except:
						pass

					for bullets in soup.find(class_='product-bullets'):
						for l in bullets.find_all('li'):
							product_bullets.append(l.get_text())

					for product in product_bullets:
						if Scraper().isRam(product):
							ram = product
							break

					for product in product_bullets:
						if Scraper().isSpeed(product):
							speed = product
							break

					
					if (Scraper().cleanRam(ram) != False) and (Scraper().cleanSpeed(speed) != False):
						# if Scraper().isRam(ram) and Scraper().isSpeed(speed):
						return title, float(price[1:]), Scraper().cleanRam(ram), int(Scraper().cleanSpeed(speed))	


				except:
					print('Failed to get' + str(URL))		
		except:
			print('This is a duplicet.')

	def scraperUpdate(self):
		self.product_links = Scraper().scrapeLinks()
		amount_of_links = len(self.product_links)
		count = 0
		df = pd.DataFrame(columns=('Name','Price','Memory','Speed'))
		for link in self.product_links:
			count += 1		
			try:
				if Scraper().scraperProductInfo(link) != None:
					print(link)
					add_to_df = pd.DataFrame([list(Scraper().scraperProductInfo(link))], columns=('Name','Price','Memory','Speed'))
					df = df.append(add_to_df,ignore_index=True)

					# print(Scraper().scraperProductInfo(link))
			except:
				print('Failed to get url ' + str(link))
			_ = system('cls')
			print('Completed ' + str(count) + '/' + str(amount_of_links) + ' links')
		return df


	def isSpeed(self, speed):
		try:
			if speed.split('MHz') != speed.split('FooBooFizz'):
				return True
			else:
				return False
		except:
			return False
	
	def isRam(self, ram):
		try:
			if ram.split('GB') != ram.split('FooBooFizz'):
				return True
			else:
				return False
		except:
			return False

	def cleanRam(self, ram):
		try:
			return int(ram.split('GB')[0][-2:])
		except:
			return False

	def cleanSpeed(self, speed):
		try:
			return int(speed.split('MHz')[0][-5:])
		except:
			return False

# print(Scraper().scraperUpdate())

# print(list((Scraper().scraperProductInfo('https://www.newegg.com/gigabyte-geforce-rtx-3070-gv-n3070eagle-8gd/p/N82E16814932344?Description=rtx 3070&cm_re=rtx_3070-_-14-932-344-_-Product'))))
