import subprocess
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import ctypes
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def wishes():
	hour = int(datetime.datetime.now().hour)
	if hour>= 0 and hour<12:
		speak("Good Morning Sir !")

	elif hour>= 12 and hour<18:
		speak("Good Afternoon Sir !") 

	else:
		speak("Good Evening Sir !") 

	
	speak("I am your virtual Assistant ")
	
	

def username():
	speak("What should i call you sir")
	username = takeCommand()
	speak(f"Welcome Mister {username}")
	print("Welcome Mr.", username)
	speak("How can i Help you, Sir")

def takeCommand():
	
	r = sr.Recognizer()
	
	with sr.Microphone() as source:
		
		print("Listening...")
		r.pause_threshold = 1
		audio = r.listen(source)

	try:
		print("Recognizing...") 
		query = r.recognize_google(audio, language ='en-in')
		print(f"you said: {query}\n")

	except Exception as e:
		print(e) 
		print("Unable to Recognize your voice.") 
		speak("Unable to Recognize your voice.") 
		return ""
	
	return query

if __name__ == '__main__':
	clear = lambda: os.system('cls')
	
	clear()
	wishes()
	username()
	
	while True:
		
		query = takeCommand().lower()

		if 'wikipedia' in query:
			speak('Searching Wikipedia...')
			query = query.replace("wikipedia", "")
			results = wikipedia.summary(query, sentences = 3)
			speak("According to Wikipedia")
			print(results)
			speak(results)

		elif 'open youtube' in query:
			speak("Ok i'm opening Youtube\n")
			webbrowser.open("youtube.com")

		elif 'open google' in query:
			speak("Ok i'm opening Google\n")
			webbrowser.open("google.com") 

		elif 'play music' in query or "play song" in query:
			speak("Sorry sir I don't have any music player I redirect you on google where you search for music")
			webbrowser.open("google.com")

		elif 'time' in query:
			strTime = datetime.datetime.now().strftime("%H:%M:%S") 
			speak(f"Sir, the time is {strTime}")

		elif 'send a mail' in query:
			speak("opening the interface to send the mail")
			webbrowser.open("https://mail.google.com/mail/u/0/#inbox?compose=new")

		elif 'how are you' in query  or 'how r u' in query:
			speak("Thank you I am fine, what about you")

		elif 'fine' in query or "well" in query:
			speak("It's good to know that you are fine")

		elif "change my name" in query:
			speak("sure sir, what i call you")
			query = query.replace("change my name", "")
			username = query

		elif "change your name" in query:
			speak("What would you like to call me, Sir ")
			assistantname = takeCommand()
			speak("Thanks for naming me")

		elif "what's your name" in query or "What is your name" in query:
			speak("My friends call me")
			speak(assistantname)
			

		elif "goodbye" in query or "bye"  in query or "close" in query or "exit" in query:
			speak("bye Thanks for giving me your time")
			exit()

		elif "who made you" in query or "who created you" in query: 
			speak("I have been created by mister Prabhat Verma.")
			
		elif 'joke' in query:
			speak(pyjokes.get_joke())
			
		elif "calculate" in query: 
			
			webbrowser.open("https://www.google.com/search?q=google+calculater&rlz=1C1CHBF_enIN1075IN1075&oq=google+calculater&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIPCAEQABgKGIMBGLEDGIAEMgkIAhAAGAoYgAQyCQgDEAAYChiABDIJCAQQABgKGIAEMgsIBRAAGAIYChiABDIJCAYQABgKGIAEMgsIBxAAGAIYChiABDIJCAgQABgKGIAEMgsICRAAGAIYChiABNIBCjYxMjM2OGowajeoAgCwAgA&sourceid=chrome&ie=UTF-8") 

		elif 'search' in query or 'play' in query:
			
			query = query.replace("search", "") 
			query = query.replace("play", "")		 
			webbrowser.open(query) 

		elif "who i am" in query:
			speak(f"If you talk then definitely your human and your name is {username}")

		elif "why you came to" in query:
			speak("Thanks to Prabhat Verma further It's a secret")

		elif 'is love' in query:
			speak("It is 7th sense that destroy all other senses")

		elif "who are you" in query:
			speak(f"I am your virtual assistant and my name is {assistantname}")

		elif 'reason for you' in query:
			speak("I was created as a task of codealpha internship")
		elif 'lock window' in query:
				speak("locking the device")
				ctypes.windll.user32.LockWorkStation()

		elif 'shutdown system' in query:
				speak("Hold On a Sec ! Your system is on its way to shut down")
				subprocess.call('shutdown / p /f')
				
		elif 'empty recycle bin' in query:
			speak("ok")
			winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
			speak("Recycle Bin Recycled")

		elif "don't listen" in query or "stop listening" in query:
			speak("ok i am stop listening thank you come again when you need me")
			exit()

		elif "where is" in query:
			query = query.replace("where is", "")
			location = query
			speak(f"User asked to Locate{location}")
			
			webbrowser.open(f"https://www.google.com/maps/place/{location}")

		elif "camera" in query or "take a photo" in query:
			speak("Sorry I could not open your camera")

		elif "restart" in query:
			subprocess.call(["shutdown", "/r"])
			
		elif "hibernate" in query or "sleep" in query:
			speak("Hibernating")
			subprocess.call("shutdown / h")

		elif "log off" in query or "sign out" in query:
			speak("Make sure all the application are closed before sign-out")
			time.sleep(5)
			subprocess.call(["shutdown", "/l"])

		elif "write a note" in query:
			speak("What should i write, sir")
			note = takeCommand()
			file = open('notes.txt', 'w')
			speak("Sir, Should i include date and time")
			snfm = takeCommand()
			if 'yes' in snfm or 'sure' in snfm:
				strTime = datetime.datetime.now().strftime("%H:%M:%S")
				file.write(strTime)
				file.write(" :- ")
				file.write(note)
			else:
				file.write(note)
		
		elif "show note" in query or "show notes" in query:
			speak("Showing Notes")
			file = open("notes.txt", "r") 
			print(file.read())
			speak(file.read(6))		
		
		elif "assistant" in query:
			
			wishes()
			speak("i am Listening sir, please say")
			

		elif "weather" in query:
			webbrowser.open("https://www.google.com/search?q=weather&rlz=1C1CHBF_enIN1075IN1075&oq=wea&gs_lcrp=EgZjaHJvbWUqBggCEEUYOzIGCAAQRRg5MgYIARBFGDsyBggCEEUYOzIGCAMQRRg8MgYIBBBFGDwyBggFEEUYPDIGCAYQRRg8MgYIBxBFGEHSAQg4ODkxajBqN6gCALACAA&sourceid=chrome&ie=UTF-8")
			
		elif "send message" in query:
			speak("opening whatsapp")
			webbrowser.open("https://web.whatsapp.com/")
		elif "wikipedia" in query:
			webbrowser.open("wikipedia.com")

		elif "good morning" in query or "good evening" in query or "good afternoon" in query:
			wishes()

		elif "will you be my gf" in query or "will you be my bf" in query: 
			speak("I'm a virtual assistant and I don't have any human feelings")

		elif "how are you" in query:
			speak("I'm fine")
		elif "good night" in query:
			speak("good night")
			exit()

		elif "i love you" in query:
			speak("Thank you but I don't have human feelings")

		elif query.strip():
			speak("Sorry is I am not connected with any ai so I have some limited power to resolve your query   Please say goodbye , bye, close, exit to close the assistant ")
			print('Please say {"goodbye" or "bye" or "close" or "exit"} to close the assistant')
