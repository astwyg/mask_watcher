import os, time, json
from selenium import webdriver
from log.logger import logger as log
from src.mail import send_mail
from config.mail_config import mail_config
from src.wechat_msg import send_msg

browser = None

def check_shop(url, keywords):
    browser.get(url)
    time.sleep(3)
    find_flag = False
    for keyword in keywords:
        if keyword in browser.page_source:
            find_flag = keyword
            break
    if not find_flag:
        log.warning("FIND!!!")
        log.warning(url)
        log.warning(keywords)
        # send_mail(
        #     "发现口罩有货!!",
        #     url,
        #     mail_config.get("to")
        # )
        send_msg("口罩有货!   "+url)


def check_all_shops():
    with open(os.path.join(os.path.dirname(__file__),"..","config","shop.json"), "r", encoding='UTF-8') as f:
        infos = json.loads(f.read())
        for info in infos:
            for shop in info["shop"]:
                log.info("checking {} / {}".format(shop, info.get("keyword")))
                keywords = info.get("key_word").split(",")
                check_shop(shop, keywords)


if __name__ == "__main__":
    while True:
        browser = webdriver.Chrome(os.path.join(os.path.dirname(__file__), "chromedriver.exe"))
        check_all_shops()
        browser.quit()