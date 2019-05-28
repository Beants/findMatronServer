#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/5/27 11:21 AM
# @Author : maxu
# @Site : 
# @File : SqlManager.py
# @Software: PyCharm
from bson.objectid import ObjectId
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, SignatureExpired, BadSignature


class SqlManager:

    def __init__(self):

        import pymongo
        self.SECRET_KEY = '9C>_Py8$Gjfh0gjpoQp1ql'
        self.myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        self.mydb = self.myclient["Fm"]

    def generate_auth_token(self, id_, expiration=600):
        s = Serializer(self.SECRET_KEY, expires_in=expiration)
        return s.dumps({'id': id_})

    # @staticmethod
    def verify_auth_token(self, token):
        s = Serializer(self.SECRET_KEY)
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None  # valid token, but expired
        except BadSignature:
            return None  # invalid token
        return data['id']

    def reg(self, username, password):
        table = self.mydb['user']

        if not table.find_one({"account": username}):
            temp = table.insert_one({"account": username, "pwd": password})
            if temp:
                return {
                    "code": 0,
                    "msg": "注册成功",
                    "data": {"id": str(temp.inserted_id)}
                }
            else:
                return {
                    "code": 500,
                    "msg": "注册失败",
                    "data": {}
                }

        else:
            return {
                "code": 500,
                "msg": "已经存在用户名",
                "data": {}
            }

    def login(self, username, password):
        table = self.mydb['user']
        temp = table.find_one({"account": username, "pwd": password})
        # print(temp)
        if temp:
            temp['_id'] = str(temp['_id']).replace('ObjectId(', '').replace(')', '')
            # print(temp)
            return {
                "code": 0,
                "msg": "登录成功",
                "data": {"token": self.generate_auth_token(temp['_id'])}
            }
        else:
            return {
                "code": 500,
                "msg": "登录失败",
                "data": {}
            }

    def cpwd(self, token, pwd):
        table = self.mydb['user']
        id_ = self.verify_auth_token(token)
        temp = table.update_one({"_id": ObjectId(id_)}, {'$set': {"pwd": pwd}})
        if temp:
            return {
                "code": 0,
                "msg": "修改成功",
                "data": {}
            }
        else:
            return {
                "code": 500,
                "msg": "修改失败",
                "data": {}
            }

    def newOrder(self, time_from, time_to, dayCount, babyCount, contactName, contactPhone, contactAddress,
                 extraInfo, price):
        table = self.mydb['order']
        temp = table.insert_one(
            {
                "from": time_from,
                "to": time_to,
                "dayCount": dayCount,
                "babyCount": babyCount,
                "contactName": contactName,
                "contactPhone": contactPhone,
                "contactAddress": contactAddress,
                "extraInfo": extraInfo,
                "price": price,
                "status": 1,
                "grade": '',
            }
        )
        # print()
        if temp:
            orderId = str(temp.inserted_id).replace('ObjectId(', '').replace(')', '')
            return {
                "code": 0,
                "msg": "创建成功",
                "data": {"orderId": orderId}
            }
        else:
            return {
                "code": 500,
                "msg": "创建失败",
                "data": {}
            }

    def getOrder(self, page, pageSize):

        table = self.mydb['order']
        res = []
        for i in table.find({}):
            i['_id'] = str(i['_id']).replace('ObjectId(', '').replace(')', '')
            res.append(i)
        res = res[page * pageSize:(page + 1) * pageSize]
        print(page * pageSize, 'ss', (page + 1) * pageSize)
        print(res)
        return {
            "code": 0,
            "msg": "",
            "data": {
                "list": res
            }
        }

    def changeOrder(self, orderId, json):
        table = self.mydb['order']
        temp = table.update_one({"_id": ObjectId(orderId)}, {'$set': json})
        if temp:
            return {
                "code": 0,
                "msg": "修改成功",
                "data": {}
            }
        else:
            return {
                "code": 500,
                "msg": "修改失败",
                "data": {}
            }

    def newBS(self, imageUrl, name, age, duration, grade, price, city, familyCount, idcardnumber, healthstatus,
              perfessionCard, Introduction):
        table = self.mydb['bs']
        temp = {
            "imageUrl": imageUrl,
            "name": name,
            "age": age,
            "duration": duration,
            "grade": grade,
            "price": price,
            "city": city,
            "familyCount": familyCount,
            "idcard": idcardnumber,
            "healthCard": healthstatus,
            "perfessionCard": perfessionCard,
            "Introduction": Introduction
        }
        print(temp)
        table.insert_one(temp)

    def getBsList(self, page, pageSize):

        table = self.mydb['bs']
        res = []
        for i in table.find({}):
            i['_id'] = str(i['_id']).replace('ObjectId(', '').replace(')', '')
            res.append(i)
        res = res[page * pageSize:(page + 1) * pageSize]
        print(res)

        return {
            "code": 0,
            "msg": "成功",
            "data": {
                "list": res
            }
        }

    def getBsDetail(self, id_):
        table = self.mydb['bs']
        temp = table.find_one({"_id": ObjectId(id_)})
        return {
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


if __name__ == '__main__':
    # temp = SqlManager().login('admin', 'admin1')
    # token = temp['data']['token']
    # temp=SqlManager().newOrder("2019-05-27", "2019-06-27", "30", "2", "name", "13000000000", "北京", 'note')
    # print(temp)
    # print(SqlManager().newBS('zhengjianzhao.jpeg', '赵 a', '33', '2018-1-1', '99', '100/天', '北京', '10',
    #                          '123456789012345678', '1558939237856.jpg', 'timg.jpeg', '我热爱生活,积极工作,爱岗敬业,无私奉献,获得一致好评!'))
    # print(SqlManager().getBsDetail('5ceb967d676262e425368109'))
    pass
