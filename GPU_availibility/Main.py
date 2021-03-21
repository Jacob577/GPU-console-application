from Scraper import Scraper
from Inet import Inet, Proshop
import datetime
from texttable import Texttable
import time 
import keyboard
import tkinter
from tkinter import messagebox

root = tkinter.Tk()
root.withdraw()

class Main:
	def __init__(self):
		self.pricerunner = " "
		self.inet = " "
		self.proshop = " "

	def updatePricerunner(self):
		self.pricerunner = Scraper().runAllPricerunner()
		x = datetime.datetime.now()

		if self.pricerunner == None:
			return "No good GPU:s at pricerunner: {}".format(x)
		else:
			messagebox.showinfo("GPU found!", "Go to: {}".format(self.pricerunner))
			return "GPU:s availible at: {}".format(self.pricerunner)

	def updateProshop(self):
		self.proshop = Proshop().isBuyable()
		x = datetime.datetime.now()

		if self.proshop:
			messagebox.showinfo("GPU found!", "Go to: {}".format(self.proshop))
			return "GPU:s availible at: {}".format(self.proshop)
		else:
			return "No good GPU:s at Proshop: {}".format(x)

	def updateInet(self):
		self.inet = Inet().isInStock()
		x = datetime.datetime.now()

		if self.inet:
			messagebox.showinfo("GPU found!", "Go to: {}".format(self.inet))
			return "GPU:s availible at: {}".format(self.inet)
		else:
			return "No good GPU:s at Inet: {}".format(x)


	def printTable(self):
		t = Texttable()
		t.add_rows([["Webbpage", "Status"], ["pricerunner",Main().updatePricerunner()],
			["Proshop", Main().updateProshop()], ["Inet", Main().updateInet()] ])
		print(t.draw())

		# if 

quit = False
while not quit:
	Main().printTable()
	print("If you want to close application press q.")
	time.sleep(300)
