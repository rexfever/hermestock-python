# -*- coding: utf-8 -*-
import calc_rank as cr
import downloader as dl
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.select import Select
from datetime import datetime
import os, glob, getpass
import requests

DRIVER = webdriver.Chrome('./chromedriver')
FILEPATH = cr.filePath
# 시장, 매수주체 선언

DATA_SOURCE = [['4', '7050'], ['4', '9000'], ['6', '7050'], ['6', '9000']]

KOSPI_fileList = ['data_0.csv', 'data_1.csv']
KOSDAQ_fileList = ['data_2.csv', 'data_3.csv']

CHANNEL_LIST = cr.read_channels('dev') #live or dev
date = cr.read_date('dev')

try:

    dl.set_date(date)
    while cr.count_file() < 4:
        sleep(10)
        if cr.count_file() == 0:
            print("file", cr.count_file())
            dl.select_market(DATA_SOURCE[0])
            print(DATA_SOURCE[0])
        elif cr.count_file() == 1:
            print("file", cr.count_file())
            dl.select_market(DATA_SOURCE[1])
            print(DATA_SOURCE[1])
        elif cr.count_file() == 2:
            print("file", cr.count_file())
            dl.select_market(DATA_SOURCE[2])
            print(DATA_SOURCE[2])
        elif cr.count_file() == 3:
            print("file", cr.count_file())
            dl.select_market(DATA_SOURCE[3])
            print(DATA_SOURCE[3])
        else:
            print("file", cr.count_file())
            continue
    cr.rename_file()
    rank_1 = cr.merge_data_set(
        cr.extract_data_set(KOSPI_fileList[0]), cr.extract_data_set(KOSPI_fileList[1]), CHANNEL_LIST
    )
    print(rank_1)
    rank_2 = cr.merge_data_set(
        cr.extract_data_set(KOSDAQ_fileList[0]), cr.extract_data_set(KOSDAQ_fileList[1]), CHANNEL_LIST
    )
    print(rank_2)


finally:
    dl.close_window()
    [os.remove(f) for f in glob.glob("/Users/"+getpass.getuser()+"/Downloads/*.csv")]

