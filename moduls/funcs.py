'''
	Необходимые функции
	1) Отправка сообщения
	2) Перевод текста
'''
import smtplib
from email.message import EmailMessage
import requests


def send_mail(addr_from, addr_form_pass, addr_to, mess='|_|_|_|_| - spikes', subject='( 0 )( 0 ) - eyes'):
	server = smtplib.SMTP('smtp.mail.ru', 25)
	server.ehlo()       
	server.starttls()
	server.ehlo()
	#print(f'Logging in {addr_from} ...')
	server.login(addr_from, addr_form_pass)
	
	#print('Creating a message ...')
	message = EmailMessage()
	message['From'] = addr_from
	message['To'] = addr_to
	message['Subject'] = subject
	message.set_content(mess)
	
	#print(f'Sending message to {addr_to} ...')
	server.send_message(msg=message)
	
	print('\nComplete.')
	server.close()


def translate_text(text):
	URL = "https://translate.yandex.net/api/v1.5/tr.json/translate"
	KEY = "trnsl.1.1.20200114T163102Z.1c7a5c106f9a341e.f424c68784a7b5e8e396f2feeef609a93b09fc30" #через три дня новый создавать
	
	params = {
        "key": KEY,     
        "text": text,
        "lang": 'ru-en'
	}
		
	response = requests.get(URL ,params=params)
	return response.json()
