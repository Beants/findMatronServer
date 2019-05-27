# findMatronServer


```


code 0 yes
    500 no
注册接口：
  入参：
  {
   "account":"abcdefg",
   "pwd":"123456"
}

出参：
{
  "code":0,
  "msg":"注册成功",
 "data":{}
}

登录接口：
入参：
{
  "account":"abcdefg",
"pwd":"123456"
}

出参：
{
    "code":0,
    "msg":"注册成功",
    "data":{
        "token":""
    }
}

获取月嫂列表数据接口
入参：
 {
   "page":"页码",
   "pageSize":"每页个数"
 }
出参：
{
    "code":0,
    "msg":"注册成功",
    "data":{
        "list":[
            {
                "imageUrl":"",
                "name":"",
                "age":"",
                "duration":"从业时间",
                "grade":"99",
                "price":"价格",
                "city":"籍贯",
                "id":"月嫂id"
            }
        ]
    }
}


月嫂详情页面接口：
入参：
{
	"id":""
}

出参:
{
    "code":0,
    "msg":"注册成功",
    "data":{
        "familyCount":"服务家庭数",
        "verify":{
            "idcard":{  //身份证
                "name":"",  
                "number":"" //身份证号脱敏
            },
            "health":{ //健康这
                "name":"",
                "status":""
            },
            "perfessionCard":{//工作证 包含什么数据？

            }
        },
        "Introduction":"简单介绍",
        "grade":"用户评价"
    }
}


创建订单：
入参：

{
    "from":"2019-05-27",
    "to":"2019-06-27",
    "dayCount":"30",
    "babyCount":"2",
    "contactName":"联系人姓名",
    "contactPhone":"13000000000",
    "contactAddress":"北京",
    "extraInfo":"备注"
}

出参：
{
    "code":0,
    "msg":"创建成功",
    "data":{
        "orderId":"订单id"
    }
}


订单列表接口：
page 0-n
pagesize  1-n
出参:
{
    "code":0,
    "msg":"",
    "data":{
        "list":[
        {
        '_id': '5ceb677d288634f85fada361',
        'from': '2019-05-27',
        'to': '2019-06-27',
        'dayCount': '30',
        'babyCount': '2',
        'contactName': 'name',
        'contactPhone': '13000000000',
        'contactAddress': '北京',
        'extraInfo': 'note',
        'price': 0,
        'status': 1,
        'grade': ''
        }


        ]
    }
}


修改密码
入参
{
"token":""
 "pwd":"" //重置的密码
}

出参：
{
	"code":0,
	"msg":"修改成功",
	"data":{}
}


```
