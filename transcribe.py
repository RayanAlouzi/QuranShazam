from os import path
from pydub import AudioSegment

import whisper 

model = whisper.load_model("base")

sound = AudioSegment.from_mp3("transcript.mp3")
sound.export("transcript.wav", format="wav")

result = model.transcribe('transcript.wav',fp16 = False)

print(result)