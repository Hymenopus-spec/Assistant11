import speech_recognition as sp
import pyttsx3 as psx


engine = psx.init()

#for index, name in enumerate(sp.Microphone.list_microphone_names()):
#    print(index,name)
def recognition():
    r = sp.Recognizer()
    with sp.Microphone(device_index=20) as micro:
        audio = r.listen(micro)
    try:
        speech = r.recognize_google(audio, language="ru")
        print(speech)
        return speech
    except sp.RequestError:
        return print("Ошибка")
    except sp.UnknownValueError:
        return print( "Ошибка распознавания")
    except sp.TranscriptionFailed:
        return print("Ошибка транскрипции")

def text(speech):
    speech = speech.lower()
    if "проверка" in speech:
        voice("2")

def voice(text):
    engine.say(text)
    engine.runAndWait()

while True:
    text(recognition())


def testing():
    print(1)