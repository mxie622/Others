

import smtplib
from email.Message import Message
from time import sleep

smtpserver = 'smtp.gmail.com'
username = 'mxie622@gmail.com'    #
password = '****'                 #
from_addr = 'mxie622@gmail.com'   #
to_addr = 'mxie622@gmail.com'  #
cc_addr = 'huzhenwei@csdn.net'  #


message = Message()
message['Subject'] = 'Mail Subject' #
message['From'] = from_addr
message['To'] = to_addr
message['Cc'] = cc_addr
message.set_payload('Massage body')   #
msg = message.as_string()


sm = smtplib.SMTP(smtpserver, port=587, timeout=20)
sm.set_debuglevel(1)
sm.ehlo()
sm.starttls()
sm.ehlo()
sm.login(username, password)
sm.sendmail(from_addr, to_addr, msg)
sleep(5)
sm.quit()

# Turn on the less secure:

# Gmail ----> google account -----> security ------>  Less secure app access (Turn on)

#--------

# Thanks for : https://blog.csdn.net/huzhenwei/article/details/7524989