#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/5/27 11:16 AM
# @Author : maxu
# @Site : 
# @File : init.py
# @Software: PyCharm
import json
import os

from flask import Flask, request, Response, send_from_directory, jsonify

# sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
from SqlManager import SqlManager

app = Flask(__name__)
app.secret_key = '9C>_Py8$Gjfh0gjpoQp1ql'

sqlManager = SqlManager()


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/reg', methods=['POST'])
@app.route('/reg/', methods=['POST'])
def reg():
    if request.method == "POST":
        print(request.headers)
        print(request.url)
        print(request.__str__())
        username = request.form['account']
        pwd = request.form['pwd']
        print(request.form)
        temp = sqlManager.reg(username, pwd)
        return Response(jsonify(temp), mimetype='application/json')


@app.route('/login/', methods=['POST'])
def login():
    if request.method == "POST":
        print(request.form)

        username = request.form['account']
        pwd = request.form['pwd']
        temp = sqlManager.login(username, pwd)
        return Response(jsonify(temp), mimetype='application/json')


@app.route('/cpwd/', methods=['POST'])
def cpwd():
    if request.method == "POST":
        print(request.form)

        token = request.form['token']
        pwd = request.form['pwd']
        temp = sqlManager.cpwd(token, pwd)
        return Response(jsonify(temp), mimetype='application/json')


@app.route('/upload/', methods=['POST'])
def upload():
    if request.method == "POST":
        print(request.form)

        import time
        f = request.files['file']
        basepath = os.path.dirname(__file__)  # 当前文件所在路径
        fname = str(time.time()) + f.filename
        upload_path = os.path.join(basepath, 'static/', fname)  # 注意：没有的文件夹一定要先创建，不然会提示没有该路径
        f.save(upload_path)
        return Response(jsonify({
            "code": 0,
            "msg": '',
            "data": {
                "filename": str(fname)
            }

        }), mimetype='application/json')


@app.route('/getImage/<string:name>', methods=['GET'])
def get_image(name):
    print(name)
    if request.method == "GET":
        return send_from_directory('static/', name, as_attachment=True)


@app.route('/verify_auth_token', methods=['POST'])
def verify_auth_token():
    if request.method == "POST":
        print(request.form)

        token = request.form['token']
        id_ = sqlManager.verify_auth_token(token)
        return Response(jsonify({
            "code": 0,
            "msg": '',
            "data": {
                "id": str(id_)
            }

        }), mimetype='application/json')


@app.route('/newOrder', methods=['POST'])
def newOrder():
    print(request.form)

    if request.method == "POST":
        from_ = request.form['from']
        to = request.form['to']
        dayCount = request.form['dayCount']
        babyCount = request.form['babyCount']
        contactName = request.form['contactName']
        contactPhone = request.form['contactPhone']
        contactAddress = request.form['contactAddress']
        extraInfo = request.form['extraInfo']
        price = request.form['price']
        # status = request.form['status']
        # grade = request.form['grade']

        temp = sqlManager.newOrder(from_, to, dayCount, babyCount, contactName, contactPhone, contactAddress, extraInfo,
                                   price)
        return Response(jsonify(temp), mimetype='application/json')


@app.route('/getOrder', methods=['POST'])
def getOrder():
    print(request.form)

    if request.method == "POST":
        page = request.form['extraInfo']
        pageSize = request.form['price']
        temp = sqlManager.getOrder(page, pageSize)
        return Response(jsonify(temp), mimetype='application/json')


@app.route('/changeOrder', methods=['POST'])
def changeOrder():
    '''
    这里的 json 参数必须是以json格式的
    例如:
    post 的数据如下:
    {
        'orderId':'5ceb676e315206fd0f2ac662',
        'json':{
            'price':10000,
        }
    }
    :return:
    '''
    if request.method == "POST":
        print(request.form)

        orderId = request.form['orderId']
        json_ = request.form['json']
        temp = sqlManager.changeOrder(orderId, json_)
        return Response(jsonify(temp), mimetype='application/json')


@app.route('/getBsList', methods=['POST'])
def getBsList():
    '''
    :param page:
    :param pageSize:
    :return:
    {
        'code': 0,
        'msg': '',
        'data': {
            'list': [{
                '_id': '5ceb677d288634f85fada361',
                'from': '2019-05-27',
                'to': '2019-06-27',
                'dayCount': '30',
                'babyCount': '2',
                'contactName': 'name',
                'contactPhone': '13000000000',
                'contactAddress': '北京',
                'extraInfo': 'note',
                'price': 10000,
                'status': 1,
                'grade': ''
            }]
        }
    }
    '''
    if request.method == "POST":
        page = request.form['page']
        print(request.form)

        pageSize = request.form['pageSize']
        temp = sqlManager.getBsList(page, pageSize)
        return Response(jsonify(temp), mimetype='application/json')


@app.route('/getBsDetail', methods=['POST'])
def getBsDetail():
    '''

    :return:
    {
            "code": 0,
            "msg": "注册成功",
            "data": {
                "familyCount": temp["familyCount"],
                'Introduction': temp['Introduction'],
                'grade': temp['grade'],
                "verify": {
                    "idcard": {
                        "name": temp['name'],
                        "number": temp['idcard']
                    },
                    "health": {
                        "img": temp['healthCard'],
                    },
                    "perfessionCard": {
                        'img': 'timg.jpeg',
                    }
                },
            }
        }
    '''
    if request.method == "POST":
        print(request.form)

        id_ = request.form['id']
        temp = sqlManager.getBsDetail(id_)
        return Response(jsonify(temp), mimetype='application/json')



if __name__ == '__main__':
    app.run('0.0.0.0', port='3567')
