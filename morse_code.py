#!/usr/bin/env python3
"""morse_code - Encode and decode Morse code."""
import sys, argparse, json

MORSE = {"A":".-","B":"-...","C":"-.-.","D":"-..","E":".","F":"..-.","G":"--.","H":"....","I":"..","J":".---","K":"-.-","L":".-..","M":"--","N":"-.","O":"---","P":".--.","Q":"--.-","R":".-.","S":"...","T":"-","U":"..-","V":"...-","W":".--","X":"-..-","Y":"-.--","Z":"--..","0":"-----","1":".----","2":"..---","3":"...--","4":"....-","5":".....","6":"-....","7":"--...","8":"---..","9":"----."}
REVERSE = {v: k for k, v in MORSE.items()}

def encode(text):
    words = text.upper().split()
    return " / ".join(" ".join(MORSE.get(ch, "?") for ch in word) for word in words)

def decode(morse):
    words = morse.split(" / ")
    return " ".join("".join(REVERSE.get(code, "?") for code in word.split()) for word in words)

def main():
    p = argparse.ArgumentParser(description="Morse code CLI")
    sub = p.add_subparsers(dest="cmd")
    e = sub.add_parser("encode"); e.add_argument("text")
    d = sub.add_parser("decode"); d.add_argument("morse")
    args = p.parse_args()
    if args.cmd == "encode":
        result = encode(args.text)
        print(json.dumps({"text": args.text, "morse": result}))
    elif args.cmd == "decode":
        result = decode(args.morse)
        print(json.dumps({"morse": args.morse, "text": result}))
    else: p.print_help()

if __name__ == "__main__": main()
