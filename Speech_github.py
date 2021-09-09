import speech_recognition as sr
audio_file=r'D:\03.wav'
recognized_text=r'D:\03.txt'

# define the recognizer
r = sr.Recognizer()

# define the audio file
audio_file = sr.AudioFile(audio_file)

# speech recognition
with audio_file as source: 
   r.adjust_for_ambient_noise(source) 
   audio = r.record(source,offset=30,duration=50)
   
result = r.recognize_google(audio,language="fr-FR")

# exporting the result 
with open(recognized_text,mode ='w') as file: 
   file.write(result) 
