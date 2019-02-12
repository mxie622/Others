# import urllib, urllib2
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

username = 'mxie622@gmail.com'
password = 'xms19911227'
sender = username
receivers = ','.join(['mxie622@aucklanduni.ac.nz'])

# Multipart
msg = MIMEMultipart()
msg['Subject'] = 'Python mail Test'
msg['From'] = sender
msg['To'] = receivers

# pure text
puretext = MIMEText('text_part，')
msg.attach(puretext)

# attached

# xlsx
xlsxpart = MIMEApplication(open('diabetes.xlsx', 'rb').read())
xlsxpart.add_header('Content-Disposition', 'attachment', filename='diabetes.xlsx')
msg.attach(xlsxpart)

# txt files
txtpart = MIMEApplication(open('stopwords.txt', 'rb').read())
txtpart.add_header('Content-Disposition', 'attachment', filename='stopwords.txt')
msg.attach(txtpart)

# jpg
# jpgpart = MIMEApplication(open('beauty.jpg', 'rb').read())
# jpgpart.add_header('Content-Disposition', 'attachment', filename='beauty.jpg')
# msg.attach(jpgpart)

# mp3
# mp3part = MIMEApplication(open('kenny.mp3', 'rb').read())
# mp3part.add_header('Content-Disposition', 'attachment', filename='benny.mp3')
# msg.attach(mp3part)

##  sending
try:
    client = smtplib.SMTP()
    client.connect('smtp.gmail.com')
    client.login(username, password)
    client.sendmail(sender, receivers, msg.as_string())
    client.quit()
    print('success！')
except smtplib.SMTPRecipientsRefused:
    print('Recipient refused')
except smtplib.SMTPAuthenticationError:
    print('Auth error')
except smtplib.SMTPSenderRefused:
    print('Sender refused')
# except smtplib.SMTPException,e:
#     print(e.message)