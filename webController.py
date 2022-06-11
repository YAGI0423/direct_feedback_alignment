import time

from selenium import webdriver
from selenium.webdriver.common.by import By


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


if __name__ == '__main__':
    web_ctrl = WebController()

    web_ctrl.open_browser('https://jstris.jezevec10.com/?play=10')

    while True:
        try:
            bot_set_ele = web_ctrl.driver.find_element(by=By.CLASS_NAME, value='bcContent')
            break
        except:
            pass
    print(bot_set_ele)