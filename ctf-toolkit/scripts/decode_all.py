#!/usr/bin/env python3
"""Tenta decodificar uma string de várias formas comuns em CTF.

Uso:
    python3 decode_all.py "ZmxhZ3toZWxsb30="
    python3 decode_all.py -r "texto"      # modo recursivo (tenta re-decodificar)
    echo "texto" | python3 decode_all.py  # lê da stdin

Mostra só resultados que viram texto ASCII imprimível, para reduzir ruído.
"""
import sys
import base64
import binascii
import codecs
import urllib.parse

FLAG_HINTS = ("flag{", "ctf{", "picoctf{", "flag", "ctf")


def printable(b):
    """True se os bytes forem majoritariamente texto legível."""
    if not b:
        return False
    try:
        s = b.decode("utf-8")
    except UnicodeDecodeError:
        return False
    ok = sum(1 for c in s if 32 <= ord(c) < 127 or c in "\n\t")
    return ok / len(s) > 0.85


def show(label, data):
    if isinstance(data, str):
        data = data.encode()
    if printable(data):
        text = data.decode("utf-8", "replace").strip()
        marker = "  <-- POSSÍVEL FLAG" if any(h in text.lower() for h in FLAG_HINTS) else ""
        print(f"[{label:14}] {text}{marker}")
        return text
    return None


def attempts(s):
    """Gera (rótulo, resultado) para cada tentativa de decodificação."""
    raw = s.strip()
    b = raw.encode()

    # Base64 / 32 / 85
    for name, fn in (("base64", base64.b64decode),
                     ("base32", base64.b32decode),
                     ("base85", base64.b85decode),
                     ("ascii85", base64.a85decode)):
        try:
            yield name, fn(raw + "=" * (-len(raw) % 8) if name == "base32" else raw)
        except Exception:
            pass

    # Hex
    try:
        yield "hex", binascii.unhexlify(raw.replace(" ", "").replace("0x", ""))
    except Exception:
        pass

    # Binário (ex: "01100110 01101100...")
    try:
        bits = raw.replace(" ", "")
        if set(bits) <= {"0", "1"} and len(bits) % 8 == 0:
            yield "binario", bytes(int(bits[i:i+8], 2) for i in range(0, len(bits), 8))
    except Exception:
        pass

    # Decimal separado por espaço/vírgula (ex: "102 108 97 103")
    try:
        parts = raw.replace(",", " ").split()
        if parts and all(p.isdigit() for p in parts):
            yield "decimal", bytes(int(p) for p in parts)
    except Exception:
        pass

    # URL encoding
    if "%" in raw:
        yield "url", urllib.parse.unquote(raw)

    # ROT13 e ROT47
    yield "rot13", codecs.encode(raw, "rot_13")
    yield "rot47", "".join(chr(33 + (ord(c) - 33 + 47) % 94) if 33 <= ord(c) <= 126 else c for c in raw)

    # Atbash (A<->Z)
    atb = []
    for c in raw:
        if c.isupper():
            atb.append(chr(ord("Z") - (ord(c) - ord("A"))))
        elif c.islower():
            atb.append(chr(ord("z") - (ord(c) - ord("a"))))
        else:
            atb.append(c)
    yield "atbash", "".join(atb)


def run(s, recursive=False, depth=0, seen=None):
    if seen is None:
        seen = set()
    if depth > 4 or s in seen:
        return
    seen.add(s)
    for label, result in attempts(s):
        text = show(f"{label}", result)
        if recursive and text and text != s:
            run(text, recursive, depth + 1, seen)


def main():
    args = [a for a in sys.argv[1:] if a not in ("-r", "--recursive")]
    recursive = any(a in ("-r", "--recursive") for a in sys.argv[1:])
    data = args[0] if args else sys.stdin.read()
    print(f"Entrada: {data.strip()}\n")
    run(data, recursive)


if __name__ == "__main__":
    main()
