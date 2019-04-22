import unittest
import requests
from hamcrest import *;

class login(unittest.TestCase):
    def test_topics_get(self):
        proxies = {
            'http': 'http://10.231.21.243:8888',
            'https': 'http://10.231.21.243:8888',
        }
        print(requests.get("https://testerhome.com/api/v3/topics.json",
                           params={"a":2},
                           headers={"header1":"header1 content"},
                           cookies={"user":"user content"},
                           proxies=proxies,verify=False).text)


    def test_topics_response(self):
        proxies = {
            'http': 'http://10.231.21.243:8888',
            'https': 'http://10.231.21.243:8888',
        }
        response = requests.get("https://testerhome.com/api/v3/topics.json",
                           params={"a":2},
                           headers={"header1":"header1 content"},
                           cookies={"user":"user content"},
                           proxies=proxies,verify=False)
        print(response.headers)
        print(response.status_code)
        print(response.json())
        print(response.encoding)
        # 对response断言
        print(len(response.json()["topics"]))

        json = response.json()
        #断言第一篇帖子的title包含招聘
        assert_that(json["topics"][0]["title"],contains_string("招聘"))
        #断言topic的个数大于20
        assert_that(len(response.json()["topics"]),less_than(20))


    def test_topics_post(self):
        proxies = {
            'http': 'http://10.231.21.243:8888',
            'https': 'http://10.231.21.243:8888',
        }
        payload = {'key1': 'value1', 'key2': 'value2'}
        requests.post("https://httpbin.org/post",
                      data=payload,
                      cookies={"user":"user content"},
                      proxies=proxies,verify=False)