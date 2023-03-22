from selenium import webdriver
from selenium.webdriver.common.by import By
import BerauBot.ppmprogramconstant as const
import os
import time

SCHOLARSHIP_URL = 'https://survey123.arcgis.com/share/0030e89f36cb4414bf5dc294db32df92'


class Scholarship(webdriver.Chrome):
    def __init__(self, driver_path='D:\coding-lab-fast-track\selenium-bot\chromedriver.exe'):
        self.driver_path = driver_path
        os.environ['PATH'] += self.driver_path
        super(Scholarship, self).__init__()
        self.maximize_window()

    def land_first_page(self):
        self.get(SCHOLARSHIP_URL)

    def insert_data(self,
                    awardee,
                    type_of_major,
                    sex,
                    university,
                    major,
                    degree,
                    year_of_enter,
                    semester,
                    gpa,
                    desc,
                    category,
                    village,
                    coordinate,
                    site,
                    kampung):
        # nama-penerima
        selected_element = self.find_element(
            By.ID, 'idp4166432')
        selected_element.send_keys(awardee)

        # tahun BEASISWA
        selected_element = self.find_element(
            By.ID, 'idp4167440')
        selected_element.send_keys('2022')
        time.sleep(4)

        # sex
        selected_element = self.find_element(
            By.XPATH, f'//span[text()="{sex}"]')
        selected_element.click()

        # university
        selected_element = self.find_element(
            By.ID, 'idp4131360')
        selected_element.send_keys(university)
        time.sleep(1)

        # major
        selected_element = self.find_element(
            By.ID, 'idp4132368')
        selected_element.send_keys(major)

        # degree
        selected_element = self.find_element(
            By.ID, 'idp4133376')
        selected_element.send_keys(degree)

        # tahun mulai
        selected_element = self.find_element(
            By.XPATH, f'//span[text()="{year_of_enter}"]')
        selected_element.click()

        # semeter
        selected_element = self.find_element(
            By.ID, 'idp3953728')
        selected_element.send_keys(str(semester))

        # gpa
        selected_element = self.find_element(
            By.ID, 'idp3954736')
        selected_element.send_keys(str(gpa))

        # # desc
        # selected_element = self.find_element(
        #     By.ID, 'idp46745792')
        # selected_element.send_keys(desc)

        # type of major
        selected_element = self.find_element(
            By.ID, 'idp3885744')
        selected_element.send_keys(type_of_major)

        # category
        selected_element = self.find_element(
            By.XPATH, f'//span[text()="{category}"]')
        selected_element.click()

        # site
        selected_element = self.find_element(
            By.XPATH, f'//span[text()="{site}"]')
        selected_element.click()

        # Kampung
        selected_element = self.find_element(
            By.CLASS_NAME, 'selected')
        selected_element.click()

        selected_element = self.find_element(
            By.XPATH, f'//span[text()="{village}"]')
        selected_element.click()

        if village == 'Lainnya':
            selected_element = self.find_element(
                By.ID, 'idp2268400')
            selected_element.send_keys(kampung)

        time.sleep(5)

        # map
        selected_element = self.find_element(
            By.CLASS_NAME, 'esri-search__input')
        selected_element.send_keys(coordinate)

        selected_element = self.find_element(
            By.CLASS_NAME, const.MAP_SEARCH_CLASS)
        selected_element.click()
        time.sleep(5)
        # button

        selected_element = self.find_element(
            By.ID, 'validate-form')
        selected_element.click()
