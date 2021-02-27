# -*- coding: utf-8 -*-
import getpass
import glob
import os
from time import sleep

import calc_rank as cr
import downloader as dl
import send_msg as sm

DATA_SOURCE = [['4', '7050'], ['4', '9000'], ['6', '7050'], ['6', '9000']]
KOSPI_fileList = ['data_0.csv', 'data_1.csv']
KOSDAQ_fileList = ['data_2.csv', 'data_3.csv']

CHANNEL_LIST = cr.read_channels('live') #live or dev
date = cr.read_date('live')


def job():
    try:
        dl.set_date(date)
        while cr.count_file() < 4:
            sleep(10)
            if cr.count_file() == 0:
                dl.select_market(DATA_SOURCE[0])
            elif cr.count_file() == 1:
                dl.select_market(DATA_SOURCE[1])
            elif cr.count_file() == 2:
                dl.select_market(DATA_SOURCE[2])
            elif cr.count_file() == 3:
                dl.select_market(DATA_SOURCE[3])
            else:
                continue

        sleep(1)
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
        [os.remove(f) for f in glob.glob("/Users/" + getpass.getuser() + "/Downloads/*.csv")]

 