import os, time, json
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from log.logger import logger as log
from src.mail import send_mail
from config.mail_config import mail_config
from src.wechat_msg import send_msg

browser = None

def make_order():
    browser.get("https://www.xiaomiyoupin.com/detail?gid=115528")
    if "登录" in browser.page_source:
        time.sleep(5)
        return False
    if "商品未开售" in browser.page_source:
        return False

    browser.find_element_by_css_selector("a:contains('立即抢购')").click()
    browser.find_element_by_css_selector("a:contains('去下单')").click()

    return True


if __name__ == "__main__":
    option = ChromeOptions()
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    browser = webdriver.Chrome(os.path.join(os.path.dirname(__file__), "chromedriver.exe"), options=option)
    flag = False
    while not flag:
        flag = make_order()
        log.info(flag)
    browser.quit()