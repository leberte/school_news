#!/user/bin/python3
# _*_ coding: utf-8 _*_

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from jinja2 import Environment, FileSystemLoader
import time

smtpserver = 'smtp.163.com'
username = 'massage_swjtu@163.com'
password = 'x2511903043'
sender = 'massage_swjtu@163.com'
receiver = ['message<massage_swjtu@163.com>','houhou<2511903043@qq.com>','zhaoyue<3152666087@qq.com>','xujingwei<1724854636@qq.com>','xuyuming<805336427@qq.com>','weixiapeng<1099366657@qq.com>']
subject = Header('学校发送新通知啦！', 'utf-8').encode()

msg = MIMEMultipart('mixed')
msg['Subject'] = subject
msg['From'] = 'message <massage_swjtu@163.com>'
msg['To'] = ";".join(receiver)
msg['Cc'] = "message<massage_swjtu@163.com>"

def mailcuowu(e):
    text = "代码出现错误，原因%s"%e
    text_plain = MIMEText(text, 'plain', 'utf-8')
    msg.attach(text_plain)

    try:
        smtp = smtplib.SMTP()
        smtp.connect('smtp.163.com')
        smtp.login(username, password)
        smtp.sendmail(sender, receiver, msg.as_string())
        smtp.quit()
    except:
        pass


def mail_message(result):
    riqi = time.strftime("%Y-%m-%d", time.localtime())
    shijian = time.strftime("%H:%M:%S", time.localtime())
    env = Environment(loader=FileSystemLoader('/home/pi/Public/dean/templates', encoding='utf-8'))
    template = env.get_template('demo.html')
    html = template.render(results=result, riqi = riqi, shijian = shijian, encoding='utf-8')  # unicode string
    text_plain = MIMEText(html, 'html', 'utf-8')
    msg.attach(text_plain)

    try:
        smtp = smtplib.SMTP()
        smtp.connect('smtp.163.com')
        smtp.login(username, password)
        smtp.sendmail(sender, receiver, msg.as_string())
        smtp.quit()
    except:
        pass
