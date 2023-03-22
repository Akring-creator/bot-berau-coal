from selenium import webdriver
import BerauBot.Educationconstant as const
import os
import time


class Education(webdriver.Chrome):
    def __init__(self, driver_path = 'D:\coding-lab-fast-track\selenium-bot\chromedriver.exe'):
        self.driver_path = driver_path
        os.environ['PATH'] += self.driver_path
        super(Education, self).__init__()
        self.maximize_window()
        

    def land_first_page(self):
        self.get(const.EDUCATION_BASE_URL)
    
    def input_data(self, 
                    name = None, 
                    major = None, 
                    education_level = None,
                    village = None, 
                    entry_year = None, 
                    semester = None, 
                    gpa = None,
                    desc = None,
                    university = None,
                    accreditation = None):
        selected_element = self.find_element('id', const.SCHOLARSHIP_AWARDEE_NAME_ID)
        selected_element.send_keys(name)
        time.sleep(2)
        selected_element = self.find_element('id', const.MAJOR_ID)
        selected_element.send_keys(major)
        time.sleep(2)
        selected_element = self.find_element('id', const.EDUCATION_LEVEL_ID)
        selected_element.send_keys(education_level)
        time.sleep(2)
        selected_element = self.find_element('id', const.VILLAGE_ID)
        selected_element.send_keys(village)
        time.sleep(2)
        selected_element = self.find_element('id', const.ENTY_YEAR_ID)
        selected_element.send_keys(entry_year)
        time.sleep(2)
        selected_element = self.find_element('id', const.SEMESTER_ID)
        selected_element.send_keys(semester)
        time.sleep(2)
        selected_element = self.find_element('id', const.GPA_ID)
        selected_element.send_keys(gpa)
        time.sleep(2)
        selected_element = self.find_element('id', const.DESCRIPTION_ID)
        selected_element.send_keys(desc)
        time.sleep(2)
        selected_element = self.find_element('id', const.UNIVERSITY_ID)
        selected_element.send_keys(university)
        time.sleep(2)
        selected_element = self.find_element('id', const.ACCREDITAION_ID)
        selected_element.send_keys(accreditation)
    
    def input_sex_data(self, sex = None):
        if sex == 'Perempuan':
            selected_element = self.find_element('id', const.FEMALE_SEX_ID)
            selected_element.click()
        else:
            selected_element = self.find_element('id', const.MALE_SEX_ID)
            selected_element.click()
    
    def input_site_data(self, site=None):
        if site == 'LMO':
            selected_element = self.find_element('id', const.LMO_SITE_ID)
            selected_element.click()
        elif site == 'BMO 1':
            selected_element = self.find_element('id', const.FIRST_BMO_SITE_ID)
            selected_element.click()
        elif site == 'BMO 2':
            selected_element = self.find_element('id', const.SECOND_BMO_SITE_ID)
            selected_element.click()
        elif site == 'GMO':
            selected_element = self.find_element('id', const.GMO_SITE_ID)
            selected_element.click()
        elif site == 'HO':
            selected_element = self.find_element('id', const.HO_SITE_ID)
            selected_element.click()
        elif site == 'PMO':
            selected_element = self.find_element('id', const.PMO_SITE_ID)
            selected_element.click()
        elif site == 'SMO':
            selected_element = self.find_element('id', const.SMO_SITE_ID)
            selected_element.click()
    def send_form(self):
        selected_element = self.find_element('id', const.BUTTON_ID)
        selected_element.click()

 
