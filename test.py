#Import the library
import MidiFile
import random
import subprocess
import winsound
import os

# Create the MIDIFile Object
# Add track name and tempo. The first argument to addTrackName and
# addTempo is the time to write the event.
MyMIDI = MidiFile.MIDIFile(1)
MyMIDI.addTrackName(0, 0, "Track 1")
MyMIDI.addTempo(0, 0, 120)
#MyMIDI.addInstrument(0, time, "C:\\VST\\FMMF.dll")
#MyMIDI.addInstrument(0, time, "C:\\VST\\dirty_harry_1_1.dll")
MyMIDI.addInstrument(0, 0, "C:\\VST\\helm.dll")
#MyMIDI.addProgramChange(0, 0, 0, 4)

MyMIDI.addNote(0, 0, 50, 0, 16, 100)
MyMIDI.addNote(0, 0, 54, 16, 20, 100)

# And write it to disk.
binfile = open("out.mid", 'wb')
MyMIDI.writeFile(binfile)
binfile.close()

subprocess.call(["C:\Users\GeorgeKrueger\Documents\GitHub\midirender\Builds\VisualStudio2015\Debug\midirender.exe",
                 "out.mid", "out.wav"])


winsound.PlaySound("out.wav", winsound.SND_FILENAME)

