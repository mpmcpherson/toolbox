import mido
from mido import Message, MidiFile, MidiTrack

def create_chord_midi(chords, durations, tempo, filename):
    # Create a new MIDI file and track
    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)

    # Set tempo (Microseconds per quarter note)
    track.append(mido.MetaMessage('set_tempo', tempo=mido.bpm2tempo(tempo)))

    # Function to add a chord to the track
    def add_chord(chord_notes, duration):
        for note in chord_notes:
            track.append(Message('note_on', note=note, velocity=64, time=0))
        for note in chord_notes:
            track.append(Message('note_off', note=note, velocity=64, time=duration))

    # Add chords to the track based on the provided progression
    for chord, duration in zip(chords, durations):
        add_chord(chord, duration)

    # Save the MIDI file
    mid.save(filename)

# Define the chords (MIDI note numbers) and durations (in ticks; default 480 ticks per beat)
chords = [
    [52, 55, 59], # Em
    [48, 52, 55], # C
    [47, 50, 55], # G
    [50, 54, 57], # D
    # Repeat or add more chords as needed
]
durations = [480] * len(chords)  # Assuming each chord is one beat at 120 BPM

# Create and save the MIDI file
create_chord_midi(chords, durations, tempo=120, filename='death_curse_song.mid')
