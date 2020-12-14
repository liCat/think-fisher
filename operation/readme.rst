下单模块
---------------
    - 查询商品信息接口
        - http://10.105.14.211:81/search/searchQuery?user_id=5061621&platform=3
        - user_id：用户ID
        - platform：1-淘宝；2-拼多多；3-京东

.. code-block::

        response = [
              {
                "buyNormalAllowance": 99, # 自购非会员抵用金
                "buyNormalCash": 59, # 自购非会员普通奖励
                "imageURL": "https://img.alicdn.com/imgextra/i4/3018230850/O1CN01KDAQL81I9LEt3wyc1_!!3018230850.jpg", # 商品图片
                "membershipAllowance": 106, # 自购会员抵用金
                "membershipCash": 59, # 自购会员奖励
                "platform": "SOURCE_TYPE_TAOBAO", # 数据来源平台
                "shareMembershipCash": 106, # 分享赚会员奖励
                "shareNormalCash": 59, # 分享赚非会员奖励
                "shortTitle": "男士短袖t恤宽松衣服潮牌潮流纯棉半袖男装2020新款春夏大码体恤", # 商品短标题
                "sourceIID": "585319218965" # 商品ID
              },
              {
                "buyNormalAllowance": 99,
                "buyNormalCash": 79,
                "imageURL": "https://img.alicdn.com/imgextra/i2/741486021/O1CN012XpyEq1uLfIDML1OR_!!741486021.jpg",
                "membershipAllowance": 142,
                "membershipCash": 79,
                "platform": "SOURCE_TYPE_TAOBAO",
                "shareMembershipCash": 142,
                "shareNormalCash": 79,
                "shortTitle": "【40颗】黑炭郎8倍清洁洗衣凝珠",
                "sourceIID": "610111784893"
              }
        ]

- 下单成功接口
    - http://10.105.14.211:81/order/placeOrder?user_id=5062573&product_id=585319218965&platform=1&flag=ok
    - user_id：用户ID
    - platform：1-淘宝；2-拼多多；3-京东
    - product_id：商品ID，需要与platform对应
    - flag: ok

.. code-block::

    response = {
                  "code": 0,
                  "data": {
                    "order_ids": [
                      "123456533592"
                    ]
                  },
                  "msg": ""
                }

- 下单成功接口（预售）
    - http://10.105.14.211:81/order/placePresaleOrder?user_id=5062573&product_id=585319218965&platform=1&flag=presale
    - user_id：用户ID
    - platform：1-淘宝；2-拼多多；3-京东
    - product_id：商品ID，需要与platform对应
    - flag: presale

.. code-block::

    response = {
                  "code": 0,
                  "data": {
                    "order_ids": [
                      "123456185568"
                    ]
                  },
                  "msg": ""
                }


- 取消订单接口
    - http://10.105.14.211:81/order/placeCancelOrder?user_id=5062573&product_id=585319218965&platform=1&flag=cancel
    - user_id：用户ID
    - platform：1-淘宝；2-拼多多；3-京东
    - product_id：商品ID，需要与platform对应
    - flag: cancel

.. code-block::

    response = {
                  "code": 0,
                  "data": {
                    "order_ids": [
                      "123456452454"
                    ]
                  },
                  "msg": ""
                }

- 维权订单接口
    - http://10.105.14.211:81/order/placeRightOrder?user_id=5062573&product_id=585319218965&platform=1&flag=right
    - user_id：用户ID
    - platform：1-淘宝；2-拼多多；3-京东
    - product_id：商品ID，需要与platform对应
    - flag: right

.. code-block::

    response = {
                  "code": 0,
                  "data": {
                    "order_ids": [
                      "123456548575"
                    ]
                  },
                  "msg": ""
                }

- 外卖订单下单成功接口
    - http://10.105.14.211:81/order/palceTakeoutOrder?user_id=5062573&platform=4&flag=ok
    - user_id：用户ID
    - platform：4-饿了么；5-美团；7-KFC
    - flag: ok

.. code-block::

    response = {
                  "code": 0,
                  "data": {
                    "order_ids": [
                      "123456308849"
                    ]
                  },
                  "msg": ""
                }


- 外卖订单下单取消接口
    - http://10.105.14.211:81/order/palceTakeoutCancelOrder?user_id=5062573&platform=4&flag=cancel
    - user_id：用户ID
    - platform：4-饿了么；5-美团；7-KFC
    - flag: cancel

.. code-block::

    response = {
                  "code": 0,
                  "data": {
                    "order_ids": [
                      "123456181105"
                    ]
                  },
                  "msg": ""
                }


- 外卖订单下单维权接口
    - http://10.105.14.211:81/order/palceTakeoutRigntOrder?user_id=5062573&platform=4&flag=right
    - user_id：用户ID
    - platform：4-饿了么；5-美团；7-KFC
    - flag: right

.. code-block::

    response = {
                  "code": 0,
                  "data": {
                    "order_ids": [
                      "123456146340"
                    ]
                  },
                  "msg": ""
                }