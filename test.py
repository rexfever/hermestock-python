import calc_rank as cr
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.select import Select
from datetime import datetime
import os, glob, getpass

DRIVER = webdriver.Chrome('./chromedriver')
FILEPATH = cr.filePath
# 시장, 매수주체 선언

DATA_SOURCE = [['3', '7050'], ['3', '9000'], ['5', '7050'], ['5', '9000']]

KOSPI_fileList = ['data.csv', 'data (1).csv']
KOSDAQ_fileList = ['data (2).csv', 'data (3).csv']



# 날짜 및 검색 항목 설정
def _set_date():
    DRIVER.get('http://marketdata.krx.co.kr/mdi#document=040404')
    sleep(5)
    DRIVER.find_element_by_css_selector(
        f'.design-fieldset > form > dl:nth-of-type(4) > dd > input:nth-child(3)').click()
    target_date = DRIVER.find_element_by_name('schdate')
    target_date.clear()
    target_date.send_keys(datetime.now().strftime('%Y%m%d'))
    #target_date.send_keys(datetime.now().strftime('20201224'))


# 매수 주체 선택 후 다운로드
def _select_buyer(element, buyer):
    element.select_by_value(buyer)
    DRIVER.find_element_by_class_name('btn-board.btn-board-search').click()
    sleep(3)
    excel_button = DRIVER.find_element_by_xpath("//*[contains(text(), 'CSV')]")
    excel_button.click()


# 시장 선택
def _select_market(data_source):
    DRIVER.find_element_by_css_selector(f'.design-fieldset > form > dl > dd > input:nth-child({data_source[0]})').click()
    select_element_id = DRIVER.find_element_by_name('var_invr_cd').get_attribute("id")
    selected_element = Select(DRIVER.find_element_by_id(select_element_id))
    _select_buyer(selected_element, data_source[1])


def _count_file():
    file_list = os.listdir(cr.filePath)
    file_list = [file for file in file_list if file.endswith(".csv")]
    return len(file_list)


def close_window():
    DRIVER.close()

try:
    _set_date()
    while _count_file() < 4:
        sleep(10)
        if _count_file() == 0:
            print("file", _count_file())
            _select_market(DATA_SOURCE[0])
            print(DATA_SOURCE[0])
        elif _count_file() == 1:
            print("file", _count_file())
            _select_market(DATA_SOURCE[1])
            print(DATA_SOURCE[1])
        elif _count_file() == 2:
            print("file", _count_file())
            _select_market(DATA_SOURCE[2])
            print(DATA_SOURCE[2])
        elif _count_file() == 3:
            print("file", _count_file())
            _select_market(DATA_SOURCE[3])
            print(DATA_SOURCE[3])
        else:
            print("file", _count_file())
            continue

    print(cr._merge_data_set(cr._extract_data_set(KOSPI_fileList[0]), cr._extract_data_set(KOSPI_fileList[1])))
    print(cr._merge_data_set(cr._extract_data_set(KOSDAQ_fileList[0]), cr._extract_data_set(KOSDAQ_fileList[1])))
finally:
    close_window()
    [os.remove(f) for f in glob.glob("/Users/"+getpass.getuser()+"/Downloads/*.csv")]

