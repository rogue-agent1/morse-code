#!/usr/bin/env python3
"""morse_code — Morse code encoder/decoder with audio timing. Zero deps."""
import sys

MORSE = {
    'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.','F':'..-.','G':'--.','H':'....',
    'I':'..','J':'.---','K':'-.-','L':'.-..','M':'--','N':'-.','O':'---','P':'.--.',
    'Q':'--.-','R':'.-.','S':'...','T':'-','U':'..-','V':'...-','W':'.--','X':'-..-',
    'Y':'-.--','Z':'--..','0':'-----','1':'.----','2':'..---','3':'...--','4':'....-',
    '5':'.....','6':'-....','7':'--...','8':'---..','9':'----.', ' ':' ',
    '.':'.-.-.-',',':'--..--','?':'..--..','!':'-.-.--','/':'-..-.',
    '(':'-.--.',')':'-.--.-','&':'.-...',':':'---...',';':'-.-.-.',
    '=':'-...-','+':'.-.-.','-':'-....-','_':'..--.-','"':'.-..-.','$':'...-..-',
    '@':'.--.-.','\'':'.----.'}
REVERSE = {v: k for k, v in MORSE.items()}

def encode(text):
    return ' / '.join(' '.join(MORSE.get(c, '?') for c in word.upper()) for word in text.split())

def decode(morse):
    words = morse.strip().split(' / ')
    return ' '.join(''.join(REVERSE.get(c, '?') for c in word.split()) for word in words)

def visualize(text):
    for ch in text.upper():
        if ch == ' ':
            print("  [space]")
            continue
        code = MORSE.get(ch, '?')
        visual = code.replace('.', '•').replace('-', '———')
        print(f"  {ch} : {code:>8}  {visual}")

def main():
    if len(sys.argv) > 1:
        text = ' '.join(sys.argv[1:])
        if all(c in '.-/ ' for c in text):
            print(f"Decoded: {decode(text)}")
        else:
            print(f"Encoded: {encode(text)}")
    else:
        msg = "Hello World"
        encoded = encode(msg)
        decoded = decode(encoded)
        print(f"Text:    {msg}")
        print(f"Morse:   {encoded}")
        print(f"Decoded: {decoded}")
        print(f"\nSOS: {encode('SOS')}")
        print("\nVisualization:")
        visualize("SOS")

if __name__ == "__main__":
    main()
