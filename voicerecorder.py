# take in voice and turn to wav file called transcript.wav
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
    
# voice record for certain amount of time 
def recordingTime(): 
    time = input("How long would you like to record for")
    return time

# actual recording
def record(time):
    frequency = 44100
    duration = time

    recording = sd.rec(int(duration * frequency), samplerate=frequency, channels=2) # Start recorder with frequency and duration
    print("Recording...")
    sd.wait()

    write("transcript.wav", frequency, recording)


if __name__ == "__main__":

    time = recordingTime()
    record(time)