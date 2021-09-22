from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

print("멜론 플레이리스트 목록 추출기 v0.0.3")
print("")
print("**주의사항**")
print("같은 디렉토리에 크롬 버젼에 맞는 \'chromedriver.exe\' 파일이 존재해야 작동합니다. (https://chromedriver.chromium.org/downloads)")
print("----------------------------------------------------------------------------------------------")
print("memberKey는 아래 링크 뒤에 오는 8자리 숫자를 입력해주세요.")
print("\"https://www.melon.com/mymusic/like/mymusiclikesong_list.htm?memberKey=\"")
print("")
print("delay는 각 페이지가 자동으로 넘어가는 지연시간을 의미합니다. 양의 정수를 입력해주세요. (1초 이상 권장)")
print("만약 에러가 난다면 delay 숫자를 더 큰수로 높여보세요.")
print("----------------------------------------------------------------------------------------------")
print("")

KEY = input("memberKey를 입력해주세요 : ")
delay = int(input("delay를 입력해주세요 (자연수만 입력) : "))

driver = webdriver.Chrome()
url = f'https://www.melon.com/mymusic/like/mymusiclikesong_list.htm?memberKey={KEY}'
driver.get(url)
action = ActionChains(driver)

array = []
pageNum = len(driver.find_element_by_css_selector('.page_num').find_elements_by_css_selector("*"))
end = False

def test(text_list):
    for i in range(int(text_list[0]), int(text_list[0]) + 20):
        temp = []
        for j in range(len(text_list)):
            if str(i) == text_list[j] and text_list[j + 1] == '재생 담기':
                temp.append(text_list[j])
                temp.append(text_list[j + 3])
                temp.append(text_list[j + 4])
                array.append(temp)

try:
    while not end:
        if 'disabled' in driver.find_element_by_css_selector('.btn_next').get_attribute('class').split():
            end = True
            pageNum = len(driver.find_element_by_css_selector('.page_num').find_elements_by_css_selector("*"))
        for i in range(2, pageNum):
            text_list = driver.find_element_by_css_selector('tbody').text.split('\n')
            test(text_list)
            driver.find_element_by_css_selector(f'.page_num > a:nth-child({i})').click()
            time.sleep(delay)
        text_list = driver.find_element_by_css_selector('tbody').text.split('\n')
        test(text_list)
        driver.find_element_by_css_selector('.btn_next').click()
        time.sleep(delay)

    f = open("melon_playlist.txt", 'w', encoding='utf8')

    isSuccess = True
    for i in range(len(array)):
        if str(i + 1) != array[i][0]:
            isSuccess = False
        f.write(f'{array[i][1]} - {array[i][2]}\n')

    f.close()

    if isSuccess:
        print("\n\n추출 성공. \'melon_playlist.txt\' 파일로 저장됨.")
    else:
        print("실패...")

except Exception as e:
    print(f'에러 발생 : {e}')