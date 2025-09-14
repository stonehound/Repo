import mido

# Create a new MIDI file
mid = mido.MidiFile()

# Add a track to the MIDI file
track = mido.MidiTrack()
mid.tracks.append(track)

# Define a tempo (microseconds per beat)
# 500000 microseconds per beat = 120 BPM
track.append(mido.Message('set_tempo', tempo=500000, time=0))

# Define a sequence of notes (MIDI note number, velocity, duration in ticks)
# Each tick represents a small unit of time based on the MIDI file's resolution
# For a standard resolution of 480 ticks per beat, a quarter note is 480 ticks.
notes = [
    (60, 64, 480),  # C4, velocity 64, duration 1 beat (quarter note)
    (62, 64, 480),  # D4
    (64, 64, 480),  # E4
    (65, 64, 480),  # F4
    (67, 64, 960),  # G4, duration 2 beats (half note)
]

# Add note messages to the track
for pitch, velocity, duration in notes:
    track.append(mido.Message('note_on', note=pitch, velocity=velocity, time=0))
    track.append(mido.Message('note_off', note=pitch, velocity=velocity, time=duration))

# Save the MIDI file
mid.save('my_note_sequence.mid')

print("MIDI file 'my_note_sequence.mid' created successfully.")

