#!/usr/bin/python3

import smtplib
from email.mime.text import MIMEText

HOST = "smtp.163.com"
SUBJECT = u"官网流量数据报表"   # 定义 邮件主题
TO = "jpf2271498@126.com"     # 定义邮件收件人
FROM = "jpf2271498@163.com"   #定义邮件发件人
msg = MIMEText("""  
        <table width="800" border="0" cellspacing="0" cellpadding="4">
          <tr>
            <td bgcoclor="#CECFAD" height="20" STYLE="font-size:14px">*官网数据 <a
    href="monitor.domain.com">更多>><\a><\d>
          </tr>
          <tr>
            <td bgcolor="#EFEBDE" height="100" style="font-size:13px">
            1) 日访问量 :<font color=red>152433</font> 访问次数:23651 页面浏览量: 45123 点击数: 545122 数据流量: 504Mb<br>
            2) 状态码信息 <br>
            &nbsp;&nbsp;500:105    404:3264   503:214<br>
            3) 访问浏览信息 <br>
            &nbsp;&nbsp;IE:50% firefox:10% chrome:30% other:10%<br>
            4) 页面信息 <br>
            &nbsp;&nbsp;/index.php 42153<br>
            &nbsp;&nbsp;/view.php 21451<br>
            &nbsp;&nbsp;/login.php 5112<br>
          </tr>
        </table>""","html","utf-8")
msg['Subject'] = SUBJECT  #邮件主题
msg['From'] = FROM   # 邮件发件人邮件头部可见
msg['To'] = TO   #邮件收件人  邮件头部可见
try:
        server = smtplib.SMTP()
        server.connect(HOST,"25")
#        server.starttls()
        server.login("jpf2271498@163.com","XFSGXTJXGAKQHEZL")
        server.sendmail(FROM,TO,msg.as_string())
        server.quit()
        print("邮件发送成功")
except Exception as e:
        print("邮件发送失败："+str(e))
