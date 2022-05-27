import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
import config

def message():
    subject="ALERT!"

    msg=MIMEMultipart()
    msg['From']=config.USER_NAME
    msg['To']=config.USER_NAME
    msg['Subject']=subject

    body="There is some activity detected in your office.An image of the detected activity is attached with this alert mail.The remaining images are backed up in your system."
    msg.attach(MIMEText(body,'plain'))
    fp=open("screen5.png",'rb')
    img=MIMEImage(fp.read())
    fp.close()
    img.add_header('Content-Disposition', 'attachment', filename="screen5.png")
    msg.attach(img)

    s=smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login(config.USER_NAME,config.PASSWORD)
    s.sendmail(config.USER_NAME,config.USER_NAME,msg.as_string())
    s.quit()
print("Done")
