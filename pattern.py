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
    
    def __copy(self):
        newEvents = []
        for ev in self.events:
            newEvents.append(Event(ev.time, ev.pitch, ev.velocity, ev.length))
        return Pattern(newEvents)
    
    def stretch(self, factor):
        print "stretch by: %s" % factor
        newPat = self.__copy()
        for ev in newPat.events:
            ev.time *= factor
            ev.length *= factor
        return newPat

    # length of pattern in bars
    def length(self):
        if self.events == 0:
            return 0
        lastEvent = self.events[len(self.events)-1]
        return lastEvent.time + lastEvent.length

    def reverse(self):
        newPat = self.__copy()
        newPat.events.reverse()
        return newPat

    def splice(start, stop, step):
        newPat = self.__copy()
        newPat.events = newPat.events[start:stop:step]
        return newPat
        

def addPatternToTrack(midiFile, track, pattern, time):
    for ev in pattern.events:
        print "NOTE t: %s, p: %s, v: %s, l: %s" % (time + ev.time, getPitch(key[0], key[1], ev.pitch), ev.velocity, ev.length)
        MyMIDI.addNote(track, 0, getPitch(key[0], key[1], ev.pitch), time + ev.time, ev.length, ev.velocity)

