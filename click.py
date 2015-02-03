#coding：utf-8
import Image
import os,requests
from bs4 import BeautifulSoup
import shutil
def get_the_code():
        url = "http://weibo.com/signup/signup.php"#微博注册的地址
        headers = {"Cookie":" lang=en-us;"}#假装自己是老外（这样就可以免去输入手机验证码了）
        html = requests.get(url,headers=headers).content
        html = BeautifulSoup(html)#处理获取的网页
        code_tag = html.find_all(class_ ="code")
        code_add = "http://weibo.com"+code_tag[0].img.attrs['src']
        img = requests.get(code_add,stream=True)
        if requests.get(code_add).status_code ==200:#把验证码下载到本地
            with open("code.jpg",'wb') as f:
                shutil.copyfileobj(img.raw,f)
        code_img = Image.open("code.jpg")#打开图片
        return code_img
