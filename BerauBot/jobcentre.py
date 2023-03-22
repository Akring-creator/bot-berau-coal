from selenium import webdriver
from selenium.webdriver.common.by import By
import BerauBot.ppmprogramconstant as const
import os
import time

BASE_URL = 'https://survey123.arcgis.com/share/0ddf8a3866634dcba8d005bab6499101'

#


class Jobcenter(webdriver.Chrome):
    def __init__(self, driver_path='D:\coding-lab-fast-track\Bot\chromedriver.exe'):
        self.driver_path = driver_path
        os.environ['PATH'] += self.driver_path
        super(Jobcenter, self).__init__()
        # self.maximize_window()

    def land_first_page(self):
        self.get(BASE_URL)

    def insert_data(self,
                    company,
                    sid,
                    name,
                    kmpd,
                    softskill,
                    desc):

        # Softskill
        selected_element = self.find_element(
            By.ID, 'idp48211024')
        selected_element.send_keys(softskill)

        # KMPD
        selected_element = self.find_element(
            By.ID, 'idp49049312')
        selected_element.send_keys(kmpd)

        # Company
        selected_element = self.find_element(
            By.ID, 'idp46313984')
        selected_element.send_keys(company)

        # SID
        selected_element = self.find_element(
            By.ID, 'idp46315136')
        selected_element.send_keys(sid)

        # Nama
        selected_element = self.find_element(
            By.ID, 'idp49048304')
        selected_element.send_keys(name)

        # Keterangan
        selected_element = self.find_element(
            By.XPATH, f'//span[text()="{desc}"]')
        selected_element.click()

    def input_data(self):
        # Button
        selected_element = self.find_element(
            By.CLASS_NAME, 'submit-container')
        selected_element.click()
        time.sleep(5)

    def check_result(self):
        check_element = self.find_element(
            By.XPATH, f'//strong[text()="Terima kasih."]'
        )
