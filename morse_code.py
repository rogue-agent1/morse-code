#!/usr/bin/env python3
"""Morse code encoder/decoder. Zero dependencies."""

MORSE = {
    'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.','F':'..-.','G':'--.','H':'....',
    'I':'..','J':'.---','K':'-.-','L':'.-..','M':'--','N':'-.','O':'---','P':'.--.',
    'Q':'--.-','R':'.-.','S':'...','T':'-','U':'..-','V':'...-','W':'.--','X':'-..-',
    'Y':'-.--','Z':'--..','0':'-----','1':'.----','2':'..---','3':'...--','4':'....-',
    '5':'.....','6':'-....','7':'--...','8':'---..','9':'----.', ' ':'/','?':'..--..','!':'-.-.--','.':'.-.-.-',',':'--..--'
}
REVERSE = {v: k for k, v in MORSE.items()}

def encode(text):
    return " ".join(MORSE.get(c, '') for c in text.upper())

def decode(morse):
    return "".join(REVERSE.get(code, '?') for code in morse.split(" "))

def to_sound(morse, dot=100, dash=300, gap=100, word_gap=700):
    """Convert morse to timing list [(freq_hz, duration_ms), ...]"""
    result = []
    for c in morse:
        if c == '.': result.append((800, dot)); result.append((0, gap))
        elif c == '-': result.append((800, dash)); result.append((0, gap))
        elif c == ' ': result.append((0, word_gap - gap))
        elif c == '/': result.append((0, word_gap))
    return result

if __name__ == "__main__":
    import sys
    text = " ".join(sys.argv[1:]) or "SOS"
    m = encode(text)
    print(f"Encode: {m}")
    print(f"Decode: {decode(m)}")
