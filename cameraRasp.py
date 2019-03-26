from picamera import PiCamera
from time import sleep
import smtplib
gmail_user = 'enriquegonz1323@gmail.com'
gmail_password = 'aternosforeve23'
import time
from datetime import datetime
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import RPi.GPIO as GPIO
import time

toaddr = 'ayudacontustareas18@gmail.com'
me = 'enriquegonz1323@gmail.com'
Subject='security aleeeeert'

GPIO.setmode(GPIO.BCM)

P=PiCamera()
P.resolution= (1024,768)
P.start_preview()
    
GPIO.setup(23, GPIO.IN)
while True:
    if GPIO.input(23):
        print("Movimiento...")
        #camera warm-up time
        time.sleep(1)
        P.capture('movement2.jpg')
        time.sleep(4)
        subject='Security allert!!'
        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = me
        msg['To'] = toaddr

        fp= open('movement2.jpg','rb')
        img = MIMEImage(fp.read())
        fp.close()
        msg.attach(img)

        server = smtplib.SMTP_SSL('smtp.gmail.com',465)
