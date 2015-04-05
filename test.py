#Import the library
from midiutil.MidiFile import MIDIFile
import random

key = ["D", "MAJ"]

scales = {}
scales["MAJ"] = [ 0, 2, 4, 5, 7, 9, 11 ]
scales["MIN"] = [ 0, 2, 3, 5, 7, 9, 10 ]
scales["PENTAMIN"] = [ 0, 3, 5, 7, 10 ]

noteNames = [ "A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#" ]

def getPitch(root, scale, n):
    sca = scales[scale]
    rootOffset = noteNames.index(root)
    octave = n / len(sca)
    degree = n % len(sca)
    #print "n: %s, rootOffset: %s, octave: %s, degree: %s, sca[degree]: %s" % (n, rootOffset, octave, degree, sca[degree])
    midiPitch = 21 + 12 * octave + rootOffset + sca[degree]
    return midiPitch

class Event:
    def __init__(self, time, pitch, velocity, length):
        self.time = time
        self.pitch = pitch
        self.velocity = velocity
        self.length = length

class Pattern:
    def __init__(self, events):
        self.events = events

    def events(self):
        return self.events

    def stretch(self, factor):
        print "stretch by: %s" % factor
        newEvents = []
        for ev in self.events:
            newEvents.append(Event(ev.time*factor, ev.pitch, ev.velocity, ev.length*factor))
        return Pattern(newEvents)
        

def addPatternToTrack(midiFile, track, pattern, time):
    for ev in pattern.events:
        print "NOTE t: %s, p: %s, v: %s, l: %s" % (time + ev.time, getPitch(key[0], key[1], ev.pitch), ev.velocity, ev.length)
        MyMIDI.addNote(track, 0, getPitch(key[0], key[1], ev.pitch), time + ev.time, ev.length, ev.velocity)

for k in range(1,11):
    # Create the MIDIFile Object
    MyMIDI = MIDIFile(1)

    # Add track name and tempo. The first argument to addTrackName and
    # addTempo is the time to write the event.
    track = 0
    time = 0
    MyMIDI.addTrackName(track,time,"Track")
    MyMIDI.addTempo(track,time, 120)

    # Add a note. addNote expects the following information:
    pitches = [ random.randint(7, 14), random.randint(7, 14), random.randint(7, 14) ]

    pat = Pattern([
        Event(0, random.randint(14, 21), random.randint(70, 110), 1),
        Event(1, random.randint(14, 21), random.randint(70, 110), 1),
        Event(2, random.randint(14, 21), random.randint(70, 110), 2) ])

    time = 0
    i = 1
    while time < 11:
        addPatternToTrack(MyMIDI, track, pat.stretch(1/float(i)), time)
        time += 4*(1/float(i))
        i += 1

    #while time < length:
    #    duration = float(random.randint(1, 4)) / scaleFac
    #    midiPitch = getPitch("C","MAJ",random.choice(pitches))
    #    MyMIDI.addNote(track, channel, midiPitch, time, duration, volume)
    #    time += float(random.randint(1, 4)) / (scaleFac / float(2))
    #    print "pitch: %s, dur: %s, time: %s" % (midiPitch, duration, time)

    # And write it to disk.
    binfile = open("test%s.mid" % k, 'wb')
    MyMIDI.writeFile(binfile)
    binfile.close()

