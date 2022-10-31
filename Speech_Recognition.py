import speech_recognition as sr

r=sr.Recognizer()
with sr.Microphone() as source:
	r.adjust_for_ambient_noise(source)  # here
	print('Say Something')
	audio=r.listen(source,timeout=3)

try:
	print('Answer:\n' + r.recognize_google(audio))
	print('Answer:\n' + r.recognize_google(audio2))
	print('Answer:\n' + r.recognize_google(audio3))
except:
	pass

l =range(10)
for i in l:
	print(i)
