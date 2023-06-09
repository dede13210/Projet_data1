import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import csv
from Station import Station


def create_station(nom, lien):
    driver.get(lien)
    time.sleep(1)
    try:
        neige_haut = driver.find_element(By.CSS_SELECTOR, selector_neige_haut)
        neige_tomber = driver.find_element(By.CSS_SELECTOR, selector_neige_tomber)
        objet = Station(nom, lien, neige_haut.text, neige_tomber.text)
        return objet
    except Exception:
        print("la staion", nom, "est fermé")


if __name__ == '__main__':

    selector_neige_haut = '#__next > div.container > div.styles_layout__2aTIJ.layout_layoutContainer__27fok.pt-3 > ' \
                          'div > article:nth-child(2) > div > div.styles_box__3xo2X > div.styles_info__3F7Vv > div > ' \
                          'div:nth-child(2) > figure > div:nth-child(2) > figcaption'
    selector_neige_tomber = '#__next > div.container > div.styles_layout__2aTIJ.layout_layoutContainer__27fok.pt-3 > ' \
                            'div > article:nth-child(2) > div > div.styles_box__3xo2X > div.styles_status__Ot_mR > ' \
                            'div:nth-child(1) > div.styles_cols__3MSRH > div:nth-child(1) > span.h4.styles_h4__2Uc5w'

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(3)
    list_element = []
    dict_station = {}
    driver.get("https://www.skiinfo.fr/alpes-du-nord/bulletin-neige")
    elements = driver.find_elements(By.CLASS_NAME, 'styles_row__1tbcd')
    for element in elements:
        tag_a = element.find_element(By.TAG_NAME, 'a')
        link = tag_a.get_attribute('href')
        name = tag_a.find_element(By.TAG_NAME, 'span')
        dict_station[name.text] = link

    list_Station = []
    for key, value in dict_station.items():
        list_Station.append(create_station(key, value))

    driver.quit()
    list_csv = []
    list_Station.remove(None)
    for station in list_Station:
        try:
            station.analyse_station()
            list_csv.append(station.list())
        except:
            print("none type exception")
    with open('enneigement.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(list_csv)
