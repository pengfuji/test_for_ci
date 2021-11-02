#!/usr/bin/python
# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText # 导入 MIMEText 类
from email.mime.multipart import MIMEMultipart  #导入MIMEMultipart类
from email.mime.image import MIMEImage   #导入MIMEImage类

HOST = "smtp.163.com" # 定义 smtp 主机
SUBJECT = u"系统性能报表" # 定义邮件主题
TO = "jpf2271498@126.com" # 定义邮件收件人
FROM = "jpf2271498@163.com" # 定义邮件发件人

def addimg(src,imgid):   #定义图片读取函数，参数1为图片路径，2为图片ID机标识符
    with open(src,'rb') as f:
        msgimage = MIMEImage(f.read())   #读取图片内容
    msgimage.add_header('Content-ID',imgid)  #指定文件的Content-ID,<img>,在HTML中图片src将用到
    return msgimage

msg = MIMEMultipart('related')  #创建MIMEMultipart对象，采用related定义内嵌资源邮件体

test = """  
<table width="600" border="0" cellspacing="0" cellpadding="4">
    <tr bgcolor="#CECFAD" height="20" style="font-size:14px">
        <td colspan=2>*系统性能数据 <a href="10.0.0.10"> 更多 >></a></td>
    </tr>
    <tr bgcolor="#EFEBDE" height="100" style="font-size:13px">
        <td>
            <img src="cid:io">   #图片地址由MIMEMultipart通过ID传递
        </td>
        <td>
            <img src="cid:key_hit">
        </td>
    </tr>
    <tr bgcolor="#EFEBDE" height="100" style="font-size:13px">
        <td>
            <img src="cid:men">
        </td>
        <td>
            <img src="cid:swap">
        </td>
    </tr>
</table>
"""
msgtext = MIMEText(test,"html","utf-8") #创建Text对象内容，包括图片<img>

msg.attach(msgtext)   #MIMEMultipart对象附加MIMEText的内容
msg.attach(addimg("1.png",'io'))  #附加图片内容，io指向HTML文本内的参数

msg['Subject'] = SUBJECT # 邮件主题
msg['From']=FROM # 邮件发件人 , 邮件头部可见
msg['To']=TO # 邮件收件人 , 邮件头部可见
try:
    server = smtplib.SMTP() # 创建一个 SMTP() 对象
    server.connect(HOST,"25") # 通过 connect 方法连接 smtp 主机
    server.starttls() # 启动安全传输模式
    server.login("jpf2271498@163.com","XFSGXTJXGAKQHEZL") # 邮箱账号登录校验
    server.sendmail(FROM, TO, msg.as_string()) # 邮件发送
    server.quit() # 断开 smtp 连接
    print("邮件发送成功！")
except Exception as e:
    print('失败：'+str(e))
