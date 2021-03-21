import requests
from bs4 import BeautifulSoup

class Inet:
	def __init__(self):
		self.disabledButton = "btn btn-buy buy disabled blocked"

		self.headers = {
			"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
		}

	def isInStock(self):
		url = "https://www.inet.se/produkt/5412097/msi-geforce-rtx-3060-12gb-ventus-3x-oc?utm_source=prisjakt&utm_medium=cpc&utm_campaign=prisjakt"

		page = requests.get(url, headers=self.headers)
		soup = BeautifulSoup(page.content, 'html.parser')

		if not soup.find(class_=self.disabledButton):
			# print("ok")
			return True
		else:
			# print("Is still not availible")
			return False


class Proshop:
	def __init__(self):
		self.headers = {
			"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
		}
		self.buyButton = "site-btn-addToBasket-lg"
		
	def isBuyable(self):
		url = "https://www.proshop.se/Grafikkort/GIGABYTE-GeForce-RTX-3060-GAMING-OC-12GB-GDDR6-SDRAM-Grafikkort/2918930?utm_source=prisjakt&utm_medium=cpc&utm_campaign=pricesite"
		page = requests.get(url, headers=self.headers)
		soup = BeautifulSoup(page.content, 'html.parser')

		if soup.find(class_=self.buyButton):
			# print("ok")
			return True
		else:
			# print("Is still not availible")
			return False


