"""
主要测试 cnode社区的话题相关的功能
主要api包括：
1.  主题首页
"""
# 引入第三方模块
import requests

import business.common as common

def test_topic_page():
    """
    测试主题首页功能
    get请求方法
    url： http://49.233.108.117:3000/api/v1/topics
    :return:
    """
    # 1. 发送get请求
    url = 'http://49.233.108.117:3000/api/v1/topics'
    getdata={
        "page":1,
        "tab":"ask",
        "limit":100,
        "mdrender":"true"
    }
    res = requests.get(url=url,params=getdata)
    print(res)
    # 2.查看状态码
    print('状态码：',res.status_code)
    # 3. 查看json结果
    # print(res.json())

    jsondata = res.json()
    data = jsondata['data']
    # print(len(data))
    assert len(data) == 1

    for d in data:
        # print(d['tab'])
        assert d['tab']=='ask'
        # if d['tab'] != 'ask':
        #     print('数据验证失败')

def test_create_topic():
    """
    创建主题
    :return:
    """
    create_url = "http://49.233.108.117:3000/api/v1/topics"
    post_data = {"accesstoken":"8aac85ba-e4b2-4093-ac23-b4154fcca626",
                 "title":"helloworld",
                 "tab":"ask",
                 "content":"xxxxxxxxxx"}
    res1 = requests.post(url=create_url,data=post_data)

    res2 = requests.post(url=create_url, data=post_data)
    # print(res.status_code)
    assert res1.status_code == 200
    res1_topic_id = res1.json()['topic_id']
    res2_topic_id = res2.json()['topic_id']
    assert not res1_topic_id == res2_topic_id

def test_topic_detail():
    """
    主题详情
    :return:
    """
    post_data = {"accesstoken": common.get_token(),
                 "title": "helloworld",
                 "tab": "ask",
                 "content": "xxxxxxxxxx"}
    topic_id = common.create_topic(post_data)

    url = "http://49.233.108.117:3000/api/v1/topic/"+topic_id
    res = requests.get(url)
    # print(res.status_code)
    assert res.status_code == 200
    # print(res.json())
    jsondata = res.json()
    # 断言title字段
    assert post_data['title'] == jsondata['data']['title']
    assert post_data['tab'] == jsondata['data']['tab']
    assert post_data['content'] in jsondata['data']['content']

def test_topic_update():
    """
    编辑主题
    :return:
    """
    post_data = {"accesstoken": common.get_token(),
                 "title": "helloworld",
                 "tab": "ask",
                 "content": "xxxxxxxxxx"}
    topic_id = common.create_topic(post_data)

    url="http://49.233.108.117:3000/api/v1/topics/update"
    update_data = {"accesstoken": common.get_token(),
                 "title": "helloworld1234",
                 "tab": "ask",
                 "topic_id":topic_id,
                 "content": "xxxxxxxxxx1234"}

    res= requests.post(url,data=update_data)
    print(res.json())

    # 更新后的id 与原来更新之前的id 保持一致。
    update_topic_id = res.json()['topic_id']
    assert topic_id == update_topic_id

    # 更新之后的内容进行断言
    # 1. 获取更新之后的内容
    res = common.get_topic_detail(update_topic_id)
    jsondata = res.json()
    # 断言title字段
    assert update_data['title'] == jsondata['data']['title']
    assert update_data['tab'] == jsondata['data']['tab']
    assert update_data['content'] in jsondata['data']['content']

def test_topic_collect():
    """
    主题收藏
    :return:
    """

def test_topic_de_collect():
    """
    取消收藏
    :return:
    """

def test_topic_from_user():
    """
    用户收藏的主题
    :return:
    """

def test_topic_reply():
    """
    话题评论
    :return:
    """

def test_reply_up():
    """
    评论点赞
    :return:
    """

def test_user_info():
    """
    用户详情
    :return:
    """

def test_user_accesstoken():
    """
    验证token的正确性
    :return:
    """

