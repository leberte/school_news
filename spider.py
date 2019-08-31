# _*_ coding: utf-8 _*_
from bs4 import BeautifulSoup
import requests
from sendmail import mailcuowu

def get_deaninfo():
    url = 'http://jiaowu.swjtu.edu.cn/servlet/NewsAction?Action=NewsMore'
    HOST = 'http://jiaowu.swjtu.edu.cn'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'Host': HOST.replace('http://', ''),
        'Referer': "http://jiaowu.swjtu.edu.cn/index.html"
    }
    a= []
    try:
        response = requests.get(url, headers=headers,timeout = 10)
        info = BeautifulSoup(response.content,"html.parser")
        result1 = info.find_all('li',{'class':'newsLi6_1'})
        result2 = info.find_all('li',{'class':'newsLi6_2'})
        result = result1 + result2
        for i in range (len(result)):
            info2 = BeautifulSoup(str(result[i]),"html.parser")
            lj = info2.find('a').attrs['href']
            lianjie = HOST + lj.replace('.','')
            title = info2.find('a').text
            time = info2.find('div',{'style':'float:left;width:75px; text-align:center; overflow:hidden;'}).text
            a.append([time,lianjie,title])
    except Exception as e:
        pass
    return a

def get_yanghau():
    url2 = 'https://yanghua.swjtu.edu.cn/WebSite/Head/AcademyBulletin.aspx?CollegeNo=001'
    headers2 = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'Host': 'yanghua.swjtu.edu.cn',
        'Referer': "https://yanghua.swjtu.edu.cn/WebSite/Head/AcademyBulletin.aspx?CollegeNo=001"
    }
    a = []
    t = 5
    try:
        response2 = requests.post(url2, headers = headers2 ,timeout = 20)
        info2 = BeautifulSoup(response2.content, "html.parser")
        result_y = info2.find_all('table',{'width':'94%'})
        info3 = BeautifulSoup(str(result_y[0]),"html.parser")
        result_detail = info3.find_all('tr')
        for i in result_detail:
            info_y = BeautifulSoup(str(i), "html.parser")
            hhh = info_y.find('td',{'width':'514'})
            lj2 = 'https://yanghua.swjtu.edu.cn/WebSite/Head/'+hhh.find('a').attrs['href']
            title2 = hhh.text.replace(')','').split('(')
            title3 = title2[0]
            time = title2[1]
            a.append([time, lj2, title3])
    except Exception as e:
        pass
    return a

def vatuu():
    url ='http://jwc.swjtu.edu.cn/vatuu/NewsAction?setAction=NewsMore&type=form'
    HOST = 'jwc.swjtu.edu.cn'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'Host': HOST.replace('http://', '')
    }
    a= []
    try:
        response = requests.get(url, headers=headers,timeout = 10)
        info = BeautifulSoup(response.content,"html.parser")
        result = info.find_all('div',{'class':'littleResultDiv'})
        for i in range (len(result)):
            info2 = BeautifulSoup(str(result[i]),"html.parser")
            title = info2.find('h3').find('a').text
            lianjie = 'http://'+ HOST + info2.find('p',{'class':'relativeInfo clearfix'}).find('a').attrs['href'].replace('.','')
            time = info2.find('p',{'class':'relativeInfo clearfix'}).find_all('span')[0].text
            a.append([time,lianjie,title])
    except Exception as e:
        pass
    return a


def get_new_yanghau():
    url2 = 'http://xg.swjtu.edu.cn/web'
    headers2 = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
        'Host': 'xg.swjtu.edu.cn',
        'Referer': "http://xg.swjtu.edu.cn/"
    }
    a = []
    result_detail2 = []
    t = 5
    try:
        response2 = requests.post(url2, headers = headers2 ,timeout = 20)
        info2 = BeautifulSoup(response2.content, "html.parser")
        result_y = info2.find_all('div',{'class':'main-box mar_t15 w_1000 clearfloat'})
        #print(result_y)
        for i in result_y :
            #print(i)
            info3 = BeautifulSoup(str(i),"html.parser")
            #print(type(info3))
            result_detail = info3.find_all('li')
            result_detail2 += result_detail
        #print(result_detail2)
        for i in result_detail2:
            info_y = BeautifulSoup(str(i), "html.parser")
            lj2 = 'http://xg.swjtu.edu.cn'+info_y.find('a').attrs['href']
            title = info_y.find('a').text
            time = info_y.find('span').text
            a.append([time, lj2, title])
        #print(a)
    except Exception as e:
        pass
    return a
	
def tumu():
    url ='https://civil.swjtu.edu.cn/vatuu/WebAction?setAction=newsList&selectType=tongzhi'
    HOST = 'civil.swjtu.edu.cn'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'Host': HOST.replace('https://', ''),
        'Referer': 'https: // civil.swjtu.edu.cn / main / index.html'
    }
    a= []
    try:
        response = requests.get(url, headers=headers,timeout = 10)
        info = BeautifulSoup(response.content,"html.parser")
        result = info.find_all('li',{'class':'news-list-item clearfix'})
        for i in range (len(result)):
            info2 = BeautifulSoup(str(result[i]),"html.parser")
            title = info2.find('div').find('a').text
            lianjie = 'https://'+ HOST + info2.find('div',{'class':'right'}).find('a').attrs['href'].replace('.','')
            time = info2.find('div',{'class':'news-info clearfix'}).find_all('span')[0].text.replace(' ','')[0:10]
            a.append([time,lianjie,title])
    except Exception as e:
        pass
    return a
