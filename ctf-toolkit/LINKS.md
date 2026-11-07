# 🔗 Links úteis para CTF

## 🧰 Canivetes suíços (abra primeiro)
- [CyberChef](https://gchq.github.io/CyberChef/) — decodificar/converter qualquer coisa. Use a receita **Magic** quando não souber o que é.
- [dCode](https://www.dcode.fr/en) — centenas de cifras e um identificador de cifras (`Cipher Identifier`).
- [HackTricks](https://book.hacktricks.wiki/) — wiki gigante de técnicas (web, pwn, privesc, forense).
- [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings) — payloads de SQLi, XSS, SSTI, LFI, etc.
- [CTF 101](https://ctf101.org/) — explicações básicas de cada categoria.
- [CTF Katana](https://github.com/JohnHammond/ctf-katana) — lista de truques por categoria.

## 🔐 Criptografia
- [quipqiup](https://quipqiup.com/) — resolve cifra de substituição monoalfabética.
- [Vigenère solver (guballa)](https://www.guballa.de/vigenere-solver) — quebra Vigenère sem chave.
- [Boxentriq Code Breaking](https://www.boxentriq.com/code-breaking) — várias cifras clássicas + identificador.
- [CrypTool Online](https://www.cryptool.org/en/cto/) — cifras clássicas e modernas.
- [FactorDB](http://factordb.com/) — fatoração de N (RSA) já conhecida.
- [Alpertron ECM](https://www.alpertron.com.ar/ECM.HTM) — fatorar números grandes no navegador.
- [RsaCtfTool](https://github.com/RsaCtfTool/RsaCtfTool) — automatiza dezenas de ataques RSA.
- [CrackStation](https://crackstation.net/) — lookup de hashes (MD5, SHA1…).
- [Hashes.com](https://hashes.com/en/decrypt/hash) — outro lookup de hash.
- [Hashcat example hashes](https://hashcat.net/wiki/doku.php?id=example_hashes) — identificar tipo de hash e modo `-m`.
- [Ciphey](https://github.com/Ciphey/Ciphey) — decodificação automática.
- [Cryptohack](https://cryptohack.org/) — treino de cripto.

## 🌐 Web
- [jwt.io](https://jwt.io/) — decodificar/editar JWT.
- [webhook.site](https://webhook.site/) — receber requisições (XSS, SSRF, exfiltração).
- [RequestBin (Pipedream)](https://pipedream.com/requestbin) — alternativa ao webhook.site.
- [RevShells](https://www.revshells.com/) — gerador de reverse shells.
- [GTFOBins](https://gtfobins.github.io/) — abuso de binários Unix (privesc, escape de shell).
- [LOLBAS](https://lolbas-project.github.io/) — equivalente para Windows.
- [SSTI payloads (HackTricks)](https://book.hacktricks.wiki/en/pentesting-web/ssti-server-side-template-injection/index.html)
- [PortSwigger XSS cheat sheet](https://portswigger.net/web-security/cross-site-scripting/cheat-sheet)
- [PortSwigger SQLi cheat sheet](https://portswigger.net/web-security/sql-injection/cheat-sheet)
- [PortSwigger Web Security Academy](https://portswigger.net/web-security) — teoria de cada vulnerabilidade.
- [RegExr](https://regexr.com/) — testar regex.
- [Wayback Machine](https://web.archive.org/) — versões antigas de páginas.
- [SecLists](https://github.com/danielmiessler/SecLists) — wordlists (diretórios, senhas, fuzzing).

## 🖼️ Esteganografia
- [Aperi'Solve](https://www.aperisolve.com/) — roda zsteg, steghide, exiftool, binwalk e planos de bits de uma vez.
- [StegOnline](https://georgeom.net/StegOnline) — planos de bits, LSB, manipulação de imagem.
- [FotoForensics](https://fotoforensics.com/) — ELA, metadados.
- [Steganography Online (stylesuxx)](https://stylesuxx.github.io/steganography/) — LSB simples.
- [Sonic Visualiser](https://www.sonicvisualiser.org/) — espectrograma de áudio (mensagens escondidas em .wav).
- [stegseek](https://github.com/RickdeJager/stegseek) — brute force de senha do steghide (muito rápido).

## 🔎 Forense
- [List of file signatures](https://en.wikipedia.org/wiki/List_of_file_signatures) — magic bytes para consertar headers.
- [Gary Kessler file signatures](https://www.garykessler.net/library/file_sigs.html)
- [Wireshark display filters](https://www.wireshark.org/docs/dfref/) — referência de filtros.
- [Volatility 3](https://github.com/volatilityfoundation/volatility3) — análise de dump de memória.
- [Volatility cheatsheet (HackTricks)](https://book.hacktricks.wiki/en/generic-methodologies-and-resources/basic-forensic-methodology/memory-dump-analysis/volatility-cheatsheet.html)
- [hexed.it](https://hexed.it/) — editor hexadecimal no navegador.
- [Autopsy](https://www.autopsy.com/) — análise de imagens de disco.

## ⚙️ Reversing
- [Dogbolt (Decompiler Explorer)](https://dogbolt.org/) — compara Ghidra, IDA, Binary Ninja etc. no navegador.
- [Compiler Explorer](https://godbolt.org/) — ver o assembly gerado por código C/C++.
- [Ghidra](https://ghidra-sre.org/) — descompilador gratuito.
- [Cutter](https://cutter.re/) — GUI do radare2.
- [dnSpy / dnSpyEx](https://github.com/dnSpyEx/dnSpy) — binários .NET.
- [JADX](https://github.com/skylot/jadx) — APK/Java.
- [pylingual](https://pylingual.io/) / [uncompyle6](https://github.com/rocky/python-uncompyle6) — descompilar `.pyc`.
- [x86 / x64 reference](https://www.felixcloutier.com/x86/) — instruções assembly.

## 💥 Pwn / Binary Exploitation
- [pwntools docs](https://docs.pwntools.com/en/stable/)
- [libc.rip](https://libc.rip/) — descobrir versão da libc pelos offsets vazados.
- [libc database (blukat)](https://libc.blukat.me/) — alternativa.
- [Syscall table x64](https://x64.syscall.sh/) — números de syscalls (x86, ARM também).
- [Shell-storm shellcodes](https://shell-storm.org/shellcode/index.html)
- [ROPgadget](https://github.com/JonathanSalwan/ROPgadget) / [ropper](https://github.com/sashs/Ropper)
- [pwndbg](https://github.com/pwndbg/pwndbg) / [GEF](https://github.com/hugsy/gef) — plugins do GDB.
- [one_gadget](https://github.com/david942j/one_gadget)
- [Nightmare](https://guyinatuxedo.github.io/) — curso de pwn com desafios resolvidos.

## 🕵️ OSINT
- [OSINT Framework](https://osintframework.com/) — mapa de ferramentas.
- [WhatsMyName](https://whatsmyname.app/) — procurar username em centenas de sites.
- [Google Lens](https://lens.google/) / [Yandex Images](https://yandex.com/images/) / [TinEye](https://tineye.com/) — busca reversa de imagem.
- [crt.sh](https://crt.sh/) — certificados → subdomínios.
- [DNSDumpster](https://dnsdumpster.com/) — mapeamento DNS.
- [Shodan](https://www.shodan.io/) — dispositivos expostos.
- [Google Dorks (Exploit-DB GHDB)](https://www.exploit-db.com/google-hacking-database)
- [SunCalc](https://www.suncalc.org/) — geolocalização por sombra/sol.
- [Overpass Turbo](https://overpass-turbo.eu/) — busca de elementos no OpenStreetMap.

## 🎲 Misc
- [Esolang decoders (dCode)](https://www.dcode.fr/brainfuck-language) — Brainfuck, Ook!, Malbolge…
- [Try It Online](https://tio.run/) — rodar código em centenas de linguagens (inclusive esotéricas).
- [QR code decoder (ZXing)](https://zxing.org/w/decode.jspx)
- [Morse decoder](https://morsecode.world/international/translator.html)
- [Unicode text steganography](https://330k.github.io/misc_tools/unicode_steganography.html) — caracteres de largura zero.
- [Braille / símbolos](https://www.dcode.fr/braille-alphabet)

## 📚 Treino e referência
- [CTFtime](https://ctftime.org/) — calendário e writeups.
- [picoCTF](https://picoctf.org/) · [OverTheWire](https://overthewire.org/wargames/) · [pwn.college](https://pwn.college/) · [TryHackMe](https://tryhackme.com/) · [Hack The Box](https://www.hackthebox.com/)
