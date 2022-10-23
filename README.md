# Web-Scraper
By: Tyler Collins

---

### Introduction
This is a web scraper made using Python which scrapes two seperate websites, xymoxdrumco.com and lonestarpercussion.com.
The program loops through the site map for both sites and obtains information such as the product name, price, type, etc. 
It then loads this data into a csv file where it is sorted into catagories and subcatagories. It then creates multiple visualizations
which compare prices and discounts between items.

---

### Contents
The Web-Scraper Github repository contains 4 files:
* sel.py: Scrapes both websites and loads information into JSON file (Creates attributes.json)
* attributes.json: Contains the data obtained from scraping both websites
* xymoxVisual.py: Uses data from attributes.json to create visualizations
* README.md: Contains information about the web scraper and instructions on how to run it

---

### How to Run
1. Place sel.py, attributes.json, and xymoxvisual.py in your directory.
2. (Optional) If you would like to scrape the websites yourself then run sel.py. This will replace the data in attibutes.json with the newly scraped information. Otherwise you can just use the attributes.json file which was provided.
3. Run xymoxVisual.py
4. A list of possible categories will be displayed and it will prompt you to enter a category. Enter a category.
5. A list of possible subcategories will be displayed and it will prompt you to enter a subcategory. Enter a subcategory.
6. Figure 1 of 4 will appear displaying 2 bar graphs. The first displays the price of each item and the second displays the discount amount of each item. The X-axis displays the different item numbers. Close the figure.
7. Figure 2 of 4 will appear displaying 4 violin plots. The first shows 
