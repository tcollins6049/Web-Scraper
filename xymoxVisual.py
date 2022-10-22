import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns


with open('attributes.json', encoding='utf-8') as inputfile:
    df = pd.read_json(inputfile)
df = df.reset_index()
df.to_csv('attributes.csv', encoding='utf-8', index=False)

#CSV file modifying section ------------------------------------------------------------
def catCreater(category, name, description, url):
    if "Book" in url or "book" in url: category = "method books"
    elif "Hardware" in url: category = "hardware"
    elif "Sticks-Mallets" in url or "Drum Sticks" in name: category = "sticks and mallets"
    elif "Keyboards" in url: category = "keyboards"
    elif ("Bass" in name or "bass" in name) and "Ambassador" not in name: category = "bass"
    elif "Pad" in name or "pad" in name or "ultra" in name or "Ultra" in name: category = "drum pads"
    elif "Stick Tape" in name or "stick tape" in name or "Stick Rapp" in name or "stick rapp" in name: category = "stick tape"
    elif "Stick Tape" in description or "stick tape" in description or "Stick Rapp" in description or "stick rapp" in description: category = "stick tape"
    elif "Timpani" in name or "timpani" in name: category = "timpani"
    elif "Cymbal" in name or "cymbal" in name or "Cymbals-Gongs" in url: category = "cymbal"
    elif "Tom" in name or "tom" in name: category = "tom"
    elif "Snare Drum" in name or "snare drum" in name: category = "snare drum"
    elif "Tenor" in name or "tenor" in name: category = "tenor"
    elif "Head" in url or "head" in url: category = "drum heads"
    elif "Castanet" in name or "castanet" in name: category = "percussion"
    elif "Sleigh Bell" in name or "sleigh bell" in name: category = "percussion"
    elif "Triangle" in name or "triangle" in name: category = "percussion"
    elif "Chimes" in name or "chimes" in name: category = "percussion"
    elif "Latin-World-Effects" in url: category = "percussion"
    elif "Apparel-Accessories" in url or "Cases-Bags" in url: category = "accessories"
    else: category = "None"
    return category

def subCatCreator(subCat, category, name, url):
    if "stick tape" in category: subCat = "tape"
    elif "bass" in category:
        if "Kick" in name: subCat = "bass kicks"
        elif "Concert" in name or "concert" in name or "Bahia" in name or "Log" in name or "Pipe Band" in name or "Cajon" in name or "Design" in name: subCat = "concert bass"
        elif ("Head" in name or "head" in name) and "Ahead" not in name: subCat = "bass heads"
        elif "Drum Set" in name or "Shell" in name: subCat = "drum sets"
        elif "Case" in name or "case" in name or "Bag" in name: subCat = "bass case"
        elif "hoop" in name or "Hoop" in name or "Beater" in name or "Patch" in name or "Decal" in name or "Pedal" in name or "Lift" in name or "Pad" in name or "Adaptor" in name or "Converter" in name: subCat = "hardware"
        elif "Sticker" in name or "Platform" in name or "Mute" in name or "Trigger" in name or "Rim" in name or "Hook" in name or "Boomwhacker" in name or "Kit" in name: subCat = "hardware"
        elif ("Carrier" in name or "Muffl" in name or "Sling" in name or "Stand" in name or "Cover" in name or "Holder" in name or "Mount" in name) and "with Carrier" not in name: subCat = "marching hardware"
        elif "Marching Bass" in name: subCat = "marching bass"
        else: subCat = "nothing"
    elif "sticks and mallets" in category:
        if "Drumsticks" in name and "Nylon" in name: subCat = "nylon tip drum sticks"
        elif "Drumsticks" in name and "Wood" in name: subCat = "wood tip drum sticks"
        elif "Drumsticks" in name or "Drum Sticks" in name: subCat = "other drum sticks"
        elif "Snare Sticks" in name: subCat = "con/mar snare sticks"
        elif "Bass Drum Mallets" in name or "Bass Mallets" in name: subCat = "con/mar bass mallets"
        elif "Tenor" in name or "tenor" in name: subCat = "tenor mallets"
        elif "Beater" in name or "beater" in name: subCat = "beater"
        elif "Timpani Mallets" in name: subCat = "timpani mallets"
        elif "Xylophone Mallets" in name or "Keyboard Mallets" in name or "Bell Mallets" in name or "Vibraphone Mallets" in name or "Marimba Mallets" in name: subCat = "keyboard mallets"
        elif "Scraper" in name or "Tipper" in name or "Brushes" in name: subCat = "scrapers/brushes/tippers"
        elif "Mallet" in name: subCat = "other mallets"
        elif "Stick" in name or "stick" in name: subCat = "other sticks"
        else: subCat = "nothing"
    elif "snare drum" in category:
        if "Hybrid" in name: subCat = "hybrid"
        elif "Head" in name: subCat = "snare head"
        elif "Bag" in name or "bag" in name or "Cover" in name or "Dampener" in name or "Reflector" in name or "Projector" in name or "Kit" in name: subCat = "snare hardware"
        elif "Snare Drum" in name and "Concert" in name: subCat = "concert snare"
        elif "Snare Drum" in name and "Marching" in name: subCat = "marching snare"
        elif "Snare Drum" in name and "Steel" in name: subCat = "steel snare"
        elif "Snare" in name: subCat = "snare variety"
        else: subCat = "nothing"
    elif "tom" in category:
        if "Case" in name or "case" in name or "Bag" in name: subCat = "tom case/bag"
        elif "Tom" in name and "Concert" in name: subCat = "concert tom"
        elif "Head" in name and "Headed" not in name and "Snare" not in name: subCat = "tom heads"
        elif "Clear" in name: subCat = "clear heads"
        elif "Headed" in name: subCat = "tom variety"
        else: subCat = "nothing"
    elif "tenor" in category:
        if "Sticks" in name: subCat = "tenor sticks"
        elif "Kick" in name: subCat = "tenor kicks"
        elif "Head" in name or "head" in name or "SST" in name: subCat = "tenor heads"
        elif ("Cover" in name or "Case" in name or "Decals" in name or "Recorder" in name or "Trim" in name or "J-Bar") and "Hardware" not in name and "Pan" not in name: subCat = "tenor hardware"
        elif "Tenor" in name: subCat = "marching tenor"
        else: subCat = "nothing"
    elif "cymbal" in category:
        if "Case" in name or "Bag" in name or "Mute" in name or "Stacker" in name or "Protectant" in name or "Polish" in name or "Cleaner" in name or "Sleeve" in name or "Stand" in name: subCat = "cymbal hardware"
        elif "Straps" in name or "Bearings" in name or "Holder" in name or "Rattler" in name or "Sizzler" in name or "Seat" in name: subCat = "cymbal hardware"
        elif "Finger" in name: subCat = "finger"
        elif "Hand" in name or "Pair" in name: subCat = "marching"
        elif "Chinese" in name or "China" in name: subCat = "china"
        elif "Crash" in name: subCat = "crash"
        elif "Gong" in name and "String" not in name: subCat = "gong"
        elif "Suspended Cymbal" in name: subCat = "suspended"
        elif "Splash" in name: subCat = "splash"
        elif "Ride" in name: subCat = "ride"
        elif "Hi Hat" in name: subCat = "hi hat"
        else: subCat = "variety"
    elif "drum pads" in category:
        if "12" in name and "Reserve" in name: subCat = "12 reserve pad"
        elif "14" in name and "Reserve" in name: subCat = "14 reserve pad"
        elif "Table Pad" in name: subCat = "table pad"
        elif "Low Prof" in name: subCat = "practice pads"
        elif "Tenor Pad" in name: subCat = "tenor pad"
        elif "Pad Head" in name: subCat = "practice pad head"
        elif "Snare-Practice-Pad" in url: subCat = "practice pads"
        else: subCat = "nothing"
    elif "timpani" in category:
        if "Timpani-Covers" in url: subCat = "covers"
        elif "Cases" in url: subCat = "cases"
        elif "Drum-Heads" in url: subCat = "heads"
        elif "/Concert/Timpani/Adams" in url: subCat = "adams concert timpani"
        elif "/Concert/Timpani/Majestic" in url: subCat = "majestic concert timpani"
        elif "Concert/Timpani/Yamaha" in url: subCat = "yamaha concert timpani"
        else: subCat = "timpani hardware"
    elif "keyboards" in category:
        if "Marching" in url: subCat = "marching keyboards"
        elif "Keyboards/Marimbas" in url: subCat = "marimbas"
        elif "Keyboards/Vibraphones" in url: subCat = "vibraphones"
        elif "Keyboards/Xylophones" in url: subCat = "xylophones"
        elif "Keyboards/Bells-Glockenspiels" in url: subCat = "bells"
        else: subCat = "keyboard varieties"
    else: subCat = "nothing"
    return subCat

def price_toFloat(price):
    if "i" in price or "a" in price:
        price = 0.00
    price = float(price)
    price = "{:.2f}".format(price)
    return price

floatPrice = df.apply(
        lambda row: price_toFloat(row['Price']),
        axis=1)
df['Price'] = floatPrice

df = df[df['Price'] != "0.00"]
df["SubCategory"] = "None"
catCreate = df.apply(
    lambda row: catCreater(row['Category'], row['Name'], row['Description'], row['URL']),
    axis=1)
df['Category'] = catCreate
df = df[df['Category'] != "None"]
subCatCreate = df.apply(
    lambda row: subCatCreator(row['SubCategory'], row['Category'], row['Name'], row['URL']),
    axis=1)
df['SubCategory'] = subCatCreate

df.to_csv('attributes.csv', encoding='utf-8', index=False)
# End of CSV file modifying section -------------------------------------------------------------------

# Bar Graph creation section ----------------------------------------------------
colors = []
def price_inStock(inStock, web):
    if "ADD TO CART" in inStock or "Add To Cart" in inStock:
        inStock = "True"
        if "Xymox" in web:
            colors.append('blue')
        else:
            colors.append('green')
    if "SOLD OUT" in inStock:
        inStock = "False"
        if "Xymox" in web:
            colors.append('red')
        else:
            colors.append('pink')
    return inStock
def price_inStock2(inStock):
    if "ADD TO CART" in inStock or "Add To Cart" in inStock:
        inStock = "True"
    if "SOLD OUT" in inStock:
        inStock = "False"
    return inStock

def price_bar_plot(df, category, subCat):
    priceData = df.drop(columns="URL")
    priceData = priceData.drop(columns="Description")
    priceData = priceData.drop(columns="Discount")
    priceData = priceData.drop(columns="Original Price")
    priceData = priceData[priceData['Price'] != 0.00]

    new = priceData.apply(
        lambda row: price_inStock(row['In stock'], row['Website']),
        axis=1)
    priceData['In stock'] = new
    #priceData = priceData.reset_index()

    priceData.to_csv('priceTable.csv', index=False)

    discountData = df.drop(columns="URL")
    discountData = discountData.drop(columns="Description")
    discountData = discountData.drop(columns="Original Price")
    discountData = discountData.drop(columns="Price")
    discountData = discountData[discountData['Discount'] != -1.00]
    new = discountData.apply(
        lambda row: price_inStock2(row['In stock']),
        axis=1)
    discountData['In stock'] = new

    fig, axis = plt.subplots(nrows=2, ncols=1)
    ax1 = priceData.plot.bar(x='index', y='Price', rot=0,ax=axis[0], color=colors)
    ax1.set_xticks([],[])
    ax1.set_xlabel('')
    ax1.set_ylabel('Price')
    ax2 = discountData.plot.bar(x='index', y='Discount', rot=0, ax=axis[1], color=colors)
    ax2.set_xlabel('Item Number')
    ax2.set_ylabel('Discount Amount')
    fig.suptitle('Item Price and Discount Amount(Category: ' + category + ", SubCategory: " + subCat + ")", fontsize=16)
    ax1.get_legend().remove()
    ax2.get_legend().remove()

    red_patch = mpatches.Patch(color='red', label='Xymox: Out')
    blue_patch = mpatches.Patch(color='blue', label='Xymox: In')
    green_patch = mpatches.Patch(color='green', label='LoneStar: In')
    pink_patch = mpatches.Patch(color='pink', label='LoneStar: Out')
    fig.legend(handles=[blue_patch, red_patch, green_patch, pink_patch], title="Website/Availability")
    fig.autofmt_xdate(rotation=90)

#End of Bar Graph Creation Section ----------------------------------------------------------
colorArr = []
def colors3D(category):
    if "bass" in category: colorArr.append('blue')
    elif "snare drum" in category: colorArr.append('red')
    elif "cymbal" in category: colorArr.append('orange')
    elif "timpani" in category: colorArr.append('green')
    elif "sticks and mal" in category: colorArr.append('yellow')
    elif "keyboards" in category: colorArr.append('purple')
    elif "drum pads" in category: colorArr.append('brown')
    elif "stick tape" in category: colorArr.append('black')
    elif "tenor" in category: colorArr.append('gray')
    elif "toms" in category: colorArr.append('cyan')
    else: colorArr.append('white')

def scatterPlot3D(df):
    df1 = df[df['Price'] < 2000]
    xydf = df1[df1['Website'] == "Xymox"]
    fig = plt.figure(figsize=plt.figaspect(0.5))
    ax = fig.add_subplot(1, 2, 1, projection='3d')
    xs = xydf['Price']
    ys = xydf['Discount']
    zs = xydf['Original Price']
    new = xydf.apply(
        lambda row: colors3D(row['Category']),
        axis=1)
    ax.scatter(xs, ys, zs, c=colorArr)
    ax.set_xlabel('Price')
    ax.set_ylabel('Discount')
    ax.set_xlabel('Original Price')
    ax.text2D(0.05, 0.95, "Xymox", transform=ax.transAxes)
    colorArr.clear()

    lsdf = df1[df1['Website'] == "LoneStar"]
    lsdf = lsdf[lsdf['Category'] != "method books"]
    lsdf = lsdf[lsdf['Category'] != "hardware"]
    lsdf = lsdf[lsdf['Category'] != "percussion"]
    lsdf = lsdf[lsdf['Category'] != "accessories"]
    lsdf = lsdf[lsdf['Category'] != "drum heads"]
    new = lsdf.apply(
        lambda row: colors3D(row['Category']),
        axis=1)
    ax1 = fig.add_subplot(1, 2, 2, projection='3d')
    x1s = lsdf['Price']
    y1s = lsdf['Discount']
    z1s = lsdf['Original Price']
    ax1.scatter(x1s, y1s, z1s, c=colorArr)
    ax1.set_xlabel('Price')
    ax1.set_ylabel('Discount')
    ax1.set_xlabel('Original Price')
    ax1.text2D(0.05, 0.95, "LoneStar", transform=ax1.transAxes)

    blue_patch = mpatches.Patch(color='blue', label='Bass')
    red_patch = mpatches.Patch(color='red', label='Snare Drum')
    orange_patch = mpatches.Patch(color='orange', label='Cymbal')
    green_patch = mpatches.Patch(color='green', label='timpani')
    yellow_patch = mpatches.Patch(color='yellow', label='Sticks and Mallets')
    purple_patch = mpatches.Patch(color='purple', label='Keyboards')
    brown_patch = mpatches.Patch(color='brown', label='Drum Pads')
    black_patch = mpatches.Patch(color='black', label='Stick Tape')
    gray_patch = mpatches.Patch(color='gray', label='Tenor')
    cyan_patch = mpatches.Patch(color='cyan', label='Toms')
    fig.legend(handles=[blue_patch, red_patch, orange_patch, green_patch, yellow_patch, purple_patch, brown_patch, black_patch, gray_patch, cyan_patch], title="Categories")
    fig.suptitle('Price Distribution for Each Category Between Websites')

def violinPlot(df, dfc, cat, subCat):
    df1 = df[df['Category'] == cat]
    fig, axes = plt.subplots(2, 2)
    ax1 = sns.violinplot(x='Website', y='Price', data=dfc, ax=axes[0, 0], showfliers=False)
    ax1.set_title("Average Price for items in category: " + cat + ", subCategory: " + subCat)
    ax2 = sns.violinplot(x='Website', y='Discount', data=dfc, ax=axes[1, 0], showfliers=False)
    ax2.set_title("Average Discount for items in category: " + cat + ", subCategory: " + subCat)
    ax3 = sns.violinplot(x='Website', y='Price', data=df1, ax=axes[0, 1], showfliers=False)
    ax3.set_title("Average Price for all items in category: " + cat)
    ax4 = sns.violinplot(x='Website', y='Discount', data=df1, ax=axes[1, 1], showfliers=False)
    ax4.set_title("Average Discount for all items in category: " + cat)
    fig.suptitle('Average Price and Discount (Category: ' + cat + ', SubCategory: ' + subCat + ')')

def boxPlot(df):
    fig, axes = plt.subplots(2, 1)
    ax = sns.boxplot(y='Price', x='Website', data=df, width=0.5, palette="colorblind", showfliers=False,ax=axes[0])
    ax1 = sns.boxplot(y='Discount', x='Website', data=df, width=0.5, palette="colorblind", showfliers=False, ax=axes[1])
    fig.suptitle('Average price and discount for all items between websites', fontsize=16)
    ax.set(xlabel=None)
    ax1.set(xlabel=None)

#User input section --------------------------------------------------------------
def main_bar():
    print("Categories: Stick Tape, Bass, Sticks and Mallets, Snare Drum, Tom, Tenor, Cymbal, Drum Pads, timpani, keyboards")
    category = input('Enter Category: ')
    category = category.lower()
    df = pd.read_csv('attributes.csv')
    dfc = df[df['Category'] == category]
    i = 0
    subStr = "SubCategories: "
    while (i < len(dfc.index)):
        value = dfc.values[i][10]
        if value not in subStr and value != "nothing":
            subStr = subStr + value + ", "
        i = i + 1
    subStr = subStr[:-2]
    print (subStr)
    subCategory = input('Enter SubCategory: ')
    subCategory = subCategory.lower()
    dfc = dfc[dfc['SubCategory'] == subCategory]
    price_bar_plot(dfc, category, subCategory)
    plt.show()
    violinPlot(df, dfc, category, subCategory)
    plt.show()
    scatterPlot3D(df)
    plt.show()
    boxPlot(df)
    plt.show()


    itemNum = input('Enter Item Number: ')
    while itemNum != "-1":
        df1 = dfc[dfc['index']==int(itemNum)]
        try:
            print("-------------------------------------------------------")
            print("Item Number: " + str(df1.values[0][0]))
            print("Item Name: " + str(df1.values[0][4]))
            print("Item Price: " + str(df1.values[0][6]))
            print("Item Discount Amount: " + str(df1.values[0][8]))
            if "ADD TO CART" in str(df1.values[0][9]) or "Add To Cart" in str(df1.values[0][9]):
                print("Item Number " + str(df1.values[0][0]) + " is in stock")
            else:
                print("Item Number " + str(df1.values[0][0]) + " is not in stock")
            print("Item URL: " + str(df1.values[0][3]))
            print("-------------------------------------------------------")
        except:
            print("Item not found...")
            print("-------------------------------------------------------")

        itemNum = input('Enter another item number or -1 to exit: ')
    df.to_csv('attributes.csv', encoding='utf-8', index=False)
if __name__ == '__main__':
    main_bar()