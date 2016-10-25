# coding: utf-8

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders


class MailSender(object):
    def __init__(self, server, port, mail_from):
        self.server = smtplib.SMTP(server, port)
        self.mail_from = mail_from

    def __del__(self):
        self.server.quit()

    def send(self, mail_to, subject, message, attach):
        mail = MIMEMultipart()
        mail['From'] = self.mail_from
        mail['To'] = mail_to
        mail['Subject'] = subject

        mail.attach(MIMEText(message, "plain", "utf-8"))

        with open(attach, 'r') as fd:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(fd.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition',
                            'attachment; filename={0}'.format(attach))

        mail.attach(part)

        self.server.sendmail(self.mail_from, mail_to, mail.as_string().encode('ascii'))
