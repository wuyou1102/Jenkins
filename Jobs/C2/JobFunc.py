# -*- encoding:UTF-8 -*-
from libs.Utility import Mail
from libs.Utility import ConsolePrint
from libs import Utility
from libs import Environment as Env
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
mail_list = []
data = Utility.get_timestamp(time_fmt="%Y年%m月%d日 %H:%M", t=Env.BUILD_TIME)
content = """
<!DOCTYPE html>
<html>
<head>
<style>
h1 {
    color: black;
    font-family: verdana;
    font-size: 300%;
}
p  {
    color: black;
    font-family: courier;
    font-size: 160%;
}
</style>
</head>
<body>
    <div>
        <h1>
            <img src="http://www.sensethink.com/webimages/logo.jpg">
        </h1>
    </div>
    <div>
        <h1>{subject}</h1>
        <a href="
        """ + Env.BUILD_URL + """
">点击查看详情</a>
        <p align="right">""" + data + """</p>

        </div>
</body>
"""


def SendJobStartMail():
    mail = Mail.Mail()
    mail.add_receiver(*mail_list)
    subject = "%s:  Started" % Env.JOB_NAME
    mail.add_subject(subject)
    mail.add_content(
        content=content
            .replace("{subject}", subject)
            .replace("{body}", u"以后这里可以写点内容。"),
        _type="html")
    mail.send()


def SendJobFinishMail():
    mail = Mail.Mail()
    mail.add_receiver(*mail_list)
    subject = "%s:  Finished" % Env.JOB_NAME
    mail.add_subject(subject)
    mail.add_content(
        content=content
            .replace("{subject}", subject)
            .replace("{body}", u"以后这里可以写点内容。"),
        _type="html")
    mail.send()


def SendJobErrorMail():
    mail = Mail.Mail()
    mail.add_receiver(*mail_list)
    subject = "%s:  Error" % Env.JOB_NAME
    mail.add_subject(subject)
    mail.add_content(
        content=content
            .replace("{subject}", subject)
            .replace("{body}", u"以后这里可以写点内容。"),
        _type="html")
    mail.send()


def RaiseException(error, msg):
    ConsolePrint.error(msg=msg)
    SendJobErrorMail()
    raise error


if __name__ == '__main__':
    SendJobStartMail()
