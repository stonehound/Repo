# This is a sound test for numpy 
import numpy as np
import sounddevice as sd

# parameters
sample_rate = 44100 # hertz
duration = 2 # seconds
frequency = 440 # hertz
amplitude = 0.5 # volume

# generate time points
t = np.linspace(0, duration, int(sample_rate * duration), endpoint = False)

# gernerate sine wave
# sine_wave = amplitude * np.sin(2 * np.pi * frequency * t)

# generate square wave
square_wave = amplitude * np.heaviside(np.sin(2 * np.pi * frequency * t), 1.0)

# play sound
# sd.play(sine_wave, sample_rate)
sd.play(square_wave, sample_rate)
sd.wait() # wait until the sound has finished

