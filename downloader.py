from time import sleep
from selenium import webdriver
from selenium.webdriver.support.select import Select
from datetime import datetime

'''
1. 목적페이지 이동 
2. 날짜 및 검색항목 설정 
3. 시장 선택 
4. 투자자 선택 후 다운로드(function화)
5. 시장 수만큼 3,4번째 항 반복
'''
DRIVER = webdriver.Chrome('./chromedriver')

# 시장, 매수주체 선언
MARKETS = [['3', 'kospi'], ['5', 'kosdaq']]
BUYERS = [['7050', 'KIK'], ['9000', 'FO']]


# 날짜 및 검색 항목 설정
def _set_date(driver):
    driver.get('http://marketdata.krx.co.kr/mdi#document=040404')
    sleep(5)
    driver.find_element_by_css_selector(
        f'.design-fieldset > form > dl:nth-of-type(4) > dd > input:nth-child(3)').click()
    target_date = driver.find_element_by_name('schdate')
    target_date.clear()
    target_date.send_keys(datetime.now().strftime('%Y%m%d'))

# 매수 주체 선택 후 다운로드
def _select_buyer(element, buyers, driver):
    for buyer in buyers:
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
        _select_buyer(selected_element, BUYERS, driver)

'''
_set_date(DRIVER)
_select_market(MARKETS, DRIVER)
'''