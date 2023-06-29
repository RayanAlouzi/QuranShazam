from pydub import AudioSegment
import whisper 


def transcribeAudio():
    # start the model
    model = whisper.load_model("base")

    # # turn mp3 to wav file
    # sound = AudioSegment.from_mp3("transcript.mp3")
    # sound.export("transcript.wav", format="wav")

    # get result
    result = model.transcribe('transcript.wav', language="ar", fp16 = False)
    transcribed_text = result['text']

    with open('transcript.txt', 'w', encoding='utf-8') as file:
        file.write(transcribed_text)

    print("Transcription saved to transcript.txt")