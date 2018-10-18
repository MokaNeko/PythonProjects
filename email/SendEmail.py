from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


to_addr = 'Moii_RB@163.com'
Title = input('Title: ')
Content = input('Content: ')

from_addr = 'Moii_RB@163.com'
password = '4tyanwakuzu'
smtp_server = 'smtp.163.com'

from_msg = '%s%s' % ('GlaDos', ' <%s>')
to_msg = '%s%s' % ('Server', ' <%s>')

msg = MIMEText(Content, 'plain', 'utf-8')
msg['From'] = _format_addr(from_msg % from_addr)
msg['To'] = _format_addr(to_msg % to_addr)
msg['Subject'] = Header(Title, 'utf-8').encode()

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
