#!/usr/bin/env python3
"""morse_code - Encode/decode Morse code."""
import argparse, sys

CODE = {"A":".-","B":"-...","C":"-.-.","D":"-..","E":".","F":"..-.","G":"--.","H":"....",
"I":"..","J":".---","K":"-.-","L":".-..","M":"--","N":"-.","O":"---","P":".--.",
"Q":"--.-","R":".-.","S":"...","T":"-","U":"..-","V":"...-","W":".--","X":"-..-",
"Y":"-.--","Z":"--..","0":"-----","1":".----","2":"..---","3":"...--","4":"....-",
"5":".....","6":"-....","7":"--...","8":"---..","9":"----.",".":" .-.-.-",",":" --..--",
"?":" ..--..","!":" -.-.--"," ":" / "}
DECODE = {v.strip(): k for k, v in CODE.items() if k != " "}

def encode(text):
    return " ".join(CODE.get(c.upper(), "") for c in text)

def decode(morse):
    words = morse.split(" / ")
    return " ".join("".join(DECODE.get(c, "?") for c in w.split()) for w in words)

def main():
    p = argparse.ArgumentParser(description="Morse code encoder/decoder")
    sub = p.add_subparsers(dest="cmd")
    e = sub.add_parser("encode"); e.add_argument("text", nargs="+")
    d = sub.add_parser("decode"); d.add_argument("morse", nargs="+")
    a = p.parse_args()
    if a.cmd == "encode": print(encode(" ".join(a.text)))
    elif a.cmd == "decode": print(decode(" ".join(a.morse)))
    else: p.print_help()

if __name__ == "__main__": main()
