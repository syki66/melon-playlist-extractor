from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
KEY = '12345678'
url = f'https://www.melon.com/mymusic/like/mymusiclikesong_list.htm?memberKey={KEY}'
driver.get(url)
action = ActionChains(driver)

array = []
pageNum = len(driver.find_element_by_css_selector('.page_num').find_elements_by_css_selector("*"))
end = False

def test(text_list):
    for i in range(len(text_list)):
        temp = []
        if str(i + 1) == text_list[i] and i + 2 == '재생 담기':
            temp.append(text_list[i + 3])
            temp.append(text_list[i + 4])

    # temp = []
    # for i in range(len(text_list)):
    #     if i % 10 == 3:
    #         temp = []
    #         temp.append(text_list[i])
    #     elif i % 10 == 4:
    #         temp.append(text_list[i])
    #         array.append(temp)

# while not end:
#     text_list = driver.find_element_by_css_selector('tbody').text.split('\n')
#     test(text_list)
#     time.sleep(0.1)
#     if 'disabled' in driver.find_element_by_css_selector('.btn_next').get_attribute('class').split():
#         end = True
#         pageNum = len(driver.find_element_by_css_selector('.page_num').find_elements_by_css_selector("*"))
#     for i in range(2, pageNum):
#         text_list = driver.find_element_by_css_selector('tbody').text.split('\n')
#         test(text_list)
#         driver.find_element_by_css_selector(f'.page_num > a:nth-child({i})').click()
#         time.sleep(0.1)
#     driver.find_element_by_css_selector('.btn_next').click()
#     time.sleep(0.1)


# 아래는 테스트

# for i in range(len(array)):
#     print(f'{i}  {array[i][0]}             {array[i][1]}')


driver.find_element_by_css_selector(f'.page_num > a:nth-child({4})').click()
time.sleep(1)
text_list = driver.find_element_by_css_selector('tbody').text.split('\n')

# for i in text_list:
#     print(i)

test(text_list)
print(array)