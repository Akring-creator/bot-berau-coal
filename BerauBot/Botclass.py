from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

JOB_CENTER_BASE_URL = 'https://survey123.arcgis.com/share/0ddf8a3866634dcba8d005bab6499101'
SCHOLARSHIP_BASE_URL = 'https://survey123.arcgis.com/share/0030e89f36cb4414bf5dc294db32df92'
PILAR_PROGRAM_BASE_URL = 'https://survey123.arcgis.com/share/eba1e09d58ac4e239d6d1477dcdb5f26'
REKAP_ASRAMA_BASE_URL = 'https://survey123.arcgis.com/share/3dbe71845e364cfd927cc4e13d944ce5'
PAKET_PENDIDIKAN_BASE_URL = 'https://survey123.arcgis.com/share/adcc1c4fe68544bb99abdb42d5201258'
TRADING_GABAH_BASE_URL = 'https://survey123.arcgis.com/share/9a343ea791064be6a52bd7e440756d9e'
SEKOLAH_GSM_BASE_URL = 'https://survey123.arcgis.com/share/075efe17f4124b02b1af4fb1748d70b8'
WTP_BASE_URL = 'https://survey123.arcgis.com/share/b27d243e7fc14f38ac737ce728e08131'

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
class Umkm(webdriver.Chrome):
    def __init__(self, driver_path='D:\coding-lab-fast-track\selenium-bot\chromedriver.exe'):
        self.driver_path = driver_path
        os.environ['PATH'] += self.driver_path
        super(Umkm, self).__init__()

    def land_first_page(self):
        self.get(PILAR_PROGRAM_BASE_URL)

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
class Asrama(webdriver.Chrome):
    def __init__(self, driver_path='D:\coding-lab-fast-track\selenium-bot\chromedriver.exe'):
        self.driver_path = driver_path
        os.environ['PATH'] += self.driver_path
        super(Asrama, self).__init__()

    def land_first_page(self):
        self.get(REKAP_ASRAMA_BASE_URL)
    
    def insert_data(self, name, school, village, coordinate, dormitory):
        # Name
        selected_element = self.find_element(
            By.ID, 'idp1648112')
        selected_element.send_keys(name)

        # School
        selected_element = self.find_element(
            By.ID, 'idp1555696')
        selected_element.send_keys(school)

        # Village
        selected_element = self.find_element(
            By.ID, 'idp1556704')
        selected_element.send_keys(village)

        # Dormitory
        selected_element = self.find_element(
            By.XPATH, f'//span[text()="{dormitory}"]')
        selected_element.click()

        # Map
        selected_element = self.find_element(
            By.CLASS_NAME, 'esri-search__input')
        selected_element.send_keys(coordinate)

        selected_element = self.find_element(
            By.CLASS_NAME, 'esri-search__submit-button')
        selected_element.click()
        time.sleep(3)
        
        # Submit
    def input_data(self): 
        selected_element = self.find_element(
            By.ID, 'validate-form')
        selected_element.click()
class PaketPendidikan(webdriver.Chrome):
    def __init__(self, driver_path='D:\coding-lab-fast-track\selenium-bot\chromedriver.exe'):
        self.driver_path = driver_path
        os.environ['PATH'] += self.driver_path
        super(PaketPendidikan, self).__init__()

    def land_first_page(self):
        self.get(PAKET_PENDIDIKAN_BASE_URL)
    
    def insert_data(self, name, village, coordinate, paket):
        # Name
        selected_element = self.find_element(
            By.ID, 'idp42618816')
        selected_element.send_keys(name)

        # Village
        selected_element = self.find_element(
            By.ID, 'idp44047456')
        selected_element.send_keys(village)

        # Dormitory
        selected_element = self.find_element(
            By.ID, 'idp44039120')
        selected_element.send_keys(paket)

        # Map
        selected_element = self.find_element(
            By.CLASS_NAME, 'esri-search__input')
        selected_element.send_keys(coordinate)

        selected_element = self.find_element(
            By.CLASS_NAME, 'esri-search__submit-button')
        selected_element.click()
        time.sleep(3)
        
        # Submit
    def input_data(self): 
        selected_element = self.find_element(
            By.ID, 'validate-form')
        selected_element.click()
class TradingGabah(webdriver.Chrome):
    def __init__(self, driver_path='D:\coding-lab-fast-track\selenium-bot\chromedriver.exe'):
        self.driver_path = driver_path
        os.environ['PATH'] += self.driver_path
        super(TradingGabah, self).__init__()

    def land_first_page(self):
        self.get(TRADING_GABAH_BASE_URL)
    
    def insert_data(self, name, village, coordinate, reason, area):
        # Name
        selected_element = self.find_element(
            By.ID, 'idp48880592')
        selected_element.send_keys(name)

        # Village
        selected_element = self.find_element(
            By.ID, 'idp45764976')
        selected_element.send_keys(village)

        # Reason
        selected_element = self.find_element(
            By.ID, 'idp46746848')
        selected_element.send_keys(reason)

        # Map
        selected_element = self.find_element(
            By.CLASS_NAME, 'esri-search__input')
        selected_element.send_keys(coordinate)

        selected_element = self.find_element(
            By.CLASS_NAME, 'esri-search__submit-button')
        selected_element.click()
        time.sleep(3)
        
        # Reason
        selected_element = self.find_element(
            By.ID, 'idp47963520')
        selected_element.send_keys(area)

        # Submit
    def input_data(self): 
        selected_element = self.find_element(
            By.ID, 'validate-form')
        selected_element.click()
class SekolahGSM(webdriver.Chrome):
    def __init__(self, driver_path='D:\coding-lab-fast-track\selenium-bot\chromedriver.exe'):
        self.driver_path = driver_path
        os.environ['PATH'] += self.driver_path
        super(SekolahGSM, self).__init__()

    def land_first_page(self):
        self.get(SEKOLAH_GSM_BASE_URL)
    
    def insert_data(self, school, village, pns, ptt, teacher_total, student_total):
        # School
        selected_element = self.find_element(
            By.ID, 'idp1535072')
        selected_element.send_keys(school)

        # Village
        selected_element = self.find_element(
            By.ID, 'idp1536080')
        selected_element.send_keys(village)

        # PNS
        selected_element = self.find_element(
            By.ID, 'idp1537520')
        selected_element.send_keys(pns)

        # PTT
        selected_element = self.find_element(
            By.ID, 'idp1215008')
        selected_element.send_keys(ptt)

        # Teacher Total
        selected_element = self.find_element(
            By.ID, 'idp1216448')
        selected_element.send_keys(teacher_total)

        # Student Total
        selected_element = self.find_element(
            By.ID, 'idp1217456')
        selected_element.send_keys(student_total)

        # Submit
    def input_data(self): 
        selected_element = self.find_element(
            By.ID, 'validate-form')
        selected_element.click()
class WTP(webdriver.Chrome):
    def __init__(self, driver_path='D:\coding-lab-fast-track\selenium-bot\chromedriver.exe'):
        self.driver_path = driver_path
        os.environ['PATH'] += self.driver_path
        super(WTP, self).__init__()

    def land_first_page(self):
        self.get(WTP_BASE_URL)
    
    def insert_data(self, name, village, coordinate):
        # Name
        selected_element = self.find_element(
            By.ID, 'idp45807520')
        selected_element.send_keys(name)

        # Village
        selected_element = self.find_element(
            By.ID, 'idp46712032')
        selected_element.send_keys(village)

        time.sleep(5)
        # Map
        selected_element = self.find_element(
            By.CLASS_NAME, 'esri-search__input')
        selected_element.send_keys(coordinate)

        selected_element = self.find_element(
            By.CLASS_NAME, 'esri-search__submit-button')
        selected_element.click()
        time.sleep(3)
        
        # Submit
    def input_data(self): 
        selected_element = self.find_element(
            By.ID, 'validate-form')
        selected_element.click()



    
    
