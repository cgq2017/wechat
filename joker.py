import itchat
import requests
import re
import time
from datetime import datetime
import random


morining = input('输入早上时间：')
evening = input('输入晚上时间：')
friend=input('输入要给发送的朋友：')

def get_joke():
    ans = []
    url = 'https://ishuo.cn/joke'
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    # 伪造请求头
    headers = {'User-Agent': user_agent}
    try:
        request = requests.get(url=url, headers=headers)
        content = request.text.encode(request.encoding).decode('utf-8')
        items = re.findall('<li.*?class="list_li.*?div.*?class="content.*?>(.*?)</div',content,re.S)
        # choice = random.randint(0, len(items) - 1)
        slice = random.sample(items, 6)
        message=''
        for i in range(len(slice)):
            message+=slice[i]+"\n"+"\n"
        # message = message.replace("<p>", "").strip()
        # message= message.replace("</p>","").strip()
        # message = message.replace("<br/>", "").strip()

    except:
        message="我的天，今天怎么没有获取到笑话，我去查看一下"

    return message


def login(joke_list,text):
    # 登陆微信(扫描二维码方式)
    itchat.auto_login(hotReload=True)
    # 查看指定朋友信息,name为通讯录备注名from

    friend_list=friend.split(';')
    for frend in friend_list:
        users = itchat.search_friends(name=frend)
        userName = users[0]['UserName']
        itchat.send_msg(joke_list, toUserName=userName)
        itchat.send_msg(text, toUserName=userName)
def main():
    while True:
        t = datetime.now().strftime('%H:%M')
        if(t==morining):
            joke_list = get_joke()
            time.sleep(1)
            login(joke_list,"妹子，早安，爱你!")
            time.sleep(60)
        if (t == evening):
            joke_list = get_joke()
            time.sleep(1)
            login(joke_list, "妹子，晚安，爱你!")
            time.sleep(60)



itchat.auto_login(hotReload=True)
main()