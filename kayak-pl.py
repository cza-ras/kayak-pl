#skrypt dostosowany do wyszukiwania dla zadanego miesiąca i długości pobytu

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import date
import datetime

#helper formatujacy dane tekstowe na liczby
def formatuj(tekst):
    liczba = tekst.replace('zł','')
    liczba = liczba.replace(' ','')
    return liczba

#dane lotu
trasa = "WAW-LIM"
wylot = date(2024,11,21)
powrot = wylot + datetime.timedelta(days=30)
dlugosc_pobytu = "14"
regula = 4000

#glowny url
url = f"https://www.kayak.pl/flights/{trasa}/{wylot.strftime('%Y-%m-%d')}/{powrot.strftime('%Y-%m-%d')}-flexible-calendar-{dlugosc_pobytu}?sort=bestflight_a&fs=stops=1"

#init przegladarki i otwarcie strony
#praca na Safari -> wymagne ustawienie Safari "allow remote automation" 
options = webdriver.SafariOptions()
options.add_argument("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4.1 Safari/605.1.15")
cookie = {'name': '_tt_enable_cookie', 'value': '1'}

driver =  webdriver.Safari(options=options)
driver.add_cookie(cookie)
driver.get(url)

#selektory CSS do pobrania
cena = "hYzH-price"

#pauza i popranie wynikow
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, cena))
    )
finally:
    _najtansze = driver.find_element(By.CLASS_NAME,cena)

    print(f"Najtanszy lot w cenie {formatuj(_najtansze.text)} na trasie {trasa} w okresie od {wylot} do {powrot}")