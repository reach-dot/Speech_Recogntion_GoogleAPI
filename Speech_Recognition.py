import speech_recognition as sr

r=sr.Recognizer()
with sr.Microphone() as source:
	r.adjust_for_ambient_noise(source)  # here
	print('Say Something')
	audio=r.listen(source,timeout=3)

try:
	print('Answer:\n' + r.recognize_google(audio))

except:
	pass

l =range(10)
for i in l:
	print(i)
for i in 10:
	print(i) 
	
	try:
	print('Guesses:\n' + r.recognize_google(audio3))

except:
	pass
try:
	print('Solutions:\n' + r.recognize_google(audio2))

except:
	pass
