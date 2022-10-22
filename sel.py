
from selenium import webdriver
import requests
from urllib.parse import urlparse
from protego import Protego
from time import sleep
import json
from selenium.webdriver.common.by import By


data = []
driver = webdriver.Firefox()
driver.get("https://xymoxdrumco.com/sitemap_products_1.xml?from=7013124145307&to=7538037326046")
d = driver.find_elements(By.TAG_NAME, "loc")
urls = []
i = 1
while (i < 559):
    urls.append(d[i].text)
    i = i + 2
start_url = "https://xymoxdrumco.com/sitemap_products_1.xml?from=7013124145307&to=7538037326046"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
headers = {'User-Agent': user_agent}
parse = urlparse(start_url)
parsed = parse[0] + "://" + parse[1]
robo = parsed + "/robots.txt"
p = parsed + parse[2]
r = requests.get(robo, headers=headers)
rp = Protego.parse(r.text)
if (rp.crawl_delay(user_agent) != None):
    delay = rp.crawl_delay(user_agent)
else:
    delay = 1


if (rp.can_fetch("https://xymoxdrumco.com", user_agent)):
    for i in urls:
        sleep(delay)
        driver.get(i)
        #//Gets the url attribute
        URL = i

        #//Gets the item name attribute
        Title = driver.title

        #//Gets the Description of item attribute
        description = driver.find_element(By.CLASS_NAME, "product-single__description")
        strDescription = description.text
        strDescription = strDescription.replace("\n", "")

        #//Gets the current item price attribute
        price = driver.find_element(By.CSS_SELECTOR, ("span.price-item--sale")).get_attribute("innerHTML")
        while (price[0].isspace() or price[0] == '$'):
            price = price[1:]
        while (price[-1].isspace() or price[-1] == 'U' or price[-1] == 'S' or price[-1] == 'D'):
            price = price[:-1]
        price = price.replace(',', '')

        #//Gets the original item price attribute
        origPrice = driver.find_element(By.CSS_SELECTOR, ("s.price-item--regular")).get_attribute("innerHTML")
        while (origPrice[0].isspace() or origPrice[0] == '$'):
            origPrice = origPrice[1:]
            if (len(origPrice) == 0):
                break;
        if (len(origPrice) > 0):
            while (origPrice[-1].isspace() or origPrice[-1] == 'U' or origPrice[-1] == 'S' or origPrice[-1] == 'D'):
                origPrice = origPrice[:-1]
        else:
            origPrice = price
        origPrice = origPrice.replace(',', '')

        #//Gets if the item is in stock or not, attribute
        inStock = driver.find_element(By.XPATH, '//button[@name="add"]')

        #//Gets the discount amount, attribute

        discount = float(origPrice) - float(price)
        discount = "{:.2f}".format(discount)

        #//Gets the catagory the item is in, attribute
        if "Stick Tape" in strDescription:
            Category = "stick tape"
        elif "Snare Stand" in strDescription:
            Category = "snare stand"
        elif "Tenor Sticks" in Title:
            Category = "tenor sticks"
        elif "Drum Sticks" in strDescription:
            Category = "drum sticks"
        elif "Tenor Pad" in Title:
            Category = "tenor pad"
        elif "Gift Card" in Title:
            Category = "gift card"
        elif "Reserve Snare" in strDescription:
            Category = "reserve snare"
        elif "Key" in strDescription:
            Category = "drum key"
        elif "Tenor Kick" in strDescription:
            Category = "tenor kick"
        elif "Table Pad" in strDescription:
            Category = "table pad"
        elif "Bass Kick" in strDescription:
            Category = "bass kick"
        elif "Low Profile Single Pad" in strDescription:
            Category = "low profile single pad"
        elif "Low Profile Snare Pad" in strDescription:
            Category = "low profile snare pad"
        elif "Hybrid Snare Drum" in strDescription:
            Category = "hybrid snare drum"
        elif "Ultra" in strDescription:
            Category = "ultra"
        elif "MusicMart Box" in Title:
            Category = "musicmart box"
        else:
            Category = "None"

        allAttributes = { 'Category': Category,
                          'Website': "Xymox",
                         'URL': URL,
                         'Name': Title,
                         'Description': strDescription,
                         'Price': price,
                         'Original Price': origPrice,
                         'Discount': discount,
                         'In stock': inStock.text}
        data.append(allAttributes)

driver.get("https://www.lonestarpercussion.com/Sitemap.xml")
d1 = driver.find_elements(By.TAG_NAME, "loc")
loneUrls = []
j = 185
while (j < 23185):
    loneUrls.append(d1[j].text)
    j = j + 1
lone_start_url = "https://www.lonestarpercussion.com/Sitemap.xml"
parse2 = urlparse(lone_start_url)
parsed2 = parse2[0] + "://" + parse2[1]
robo = parsed2 + "/robots.txt"
p = parsed2 + parse2[2]
r = requests.get(robo, headers=headers)
rp = Protego.parse(r.text)
if (rp.crawl_delay(user_agent) != None):
    delay = rp.crawl_delay(user_agent)
else:
    delay = 1
if (rp.can_fetch("https://www.lonestarpercussion.com/", user_agent)):
    for i in loneUrls:
        sleep(delay)
        driver.get(i)
        #//Gets the url attribute
        URL = i

        Title = driver.title

        try:
            description = driver.find_element(By.CLASS_NAME, "productDescription")
            strDescription = description.text
        except:
            strDescription = "None"
            pass
        strDescription = strDescription.replace("\n", "")

        try:
            price = driver.find_element(By.CSS_SELECTOR, ("span.productPrice")).get_attribute("innerHTML")
        except:
            price = "$0.00"
            pass
        if "his" in price or "item" in price:
            price = "$0.00"
        price = price.replace(',', '')
        price = price.replace(" ", "")
        price = price.replace("$", "")

        try:
            origPrice = driver.find_element(By.CSS_SELECTOR, ("span.productMsrp")).get_attribute("innerHTML")
        except:
            origPrice = price
            pass
        origPrice = origPrice.replace(',', '')
        origPrice = origPrice.replace(" ", "")
        origPrice = origPrice.replace("$", "")


        try:
            discount = float(origPrice) - float(price)
            discount = "{:.2f}".format(discount)
        except:
            discount = 0.00
            pass
        try:
            if (float(price) == 0):
                discount = -1.00
        except:
            discount = -1.00

        try:
            inStock = driver.find_element(By.CSS_SELECTOR, ("button.icon-24-cart-black")).get_attribute("innerHTML")
        except:
            inStock = "False"
            pass

        if "Tape" in Title:
            Category = "stick tape"
        elif "Cymbal" in Title:
            Category = "cymbal"
        elif "Mallet" in Title:
            Category = "mallet"
        elif "Bass" in Title:
            Category = "bass"
        elif "Ear" in Title:
            Category = "ear phones"
        elif "Stand" in Title:
            Category = "snare stand"
        elif "Tenor Sticks" in Title:
            Category = "tenor sticks"
        elif "Drum Sticks" in Title:
            Category = "drum sticks"
        elif "Key" in strDescription:
            Category = "drum key"
        elif "Timpani" in Title:
            Category = "timpani"
        elif "Triangle" in Title:
            Category = "triangle"
        elif "Chimes" in Title:
            Category = "chimes"
        elif "Head" in Title:
            Category = "drum head"
        else:
            Category = "None"

        allAttributes = {'Category': Category,
                         'Website': "LoneStar",
                         'URL': URL,
                         'Name': Title,
                         'Description': strDescription,
                         'Price': price,
                         'Original Price': origPrice,
                         'Discount': discount,
                         'In stock': inStock}
        data.append(allAttributes)
driver.close()

json_string = json.dumps(data)
with open('attributes.json', 'w') as outfile:
    #json.dump(json_string, outfile)
    outfile.write(json_string)