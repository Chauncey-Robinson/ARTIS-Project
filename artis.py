
import sounddevice as sd  # For recording audio
import numpy as np       # For handling arrays, used with sounddevice
import soundfile as sf   # For saving the recorded audio to a file
import whisper           # For using OpenAI's Whisper model to transcribe audio

print("Hello from ARTIS!")
def record_audio(filename, duration=5, fs=44100):
    print("Recording...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=2, dtype='float64')
    sd.wait()  # Wait for the recording to finish
    print("Recording stopped.")
    sf.write(filename, recording, fs)  # Save the recording as a WAV file

def transcribe_audio(filename):
    model = whisper.load_model("base")
    result = model.transcribe(filename)
    return result['text']

if __name__ == "__main__":
    filename = 'output.wav'
    record_audio(filename, duration=10)  # Record for 10 seconds
    transcription = transcribe_audio(filename)
    print("Transcription:", transcription)


