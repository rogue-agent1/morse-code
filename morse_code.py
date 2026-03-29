import sys, argparse

MORSE = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.",
    "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
    "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
    "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
    "Y": "-.--", "Z": "--..", "0": "-----", "1": ".----", "2": "..---",
    "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...",
    "8": "---..", "9": "----.", " ": "/",
}
REVERSE = {v: k for k, v in MORSE.items()}

def encode(text):
    return " ".join(MORSE.get(c.upper(), c) for c in text)

def decode(morse):
    return "".join(REVERSE.get(s, s) for s in morse.split(" "))

def main():
    p = argparse.ArgumentParser(description="Morse code encoder/decoder")
    p.add_argument("action", choices=["encode", "decode", "e", "d"])
    p.add_argument("text", nargs="?")
    args = p.parse_args()
    text = args.text or sys.stdin.read().strip()
    print(encode(text) if args.action in ("encode", "e") else decode(text))

if __name__ == "__main__":
    main()
