import urllib.request
from bs4 import BeautifulSoup

# Stáhnutí HTML kódu stránky
url = "http://vlada.cz"
try:
    print(f"Stahuji HTML kód stránky {url}...")
    with urllib.request.urlopen(url) as response:
        html = response.read().decode("utf-8")
except Exception as e:
    print(f"Chyba při stahování stránky: {e}")
    exit()

# Parsování HTML kódu pomocí BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# 1. Titulek stránky
title = soup.title.string if soup.title else "Titulek nenalezen"
print(f"\nTitulek stránky:\n{title}")

# 2. Nadpisy úrovně H1 a H2
print("\nNadpisy H1 a H2 na stránce:")
for header in soup.find_all(["h1", "h2"]):
    print(f"{header.name}: {header.get_text(strip=True)}")

# 3. URL adresy všech odkazů na stránce
print("\nURL adresy všech odkazů na stránce:")
for link in soup.find_all("a", href=True):
    print(link["href"])