# 💻 Comandos por categoria

## 🔍 Reconhecimento de arquivo
```bash
file arquivo                       # identifica o tipo real (ignora a extensão)
xxd arquivo | head                 # ver bytes/header (magic bytes)
exiftool arquivo                   # metadados (autor, GPS, comentários…)
strings -n 6 arquivo               # strings legíveis (ótimo p/ achar a flag)
strings -e l arquivo               # strings UTF-16 (little-endian)
binwalk arquivo                    # detecta arquivos embutidos
binwalk -e arquivo                 # extrai o que encontrar
foremost arquivo                   # recupera arquivos por carving
grep -raoE 'flag\{[^}]*\}' .       # procura a flag em tudo recursivamente
```

## 🖼️ Esteganografia
```bash
steghide extract -sf img.jpg               # extrai (pede senha; tente vazia)
stegseek img.jpg wordlist.txt              # brute force da senha do steghide
zsteg -a img.png                           # LSB em PNG/BMP (-a = todos os métodos)
zsteg -E 'b1,rgb,lsb,xy' img.png           # extrai um canal específico
pngcheck -v img.png                         # valida/mostra chunks do PNG
convert img.png -separate canais_%d.png     # separa canais RGBA (ImageMagick)
```

## 🎵 Áudio
```bash
# Abra no Audacity/Sonic Visualiser e veja o ESPECTROGRAMA
sox audio.wav -n spectrogram -o spec.png    # gera espectrograma via linha de comando
# DTMF (tons de telefone) e SSTV também aparecem no espectrograma
```

## 🌐 Rede / PCAP
```bash
tshark -r cap.pcap                                  # lista pacotes
tshark -r cap.pcap -Y 'http.request'                # só requisições HTTP
tshark -r cap.pcap -z follow,tcp,ascii,0            # segue um stream TCP
tcpflow -r cap.pcap                                 # reconstrói streams em arquivos
# No Wireshark: File > Export Objects > HTTP para extrair arquivos transferidos
# Filtros úteis: http  |  dns  |  ftp-data  |  tcp.stream eq 0
```

## 🔐 Hashes e senhas
```bash
hashid 'HASH'                                       # identifica o tipo de hash
hashcat -m 0 hash.txt rockyou.txt                   # -m 0 = MD5 (veja a wiki p/ o modo)
john --wordlist=rockyou.txt hash.txt                # John the Ripper
john --format=NT hash.txt                           # especifica o formato
zip2john arq.zip > h.txt && john h.txt              # senha de ZIP
# Extratores: pdf2john, rar2john, ssh2john, office2john, keepass2john…
# A rockyou costuma estar em /usr/share/wordlists/rockyou.txt (Kali)
```

## 🌐 Web / enumeração
```bash
curl -s -i http://alvo/                             # headers + corpo
curl -s http://alvo/ -H 'Cookie: admin=1'           # mandar cookie
gobuster dir -u http://alvo -w wordlist.txt         # fuzz de diretórios
ffuf -u http://alvo/FUZZ -w wordlist.txt            # fuzzing flexível
ffuf -u http://alvo/ -H 'Host: FUZZ.alvo' -w sub.txt # vhost/subdomínio
nikto -h http://alvo                                # scanner de vulnerabilidades
# Sempre olhe: /robots.txt  /.git/  /sitemap.xml  código-fonte (Ctrl+U)
```

## ⚙️ Reversing / Pwn
```bash
checksec --file=./bin           # proteções (NX, PIE, Canary, RELRO)
nm ./bin                        # símbolos/funções
objdump -d -M intel ./bin       # desmontar (sintaxe Intel)
ltrace ./bin                    # chamadas de biblioteca
strace ./bin                    # chamadas de sistema
ROPgadget --binary ./bin        # procurar gadgets ROP
one_gadget ./libc.so.6          # achar one-shot RCE na libc
gdb ./bin                       # (com pwndbg/GEF instalado)
```

## 🔢 Conversões rápidas (terminal)
```bash
echo -n 'texto' | base64                            # codifica base64
echo 'dGV4dG8=' | base64 -d                          # decodifica
echo -n 'texto' | xxd -p                             # texto → hex
echo '7465787400' | xxd -r -p                        # hex → texto
echo 'ibg{...}' | tr 'A-Za-z' 'N-ZA-Mn-za-m'         # ROT13
printf '%d\n' 0x1337                                 # hex → decimal
python3 -c "print(0x41)"                             # avaliar expressões
```
