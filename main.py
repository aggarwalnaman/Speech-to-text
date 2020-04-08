import speech_recognition as sr
AudFile=("female.wav")

r=sr.Recognizer()

with sr.AudioFile(AudFile)  as audi:
    audio=r.record(audi)

try:
    print("It contains : "+r.recognize_google(audio))
except sr.UnknownValueError:
    print("Can not understand audio")
except sr.RequestError:
    print("Could not found result")

