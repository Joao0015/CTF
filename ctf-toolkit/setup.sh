#!/usr/bin/env bash
# Instala as ferramentas principais de CTF (Debian/Ubuntu/Kali).
# Uso: ./setup.sh
set -e

echo "[*] Atualizando apt..."
sudo apt update

echo "[*] Instalando ferramentas base..."
sudo apt install -y \
  file binutils xxd exiftool steghide binwalk foremost \
  zsteg pngcheck sox imagemagick \
  tshark tcpflow nmap gobuster ffuf nikto \
  hashcat john hashid \
  gdb ltrace strace radare2 \
  python3 python3-pip curl git || \
  echo "[!] Alguns pacotes podem não existir na sua distro; instale manualmente."

echo "[*] Instalando pacotes Python..."
pip3 install --user pwntools requests ropgadget || true

echo "[*] Plugins de GDB (opcional) — descomente se quiser:"
echo "    git clone https://github.com/pwndbg/pwndbg && cd pwndbg && ./setup.sh"

echo "[*] Wordlist rockyou:"
echo "    Kali: /usr/share/wordlists/rockyou.txt (pode precisar: gunzip rockyou.txt.gz)"

echo "[+] Pronto. Dê permissão aos scripts: chmod +x scripts/*"
