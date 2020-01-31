import requests
from config import wechat_config

def send_msg(msg=""):
    requests.post("http://wxpusher.zjiecode.com/api/send/message", json={
        "appToken": wechat_config.APP_TOKEN,
        "content": msg,
        "contentType": 1,
        "topicIds": [ # 不知道有啥用
            123
        ],
        "uids": wechat_config.UID.split(",")
    })

if __name__ == "__main__":
    send_msg("测试消息!!    https://detail.tmall.com/item.htm?id=539798535423")