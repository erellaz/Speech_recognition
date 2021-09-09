# Speech_recognition
Programs around the Speech Recognition Python module.

A few tips:
- Transcribe to .wav first. I use something like: ffmpeg -i input.m4a output.wav
- Recognize_google rejects big files with an obscure error message.  Use Offset and Duration in r.record to be below 10M and 1 minute.
