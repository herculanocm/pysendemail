# -*- coding: utf-8 -*-

from tools import *
import sys

iterator = 0
frm = None
to= None
subject= None
body=None
att=None
files_body=None

for arg in sys.argv:
    iterator += 1
    if iterator == 2:
        frm=arg
        #1 argumento email from
    if iterator == 3:
        to=arg
        #2 argumento email to
    if iterator == 4:
        subject=arg
    if iterator == 5:
        att = arg
    if iterator == 6:
        body = arg
    if iterator == 7:
        files_body = arg



print ("From : ", (frm))
print ("To : ", (to))
print ("Subject : ", (subject))
print ("Body : ", (body))
print ("Att : ", (att))

#enviaEmail("herculanocm@algartech.com","herculanocm@algartech.com",'Assunto teste xls','<p>html text <b>bold</b> </p>',["C:\\Users\\herculanocm\\Documents\\teste.xls","C:\\Users\\herculanocm\\Documents\\outroTeste.xlsx"])

if iterator >= 5:
    print ("Enviando Email")
    envia_email(frm, to, subject, att, body, files_body)
else:
    print ("Email nao Enviado")

print ("Finalizado")