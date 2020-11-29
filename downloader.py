from time import sleep
from selenium import webdriver
from selenium.webdriver.support.select import Select
from datetime import datetime

'''
1. 목적페이지 이동 (function화)
2. 날짜 세팅 (function화)
3. 시장 선택 (function화)
4. 투자자 선택 후 다운로드(function화)
4. 시장 수만큼 3번째 항 반복
'''
DRIVER = webdriver.Chrome('./chromedriver')

# 시장, 매수주 선언
MARKETS = [['3', 'kospi'], ['5', 'kosdaq']]
BUYERS = [['7050', 'KIK'], ['6000', 'YEON'], ['9000', 'FO']]


# 날짜 세팅
def _set_date(driver):
    driver.get('http://marketdata.krx.co.kr/mdi#document=040404')
    sleep(5)
    target_date = driver.find_element_by_name('schdate')
    target_date.clear()
    target_date.send_keys(datetime.now().strftime('%Y%m%d'))


# 매수 주체 선택 후 다운로
def _select_buyer(element, buyers, driver):
    for buyer in buyer:
        element.select_by_value(buyer[0])
        driver.find_element_by_class_name('btn-board.btn-board-search').click()
        sleep(2)
        excel_button = driver.find_element_by_xpath("//*[contains(text(), 'CSV')]")
        excel_button.click()


# 시장 선택
def _select_market(markets, driver):
    for market in markets:
        driver.find_element_by_css_selector(f'.design-fieldset > form > dl > dd > input:nth-child({market[0]})').click()
        select_element_id = driver.find_element_by_name('var_invr_cd').get_attribute("id")
        selected_element = Select(driver.find_element_by_id(select_element_id))
        _select_buyer(selected_element, BUYERS, DRIVER)


