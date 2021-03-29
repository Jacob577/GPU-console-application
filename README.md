### GPU-console-application

This console application was created in order to help me get my hands on the a graphics card of the 3000-series. I now got a RTX 3060 so it ended quite well.

## Technologies
Project is created with:
* Pandas: 1.2.2
* requests: 2.22.0
* psycopg2: 2.8.6


#How it works

Firstly there is a scraper to collect information from Newegg so you can sort through what graphics card you want.
Secondly a availibility check is ran. I decided to look for specifically RTX 3060 so the application scrapes through the two first pages of Pricerunner as well as a specific graphics card on Inet and Proshop.

![Menue](/menue.PNG)

You can then update the price and spec list of the GPU:s with option 1 followed up by entering the filters you see fit with the other options.

![Update](/updating.PNG)


This is a console app suppused to scrape inormation about modern GPU:s on amazon.com and furhtermore store in a SQL-database.
Information can be called for and there will be filters availible to sort information and compare GPU:s
