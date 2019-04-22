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
        response=requests.post("https://www.douban.com/",
                      data=payload,
                      cookies={"Cookie":'''ll="108288"; bid=ufm8svqInPI; __utmc=30149280; douban-fav-remind=1; gr_user_id=4171796e-842c-4c4a-90a0-26e6738a48d0; _vwo_uuid_v2=DCD0C06E626E1D6DFE13B60EAD6341A39|d72f1edb0d54ead74d312fdccc346905; __yadk_uid=D5htNM4K5N9sqGUCr3fbvz5kAD82ZqNh; push_noty_num=0; push_doumail_num=0; __utmv=30149280.4603; dbcl2="46030598:CTVyUd554yw"; ck=V0h1; ap_v=0,6.0; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1555902253%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_ses.100001.8cb4=*; __utma=30149280.526818714.1553674558.1555585905.1555902254.24; __utmz=30149280.1555902254.24.6.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmt=1; _pk_id.100001.8cb4=159c3a6479396543.1553674557.21.1555902320.1555585898.; __utmb=30149280.4.10.1555902254'''},
                      proxies=proxies,verify=False,
                      param={"ck":"V0h1","comment":"test"})
        print(response.headers)
        print(response.status_code)
        print(response.json())

    def test_httpbin(self):
        # proxies = {
        #     'http': 'http://10.231.21.243:8888',
        #     'https': 'http://10.231.21.243:8888',
        # }
        payload = {'key1': 'value1', 'key2': 'value2'}
        a = requests.post("http://httpbin.org/post", data=payload).text
        print(a)


    def test_httpbin2(self):
        # proxies = {
        #     'http': 'http://10.231.21.243:8888',
        #     'https': 'http://10.231.21.243:8888',
        # }
        # //请求内容为json表单
        payload = {'key1': 'value1', 'key2': 'value2', "key3":{"key4":[1,2,3]}}
        a = requests.post("http://httpbin.org/post",
                      json=payload).text
        print(a)

    def test_auth(self):
        print(requests.get("http://httpbin.org/basic-auth/username/pw",auth={"user": "username","passwd":"pw"}).text)