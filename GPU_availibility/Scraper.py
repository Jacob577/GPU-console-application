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

	def scrapeLinks(self):
		productListing = "pj-ui-product-listing--item pj-ui-product-listing--item-row"
		URL = {
		'Page 1':'https://www.prisjakt.nu/search?search=3060',
		'Page 2':'https://www.prisjakt.nu/search?search=3060&offset=24',
		}

		for link in list(URL.values()):
			try:
				page = requests.get(link, headers=self.headers)
				soup = BeautifulSoup(page.content, 'html.parser')

				for i in soup.find_all(class_=productListing):
					for a in i.find_all('a', href=True): 
						if a.text:
							self.product_links.append("https://www.prisjakt.nu{}".format(a['href']))
			except:
				print('Failed to get ' + str(link))
		return self.product_links

	def priceRunnerCheck(self,url):
		URL = url
		inStock = "pj-ui-icon--in-stock"
		isInStock = False
		try:
			page = requests.get(URL, headers=self.headers)
			soup = BeautifulSoup(page.content, 'html.parser')
			# title = soup.find()

			if soup.find(class_=inStock):
				isInStock = True

		except:
			print("Error occured with URL: {}".format(URL))

		return isInStock,URL

	def runAllPricerunner(self):
		validURLS = []
		manualExceptions = [
		"https://www.prisjakt.nu/produkt.php?p=5728506",
		"https://www.prisjakt.nu/produkt.php?p=5710334",
		"https://www.prisjakt.nu/produkt.php?p=5710341",
		"https://www.prisjakt.nu/produkt.php?p=5710339",
		"https://www.prisjakt.nu/produkt.php?p=5710337",
		"https://www.prisjakt.nu/produkt.php?p=5664949 ",
		"https://www.prisjakt.nu/produkt.php?p=5710338",
		"https://www.prisjakt.nu/produkt.php?p=5694761",
		"https://www.prisjakt.nu/produkt.php?p=5664949"
		]
		count = 0
		links = Scraper().scrapeLinks()
		for url in links:
			count += 1
			isInStock, url = Scraper().priceRunnerCheck(url)
			if isInStock and (url not in manualExceptions):
				# print("GPU is availible at: {} ".format(url))
				validURLS.append(url)
			# if count%10 == 0:
					# print("Updating...")
			# else:
				# print("No GPU at: {}".format(url))

		if validURLS != []:
			return validURLS
		else:
			return None
		

