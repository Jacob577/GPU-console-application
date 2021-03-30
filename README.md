### GPU-console-application

This console application was created in order to help me get my hands on a graphics card of the 3000-series. I now have a RTX 3060 so it ended quite well.

## Technologies
Project is created with:
* Pandas: 1.2.2
* requests: 2.22.0
* psycopg2: 2.8.6
* BeautifulSoup: 4.8.2

# Clone this project
Navigate to desired location and type:
```
git clone https://github.com/Jacob577/GPU-console-application.git
```

# How it works

Firstly there is a scraper to collect information from Newegg so you can sort through what graphics card you want.
Secondly a availibility check is ran. I decided to look for specifically RTX 3060 so the application scrapes through the two first pages of Pricerunner as well as a specific graphics card on Inet and Proshop.

![Menue](/menue.PNG)

You can then update the price and spec list of the GPU:s with option 1 followed up by entering the filters you see fit with the other options.

![updating](/updating.PNG)

## Availibility check
After that we can run the availibility code in order to locate where a graphics card can be bought.

![availibility](/availibility.PNG)


### What this project taught me:
* Scraping information from websites
* Utilizing SQL together with Python in order to make querys in the application itself

