#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

class ChromeTest:
    def __init__(self):
        self.options = Options()
        self.options.add_argument('--headless')
        self.options.add_argument('--disable-dev-shm-usage')
        self.options.add_argument("--remote-debugging-port=9222")
        self.browser = webdriver.Chrome('/usr/local/bin/chromedriver', options=self.options)

class WebTest(ChromeTest):
    def __init__(self):
        super(WebTest, self).__init__()

    def test(self):
        self.browser.implicitly_wait(5)
        self.browser.get("http://www.test.com")
        popup_button_close = self.browser.find_elements_by_class_name('popup-button-close')

        for element in popup_button_close:
            print(element.rect)
            if element.is_displayed() and element.is_enabled():
                element.click()

        menus = self.browser.find_elements_by_class_name('gnb-left')
        for m in menus:
            print(m.text)

        time.sleep(5)
        self.browser.close()
        self.browser.quit()


if __name__== "__main__" :
    Web_test = WebTest()
    Web_test.test()