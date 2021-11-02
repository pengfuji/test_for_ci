#!/usr/bin/pthon
# -*- coding: utf-8 -*-


import smtplib
from email.mime.text import MIMEText # 导入 MIMEText 类
from email.mime.multipart import MIMEMultipart  #导入MIMEMultipart类
from email.mime.image import MIMEImage   #导入MIMEImage类
from email.mime.base import MIMEBase  #MIME子类的基类
from email import encoders   #导入编码器

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

#创建一个MIMEText对象，HTML元素包括文字与图片
msgtext = MIMEText("<font color=red> 官网业务周平均延时图表 :<br><img src=\"cid:weekly\"border=\"1\"><br> 详细内容见附件。</font>","html","utf-8")

msg.attach(msgtext)   #将msgtext内容附加到MIMEMultipart对象中
msg.attach(addimg("1.png",'weekly')) #使用MIMEMultipart对象附加MIMEImage的内容

#附件文件定义
#创建一个MIMEText对象，附加表格文件（week.xlsx）
filename = 'linux运维工程师.pdf'
attachfile = MIMEBase('applocation','octet-stream') #创建对象指定主要类型和次要类型
attachfile.set_payload(open(filename,'rb').read()) #将消息内容设置为有效载荷
attachfile.add_header('Content-Disposition','attachment',filename=('utf-8','',filename))  #扩展标题设置
encoders.encode_base64(attachfile)
msg.attach(attachfile) #附加对象加入到msg


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
