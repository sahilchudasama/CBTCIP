import sounddevice as sd
import wavio
import numpy as np

def record_audio(duration, samplerate=44100):
    print("Recording...")
    recording = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=2, dtype=np.int16)
    sd.wait()  # Wait until recording is finished
    print("Recording complete.")
    return recording

def save_audio(filename, recording, samplerate=44100):
    wavio.write(filename, recording, samplerate, sampwidth=2)
    print(f"Audio saved as {filename}")

def play_audio(filename):
    import scipy.io.wavfile as wav
    from scipy.io import wavfile
    samplerate, data = wavfile.read(filename)
    sd.play(data, samplerate)
    sd.wait()
    print("Playback finished.")

if __name__ == "__main__":
    duration = 5  # seconds
    samplerate = 44100  # Sample rate

    recording = record_audio(duration, samplerate)
    save_audio("output.wav", recording, samplerate)
    play_audio("output.wav")
