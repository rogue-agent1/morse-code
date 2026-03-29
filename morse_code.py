#!/usr/bin/env python3
"""Morse Code - Encode and decode text to/from Morse code."""
import sys

MORSE = {"A":".-","B":"-...","C":"-.-.","D":"-..","E":".","F":"..-.","G":"--.","H":"....",
    "I":"..","J":".---","K":"-.-","L":".-..","M":"--","N":"-.","O":"---","P":".--.",
    "Q":"--.-","R":".-.","S":"...","T":"-","U":"..-","V":"...-","W":".--","X":"-..-",
    "Y":"-.--","Z":"--..","0":"-----","1":".----","2":"..---","3":"...--","4":"....-",
    "5":".....","6":"-....","7":"--...","8":"---..","9":"----.",".":" .-.-.-",",":" --..--",
    "?":"..--..","!":"-.-.--"," ":" / "}

REVERSE = {v.strip(): k for k, v in MORSE.items()}

def encode(text):
    return " ".join(MORSE.get(c.upper(), "?") for c in text)

def decode(morse):
    words = morse.split(" / ")
    result = ""
    for word in words:
        for code in word.strip().split(" "):
            if code: result += REVERSE.get(code, "?")
        result += " "
    return result.strip()

def visual(morse):
    return morse.replace(".", "·").replace("-", "━")

def main():
    if len(sys.argv) < 2:
        text = "HELLO WORLD"
    elif sys.argv[1] == "-d":
        morse = " ".join(sys.argv[2:]); print(decode(morse)); return
    else:
        text = " ".join(sys.argv[1:])
    encoded = encode(text)
    print(f"=== Morse Code ===\n")
    print(f"Text:   {text}")
    print(f"Morse:  {encoded}")
    print(f"Visual: {visual(encoded)}")
    print(f"\nDecode: {decode(encoded)}")

if __name__ == "__main__":
    main()
