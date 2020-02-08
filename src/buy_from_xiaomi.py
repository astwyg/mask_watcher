import requests, time
from log.logger import logger as log


def make_order(order_num):

    order_num = str(order_num)
    ts = int(time.time())
    # step1
    r = requests.post("https://m.xiaomiyoupin.com/app/stat/visitv2",
                      data=[{"e":{"et":"shop","ref":"$Detail$?v=8&id=https%3A%2F%2Fm.xiaomiyoupin.com%2Fdetail%3Fgid%3D{order_num}&event=TOUCH&time={ts}&area=buy_confirm&iid=g%3D{order_num}%26pid%3D87152".format(order_num=order_num, ts=ts),
                                  "t":ts,"spm":"YouPinM.$Detail$_{order_num}.buy_confirm.0.50164756".format(order_num=order_num)}}],
                      headers={
                          "Content-Type":"application/x-www-form-urlencoded",
                          "DToken":"",
                          "Origin":"https://m.xiaomiyoupin.com",
                          "Referer":"https://m.xiaomiyoupin.com/detail?gid=115147",
                          "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Mobile Safari/537.36",
                          "X-User-Agent":"channel/youpin platform/youpin.m",
                          "X-Yp-App-Source":"front-RNWeb-old"
                      })
    log.info("step1 result: "+str(r.status_code))

    # step2
    r = requests.post("https://m.xiaomiyoupin.com/api/auth/login/isloggedin",
                      headers={ # Reffer 中有加密字段, 暂时放弃
                          "Content-Type":"application/x-www-form-urlencoded",
                          "DToken":"",
                          "Origin":"https://m.xiaomiyoupin.com",
                          "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Mobile Safari/537.36",
                          "X-User-Agent":"channel/youpin platform/youpin.m",
                          "X-Yp-App-Source":"front-RNWeb-old"
                      })
    log.info("step2 result: "+str(r.text))

    # step3
    r = requests.post("https://m.xiaomiyoupin.com/app/stat/visitv2",
                      )


if __name__ == "__main__":
    make_order("115147")