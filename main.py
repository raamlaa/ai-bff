import os
import speech_recognition as sr
from gtts import gTTS 
from playsound import playsound
from pygame import mixer
from io import BytesIO
import openai


 #configuer openai 
 
openai.api_key="your_api_key"
 
messages_array=[
    {
        "role":"system",
        "content":"You are my amazing best friend Named Alexa "
    }
]
 
 
 #logic
 
 
 #s1 define func catches voice 
 
 
def listen ():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("LISTENING...")
        r.pause_threshold = 1
        audio = r.listen(source) 
    
    try:    
        print('Recognizing...')
        query=r.recognize_google(audio,language='en-in')
        print('user said: ',query)
        messages_array.append({
            "role":"user",
            "content":query
        })
        
        respond(audio)
        
    except Exception as e:
        print('Say that again please...', e)
        
    
    
#step2 repond

def respond(audio):
    print('RESPONDING...')
    
    
    res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = messages_array,
    )
    
    res_message= res.choices[0].message
    messages_array.append(res_message)
    
    speak(res_message.content)
    
    
#step3 speak

def speak(text):
    
    speech = gTTS(text=text,lang='en' , slow=False)
    
    speech.save('captured_voice.mp3')
    playsound('captured_voice.mp3')
    
    os.remove('captured_voice.mp3')
    listen()
    pass
    
    
query=listen()



    