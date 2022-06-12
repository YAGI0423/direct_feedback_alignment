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


if __name__ == '__main__':
    web_ctrl = WebController()

    web_ctrl.open_browser('https://jstris.jezevec10.com/login')

    success, id_text_ele = web_ctrl.get_element(by=By.NAME, value='name', wait_time=2)
    success, pw_text_ele = web_ctrl.get_element(by=By.NAME, value='password', wait_time=2)

    id_text_ele.send_keys('9945735@naver.com')
    pw_text_ele.send_keys('1q2w3e4r5t6y!Q@W#E$R%T^Y')

    

    # success, login_btn_ele = web_ctrl.get_element(by=By.)
    # success, ele = web_ctrl.get_element(by=By.CLASS_NAME, value='bcContent', wait_time=5)
    # print(success, ele)