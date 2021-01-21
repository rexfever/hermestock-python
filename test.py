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

CHANNEL_LIST = ["https://hooks.slack.com/services/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"]

#CHANNEL_LIST = ["https://hooks.slack.com/services/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"] #양인석 웹훅
def send_message_to_slack(text):
    for channel in CHANNEL_LIST:
        url = channel
        payload = { "text" : text }
        requests.post(url, json=payload)

# 날짜 및 검색 항목 설정
def _set_date():
    DRIVER.get('http://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201020303')
    sleep(5)
    target_sdate = DRIVER.find_element_by_name('strtDd')
    target_edate = DRIVER.find_element_by_name('endDd')
    target_sdate.clear()
    target_edate.clear()
    #target_sdate.send_keys(datetime.now().strftime('%Y%m%d'))
    #target_edate.send_keys(datetime.now().strftime('%Y%m%d'))
    target_sdate.send_keys(datetime.now().strftime('20201228'))
    target_edate.send_keys(datetime.now().strftime('20201228'))


# 매수 주체 선택 후 다운로드
def _select_buyer(element, buyer):
    element.select_by_value(buyer)
    DRIVER.find_element_by_class_name('btn_black.btn_component_search').click()
    sleep(3)
    excel_button = DRIVER.find_element_by_xpath('//*[@id="MDCSTAT024_FORM"]/div[2]/div/p[2]/button[2]')
    excel_button.click()
    csv_button = DRIVER.find_element_by_link_text('CSV')
    csv_button.click()


# 시장 선택
def _select_market(data_source):
    #DRIVER.find_element_by_css_selector(f'.design-fieldset > form > dl > dd > input:nth-child({data_source[0]})').click()
    DRIVER.find_element_by_css_selector(f'#MDCSTAT024_FORM > div.search_tb > div > table > tbody > tr:nth-child(1) > td > label:nth-child({data_source[0]})').click()
    select_element_id = DRIVER.find_element_by_name('invstTpCd').get_attribute("id")
    selected_element = Select(DRIVER.find_element_by_id(select_element_id))
    _select_buyer(selected_element, data_source[1])


def _count_file():
    file_list = os.listdir(cr.filePath)
    file_list = [file for file in file_list if file.endswith(".csv")]
    return len(file_list)


def close_window():
    DRIVER.close()


try:

    dl._set_date()
    while cr._count_file() < 4:
        sleep(10)
        if cr._count_file() == 0:
            print("file", cr._count_file())
            dl._select_market(DATA_SOURCE[0])
            print(DATA_SOURCE[0])
        elif cr._count_file() == 1:
            print("file", cr._count_file())
            dl._select_market(DATA_SOURCE[1])
            print(DATA_SOURCE[1])
        elif cr._count_file() == 2:
            print("file", cr._count_file())
            dl._select_market(DATA_SOURCE[2])
            print(DATA_SOURCE[2])
        elif cr._count_file() == 3:
            print("file", cr._count_file())
            dl._select_market(DATA_SOURCE[3])
            print(DATA_SOURCE[3])
        else:
            print("file", cr._count_file())
            continue

    cr._rename_file()
    rank_1 = cr._merge_data_set(cr._extract_data_set(KOSPI_fileList[0]), cr._extract_data_set(KOSPI_fileList[1]))
    print(rank_1)
    send_message_to_slack(rank_1.to_string())
    rank_2 = cr._merge_data_set(cr._extract_data_set(KOSDAQ_fileList[0]), cr._extract_data_set(KOSDAQ_fileList[1]))
    print(rank_2)
    send_message_to_slack(rank_2.to_string())

finally:
    close_window()
    [os.remove(f) for f in glob.glob("/Users/"+getpass.getuser()+"/Downloads/*.csv")]

