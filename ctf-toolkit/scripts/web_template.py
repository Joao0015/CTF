#!/usr/bin/env python3
"""Template de interação web com requests + checagem de caminhos comuns.

Uso:
    python3 web_template.py http://alvo:porta/

Requer: pip install requests
"""
import sys
import requests

COMMON_PATHS = [
    "robots.txt", ".git/HEAD", ".git/config", "sitemap.xml",
    "admin", "login", "flag", "flag.txt", "backup", "backup.zip",
    ".env", "config.php", "index.php.bak", "api", "debug",
    ".htaccess", "server-status", "phpinfo.php",
]


def check_paths(base):
    print(f"[*] Checando caminhos comuns em {base}")
    for path in COMMON_PATHS:
        url = base.rstrip("/") + "/" + path
        try:
            r = requests.get(url, timeout=5, allow_redirects=False)
            if r.status_code < 400 or r.status_code in (401, 403):
                print(f"  [{r.status_code}] {url}  ({len(r.content)} bytes)")
        except requests.RequestException:
            pass


def demo_session(base):
    """Exemplo de sessão com cookie/parâmetros — edite para o desafio."""
    s = requests.Session()
    s.headers.update({"User-Agent": "ctf"})
    # s.cookies.set("admin", "1")

    r = s.get(base)
    print(f"\n[*] GET {base} -> {r.status_code}")
    for h in ("Server", "X-Powered-By", "Set-Cookie", "Location"):
        if h in r.headers:
            print(f"    {h}: {r.headers[h]}")

    # Procura a flag no corpo e nos comentários
    for marker in ("flag{", "CTF{", "<!--"):
        if marker in r.text:
            i = r.text.find(marker)
            print(f"    encontrado '{marker}': ...{r.text[i:i+80]}...")

    # Exemplos de payload (descomente e adapte):
    # r = s.get(base, params={"id": "1' OR '1'='1"})          # SQLi
    # r = s.get(base, params={"page": "../../../../etc/passwd"})  # LFI
    # r = s.post(base + "/login", data={"user": "admin", "pass": "x' OR 1=1-- -"})


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return
    base = sys.argv[1]
    if not base.startswith("http"):
        base = "http://" + base
    check_paths(base)
    demo_session(base)


if __name__ == "__main__":
    main()
