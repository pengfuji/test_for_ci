#!/usr/bin/python
#-*- coding: utf-8 -*-

import smtplib
import string


HOST = "smtp.163.com"
SUBJECT = "Test email from python"
TO = "jpf2271498@126.com"
FROM = "jpf2271498@163.com"
text = "Python rules them all!"
BODY = string.join((                         # 组装sengmaild 的方法的邮件的主题内容，各段以'\r\n'进行隔离
        "From: %s"% FROM,
        "TO: %s"% TO,
        "SUBJECT:%s"% SUBJECT,
        "",
        text
        ),"\r\n")

server = smtplib.SMTP()
server.connect(HOST,"25")
server.starttls()
server.login("jpf2271498@163.com","XFSGXTJXGAKQHEZL")
server.sendmail(FROM,[TO],BODY)
server.quit()

