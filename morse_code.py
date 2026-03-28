#!/usr/bin/env python3
"""morse_code - Encode and decode Morse code."""
import sys

MORSE = {"A":".-","B":"-...","C":"-.-.","D":"-..","E":".","F":"..-.","G":"--.","H":"....","I":"..","J":".---","K":"-.-","L":".-..","M":"--","N":"-.","O":"---","P":".--.","Q":"--.-","R":".-.","S":"...","T":"-","U":"..-","V":"...-","W":".--","X":"-..-","Y":"-.--","Z":"--..","0":"-----","1":".----","2":"..---","3":"...--","4":"....-","5":".....","6":"-....","7":"--...","8":"---..","9":"----."}
REV = {v: k for k, v in MORSE.items()}

def encode(text):
    return " / ".join(" ".join(MORSE.get(c, "?") for c in w.upper()) for w in text.split())

def decode(morse):
    return " ".join("".join(REV.get(c, "?") for c in w.split()) for w in morse.split(" / "))

if __name__ == "__main__":
    if len(sys.argv) < 3: print("Usage: morse_code <encode|decode> <text>"); sys.exit(1)
    cmd, text = sys.argv[1], " ".join(sys.argv[2:])
    print(encode(text) if cmd == "encode" else decode(text))
