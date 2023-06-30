from gtts import gTTS
import  speech_recognition as sr

def transcribeAudio():
    r=sr.Recognizer()
    with sr.Microphone() as src:
        print('Say something....')
        audio=r.listen(src)
    try:
        t=r.recognize_google(audio,language='ar-AR')
        print(t)
        f=open('transcript.txt','w',encoding='utf-8')
        f.writelines(t+'\n')
        f.close()
        obj=gTTS(text=t,lang='ar',slow=False)
        obj.save('transcript.wav')
    except sr.UnknownValueError as U:
        print(U)
    except sr.RequestError as R:
        print(R)