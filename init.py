#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/5/27 11:16 AM
# @Author : maxu
# @Site : 
# @File : init.py
# @Software: PyCharm
import json
import os

from flask import Flask, request, Response, send_from_directory

# sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
from SqlManager import SqlManager

app = Flask(__name__)
app.secret_key = '9C>_Py8$Gjfh0gjpoQp1ql'

sqlManager = SqlManager()


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/reg/', methods=['POST'])
def reg():
    if request.method == "POST":
        username = request.form['account']
        pwd = request.form['pwd']
        temp = sqlManager.reg(username, pwd)
        return Response(json.dumps(temp), mimetype='application/json')


@app.route('/login/', methods=['POST'])
def login():
    if request.method == "POST":
        username = request.form['account']
        pwd = request.form['pwd']
        temp = sqlManager.login(username, pwd)
        return Response(json.dumps(temp), mimetype='application/json')


@app.route('/cpwd/', methods=['POST'])
def cpwd():
    if request.method == "POST":
        token = request.form['token']
        pwd = request.form['pwd']
        temp = sqlManager.cpwd(token, pwd)
        return Response(json.dumps(temp), mimetype='application/json')


@app.route('/upload/', methods=['POST'])
def upload():
    if request.method == "POST":
        import time
        f = request.files['file']
        basepath = os.path.dirname(__file__)  # 当前文件所在路径
        fname = str(time.time()) + f.filename
        upload_path = os.path.join(basepath, 'static/', fname)  # 注意：没有的文件夹一定要先创建，不然会提示没有该路径
        f.save(upload_path)
        return Response(json.dumps({
            "code": 0,
            "msg": '',
            "data": {
                "filename": str(fname)
            }

        }), mimetype='application/json')


@app.route('/getImage/<string:name>', methods=['GET'])
def getImage(name):
    print(name)
    if request.method == "GET":
        return send_from_directory('static/', name, as_attachment=True)


if __name__ == '__main__':
    app.run('0.0.0.0')
