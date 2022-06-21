import re

import requests
from bs4 import BeautifulSoup

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0"}
# might combine all methods into dynamic one


def AllSearch(sv):
    """Searches In Every Website and organizes the result in dictionary"""
    dic = {"Ivory": IvoryPrice(sv), "Bug": BugPrice(sv), "shop5": Shop5Price(sv), "SpeedComputers": SpeedComputersPrice(sv), "Zol4u": ZoluPrice(sv), "PcCenter": PcCenterPrice(sv), "gamestorm": GameStormPrice(sv), "AAComputers": AAComputersPrice(sv)}
    return dic


def BugPrice(sv):
    """Gets The Price in Bug"""
    try:
        purl = "https://www.bug.co.il/search?q="+sv#+"&key=&orderby=cte"
        page = requests.get(url=purl, headers=headers)
        soup = BeautifulSoup(page.content, 'lxml')
        price = soup.find('div', class_='price')
    # print(soup.prettify())
    # print(price)
        if price is not None:
            price = price.get_text()
            price = price.strip()
            price = re.sub("\D", "", price)
            print(price)
            return price+"₪", purl
        else:
            return "No Results", "#NoResults"
            print("NONE")
    except:
        return "No Results(Error)", "#Error"


def Shop5Price(sv):
    """Gets The Price in Shop5"""
    try:
        purl = "https://www.shop5.co.il/on/demandware.store/Sites-topfive-Site/iw_IL/Search-Show?q="+sv
        page = requests.get(url=purl, headers=headers)
        soup = BeautifulSoup(page.content, 'lxml')
        price = soup.find('span', class_='value')
        # print(soup.prettify())
        # print(price)
        if price is not None:
            price = price.get_text()
            price = price.strip()
            price = re.sub("\D", "", price)
            print(price)
            return price+"₪", purl
        else:
            return "No Results", "#NoResults"
            print("NONE")
    except:
        return "No Results(Error)", "#Error"


def SpeedComputersPrice(sv):
    """Gets The Price in SpeedComputers"""
    try:
        purl = "https://www.speed4u.co.il/items.asp?Qsearch="+sv
        page = requests.get(url=purl, headers=headers)
        soup = BeautifulSoup(page.content, 'lxml')
        price = soup.find('span', class_='priceholder')
    #print(soup.prettify())
    #print(price)
        if price is not None:
            price = price.get_text()
            price = price.strip()
            price = re.sub("\D", "", price)
            print(price)
            return price+"₪", purl
        else:
            return "No Results", "#NoResults"
            print("NONE")
    except:
        return "No Results(Error)", "#Error"


def ZoluPrice(sv):
    """Gets The Price in Zolu"""
    try:
        purl = "https://www.zol4u.co.il/search/?q=" + sv
        page = requests.get(url=purl, headers=headers)
        soup = BeautifulSoup(page.content, 'lxml')
        price = soup.find('span', class_='price center-price-in-grid text-right')
        #print(soup.prettify())
        # print(price)
        if price is not None:
            price = price.get_text()
            price = price.strip()
            price = re.sub("\D", "", price)
            print(price)
            return price+"₪", purl
        else:
            return "No Results", "#NoResults"
            print("NONE")
    except:
        return "No Results(Error)", "#Error"


def PcCenterPrice(sv):
    """Gets The Price in PcCenter"""
    try:
        purl = "https://www.pccenter.co.il/items.asp?IsPostback=true&Qsearch="+sv
        page = requests.get(url=purl, headers=headers)
        soup = BeautifulSoup(page.content, 'lxml')
        price = soup.find('div', issameitem='0')
#    print(soup.prettify())
    #print(price)

        if price is not None:
            price = price.find('span', class_='priceholder')
            price = price.get_text()
            price = price.strip()
            price = re.sub("\D", "", price)
            print(price)
            return price+"₪", purl
        else:
            return "No Results", "#NoResults"
            print("NONE")
    except:
        return "No Results(Error)", "#Error"


def GameStormPrice(sv):
    """Gets The Price in Gamestorm"""
    try:
        purl = "https://www.gamestorm.co.il/search/" + sv
        page = requests.get(url=purl, headers=headers)
        soup = BeautifulSoup(page.content, 'lxml')
        price = soup.find('div', class_='price_current')
    #    print(soup.prettify())
    # print(price)

        if price is not None:
            price = price.get_text()
            price = price.strip()
            price = re.sub("\D", "", price)
            print(price)
            return price+"₪", purl
        else:
            return "No Results", "#NoResults"
            print("NONE")
    except:
        return "No Results(Error)", "#Error"


def AAComputersPrice(sv):
    """Gets The Price in AAComputers"""
    try:
        purl = "https://1pc.co.il/search.aspx?keyword="+sv
        page = requests.get(url=purl, headers=headers)
        soup = BeautifulSoup(page.content, 'lxml')

    #print(soup.prettify())
        price = soup.find('div', class_='pr')
        if price is not None:
            price = price.get_text()
            price = price.strip()
            price = re.sub("\D", "", price)
            print(price)
            return price + "₪", purl
        else:
            return "No Results", "#NoResults"
            print("NONE")
    except:
        return "No Results(Error)", "#Error"



def IvoryPrice(sv):
    """Gets The Price in Ivory"""
    try:
        purl = "https://www.ivory.co.il/catalog.php?act=cat&q="+sv
        page = requests.get(url=purl, headers=headers)
        soup = BeautifulSoup(page.content, 'lxml')
    #print(soup.prettify())
        price = soup.find('span', class_='price')
        if price is not None:
            price = price.get_text()
            price = price.strip()
            price = re.sub("\D", "", price)
            print(price)
            return price+"₪", purl
        else:
            return "No Results", "#NoResults"
            print("NONE")
    except:
        return "No Results(Error)", "#Error"
