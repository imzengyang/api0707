"""
常用功能：
1. 发布话题
"""
import requests
def create_topic(topic_data):
    create_url = "http://49.233.108.117:3000/api/v1/topics"

    res_create_topic = requests.post(url=create_url, data=topic_data)
    topic_id = res_create_topic.json()['topic_id']
    return topic_id

def get_topic_detail(topic_id):
    url = "http://49.233.108.117:3000/api/v1/topic/" + topic_id
    res = requests.get(url)
    return res

def get_token():
    """
    获取最新的token值
    :return:
    """
    return "8aac85ba-e4b2-4093-ac23-b4154fcca626"