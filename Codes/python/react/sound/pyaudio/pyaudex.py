import pyaudio
import wave
sound  = True
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 1000
WAVE_OUTPUT_FILENAME = "output.wav"
r1 = "* recording"
r2 = "* done recording"
p = pyaudio.PyAudio()
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                input_device_index = 2,
                frames_per_buffer=CHUNK)
print(r1)
frames = []
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
 data = stream.read(CHUNK)
 frames.append(data)
print(r2)
stream.stop_stream()
stream.close()
p.terminate()
wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()
