import smtplib
from email.Message import Message
from time import sleep
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os
print(os.path.dirname(__file__))

smtpserver = 'smtp.gmail.com'
username = 'mxie622@gmail.com'    #
password = '****'                 #
from_addr = 'mxie622@gmail.com'   #
to_addr = 'mxie622@gmail.com'  #
# cc_addr = 'huzhenwei@csdn.net'  #


message = Message()
message['Subject'] = 'Mail Subject' #
message['From'] = from_addr
message['To'] = to_addr
# message['Cc'] = cc_addr
message.set_payload('Massage body')   #
# msg = message.as_string()

msg = MIMEMultipart()
part = MIMEApplication(open('keras.pdf','rb').read()) #
part.add_header('Content-Disposition', 'attachment', filename="keras.pdf") #
msg.attach(part)

sm = smtplib.SMTP(smtpserver, port=587, timeout=20)
sm.set_debuglevel(1)
sm.ehlo()
sm.starttls()
sm.ehlo()
sm.login(username, password)
sm.sendmail(from_addr, to_addr, msg.as_string())
sleep(5)
sm.quit()

