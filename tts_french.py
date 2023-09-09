# -*- coding: utf8 -*
import pyttsx3, sys, re, os


#--- General Usage 
if len(sys.argv) < 4:
    print("Usage: tts_french.py -name [actor] source_text", file=sys.stderr)
    print("Example: ", file=sys.stderr)
    print("py tts_french.py -name julie test_fr.txt", file=sys.stderr)
    sys.exit()

#--- Options
actor = sys.argv[2] # actor
source = sys.argv[3] # source_text

#--- Others Usages
if not os.path.isfile(source):
    print(f"File: {source} does not exist!", file=sys.stderr)
    sys.exit()

print("Actor:", actor)
print("Source", source)


'''Doc : The library supports the following engines:
sapi5 - SAPI5 on Windows
    French voices : Hortense, Julie, Paul
nsss - NSSpeechSynthesizer on Mac OS X
espeak - eSpeak on every other platform'''
pyttsx3.init(driverName='sapi5') 


engine = pyttsx3.init()


#--- Language Option
def num_language(voices, actor):
    n = len(voices)
    for i in range(n):
        if "french".lower() in voices[i].name.lower():
            if actor.lower() in voices[i].name.lower():
                return i
    raise TypeError('LanguageNotFound')

voices = engine.getProperty('voices')
try:
    num = num_language(voices, actor)
except:
    print("Actor not found!", file=sys.stderr)
    sys.exit()

voice = engine.getProperty('voices')[num]


# language Implementation
engine.setProperty('voice', voice.id)
engine.setProperty('rate', 110) # sets speed of speech


# Concatenation of the input file into a string
f = open(source, "r", encoding="utf-8")
text = ""
lines = f.readlines()
for line in lines:
    text += line + " "
f.close()


#--- MP3 saving
target = source.replace(".txt", ".mp3")
print("Target:", target)
engine.save_to_file(text, target)


engine.runAndWait()

