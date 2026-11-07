#!/usr/bin/env python3
"""Força bruta de cifra de César e decifra Vigenère com chave conhecida.

Uso:
    python3 caesar.py "synt{grfgr}"              # mostra os 26 deslocamentos
    python3 caesar.py -k 3 "texto"               # deslocamento fixo
    python3 caesar.py -v CHAVE "texto cifrado"   # Vigenère com chave
"""
import sys

FLAG_HINTS = ("flag", "ctf", "{")


def shift(text, k):
    out = []
    for c in text:
        if c.isupper():
            out.append(chr((ord(c) - 65 + k) % 26 + 65))
        elif c.islower():
            out.append(chr((ord(c) - 97 + k) % 26 + 97))
        else:
            out.append(c)
    return "".join(out)


def caesar_brute(text):
    for k in range(26):
        res = shift(text, k)
        marker = "  <-- olhar" if any(h in res.lower() for h in FLAG_HINTS) else ""
        print(f"ROT {k:2}: {res}{marker}")


def vigenere(text, key, decrypt=True):
    key = [ord(k.lower()) - 97 for k in key if k.isalpha()]
    out, j = [], 0
    for c in text:
        if c.isalpha():
            k = key[j % len(key)]
            if decrypt:
                k = -k
            base = 65 if c.isupper() else 97
            out.append(chr((ord(c) - base + k) % 26 + base))
            j += 1
        else:
            out.append(c)
    return "".join(out)


def main():
    a = sys.argv[1:]
    if not a:
        print(__doc__)
        return
    if a[0] in ("-v", "--vigenere"):
        print(vigenere(a[2], a[1]))
    elif a[0] in ("-k", "--key"):
        print(shift(a[2], int(a[1])))
    else:
        caesar_brute(a[0])


if __name__ == "__main__":
    main()
