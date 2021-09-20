from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
KEY = '12345678'
url = f'https://www.melon.com/mymusic/like/mymusiclikesong_list.htm?memberKey={KEY}'
driver.get(url)
action = ActionChains(driver)

driver.find_element_by_css_selector('.page_num > a').click()