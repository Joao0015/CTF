#!/usr/bin/env python3
"""Ataques básicos de RSA para CTF.

Uso:
    # Você tem p e q (fatoração conhecida):
    python3 rsa_tool.py --p P --q Q --e E --c C

    # Você tem n (tenta Fermat: p e q próximos) e decifra:
    python3 rsa_tool.py --n N --e E --c C

    # 'e' pequeno (e=3) sem padding -> raiz e-ésima direta:
    python3 rsa_tool.py --n N --e 3 --c C --cube

Dica: se nada funcionar, cole o N em http://factordb.com/ ou use o RsaCtfTool.
Todos os números podem ser decimais ou hex (0x...).
"""
import sys
import argparse
from math import isqrt, gcd


def num(x):
    return int(x, 0) if isinstance(x, str) else x


def egcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x, y = egcd(b, a % b)
    return g, y, x - (a // b) * y


def inv(a, m):
    g, x, _ = egcd(a % m, m)
    if g != 1:
        raise ValueError("sem inverso modular (e e phi não são coprimos)")
    return x % m


def iroot(x, n):
    """Raiz n-ésima inteira (busca binária)."""
    if x < 0:
        return -1
    lo, hi = 0, 1 << ((x.bit_length() // n) + 1)
    while lo < hi:
        mid = (lo + hi) // 2
        if mid ** n < x:
            lo = mid + 1
        else:
            hi = mid
    return lo


def fermat(n):
    """Fatora n quando p e q estão próximos."""
    a = isqrt(n)
    if a * a < n:
        a += 1
    for _ in range(1 << 22):
        b2 = a * a - n
        b = isqrt(b2)
        if b * b == b2:
            return a - b, a + b
        a += 1
    return None


def to_text(m):
    """Converte o inteiro decifrado em bytes/texto."""
    length = (m.bit_length() + 7) // 8
    raw = m.to_bytes(length, "big")
    try:
        return raw.decode()
    except UnicodeDecodeError:
        return repr(raw)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--n")
    p.add_argument("--p")
    p.add_argument("--q")
    p.add_argument("--e", default="65537")
    p.add_argument("--c", required=True)
    p.add_argument("--cube", action="store_true", help="tenta raiz e-ésima (e pequeno, sem padding)")
    args = p.parse_args()

    e, c = num(args.e), num(args.c)

    # Caso 1: e pequeno, m^e < n -> raiz direta
    if args.cube:
        m = iroot(c, e)
        print(f"[cube/root] m = {m}")
        print(f"[cube/root] texto = {to_text(m)}")
        return

    pv = num(args.p) if args.p else None
    qv = num(args.q) if args.q else None

    # Caso 2: só n -> tenta Fermat
    if pv is None and args.n:
        n = num(args.n)
        print("[*] Tentando Fermat (p e q próximos)...")
        f = fermat(n)
        if not f:
            print("[!] Fermat falhou. Tente factordb.com ou RsaCtfTool.")
            return
        pv, qv = f
        print(f"[+] p = {pv}\n[+] q = {qv}")

    if pv is None or qv is None:
        print("[!] Preciso de (p e q) ou (n). Veja --help.")
        return

    n = pv * qv
    phi = (pv - 1) * (qv - 1)
    d = inv(e, phi)
    m = pow(c, d, n)
    print(f"[+] d = {d}")
    print(f"[+] m (int) = {m}")
    print(f"[+] texto = {to_text(m)}")


if __name__ == "__main__":
    main()
