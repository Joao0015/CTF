#!/usr/bin/env bash
# Análise inicial de um arquivo desconhecido em CTF.
# Uso: ./triage.sh arquivo [prefixo_da_flag]
# Ex.: ./triage.sh imagem.png "picoCTF"

set -u
FILE="${1:-}"
FLAG="${2:-flag}"

if [ -z "$FILE" ] || [ ! -f "$FILE" ]; then
  echo "Uso: $0 arquivo [prefixo_da_flag]"
  exit 1
fi

have() { command -v "$1" >/dev/null 2>&1; }
line() { printf '\n===== %s =====\n' "$1"; }

line "TIPO (file)"
file "$FILE"

line "HEADER (primeiros bytes)"
xxd "$FILE" | head -n 4

line "TAMANHO"
ls -lh "$FILE" | awk '{print $5}'

if have exiftool; then
  line "METADADOS (exiftool)"
  exiftool "$FILE"
fi

line "BUSCA DIRETA PELA FLAG"
if strings -n 4 "$FILE" | grep -iE "${FLAG}\{?" ; then
  echo ">> Possível flag acima!"
else
  echo "(nada óbvio; veja as strings completas abaixo)"
fi

line "STRINGS (20 primeiras linhas)"
strings -n 6 "$FILE" | head -n 20

if have binwalk; then
  line "ARQUIVOS EMBUTIDOS (binwalk)"
  binwalk "$FILE"
fi

# Específico de imagens
case "$(file -b --mime-type "$FILE")" in
  image/png|image/bmp)
    if have zsteg; then line "ZSTEG (LSB)"; zsteg -a "$FILE" 2>/dev/null | head -n 30; fi
    if have pngcheck; then line "PNGCHECK"; pngcheck -v "$FILE" 2>/dev/null | head; fi
    ;;
  image/jpeg)
    if have steghide; then
      line "STEGHIDE (senha vazia)"
      steghide extract -sf "$FILE" -p "" 2>&1 | head
    fi
    ;;
esac

line "FIM"
echo "Próximos passos sugeridos: binwalk -e, Aperi'Solve (web), stegseek + rockyou."
