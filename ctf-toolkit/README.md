# 🏴 CTF Toolkit

Coleção pessoal de links, comandos e scripts para competições CTF.

## 📁 Estrutura

| Arquivo | Conteúdo |
|---|---|
| [`LINKS.md`](LINKS.md) | Sites e ferramentas organizados por categoria |
| [`cheatsheets/COMANDOS.md`](cheatsheets/COMANDOS.md) | Comandos de terminal por categoria |
| [`cheatsheets/METODOLOGIA.md`](cheatsheets/METODOLOGIA.md) | Checklist do que tentar primeiro em cada tipo de desafio |
| [`scripts/decode_all.py`](scripts/decode_all.py) | Decodifica base64/32/85, hex, binário, decimal, URL, ROT13/47… |
| [`scripts/caesar.py`](scripts/caesar.py) | Força bruta de César (26 deslocamentos) + Vigenère com chave |
| [`scripts/xor_tool.py`](scripts/xor_tool.py) | XOR: brute de 1 byte e recuperação de chave com prefixo conhecido |
| [`scripts/rsa_tool.py`](scripts/rsa_tool.py) | RSA: decifrar com p/q, `e` pequeno, Fermat |
| [`scripts/pwn_template.py`](scripts/pwn_template.py) | Template pwntools (local / remoto / GDB) |
| [`scripts/web_template.py`](scripts/web_template.py) | Template `requests` + checagem de caminhos comuns |
| [`scripts/triage.sh`](scripts/triage.sh) | Análise inicial de qualquer arquivo (file, exif, strings, binwalk, stego) |
| [`setup.sh`](setup.sh) | Instala as ferramentas principais (Debian/Ubuntu/Kali) |

---

## 💻 Rodando SEM Linux (só navegador)

Sem notebook próprio e sem ambiente Linux, dá pra fazer **quase tudo pelo navegador**. Veja por necessidade.

### 🥇 Google Colab — um Linux inteiro no navegador

[colab.research.google.com](https://colab.research.google.com/) é a melhor opção: te dá uma máquina Linux completa, só precisa de conta Google e internet. Roda os scripts deste kit **e** comandos de Linux.

**Passo a passo:**

1. Abra o Colab e crie um notebook novo (`Arquivo → Novo notebook`).
2. Para enviar os arquivos do desafio: clique no ícone de **pasta** na barra lateral esquerda → **upload** (⬆️). Eles ficam em `/content/`.
3. Numa célula, **instale as ferramentas** (o `!` roda comando de terminal):
   ```python
   !apt install -y steghide binwalk exiftool foremost
   !pip install pwntools requests
   ```
4. **Rode comandos de Linux** com `!` na frente:
   ```python
   !file imagem.png
   !strings -n 6 imagem.png | grep -i flag
   !binwalk imagem.png
   !exiftool foto.jpg
   ```
5. **Rode os scripts deste kit** — suba o `.py` pelo upload e execute:
   ```python
   !python3 decode_all.py "ZmxhZ3toZWxsb30="
   !python3 rsa_tool.py --n 3233 --e 17 --c 2557
   ```
   Ou cole o conteúdo do script direto numa célula.

> 💡 O Colab resolve tanto os scripts Python quanto o `triage.sh` inteiro. É o mais perto de ter um Kali sem notebook.

### 🥈 Resolver direto no site (sem rodar nada)

Boa parte do que os scripts fazem já existe pronto na web:

| Em vez de… | Use |
|---|---|
| `decode_all.py`, `xor_tool.py`, `caesar.py` | [CyberChef](https://gchq.github.io/CyberChef/) — receita **Magic** adivinha sozinha |
| `triage.sh` em imagens | [Aperi'Solve](https://www.aperisolve.com/) — roda binwalk, zsteg, steghide, exif de uma vez |
| `rsa_tool.py` (fatorar N) | [FactorDB](http://factordb.com/) + [Alpertron](https://www.alpertron.com.ar/ECM.HTM) |
| cifras clássicas | [dCode](https://www.dcode.fr/en) |

### 🥉 Python puro, sem `apt`

Para scripts que só usam Python padrão (decode, caesar, xor, rsa) e não precisam instalar ferramenta de sistema:

- [OnlineGDB](https://www.onlinegdb.com/online_python_compiler) · [Programiz](https://www.programiz.com/python-programming/online-compiler/) · [Replit](https://replit.com/)

> ⚠️ Esses **não** têm `apt`, então não rodam steghide/binwalk. Para stego/forense, use o Colab ou os sites acima.

### ⚠️ Dois cuidados

1. **Tudo isso depende de internet liberada no CTF.** Se a rede for fechada, baixe antes o [CyberChef standalone](https://github.com/gchq/CyberChef/releases) — é **um único arquivo HTML que roda offline** no navegador. Confirme com a organização se haverá internet externa.
2. **Pense antes de subir o arquivo do desafio em site de terceiros.** Em treino é tranquilo; se for algo sigiloso, prefira o Colab (teu próprio ambiente) a jogar num site público.

**Resumo:** Colab pra fazer de tudo · CyberChef + Aperi'Solve + FactorDB pra resolver rápido sem instalar nada.

---

## 🔎 Guia de percepção — reconhecendo os padrões

A maior parte do tempo em CTF é **descobrir que tipo de desafio é aquilo**. Estes são os sinais que entregam o jogo.

### Cheiros de codificação (muito comuns)

| Você vê… | Provavelmente é… | Faça |
|---|---|---|
| Texto com `=` no final, letras e números | **Base64** | CyberChef / `decode_all.py` |
| Só `A–Z` e `2–7`, geralmente MAIÚSCULO | **Base32** | `decode_all.py` |
| Só `0-9 a-f`, tamanho par | **Hex** | `xxd -r -p` ou CyberChef |
| Só `0` e `1`, em blocos de 8 | **Binário** | `decode_all.py` |
| Números separados por espaço (65 66 67…) | **Decimal / ASCII** | `decode_all.py` |
| `%41%42` no meio de uma URL | **URL encoding** | CyberChef |
| `=C3=A9`, `=20` | **Quoted-printable** | CyberChef |
| Texto embaralhado mas com a MESMA estrutura da flag | **ROT13 / César** | `caesar.py` |
| `.... . .-..` | **Código Morse** | dCode |
| `++++.>+++` | **Brainfuck** (esolang) | dCode / tio.run |

> 🧠 Regra prática: se o texto tem só um alfabeto limitado, é **encoding** (reversível direto). Se tem chave/senha envolvida, é **cripto** (precisa de ataque).

### Sinais por categoria

**🔐 Crypto** — viu `n`, `e`, `c` grandes? É **RSA**. Dois textos cifrados do mesmo tamanho? Suspeite de **XOR**. Chave/palavra repetida? **Vigenère**. Um hash isolado (32/40/64 hex)? Não "descriptografa" — tem que quebrar (CrackStation/hashcat).

**🌐 Web** — SEMPRE veja o código-fonte (Ctrl+U) e os comentários `<!-- -->`. Olhe `/robots.txt`, `/.git/`, cookies e headers. Campo de login → teste `' OR 1=1 -- -` (SQLi). Reflete o que você digita → XSS. Renderiza `{{7*7}}` como `49` → SSTI. Parâmetro com nome de arquivo → LFI (`../../etc/passwd`).

**🖼️ Stego** — extensão não bate com o `file`? Header quebrado. `exiftool` primeiro (metadados escondem muita flag). Imagem "normal" demais → LSB (zsteg/StegOnline). **Áudio** → abra o **espectrograma** (a mensagem costuma estar desenhada nele).

**🔎 Forense** — `file` sempre primeiro. ZIP/PDF com senha → `zip2john`/`pdf2john` + John. `.pcap` → Wireshark, siga os streams TCP, exporte objetos HTTP. Dump de memória → Volatility.

**⚙️ Reversing** — `strings` antes de tudo (a flag pode estar à vista). Depois descompile no [Dogbolt](https://dogbolt.org/)/Ghidra. `.pyc` → descompilador de Python. APK → JADX.

### O título e o nome do arquivo são DICAS

O nome do desafio quase sempre aponta a técnica. Alguns clássicos:
- "Caesar's secret", "Salad" → César/ROT
- "Repeating key", "Vernam" → XOR/Vigenère
- "Broadcast", "small e", "cube" → ataque específico de RSA
- "Looks can deceive", "hidden" → esteganografia
- "SQL", "injection", "little bobby" → SQLi
- "Baby", "intro", "warmup" no nome → é o mais fácil daquela categoria, comece por eles

### Formato da flag é sua bússola

Descubra cedo o formato (`flag{...}`, `CTF{...}`, `picoCTF{...}`) e faça `grep` por ele em **tudo**:
```bash
grep -raoE 'flag\{[^}]*\}' .
```
Achou algo que *parece* mas não é a flag exata? Provavelmente é a resposta de um passo intermediário — continue a cadeia.

### Erros que fazem perder tempo

- ❌ Ficar travado 1h no mesmo desafio → troque e volte com a cabeça fresca.
- ❌ Ignorar o enunciado → leia duas vezes, cada palavra pode ser pista.
- ❌ Confiar na extensão do arquivo → rode `file` sempre.
- ❌ Esquecer de tentar **senha vazia** no steghide (`-p ""`) e usuários/senhas óbvios (`admin:admin`).
- ❌ Decodificar uma camada e parar → muitos desafios têm 2-3 camadas (base64 → hex → ROT…).

---

## ⚡ Uso rápido (com Linux)

```bash
git clone https://github.com/Joao0015/ctf-toolkit && cd ctf-toolkit
chmod +x setup.sh scripts/*.sh scripts/*.py
./setup.sh                      # opcional, instala ferramentas

python3 scripts/decode_all.py "ZmxhZ3toZWxsb30="
python3 scripts/caesar.py "synt{grfgr}"
python3 scripts/xor_tool.py --hex 1c1a0f1e... --prefix "flag{"
python3 scripts/rsa_tool.py --n N --e E --c C
./scripts/triage.sh imagem.png "picoCTF"
```

## 🧠 Regra de ouro

1. Leia o enunciado e o **título** duas vezes — quase sempre são dicas.
2. Descubra o formato da flag e faça `grep` por ele em tudo.
3. Travou 20 min? Troque de desafio e volte depois.
