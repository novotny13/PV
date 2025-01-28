import urllib.request

# URL stránky
url = "http://vlada.cz"

try:
    # Otevření URL a načtení obsahu
    print(f"Připojuji se k {url}...")
    with urllib.request.urlopen(url) as response:
        # Zjištění kódování stránky (default na UTF-8, pokud není uvedeno)
        encoding = response.headers.get_content_charset() or "utf-8"
        print(f"Použité kódování: {encoding}")

        # Přečtení obsahu a dekódování
        html = response.read().decode(encoding)

    # Výpis HTML kódu jako prostý text
    print("HTML kód stránky:")
    print(html)

except urllib.error.URLError as e:
    print(f"Chyba při načítání stránky: {e}")
except Exception as ex:
    print(f"Neočekávaná chyba: {ex}")