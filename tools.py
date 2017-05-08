# -*- coding: utf-8 -*-
import requests
import os
import sys
import smtplib
import mimetypes
from optparse import OptionParser
from email import encoders
from email.message import Message
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.utils import COMMASPACE, formatdate
import csv
import pandas as pd







def envia_email(frm, to,subject, files, html_text, files_body):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = frm
    msg['To'] = to

    mnt_html = None

    if files is not None:    files = files.split(',')

    if files_body is not None:    files_body = files_body.split(',')

    html = html_text

    #df = pd.read_csv("C:\\Users\\herculanocm\\Documents\\bodii.txt",delimiter=';',encoding='utf-8')

    for fb in files_body or []:
        if os.path.isfile(fb.strip()):
            print("Anexando arquivo ao corpo do email : ", (fb))
            df = pd.read_csv(fb.strip(), delimiter=';', encoding='utf-8')
            html += "<br><br>"
            html += df.to_html()





    # Record the MIME types of both parts - text/plain and text/html.

    part2 = MIMEText(html, 'html')
    #print (files)
    #fileMsg = MIMEBase('application', 'vnd.ms-excel')
    #fileMsg.set_payload(file(files).read())
    for f in files or []:
       if os.path.isfile(f.strip()):
           print ("Arquivo existe : ", (f))
           with open(f.strip(), "rb") as fil:
                part = MIMEApplication(
                fil.read(),
                Name=basename(f)
                )
                part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
                msg.attach(part)
       else:
           print ("Arquivo não existe : ", (f))

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.

    msg.attach(part2)

    # Send the message via local SMTP server.
    s = smtplib.SMTP('UDPRELAYAP01')

    # sendmail function takes 3 arguments: sender's address, recipient's address
    # and message to send - here it is sent as one string.


    s.sendmail(frm,to, msg.as_string())
    s.quit()