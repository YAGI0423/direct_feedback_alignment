import time
import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class WebController:
    def __init__(self):
        def init_option(option):
            option.add_argument("disable-gpu")   # 가속 사용 x
            option.add_argument('lang=ko_KR')   #플러그인 탑재
            option.add_argument(
                'user-agent=Mozilla/5.0 (Macintosh; \
                Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) \
                Chrome/61.0.3163.100 Safari/537.36'
            )

        
        self.web_option = webdriver.ChromeOptions()
        init_option(option=self.web_option)

        self.driver = webdriver.Chrome('./chromedriver/chromedriver')
        
    
    def open_browser(self, url):
        self.driver.maximize_window()    #창 크기 최대화
        self.driver.get(url)    #url 접속

    def get_element(self, by, value, wait_time=1):
        #waiting for up load element
        #return [success load ele], [element]

        s = time.time()

        while (time.time() - s) < wait_time:
            try:
                ele = self.driver.find_element(by=by, value=value)
                return True, ele
            except:
                pass
        return False, None

    def act_login(self, id, pw):
        success, id_text_ele = self.get_element(by=By.NAME, value='name', wait_time=2)
        success, pw_text_ele = self.get_element(by=By.NAME, value='password', wait_time=2)

        id_text_ele.send_keys(id)
        pw_text_ele.send_keys(pw)
        
        success, log_btn = self.get_element(by=By.CLASS_NAME, value='btn-primary', wait_time=2)
        log_btn.click()

    def setting_bot(self):
        success, delete_bot_btn = self.get_element(by=By.CLASS_NAME, value='fa-trash-alt', wait_time=3)    #delete init bot
        delete_bot_btn.click()

        for idx in range(4):
            success, add_bot_btn = self.get_element(by=By.CLASS_NAME, value='add-btn', wait_time=1)
            add_bot_btn.click()

            success, bot_list_ele = self.get_element(by=By.CSS_SELECTOR, value='.content select', wait_time=1)
            bot_list_ele = Select(bot_list_ele)
            bot_list_ele.select_by_index(random.randint(0, 3))

            success, bot_name_ele = self.get_element(by=By.CSS_SELECTOR, value='.content input', wait_time=1)
            bot_name_ele.clear()
            bot_name_ele.send_keys(f'BOT {idx}')

            success, apply_btn = self.get_element(by=By.CLASS_NAME, value='apply-btn', wait_time=1)
            apply_btn.click()

        success, apply_btn = self.get_element(by=By.CLASS_NAME, value='apply-btn', wait_time=1)
        apply_btn.click()



if __name__ == '__main__':
    web_ctrl = WebController()

    web_ctrl.open_browser('https://jstris.jezevec10.com/login')
    web_ctrl.act_login(id='9945735@naver.com', pw='1q2w3e4r5t6y!Q@W#E$R%T^Y')
    time.sleep(2)

    web_ctrl.driver.get('https://jstris.jezevec10.com/?play=10')
    time.sleep(4)
    web_ctrl.setting_bot()

    success, start_btn = web_ctrl.get_element(by=By.ID, value='res', wait_time=1)
    start_btn.send_keys(Keys.F12)

