#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/5/27 1:09 PM
# @Author : maxu
# @Site : 
# @File : test.py
# @Software: PyCharm

#
# import requests
#
# html = requests.post(' http://0.0.0.0:5000/upload', files={'file': open('test.py', 'r'), })
# print(html.text)
# import random
#
# from SqlManager import SqlManager
#
# strs = '彭万里、高大山、谢大海、马宏宇、林莽、黄强辉、章汉夫、范长江、林君雄、谭平山、朱希亮、李四光、甘铁生、张伍绍祖、马继祖、程孝先、宗敬先、年广嗣、汤绍箕、吕显祖、何光宗、孙念祖、马建国、节振国、冯兴国、郝爱民、于学忠、马连良、胡宝善、李宗仁、洪学智、余克勤、吴克俭、杨惟义、李文信、王德茂、李书诚、杨勇、高尚德、刁富贵、汤念祖、吕奉先、何光宗、冷德友、安怡孙、贾德善、蔡德霖、关仁、郑义、贾怡、孙天民、赵大华、赵进喜、赵德荣、赵德茂、钱汉祥、钱运高、钱生禄、孙寿康、孙应吉、孙顺达、李秉贵、李厚福、李开富、王子久、刘永生、刘宝瑞、关玉和、王仁兴、李际泰、罗元发、刘造时、刘乃超、刘长胜、张成基、张国柱、张志远、张广才、吕德榜、吕文达、吴家栋、吴国梁、吴立功、李大江、张石山、王海'
# names = strs.split('、')
# for name in names:
#     age = random.randint(30, 50)
#     grade = random.randint(60, 100)
#     num = str(random.randint(5, 100))
#     price = str(random.randint(100, 500)) + '/天'
#     id = str(random.randint(111111, 999999)) + str(random.randint(111111, 999999)) + str(random.randint(111111, 999999))
#     SqlManager().newBS('zhengjianzhao.jpeg', name, str(age), '2018-1-1', str(grade), price, '北京', num,
#                        id, '1558939237856.jpg', 'timg.jpeg', '我热爱生活,积极工作,爱岗敬业,无私奉献,获得一致好评!')
import requests

url1 = 'http://39.96.222.175:3567/getImage/timg.jpeg'
url = 'http://0.0.0.0:3567/getBsList/'
html = requests.post(url, {
    'page': 1,
    "pageSize": 5,
    "sort": 1
}
                    )
print(html.url)
print(html.text)
print(html.status_code)
