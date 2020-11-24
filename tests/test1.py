# -*- coding: utf-8 -*-
import requests
if __name__ == "__main__":
    s = requests.session()
    r = s.post('https://httpbin.org/anything', data={'hello': 'kevin'}, verify=False)
    # 返回文本型response
    print(r.text)
    # #返回文本型response，并用utf-8格式编码
    # # 当你用r.text得出的结果是不可读的内容例如包括类似xu'\xe1'或者有错误提示“'ascii' codec can't encode characters in position”时，可以用encode
    print(r.text.encode('utf-8'))
    # # 获取二进制返回值
    print(r.content)
    # # 获取请求返回码
    print(r.status_code)
    # 获取response的headers
    print(r.headers)
    # 获取请求返回的cookies
    s.get('http://google.com')
    print(s.cookies.get_dict())