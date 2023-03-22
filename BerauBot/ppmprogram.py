from selenium import webdriver
from selenium.webdriver.common.by import By
import BerauBot.ppmprogramconstant as const
import os
import time


class Ppmprogram(webdriver.Chrome):
    def __init__(self, driver_path='D:\coding-lab-fast-track\selenium-bot\chromedriver.exe'):
        self.driver_path = driver_path
        os.environ['PATH'] += self.driver_path
        super(Ppmprogram, self).__init__()
        self.maximize_window()

    def land_first_page(self):
        self.get(const.PPMPROGRAM_BASE_URL)

    def insert_data(self,
                    pilar_program,
                    tahun_program,
                    nama,
                    sub_program,
                    program,
                    coordinate,
                    tot_benef,
                    desc,
                    lokasi):

        # Kampung
        selected_element = self.find_element(
            By.CLASS_NAME, 'selected')
        selected_element.click()

        selected_element = self.find_element(
            By.XPATH, f'//span[text()="{nama}"]')
        selected_element.click()

        time.sleep(5)

        # site
        selected_element = self.find_element(
            By.XPATH, f'//span[text()="{lokasi}"]')
        selected_element.click()
        time.sleep(5)

        # # keterangan
        # selected_element = self.find_element(
        #     By.ID, 'idp46982928')
        # selected_element.send_keys(desc)
        # time.sleep(5)

        # Total Beneficieris
        if tot_benef == '':
            tot_benef = ''
        else:
            tot_benef = int(tot_benef)
        selected_element = self.find_element(
            By.ID, 'idp46981920')
        selected_element.send_keys(tot_benef)
        time.sleep(1)

        # sub_program
        selected_element = self.find_element(
            By.ID, 'idp47950944')
        selected_element.send_keys(sub_program)
        time.sleep(1)

        # program
        selected_element = self.find_element(
            By.ID, 'idp47951952')
        selected_element.send_keys(program)
        time.sleep(5)

        #
        selected_element = self.find_element(
            By.XPATH, f'//span[text()="{pilar_program}"]')
        selected_element.click()

        selected_element = self.find_element(
            By.XPATH, f'//span[text()="{tahun_program}"]')
        selected_element.click()

        time.sleep(5)
        # map
        selected_element = self.find_element(
            By.CLASS_NAME, 'esri-search__input')
        selected_element.send_keys(coordinate)

        selected_element = self.find_element(
            By.CLASS_NAME, const.MAP_SEARCH_CLASS)
        selected_element.click()
        time.sleep(7)
        # button
        selected_element = self.find_element(
            By.ID, 'validate-form')
        selected_element.click()
