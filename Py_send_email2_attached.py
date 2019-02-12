import urllib, urllib2
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

username = 'mxie622@gmail.com'
password = 'xms19911227'
sender = username
receivers = ','.join(['mxie622@aucklanduni.ac.nz'])

# 如名字所示： Multipart就是多个部分
msg = MIMEMultipart()
msg['Subject'] = 'Python mail Test'
msg['From'] = sender
msg['To'] = receivers

# 下面是文字部分，也就是纯文本
puretext = MIMEText('text_part，')
msg.attach(puretext)

# 下面是附件部分 ，这里分为了好几个类型

# 首先是xlsx类型的附件
xlsxpart = MIMEApplication(open('diabetes.xlsx', 'rb').read())
xlsxpart.add_header('Content-Disposition', 'attachment', filename='diabetes.xlsx')
msg.attach(xlsxpart)

# txt files
txtpart = MIMEApplication(open('stopwords.txt', 'rb').read())
txtpart.add_header('Content-Disposition', 'attachment', filename='stopwords.txt')
msg.attach(txtpart)

# jpg类型的附件
# jpgpart = MIMEApplication(open('beauty.jpg', 'rb').read())
# jpgpart.add_header('Content-Disposition', 'attachment', filename='beauty.jpg')
# msg.attach(jpgpart)

# mp3类型的附件
# mp3part = MIMEApplication(open('kenny.mp3', 'rb').read())
# mp3part.add_header('Content-Disposition', 'attachment', filename='benny.mp3')
# msg.attach(mp3part)

##  下面开始真正的发送邮件了
try:
    client = smtplib.SMTP()
    client.connect('smtp.gmail.com')
    client.login(username, password)
    client.sendmail(sender, receivers, msg.as_string())
    client.quit()
    print('带有各种附件的邮件发送成功！')
except smtplib.SMTPRecipientsRefused:
    print('Recipient refused')
except smtplib.SMTPAuthenticationError:
    print('Auth error')
except smtplib.SMTPSenderRefused:
    print('Sender refused')
except smtplib.SMTPException,e:
    print (e.message)