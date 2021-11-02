#!/usr/bin/python3
#-*- coding: UTF-8 -*-


from __future__ import print_function
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

SMTP_SERVER = 'smtp.163.com'
SMTP_PORT = 25

def send_mail(user,pwd,to,subject):
    msg = MIMEMultipart('mixed')
    msg['From'] = user
    msg['To'] = to
    msg['subject'] = Header(subject,'utf-8')

    text_info = '简单测试一下连通性'          # <----在次添加需要发送 text_info 的内容
    text_sub = MIMEText(text_info,'plain','utf-8')
    text_sub.add_header('Content-Disposition','attachment',filename = "text")
    msg.attach(text_sub)

    html_info = """
    <table width="800" border="0" cellspacing="0" cellpadding="4">
          <tr>
            <td bgcoclor="#CECFAD" height="20" STYLE="font-size:14px">*官网数据 <a
href="monitor.domain.com">更多>><\a><\d>
          </tr>
          <tr>
            <td bgcolor="#EFEBDE" height="100" style="font-size:13px">
            1) 日访问量 :<font color=red>152433</font> 访问次数:23651 页面浏览量: 45123 点击数: 545122 数据流量: 504Mb<b
r>
            2) 状态码信息 <br>
            &nbsp;&nbsp;500:105    404:3264   503:214<br>
            3) 访问浏览信息 <br>
             &nbsp;&nbsp;IE:50% firefox:10% chrome:30% other:10%<br>
            4) 页面信息 <br>
            &nbsp;&nbsp;/index.php 42153<br>
            &nbsp;&nbsp;/view.php 21451<br>
            &nbsp;&nbsp;/login.php 5112<br>
          </tr>
    </table>"""         # <----在次添加需要发送 html_info 的内容
    html_sub = MIMEText(html_info,'html','utf-8')
    msg.attach(html_sub)

    image_info = open(r'/root/python3/smtp/1.jpg','rb').read()     #  将 src 改为需要添加的 图片文件路径
    image_sub = MIMEImage(image_info)
    image_sub.add_header('Content-ID', '<image1>')
    image_sub.add_header('Content-Disposition','attachment',filename = "美女.jpg")    # <--- "" 添加重命名的图片文件名 例如：xxx.jpg xxx.png
    msg.attach(image_sub)

    file_info = open(r'/root/python3/smtp/linux运维工程师.pdf','rb').read()
    file_sub = MIMEText(file_info,'base64','utf-8')
    file_sub['Content-Type'] = 'application/octet-stream'
    file_sub.add_header('Content-Disposition','attachment',filename = "简历.pdf")         # <---- "" 中添加重命名的文件名称
    msg.attach(file_sub)

    smtp_server = smtplib.SMTP()
    try:
        smtp_server.connect(SMTP_SERVER,SMTP_PORT)
        smtp_server.login(user,pwd)
        smtp_server.sendmail(user,to,msg.as_string())
    except Exception as e:
        print("邮件发送失败！！请检测代码！以下是错误输出 :")
        print(e)
    finally:
        print("邮件发送成功！！")
        smtp_server.quit()

def main():

    send_mail('jpf2271498@163.com','XFSGXTJXGAKQHEZL','jpf2271498@126.com','This is a test!!')

if __name__ == '__main__':
    main()

