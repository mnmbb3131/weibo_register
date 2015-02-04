headers = {
"Host": "huodong.weibo.com",
"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0",
"Accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language': 'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3',
'Accept-Encoding':' gzip, deflate',
'Content-Type':' application/x-www-form-urlencoded',
'X-Requested-With':' XMLHttpRequest',
'Referer':' http://huodong.weibo.com/hongbao',
'Cookie':' UOR=www.jq22.com,widget.weibo.com,login.sina.com.cn; SUBP=0033WrSXqPxfM72wWs9jqgMF55529P9D9Whn_MUFrOI7WWQGviSQbJWA5JpV2s8yMcx09s8092WpMC4odcXt; SINAGLOBAL=8177432161489.339.1420704536530; ULV=1423021802177:4:3:3:9035661063700.262.1423021802145:1422880157764; SUB=_2AkMjjG5HdcNhrAZUmP8SzW_lZI5Xm1m37ZWlYQ2IZ2JCMnoQgT5nqiRotBF_DN6U60e6fQafk4o6rwbF2go26bqTAjY9Ih4.; SUHB=0tK6lVaFozFzq7; myuid=5507714783; un=979847383@qq.com; CONTENT-HUATI-G0-YF=081466c46ce96d1bd9623974d58a345e; _s_tentry=-; Apache=9035661063700.262.1423021802145; WBStore=3f8ca8cd96b39592|undefined',
'Connection':' keep-alive'
}

for num in range(50):
    wb_url = "http://huodong.weibo.com/aj_hongbao/top?page="+str(num)+"&ajtarget=topTargetU&transName=home_top&type=hot&daily=0&_t=0&__rnd=1423021821988"
    wb_json = requests.get(wb_url,headers=headers)
    if wb_json.status_code == 200:
        real_html = BeautifulSoup(wb_json.json()["data"]['html'])
        for li in  real_html.find(class_="list list_box2").find_all("li"):
            if li.find_all("span",class_="list_txt")[2].text.strip() == u"礼品价值0元":
                for add in li.find_all("a",class_="btn rob_btn"):
                    red_url =  add["href"]
                    result = BeautifulSoup(requests.get(red_url).content).find_all("span",class_ = "red_end")#一个list来承载着"抢光了"的信息
                    if len(result)==0:
                        print "Hey! Brothers!We find the treasure!"
                        print "The address is=>",red_url
                        for name in li.find_all("p",class_="name"):
                            print name.text.strip()
                        for money in li.find_all("span",class_="list_txt list_money"):
                            print money.text.strip()
                        print "*"*50

