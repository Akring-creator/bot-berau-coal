from selenium import webdriver
from selenium.webdriver.common.by import By
import BerauBot.ppmprogramconstant as const
import os
import time

BASE_URL = 'https://survey123.arcgis.com/share/eba1e09d58ac4e239d6d1477dcdb5f26'


class Umkm(webdriver.Chrome):
    def __init__(self, driver_path='D:\coding-lab-fast-track\selenium-bot\chromedriver.exe'):
        self.driver_path = driver_path
        os.environ['PATH'] += self.driver_path
        super(Umkm, self).__init__()

    def land_first_page(self):
        self.get(BASE_URL)

    def insert_data(self,
                    pilarprogram,
                    tahunprogram,
                    subprogram,
                    namakelompok,
                    namaketua,
                    jenisekraf,
                    hasil,
                    coordinate,
                    village,
                    kampung,
                    site):

        # Pilar Program
        selected_element = self.find_element(
            By.XPATH, f'//span[text()="{pilarprogram}"]')
        selected_element.click()

        # Sub Program
        selected_element = self.find_element(
            By.ID, 'idp47441104')
        selected_element.send_keys(subprogram)

        # Tahun Program
        selected_element = self.find_element(
            By.XPATH, f'//span[text()="{tahunprogram}"]')
        selected_element.click()

        # Nama Kelompok
        selected_element = self.find_element(
            By.ID, 'idp47421200')
        selected_element.send_keys(namakelompok)

        # Nama Ketua
        selected_element = self.find_element(
            By.ID, 'idp47303488')
        selected_element.send_keys(namaketua)

        # Jenis Ekraf
        selected_element = self.find_element(
            By.ID, 'idp47304496')
        selected_element.send_keys(jenisekraf)

        # Hasil Ekraf
        selected_element = self.find_element(
            By.ID, 'idp47305504')
        selected_element.send_keys(hasil)

        time.sleep(5)
        # map
        selected_element = self.find_element(
            By.CLASS_NAME, 'esri-search__input')
        selected_element.send_keys(coordinate)

        selected_element = self.find_element(
            By.CLASS_NAME, const.MAP_SEARCH_CLASS)
        selected_element.click()
        time.sleep(7)

        # Kampung
        selected_element = self.find_element(
            By.CLASS_NAME, 'selected')
        selected_element.click()

        selected_element = self.find_element(
            By.XPATH, f'//span[text()="{village}"]')
        selected_element.click()

        time.sleep(2)
        if village == 'Lainnya':
            selected_element = self.find_element(
                By.ID, 'idp45847040')
            selected_element.send_keys(kampung)

        # site
        selected_element = self.find_element(
            By.XPATH, f'//span[text()="{site}"]')
        selected_element.click()

        # button
        selected_element = self.find_element(
            By.ID, 'validate-form')
        selected_element.click()
