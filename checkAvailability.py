#!/usr/bin/python3
'''
Checkt Verfügbarkeit von einem Produkt im Mediamarkt & Saturn Online Store (AT)
Eingabeparameter: URL des Produkts, eg: "https://www.saturn.at/de/product/_apple-macbook-pro-16"
'''

'''
und wtf warum funktioniert die/der shebang mit allen 
python pfaden die ich probiert habe nicht
'''

from bs4 import BeautifulSoup
import requests
from datetime import datetime


# TODO Ausnahmen chekcen / abfangen
def check_availability_media_saturn(URL: str):
    response = requests.get(str(URL))
    page_content = response.content
    soup = BeautifulSoup(page_content, "html.parser")
    date_today = datetime.now()

    availability = str(soup.find(property="og:availability"))
    product_name = str(soup.title).strip("<title>").strip("</title>").strip("online kaufen | MediaMark") \
        .strip("online kaufen | SATURN")

    print("Bezeichnung: ", product_name)
    if availability.find("nicht") != -1:  # add: -1 = substring nicht enthalten
        print("Produkt NICHT Verfügbar   |  Date:", date_today)  # vlt produktname nicht verfügbar printen TODO
    else:
        print("Produkt YAY Verfügbar   |  Date:", date_today)  # vlt produktname nicht verfügbar printen TODO


def check_availability_etec(URL: str):
    response = requests.get(str(URL))
    page_content = response.content
    soup = BeautifulSoup(page_content, "html.parser")
    date_today = datetime.now()

    availability = str(soup.find("span", class_="warten"))
    product_name = str(soup.title).strip("<title>").strip("</title>")

    print("Bezeichnung: ", product_name)
    if(availability.find("vorbestellen") != -1):
        print("Produkt NICHT Verfügbar   |  Date:", date_today)
    else:
        print("Produkt YAY Verfügbar   |  Date:", date_today)





# TESTING
print("-------e-tec-------")
check_availability_etec("https://www.e-tec.at/details.php?artnr=296963")

print("\n-------Mediamarkt-------")
check_availability_media_saturn(
    "https://www.mediamarkt.at/de/product/_apple-macbook-pro-16-zoll-mit-touch-bar-space-grau-mvvj2d-a-1761193.html")
print()
check_availability_media_saturn(
    "https://www.mediamarkt.at/de/product/_apple-macbook-pro-16-zoll-mit-touch-bar-silber-mvvl2d-a-1761192.html")

print("\n-------Saturn-------")
check_availability_media_saturn(
    "https://www.saturn.at/de/product/_apple-macbook-pro-16-zoll-mit-touch-bar-silber-mvvl2d-a-1761192.html")
print()
check_availability_media_saturn(
    "https://www.saturn.at/de/product/_apple-macbook-pro-16-zoll-mit-touch-bar-space-grau-mvvj2d-a-1761193.html")

