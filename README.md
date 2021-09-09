# Speech_recognition
Programs around the Speech Recognition module
A few tuips to use speech recognition in Python:
Transcribe to .wav first. I use something like: ffmpeg -i input.m4a output.wav
Recognize_google rejects big files with an obscure error message.  Use Offset and Duration in r.record to overcome this.
