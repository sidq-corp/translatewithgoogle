#pip install pyaudio
#pip install googletrans
#pip install SpeechRecognition
#pip install pyttsx3

import speech_recognition as sr
import pyttsx3
import time

from googletrans import Translator

translator = Translator()

def say(text, lang):
	if lang == 'uk':
		text = text.lower().replace('и', 'ы').replace('і', 'и').replace('ї', 'йи')
	rec = pyttsx3.init()
	rec.say(text)
	rec.runAndWait()
	

def callback(recognizer, audio):
	global lang
	try:
		voice = recognizer.recognize_google(audio, language = "ru-RU").lower()
		result = translator.translate(voice, dest = lang)
		print("[log] Распознано: " + voice + '. Перевод: ' + result.text)

		say(result.text, lang)
	except sr.UnknownValueError:
		print("[log] Голос не распознан!")
	except sr.RequestError as e:
		print("[log] Неизвестная ошибка, проверьте интернет!")

r = sr.Recognizer()
m = sr.Microphone()
 
with m as source:
	r.adjust_for_ambient_noise(source)
 
lan = input('''
[1]English 
[2]French
[3]Ukrainian
[4]Russian
[5]Spanish
''')

if lan == '1':
	lang = 'en'
elif lan == '2':
	lang = 'fr'
elif lan == '3':
	lang = 'uk'
elif lan == '4':
	lang = 'ru'
elif lan == '5':
	lang = 'es'

print('Говори')
stop_listening = r.listen_in_background(m, callback)
while True: time.sleep(0.1) 