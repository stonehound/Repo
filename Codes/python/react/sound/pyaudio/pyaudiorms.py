# Measure the RMS value of the input volume

import pyaudio
import audioop
import time

# --- Configuration ---
CHUNK = 1024  # Number of audio frames per buffer
FORMAT = pyaudio.paInt16  # Audio format (16-bit)
CHANNELS = 1  # Use 1 for mono, 2 for stereo
RATE = 44100  # Sample rate
INPUT_DEVICE_INDEX = 2  # <--- Change this to your device's ID

# --- Main script ---
try:
    p = pyaudio.PyAudio()
    
    # Open a stream for audio input
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    input_device_index=INPUT_DEVICE_INDEX,
                    frames_per_buffer=CHUNK)

    print("* Measuring volume. Press Ctrl+C to stop.")

    while True:
        # Read a chunk of audio data from the stream
        data = stream.read(CHUNK)
        
        # Calculate the root mean square (RMS) of the audio chunk
        rms = audioop.rms(data, 2)  # The '2' is the width of a sample in bytes (16-bit = 2 bytes)
        
        print(f"Volume (RMS): {rms}")
        
        # Add a short delay to control the print rate if needed
        time.sleep(0.01)

except KeyboardInterrupt:
    print("\n* Stopping measurement.")

finally:
    # --- Clean up ---
    stream.stop_stream()
    stream.close()
    p.terminate()

