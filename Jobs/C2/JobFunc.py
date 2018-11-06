# -*- encoding:UTF-8 -*-
from libs.Utility import Mail
from libs.Utility import ConsolePrint
from libs import Utility
from libs import Environment as Env
from Config import Path
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

sep = " *|* "

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


def parse_version_config(config_path=None):
    config_path = config_path if config_path else Path.__CONFIG_PATH
    with open(config_path) as old:
        config = dict()
        for line in old.readlines():
            tmp = line.strip('\r\n').split(sep)
            config[tmp[0]] = tmp[1]
    config['Edition'] = '{0:02d}'.format(int(config['Edition']))
    config['Release'] = '{0:02d}'.format(int(config['Release']))
    config['Internal'] = '{0:03d}'.format(int(config['Internal']) + 1)
    version_name = "{p}-{h}-{m}-{r}".format(p=config['Project'], h=config['HW'], m=config['Market'],
                                            r=config['Reserved'])
    version_number = '{e}.{r}.{i}'.format(e=config['Edition'], r=config['Release'], i=config['Internal'])
    version = '{name}-{number}'.format(name=version_name, number=version_number)
    with open(config_path, 'w') as new:
        for attr_name in ['Project', 'HW', 'Market', 'Reserved', 'Edition', 'Release', 'Internal']:
            new.write('{name}{sep}{value}\n'.format(name=attr_name, sep=sep, value=config[attr_name]))
    print version
    return version


if __name__ == '__main__':
    parse_version_config('D:\Profile\Desktop\C2.txt')
