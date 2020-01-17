'''
	Необходимые функции
	1) Отправка сообщения
	2) Перевод текста
	3) Преобразование звука в текст
'''
import smtplib
from email.message import EmailMessage
import requests
import speech_recognition as sr
from pydub import AudioSegment


def send_mail(addr_from, addr_form_pass, addr_to, mess='|_|_|_| - spikes', subject='( 0 )( 0 ) - eyes'):
	server = smtplib.SMTP('smtp.mail.ru', 25)
	server.ehlo()       
	server.starttls()
	server.ehlo()

	server.login(addr_from, addr_form_pass)
	
	message = EmailMessage()
	message['From'] = addr_from
	message['To'] = addr_to
	message['Subject'] = subject
	message.set_content(mess)
	
	server.send_message(msg=message)
	
	print('\nComplete.')
	server.close()


def translate_text(text):
	URL = "https://translate.yandex.net/api/v1.5/tr.json/translate"
	KEY = "trnsl.1.1.20200114T163102Z.1c7a5c106f9a341e.f424c68784a7b5e8e396f2feeef609a93b09fc30"
	
	params = {
        "key": KEY,     
        "text": text,
        "lang": 'ru-en'
	}
		
	response = requests.get(URL ,params=params)
	return response.json()


def sound_recognition(voice_file):
	name = voice_file
	src = f"/home/volerij/audios/{name}.mp3"
	dst = f"/home/volerij/audios/{name}.wav"

	sound = AudioSegment.from_mp3(src)
	sound.export(dst, format="wav")


	r = sr.Recognizer()
	with sr.WavFile(f'/home/volerij/audios/{name}.wav') as source:
		audio = r.listen(source)

	try:
		text = r.recognize_google(audio, language='ru-RU')
	except sr.UnknownValueError:
		return 0
	except sr.RequestError as e:
		return 0
	
	return text
