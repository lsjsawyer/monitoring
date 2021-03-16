# -*- coding: utf-8 -*-
import requests
import json



def msg(text):
    token = "2145e5f2c38489b83a59ab04c4f1bef48421ffe30a5b2df8b7bccbc78f2f0326"
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    api_url = f"https://oapi.dingtalk.com/robot/send?access_token={token}"
    json_text = {
        "msgtype": "text",
        "text": {
            "content": text
        }
    }
    requests.post(api_url, json.dumps(json_text), headers=headers)
