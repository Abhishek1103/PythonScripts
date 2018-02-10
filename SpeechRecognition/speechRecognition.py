import speech_recognition as sr

# r = sr.Recognizer()
# with sr.Microphone() as source:
#     print("Say Somethig")
#     audio = r.listen(source)

from os import path
#AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "english.wav")
#AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "kendra.wav")
AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "eric.wav")
r = sr.Recognizer()                 # Supports only .wav audio file
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)

try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
except Exception as ex:
    print("Some error occured: "+ex)
# try:
#     print("Sphinx thinks you said "+r.recognize_sphinx(audio))
# except sr.UnknownValueError:
#     print("Sphinx could not understand")
# except sr.RequestError as e:
#     print("Sphinx error; {0}".format(e))

# import speech_recognition as sr
# for index, name in enumerate(sr.Microphone.list_microphone_names()):
#     print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))
