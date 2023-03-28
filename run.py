from BerauBot.Botclass import Jobcenter, Ppmprogram, Scholarship, Umkm, Asrama, PaketPendidikan, TradingGabah, SekolahGSM, WTP
import time
import pandas as pd
import numpy as np
import math

PATH_TO_SCHOLARSHIP_FILE = 'D:\coding-lab-fast-track\Bot\excel\Beasiswa.xlsx'
PATH_TO_PPM_FILE = 'D:\coding-lab-fast-track\Bot\excel\Realisasi Program PPM 2022.xlsx'
PATH_TO_JOB_CENTER_FILE = r'D:\coding-lab-fast-track\Bot\excel\UPDATE PESERTA JOB CENTRE PPKP.xlsx'
PATH_TO_UMKM_FILE = 'D:\coding-lab-fast-track\Bot\excel\Penerima manfaat umkm.xlsx'
PATH_TO_REKAP_ASRAMA_FILE = r'D:\coding-lab-fast-track\Bot\excel\REKAP ASRAM KAT.xlsx'
PATH_TO_PAKET_FILE = r'D:\coding-lab-fast-track\Bot\excel\REKAP KEJAR PAKET C.xlsx'
PATH_TO_TRADING_GABAH = r'D:\coding-lab-fast-track\Bot\excel\Penerima Manfaat Trading Gabah.xlsx'
PATH_TO_sEKOLAH_GSM = r'D:\coding-lab-fast-track\Bot\excel\SEKOLAH GSM.xlsx'
PATH_TO_WTP = r'D:\coding-lab-fast-track\Bot\excel\WTP.xlsx'
def cleaningFile(file):
    df = pd.read_excel(file)
    df = df.replace(np.nan, '')
    # df = df.astype(str)
    return df
def cleaningForScholarshipfILE(file=PATH_TO_SCHOLARSHIP_FILE):
    df = pd.read_excel(file)
    df['Semester'] = df['Semester'].replace(
        np.nan, 9999).astype(str).map(lambda x: x.rstrip('.0')).replace('9999', '')
    df['Angkatan'] = df['Angkatan'].astype(str)
    df = df.replace(np.nan, '')

    return df
def umkmBot():
    with Umkm() as bot:
        file = cleaningFile(PATH_TO_UMKM_FILE)

        for ind in range(85, len(file)):
            bot.land_first_page()
            time.sleep(10)
            bot.insert_data(
                pilarprogram=file['Pilar Program'][ind],
                tahunprogram=file['Tahun Program'][ind],
                subprogram=file['Sub Program'][ind],
                namakelompok=file['Nama Kelompok'][ind],
                namaketua=file['Nama Ketua / Penanggung Jawab'][ind],
                jenisekraf=file['Jenis Ekraf'][ind],
                hasil=file['Hasil Olahan'][ind],
                coordinate=file['Lainnya'][ind],
                village=file['nama'][ind],
                kampung=file['Kampung'][ind],
                site=file['Site'][ind]
            )
            time.sleep(10)
            print(f'Good Data {ind+1}')
            # Good Data 7
def ppmBot():
    with Ppmprogram() as bot:
        file = cleaningFile(PATH_TO_PPM_FILE)
        for ind in range(116, len(file) + 1):
            bot.land_first_page()
            time.sleep(10)
            bot.insert_data(
                nama=file['nama'][ind],
                pilar_program=file['Pilar Program'][ind],
                desc=file['Keterangan'][ind],
                tot_benef=file['Penerima Manfaat'][ind],
                program=file['Program'][ind],
                lokasi=file['Lokasi Site'][ind],
                sub_program=file['Sub Program'][ind],
                coordinate=file['Koordinat'][ind],
                tahun_program=str(file['Tahun Program'][ind])
            )
            time.sleep(10)
            print(f'Good Data {ind+1}')
def scholarshipBot():
    with Scholarship() as bot:
        file = cleaningForScholarshipfILE(PATH_TO_SCHOLARSHIP_FILE)

        for ind in range(269, len(file)):
            bot.land_first_page()
            time.sleep(15)
            bot.insert_data(
                awardee=file['Nama Penerima Beasiswa'][ind],
                type_of_major=file['Kategori Penjurusan'][ind],
                sex=file['Jenis Kelamin'][ind],
                university=file['Perguruan Tinggi/Universitas'][ind],
                major=file['Jurusan'][ind],
                degree=file['Jenjang Pendidikan'][ind],
                year_of_enter=file['Angkatan'][ind],
                semester=file['Semester'][ind],
                gpa=file['IP'][ind],
                desc=file['Keterangan Status'][ind],
                category=file['Kategori'][ind],
                village=file['nama'][ind],
                coordinate=file['coordinate'][ind],
                site=file['Lokasi Site'][ind],
                kampung=file['Kampung'][ind]
            )
            time.sleep(10)
            print(f'Good Data {ind+1}')
            # Good Data 7
def jobCenterBot():

    with Jobcenter() as bot:
        file = cleaningFile(PATH_TO_JOB_CENTER_FILE)
        for ind in range(1440, len(file)):
            bot.land_first_page()
            time.sleep(15)
            bot.insert_data(
                company=file['Nama Perusahaan'][ind],
                sid=file['Kode SID'][ind],
                name=file['Nama'][ind],
                kmpd=file['KMPD'][ind],
                softskill=file['Soft Skill'][ind],
                desc=file['Keterangan'][ind]
            )
            bot.input_data()
            time.sleep(5)
            bot.check_result()
            print(f'Insert Data Number {ind + 1} Success')
def dormiBot():
    with Asrama() as bot:
        file = cleaningFile(PATH_TO_REKAP_ASRAMA_FILE)
        for ind in range(0, len(file)):
            bot.land_first_page()
            time.sleep(10)
            bot.insert_data(
                name=file['NAMA'][ind],
                school=file['SEKOLAH'][ind],
                village=file['ASAL KAMPUNG'][ind],
                coordinate=file['Koordinat'][ind],
                dormitory=file['Asrama'][ind]
            )
            bot.input_data()
            time.sleep(5)
            print(f'Insert Data Number {ind + 1} Success')
def paketBot():
    with PaketPendidikan() as bot:
        file = cleaningFile(PATH_TO_PAKET_FILE)
        for ind in range(0, len(file)):
            bot.land_first_page()
            time.sleep(10)
            bot.insert_data(
                name=file['Nama'][ind],
                village=file['Kampung'][ind],
                coordinate=file['Koordinat'][ind],
                paket=file['Kejar Paket'][ind]
            )
            bot.input_data()
            time.sleep(5)
            print(f'Insert Data Number {ind + 1} Success')
def tradingGabah():

    with TradingGabah() as bot:
        file = cleaningFile(PATH_TO_TRADING_GABAH)
        for ind in range(0, len(file)):
            bot.land_first_page()
            time.sleep(10)
            bot.insert_data(
                name=file['Nama'][ind],
                village=file['Kampung'][ind],
                coordinate=file['Koordinat'][ind],
                reason=file['Alasan'][ind],
                area=file['Luas Lahan'][ind],
            )
            bot.input_data()
            time.sleep(5)
            print(f'Insert Data Number {ind + 1} Success')
def sekolahGSM():

    with SekolahGSM() as bot:
        file = cleaningFile(PATH_TO_sEKOLAH_GSM)
        for ind in range(0, len(file)):
            bot.land_first_page()
            time.sleep(10)
            bot.insert_data(
                school=file['Sekolah'][ind],
                village=file['Kampung'][ind],
                pns=file['PNS'][ind],
                ptt=file['PTT'][ind],
                teacher_total=file['Total Guru'][ind],
                student_total=file['Total Siswa'][ind]
            )
            bot.input_data()
            time.sleep(5)
            print(f'Insert Data Number {ind + 1} Success')
def wtp():
    with WTP() as bot:
        file = cleaningFile(PATH_TO_WTP)
        for ind in range(392, len(file)):
            bot.land_first_page()
            time.sleep(10)
            bot.insert_data(
                name=file['Nama'][ind],
                village=file['Kampung'][ind],
                coordinate=file['Koordinat'][ind]
            )
            bot.input_data()
            time.sleep(5)
            print(f'Insert Data Number {ind + 1} Success')
wtp()
