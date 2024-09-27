From="邮箱地址"
pwd="口令"
To2="目的邮箱地址"
import smtplib
from email.mime.text import MIMEText
import threading
import sys




def sendMail(message,head, From=From, pwd=pwd, To=To2):
    # login
    smtp=smtplib.SMTP_SSL('smtp.qq.com',465)
    print("[mail]:",smtp.connect('smtp.qq.com',465))
    print("[mail]:",smtp.login(From,pwd))

    # email
    mail = MIMEText(message)
    mail['Subject'] = head
    mail['From'] = From
    mail['To'] = To2

    # send
    smtp.sendmail(From, To, mail.as_string())
    print("[mail]:",'send email success')

    smtp.quit()
    
if __name__ == "__main__":
    sendMail(str(sys.argv[1]),str(sys.argv[2]))
