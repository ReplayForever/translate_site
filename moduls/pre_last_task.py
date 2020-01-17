# веб-приложение

# login: mem_gem_kektus@mail.ru    левый адрес
# password: lolKekmemGem1337
from funcs import *


def check_translate_text(rus_text='Пустое сообщение.'):
	text = translate_text(rus_text)
	text = ''.join(text['text'])
	
	return text

def check_send_mail(addr_to, mess='Do not reply.'):
	addr_from = 'mem_gem_kektus@mail.ru'
	addr_form_pass = 'lolKekmemGem1337'
	
	addr_to = addr_to
	
	subject = 'Test message.'
	
	send_mail(addr_from, addr_form_pass, addr_to, mess, subject)
	

if __name__ == '__main__':
	voice_file = 'fast_hhay'
	
	response = sound_recognition(voice_file)
	print(response)
	
	if response:
		rus_text = response
		addr_to = 'painvsmind@gmail.com'#input('Send to(e-mail): ')
		
		try:
			text = check_translate_text(rus_text)
			print(text)
			
			check_send_mail(addr_to, text)
		except:
			print('Something went wrong')
	else:
		print('Something went wrong')
	
	
	
	
