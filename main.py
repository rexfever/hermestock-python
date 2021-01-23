# -*- coding: utf-8 -*-
import downloader as dl
import send_msg as sm
from time import sleep
import calc_rank as cr
import os, glob
import getpass


DATA_SOURCE = [['4', '7050'], ['4', '9000'], ['6', '7050'], ['6', '9000']]
KOSPI_fileList = ['data_0.csv', 'data_1.csv']
KOSDAQ_fileList = ['data_2.csv', 'data_3.csv']
'''
CHANNEL_LIST = [["https://hooks.slack.com/services/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", "대기와 나"],
                ["https://hooks.slack.com/services/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", "현주유경"]
                ["https://hooks.slack.com/services/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", "ROTC"]]
'''
CHANNEL_LIST = [["https://hooks.slack.com/services/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","대기와 나"],
                ["https://hooks.slack.com/services/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11","대기와 나"]]
try:
    dl._set_date()
    while cr._count_file() < 4:
        sleep(10)
        if cr._count_file() == 0:
            dl._select_market(DATA_SOURCE[0])
        elif cr._count_file() == 1:
            dl._select_market(DATA_SOURCE[1])
        elif cr._count_file() == 2:
            dl._select_market(DATA_SOURCE[2])
        elif cr._count_file() == 3:
            dl._select_market(DATA_SOURCE[3])
        else:
            continue

    sleep(3)
    cr._rename_file()
    rank_1 = cr._merge_data_set(
        cr._extract_data_set(KOSPI_fileList[0]), cr._extract_data_set(KOSPI_fileList[1]), CHANNEL_LIST
    )
    sm.send_message_to_slack(rank_1.to_string())
    rank_2 = cr._merge_data_set(
        cr._extract_data_set(KOSDAQ_fileList[0]), cr._extract_data_set(KOSDAQ_fileList[1]), CHANNEL_LIST
    )
    sm.send_message_to_slack(rank_2.to_string())
except:
    print("오류 발생")
finally:
    dl.close_window()
    [os.remove(f) for f in glob.glob("/Users/" + getpass.getuser() + "/Downloads/*.csv")]

