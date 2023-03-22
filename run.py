from BerauBot.umkm import Umkm
from BerauBot.ppmprogram import Ppmprogram
from BerauBot.scholarship import Scholarship
from BerauBot.jobcentre import Jobcenter
import time
import pandas as pd
import numpy as np
import math

PATH_TO_SCHOLARSHIP_FILE = 'D:\coding-lab-fast-track\Bot\excel\Beasiswa.xlsx'
PATH_TO_PPM_FILE = 'D:\coding-lab-fast-track\Bot\excel\Realisasi Program PPM 2022.xlsx'
PATH_TO_JOB_CENTER_FILE = r'D:\coding-lab-fast-track\Bot\excel\UPDATE PESERTA JOB CENTRE PPKP.xlsx'
PATH_TO_UMKM_FILE = 'D:\coding-lab-fast-track\Bot\excel\Penerima manfaat umkm.xlsx'


def cleaningFile(file):
    df = pd.read_excel(file)
    df = df.replace(np.nan, '')
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


jobCenterBot()
