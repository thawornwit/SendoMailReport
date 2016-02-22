#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText

class ReportMail(object):

    def Send(self, body, ticker):
        try:
            smtp = smtplib.SMTP('smtp.gmail.com', 587)
            smtp.starttls()

            smtp.login('email@email.com.br', 'senha')

            de = 'email@email.com.br'
            para = 'para@email.com.br'

            html = """\
                    <!DOCTYPE html>
                    <html>
                      <head>
                      </head>
                      <body>
                          <table style='width: 700px; border:1px;'>
                             <caption>SendMailReport</caption>
                             <tr style='background-color: #4CAF50'><td style='text-align: center; padding: 8px; color: #FFFFFF;'><strong>%s</strong></td></tr>
                             <tr style='background-color: #f2f2f2'><td style='padding: 8px;'>%s</td></tr>
                          </table>
                      </body>
                    </html>
                    """ %(ticker, body)

            mail = MIMEText(html, 'html')

            mail["To"] = para
            mail["Subject"] = "Assunto"


            smtp.sendmail(de, para, mail.as_string())

            smtp.quit()

        except Exception as e:
            print "%", e

reportMail = ReportMail()
