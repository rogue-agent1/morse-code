#!/usr/bin/env python3
"""morse_code - Morse code encoder/decoder with WAV output."""
import argparse, math, struct

MORSE = {'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.','F':'..-.','G':'--.','H':'....',
    'I':'..','J':'.---','K':'-.-','L':'.-..','M':'--','N':'-.','O':'---','P':'.--.',
    'Q':'--.-','R':'.-.','S':'...','T':'-','U':'..-','V':'...-','W':'.--','X':'-..-',
    'Y':'-.--','Z':'--..','0':'-----','1':'.----','2':'..---','3':'...--','4':'....-',
    '5':'.....','6':'-....','7':'--...','8':'---..','9':'----.'}
DECODE = {v: k for k, v in MORSE.items()}

def encode(text):
    return ' / '.join(' '.join(MORSE.get(c, '') for c in word.upper() if c in MORSE) for word in text.split())

def decode(morse):
    return ' '.join(''.join(DECODE.get(c, '?') for c in word.split()) for word in morse.split(' / '))

def to_audio(morse, wpm=15, freq=700, sr=44100):
    dot_dur = 60 / (50 * wpm)
    samples = []
    def tone(duration):
        n = int(sr * duration)
        return [0.7 * math.sin(2*math.pi*freq*t/sr) for t in range(n)]
    def silence(duration):
        return [0] * int(sr * duration)
    for c in morse:
        if c == '.': samples.extend(tone(dot_dur)); samples.extend(silence(dot_dur))
        elif c == '-': samples.extend(tone(dot_dur*3)); samples.extend(silence(dot_dur))
        elif c == ' ': samples.extend(silence(dot_dur*2))
        elif c == '/': samples.extend(silence(dot_dur*4))
    return samples

def write_wav(path, samples, sr=44100):
    n = len(samples)
    with open(path, 'wb') as f:
        f.write(b'RIFF'); f.write(struct.pack('<I', 36+n*2))
        f.write(b'WAVEfmt '); f.write(struct.pack('<IHHIIHH', 16, 1, 1, sr, sr*2, 2, 16))
        f.write(b'data'); f.write(struct.pack('<I', n*2))
        for s in samples: f.write(struct.pack('<h', max(-32767, min(32767, int(s*32767)))))

def main():
    p = argparse.ArgumentParser(description="Morse code")
    p.add_argument("cmd", choices=["encode", "decode", "audio"])
    p.add_argument("text")
    p.add_argument("-o", "--output", default="morse.wav")
    p.add_argument("--wpm", type=int, default=15)
    args = p.parse_args()
    if args.cmd == "encode":
        morse = encode(args.text)
        print(morse)
    elif args.cmd == "decode":
        print(decode(args.text))
    elif args.cmd == "audio":
        morse = encode(args.text)
        print(f"Morse: {morse}")
        samples = to_audio(morse, args.wpm)
        write_wav(args.output, samples)
        print(f"Audio: {args.output} ({len(samples)/44100:.1f}s)")

if __name__ == "__main__":
    main()
