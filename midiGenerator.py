#region Note -> Hex
# Make a dictionary that convert the notes into hexadecimal format
rows = [x for x in range(-1, 10)]                                                   #octaves
columns = [ "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]        # number of notes
note_list = []

for i in range(len(rows)):
    for j in range(len(columns)):
        note_list.append(columns[j] + str(rows[i]))

note_matrix = {}

for x in note_list:
    note_matrix.update({x : note_list.index(x)})


def convert_notes_to_hexa(note_name,octave_number):
    note = note_name + str(octave_number)
    note = note.replace(' ', '')

    output = note_matrix[note]
    output = hex(output)
    output = output[2:]
    return output

print(convert_notes_to_hexa("B",5))
#endregion

#region Make txt file


import os
if not os.path.exists("midi_file.txt"):
  with open("midi_file.txt", 'w') as file:
        file.write('4D 54 68 64 00 00 00 06 00 01 00 01 00 60')
        
else:
  print("The midi txt already exists.")

f = open("midi_file.txt", "r")
print(f.read())

#endregion