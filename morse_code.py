#!/usr/bin/env python3
"""morse_code - Encode/decode Morse code."""
import sys
CODE = {'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.','F':'..-.','G':'--.','H':'....',
'I':'..','J':'.---','K':'-.-','L':'.-..','M':'--','N':'-.','O':'---','P':'.--.','Q':'--.-',
'R':'.-.','S':'...','T':'-','U':'..-','V':'...-','W':'.--','X':'-..-','Y':'-.--','Z':'--..',
'0':'-----','1':'.----','2':'..---','3':'...--','4':'....-','5':'.....',
'6':'-....','7':'--...','8':'---..','9':'----.','.'  :'.-.-.-',','  :'--..--',
'?':'..--..','!':'-.-.--','/':'-..-.','(':'-.--.',')':'-.--.-','&':'.-...',
':':'---...',';':'-.-.-.','=':'-...-','+':'.-.-.','@':'.--.-.'}
DECODE = {v:k for k,v in CODE.items()}

def encode(text):
    words = text.upper().split()
    return ' / '.join(' '.join(CODE.get(c,'?') for c in w) for w in words)

def decode(morse):
    words = morse.split(' / ')
    return ' '.join(''.join(DECODE.get(c,'?') for c in w.split()) for w in words)

def main():
    args = sys.argv[1:]
    if not args or '-h' in args:
        print("Usage: morse_code.py encode TEXT | decode MORSE"); return
    cmd = args[0]
    text = ' '.join(args[1:]) if len(args)>1 else sys.stdin.read().strip()
    if cmd in ('e','encode'): print(encode(text))
    elif cmd in ('d','decode'): print(decode(text))
    else: print(encode(' '.join(args)))

if __name__ == '__main__': main()
