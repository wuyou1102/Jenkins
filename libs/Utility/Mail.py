# -*- encoding:UTF-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header


class Mail(object):
    def __init__(self):
        self.host = "smtp.163.com"
        self.sender = "SP_Jenkins@163.com"
        self.user = "SP_Jenkins"
        self.password = "Password01"
        self.port = 465
        self._type = "plain"
        self.subject = ""
        self.content = ""
        self.receiver = ['you.wu@sensethink.cn', 'wei.cheng@sensethink.com']

    def send(self):
        try:
            smtp = smtplib.SMTP_SSL(self.host, port=self.port)
            smtp.login(self.user, self.password)
            msg = MIMEText(self.content, self._type, 'utf-8')
            msg["Subject"] = Header(self.subject, 'utf-8')
            msg["From"] = self.sender
            msg["To"] = ','.join(self.receiver)
            smtp.sendmail(self.sender, self.receiver, msg.as_string())
            smtp.quit()
        except smtplib.SMTPException:
            print "Error: unable to send email"

    def add_subject(self, subject):
        self.subject = subject

    def add_content(self, content, _type="plain"):
        self._type = _type if _type.lower() in ["plain", "html"] else "plain"
        self.content = content

    def add_receiver(self, *receiver):
        for r in receiver:
            self.receiver.append(r)


if __name__ == '__main__':
    mail = Mail()
    mail.add_subject("今天天气真好")
    mail.add_content("""
    123
    4345
    sadjh
    """)
    mail.send()
