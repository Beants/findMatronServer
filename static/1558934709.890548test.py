#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/5/27 1:09 PM
# @Author : maxu
# @Site : 
# @File : test.py
# @Software: PyCharm


import requests

html = requests.post(' http://0.0.0.0:5000/upload', files={'file': open('test.py', 'r'), })
print(html.text)
