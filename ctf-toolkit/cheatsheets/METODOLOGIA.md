# 🧭 Metodologia — o que tentar primeiro

> Antes de tudo: leia o enunciado e o **título** (quase sempre é dica), e descubra o formato da flag.

## 🔐 Crypto
1. Parece base64/hex/binário? → `decode_all.py` ou CyberChef (receita **Magic**).
2. Só letras embaralhadas? → César (`caesar.py`), depois substituição (quipqiup).
3. Tem chave/palavra repetida? → Vigenère (guballa).
4. Viu `n`, `e`, `c`? → **RSA** (`rsa_tool.py`, RsaCtfTool, FactorDB).
5. Dois textos cifrados do mesmo tamanho? → suspeite de **XOR** (`xor_tool.py`).
6. Um hash? → CrackStation / hashcat. Não "descriptografa", só quebra por força.

## 🌐 Web
1. Veja o **código-fonte** (Ctrl+U) e os comentários.
2. `/robots.txt`, `/.git/`, `/sitemap.xml`, headers de resposta, cookies.
3. Campo de login/busca? → teste **SQLi** (`' OR 1=1 -- -`).
4. Reflete o que você digita? → **XSS**. Renderiza template? → **SSTI** (`{{7*7}}`).
5. Parâmetro com nome de arquivo/caminho? → **LFI/path traversal** (`../../etc/passwd`).
6. Parâmetro com URL? → **SSRF** (aponte p/ webhook.site).
7. JWT no cookie? → jwt.io (teste `alg: none`, chave fraca).

## 🖼️ Stego
1. `exiftool` → metadados e comentários.
2. `strings` → flag em texto claro.
3. `binwalk` → arquivo escondido dentro.
4. `steghide`/`stegseek` (JPG), `zsteg` (PNG/BMP).
5. Nada? → **Aperi'Solve** faz tudo de uma vez.
6. Áudio? → **espectrograma** (Sonic Visualiser / `sox`).

## 🔎 Forense
1. `file` sempre primeiro. Extensão errada ou header quebrado? → conserte os magic bytes.
2. ZIP/PDF com senha? → `zip2john`/`pdf2john` + John.
3. `.pcap`? → Wireshark, siga streams, exporte objetos HTTP.
4. Dump de memória? → **Volatility 3** (`windows.pslist`, `windows.cmdline`…).
5. Disco? → `binwalk`/`foremost`/Autopsy para recuperar arquivos.

## ⚙️ Reversing
1. `file` + `strings` (flag pode estar visível).
2. `checksec`, depois descompile: **Ghidra** / Dogbolt.
3. `.pyc` → pylingual/uncompyle6. `.class`/APK → JADX. `.NET` → dnSpy.
4. Ache a comparação da senha/flag; use `ltrace` para ver `strcmp`.

## 💥 Pwn
1. `checksec` → quais proteções (NX, PIE, Canary, RELRO).
2. Ache o **buffer overflow** (padrão cíclico do pwntools p/ achar o offset).
3. Sem canary + NX? → ret2win ou ret2libc (`libc.rip` p/ a versão).
4. Tem `system`/`/bin/sh` no binário? → ret2win direto.
5. Monte com `pwn_template.py`. Teste local antes do remoto.

## 🕵️ OSINT
1. Busca reversa de imagem (Lens/Yandex/TinEye).
2. Username? → WhatsMyName. Domínio? → crt.sh / DNSDumpster.
3. EXIF da foto pode ter GPS. Sombra/sol → SunCalc.
4. Leia metadados de qualquer documento fornecido.
