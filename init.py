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


class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, bytes):
            return str(obj, encoding='utf-8')
        return json.JSONEncoder.default(self, obj)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/reg', methods=['POST'])
@app.route('/reg/', methods=['POST'])
def reg():
    '''
    注册
    :return:
    '''
    if request.method == "POST":
        print(request.headers)
        print(request.url)
        print(request.form)
        username = request.form['account']
        pwd = request.form['pwd']
        temp = sqlManager.reg(username, pwd)
        return Response(json.dumps(temp, cls=MyEncoder), mimetype='application/json')


@app.route('/login/', methods=['POST'])
def login():
    '''
    登录
    :return:
    '''
    if request.method == "POST":
        print(request.form)

        username = request.form['account']
        pwd = request.form['pwd']
        temp = sqlManager.login(username, pwd)
        return Response(json.dumps(temp, cls=MyEncoder), mimetype='application/json')


@app.route('/cpwd/', methods=['POST'])
def cpwd():
    '''
    change pwd
    :return:
    '''
    if request.method == "POST":
        print(request.form)

        token = request.form['token']
        pwd = request.form['pwd']
        temp = sqlManager.cpwd(token, pwd)
        return Response(json.dumps(temp, cls=MyEncoder), mimetype='application/json')


@app.route('/upload/', methods=['POST'])
def upload():
    '''
    上传文件
    :return:
    '''
    if request.method == "POST":
        print(request.form)

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

        }, cls=MyEncoder), mimetype='application/json')


@app.route('/getImage/<string:name>', methods=['GET'])
def get_image(name):
    '''
    下载图片
    :param name:
    :return:
    '''
    print(name)
    if request.method == "GET":
        return send_from_directory('static/', name, as_attachment=True)


@app.route('/getImage2/<string:name>', methods=['GET'])
def get_image2(name):
    '''
    直接打开图片
    :param name:
    :return:
    '''
    print(name)
    if request.method == "GET":
        with open('static/' + name,'rb')as f:
            img = f.read()
            return Response(img, mimetype="image/jpeg")
        # return send_from_directory('static/', name, as_attachment=True)


@app.route('/verify_auth_token/', methods=['POST'])
def verify_auth_token():
    '''
    确认token
    :return:
    '''
    if request.method == "POST":
        print(request.form)

        token = request.form['token']
        id_ = sqlManager.verify_auth_token(token)
        return Response(json.dumps({
            "code": 0,
            "msg": '',
            "data": {
                "id": str(id_)
            }

        }, cls=MyEncoder), mimetype='application/json')


@app.route('/newOrder/', methods=['POST'])
def newOrder():
    '''
    新订单
    :return:
    '''
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
        return Response(json.dumps(temp, cls=MyEncoder), mimetype='application/json')


@app.route('/getOrder/', methods=['POST'])
def getOrder():
    '''
    获取order
    '''
    print(request.form)

    if request.method == "POST":
        page = int(request.form['page'])
        pageSize = int(request.form['pageSize'])

        temp = sqlManager.getOrder(page, pageSize)
        return Response(json.dumps(temp, cls=MyEncoder), mimetype='application/json')


@app.route('/getOrderById/', methods=['POST'])
def getOrderById():
    '''
    获取该用户的 order
    '''
    print(request.form)

    if request.method == "POST":
        page = int(request.form['page'])
        pageSize = int(request.form['pageSize'])
        token = request.form['token']
        id_ = sqlManager.verify_auth_token(token)
        temp = sqlManager.getOrderById(page, pageSize, id_)
        return Response(json.dumps(temp, cls=MyEncoder), mimetype='application/json')


@app.route('/changeOrder/', methods=['POST'])
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
        return Response(json.dumps(temp, cls=MyEncoder), mimetype='application/json')


@app.route('/getBsList/', methods=['POST'])
def getBsList():
    '''
    :param sort 0:综合 1:价格 2:评分
    :param page:
    :param pageSize:
    :return:
    {
        'code': 0,
        'msg': '',
        'data':
            [
                {
                '_id': '5cebca48e4967cff06320f50',
                'imageUrl': 'zhengjianzhao.jpeg',
                'name': '彭万里',
                'age': '33',
                'duration': '2018-1-1',
                'grade': '72',
                'price': '385/天',
                'city': '北京',
                'familyCount': '51',
                'idcard': '377632393017458497',
                'healthCard': '1558939237856.jpg',
                'perfessionCard': 'timg.jpeg',
                'Introduction': '我热爱生活,积极工作,爱岗敬业,无私奉献,获得一致好评!'
                },
            ]
        }
    }
    '''
    if request.method == "POST":
        page = int(request.form['page'])
        pageSize = int(request.form['pageSize'])
        sort = int(request.form['sort'])
        temp = sqlManager.getBsList(page, pageSize)
        if sort == 0:
            temp = temp
        elif sort == 1:
            temp = sorted(temp, key=lambda i: int(str(i['price']).replace('/天', '')))
        elif sort == 2:
            temp = sorted(temp, key=lambda i: int(i['grade']))
        return Response(json.dumps(temp, cls=MyEncoder), mimetype='application/json')


@app.route('/getBsDetail/', methods=['POST'])
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
        return Response(json.dumps(temp, cls=MyEncoder), mimetype='application/json')



if __name__ == '__main__':
    app.run('0.0.0.0', port='3567')
