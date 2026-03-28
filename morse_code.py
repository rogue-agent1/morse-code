#!/usr/bin/env python3
"""Morse code encoder/decoder."""
import sys

MORSE = {'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.','F':'..-.','G':'--.','H':'....','I':'..','J':'.---','K':'-.-','L':'.-..','M':'--','N':'-.','O':'---','P':'.--.','Q':'--.-','R':'.-.','S':'...','T':'-','U':'..-','V':'...-','W':'.--','X':'-..-','Y':'-.--','Z':'--..','0':'-----','1':'.----','2':'..---','3':'...--','4':'....-','5':'.....','6':'-....','7':'--...','8':'---..','9':'----.','.'   :'.-.-.-',',':'--..--','?':'..--..','!':'-.-.--','/':'-..-.','(':'-.--.',')':'-.--.-','&':'.-...',':':'---...',';':'-.-.-.','=':'-...-','+':'.-.-.','−':'-....-','_':'..--.-','"':'.-..-.','$':'...-..-','@':'.--.-.'}
REVERSE = {v: k for k, v in MORSE.items()}

def encode(text):
    words = text.upper().split()
    return ' / '.join(' '.join(MORSE.get(c, c) for c in w) for w in words)

def decode(morse):
    words = morse.strip().split(' / ')
    return ' '.join(''.join(REVERSE.get(c, c) for c in w.split()) for w in words)

def main():
    if len(sys.argv) < 3:
        print("Usage: morse_code.py <encode|decode> <text>")
        sys.exit(1)
    cmd, text = sys.argv[1], ' '.join(sys.argv[2:])
    if cmd == 'encode':
        print(encode(text))
    elif cmd == 'decode':
        print(decode(text))
    else:
        print(f"Unknown command: {cmd}")
        sys.exit(1)

if __name__ == '__main__':
    main()
