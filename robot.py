# -*- coding: utf-8 -*-
# @Time    : 2019/3/25 19:10
# @Author  : LY
# @FileName: robot
# @Software: PyCharm
# @Official Accounts：大数据学习废话集
import ast
import re

import werobot
import requests
import json

robot = werobot.WeRoBot(token='tokenhere')


@robot.text
def text_(message):
    return text_process(message)


@robot.image
def image_(message):
    return '对不起！我还不能处理图片信息！'


post_url = 'https://www.aixxz.com/test/ApiTest_main.php?randkey=R9UThn77gX5YMhugP32C'


def text_process(message):
    text = message.content
    res = requests.post(post_url, data={'text': text, 'aixxz_api': '/api3'})
    reply = res.content.decode('utf-8', 'ignore')
    reply = re.findall('返回:jason.*?\r\n(.*)', reply)[0].strip().replace('\\', '')
    reply = json.loads(reply)
    data = reply['data']
    return data


# 让服务器监听在 0.0.0.0:6987
robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 6987
robot.run()
