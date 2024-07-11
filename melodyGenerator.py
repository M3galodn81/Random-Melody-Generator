from random import choice
from random import randint

lowOctave = -1 # REAPER has this
highOctave = 9

notes_withSharp = [ "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
notes_withFlat  = [ "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab" ,"A", "Bb", "B"]

duration        = [ 1,    0.5,  0.25,  0.125,   0.0625]
duration_mapping = {
    1: "1",
    0.5: "1/2",
    0.25: "1/4",
    0.125: "1/8",
    0.0625: "1/16"
}

# Size of the melody in BARS
while True:
    try:
        bars = int(input(f"How many bars do you want your melody have? "))
        if bars < 0:
            raise IndexError
        break
    except ValueError:
        print("Please enter a positive number.")
        continue
    except IndexError:
        print(f"{bars} is not a positive number.")
        continue

# Make a 2d array for storing randomize notes 
# [duration, note, octave]
randomize_notes = []

duration_array = []
note_array = []
octave_array = []

while sum(duration_array) != bars:
    rand_duration = 0
    rand_duration = choice(duration)
    duration_array.append(rand_duration)

    if sum(duration_array) > bars:
        duration_array.pop()

duration_array = [duration_mapping[d] for d in duration_array]

for x in duration_array:
    rand_note = ""
    rand_note = choice(notes_withSharp)
    note_array.append(rand_note)

for x in duration_array:
    rand_octave = ""
    rand_octave = randint(lowOctave, highOctave)
    octave_array.append(rand_octave)

# Combine into 1 array
randomize_notes = [[d, n, o] for d, n, o in zip(duration_array,note_array,octave_array)]

print(f" Random Generated {bars} bar Melody: ")
print(f" Notes \t\t  |  Octave \t\t  |  Duration")
for x in randomize_notes:
    print(f" {x[1]}\t\t  |  {x[2]}\t\t  |  {x[0]}")








