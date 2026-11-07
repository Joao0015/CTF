#!/usr/bin/env python3
"""Ataques de XOR comuns em CTF.

Uso:
    # Brute force de chave de 1 byte (testa as 256 possibilidades)
    python3 xor_tool.py --hex 1c1a0f1e... --brute
    python3 xor_tool.py --str "texto" --brute

    # Recuperar a chave quando você sabe o começo do texto claro
    python3 xor_tool.py --hex 1c1a0f... --prefix "flag{"

    # XOR com chave conhecida (texto ou hex)
    python3 xor_tool.py --hex 1c1a0f... --key "segredo"
"""
import sys
import argparse

FLAG_HINTS = (b"flag", b"ctf", b"{")


def xor(data, key):
    return bytes(b ^ key[i % len(key)] for i, b in enumerate(data))


def looks_text(b):
    return b and sum(1 for c in b if 32 <= c < 127 or c in b"\n\t") / len(b) > 0.9


def main():
    p = argparse.ArgumentParser()
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--hex")
    g.add_argument("--str")
    p.add_argument("--brute", action="store_true")
    p.add_argument("--prefix")
    p.add_argument("--key")
    args = p.parse_args()

    data = bytes.fromhex(args.hex.replace(" ", "")) if args.hex else args.str.encode()

    if args.brute:
        print("# Brute force de chave de 1 byte (só resultados legíveis):")
        for k in range(256):
            res = xor(data, bytes([k]))
            if looks_text(res):
                mark = "  <-- olhar" if any(h in res.lower() for h in FLAG_HINTS) else ""
                print(f"chave 0x{k:02x} ({k:3}): {res.decode('utf-8','replace')}{mark}")

    elif args.prefix:
        pfx = args.prefix.encode()
        key = xor(data[:len(pfx)], pfx)
        print(f"# Chave provável (dos primeiros {len(pfx)} bytes): {key!r}")
        print(f"# Como hex: {key.hex()}")
        print(f"# Texto completo com essa chave repetida:")
        print(xor(data, key).decode("utf-8", "replace"))

    elif args.key:
        key = bytes.fromhex(args.key) if all(c in "0123456789abcdefABCDEF" for c in args.key) and len(args.key) % 2 == 0 else args.key.encode()
        res = xor(data, key)
        print(res.decode("utf-8", "replace"))
    else:
        print(__doc__)


if __name__ == "__main__":
    main()
