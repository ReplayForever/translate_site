# получение ауди4096йла и преобразование в текст
# перевод
# веб-приложение

# login: mem_gem_kektus@mail.ru    левый адрес
# password: lolKekmemGem1337
from funcs import *


def check_translate_text(rus_text='Пустое сообщение.'):
	text = translate_text(rus_text)
	text = ''.join(text['text'])
	print(text)
	
	return text

def check_send_mail(addr_to, mess='Do not reply.'):
	addr_from = 'mem_gem_kektus@mail.ru'
	addr_form_pass = 'lolKekmemGem1337'
	
	addr_to = addr_to
	
	subject = 'Test message.' # нет проверки на запрещенные символы, типа \n и т.д.
	
	send_mail(addr_from, addr_form_pass, addr_to, mess, subject)
	

if __name__ == '__main__':
	rus_text = input('Message (Rus): ')
	addr_to = input('Send to(e-mail): ')
	
	try: #самый простой Try except
		text = check_translate_text(rus_text)
		check_send_mail(addr_to, text)
	except:
		print('Something went wrong')
