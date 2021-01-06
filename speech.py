import speech_recognition as sr

r = sr.Recognizer()

# to use microphone we have to install another library named PyAudio
# to download pyaudio first install pipwin by typing
# pip install pipwin
# and then pipwin install pyaudio

with sr.Microphone() as source:
    print('speak anything : ')
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print('You said: {}'.format(text))
    except:
        print("Sorry could not read!!!")
