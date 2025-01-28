import urllib.request
from bs4 import BeautifulSoup


def get_html(url):
    """Stáhne a vrátí HTML kód stránky."""
    try:
        with urllib.request.urlopen(url) as response:
            return response.read().decode("utf-8")
    except Exception as e:
        print(f"Chyba při připojování k URL {url}: {e}")
        return None


def parse_page(url):
    """Stáhne HTML, vrátí titulek a seznam odkazů."""
    html = get_html(url)
    if html is None:
        return None, []

    soup = BeautifulSoup(html, "html.parser")

    # Získat titulek stránky
    title = soup.title.string.strip() if soup.title else "Bez titulku"

    # Získat všechny odkazy na stránce
    links = [link["href"] for link in soup.find_all("a", href=True)]

    return title, links


def absolute_url(base_url, link):
    """Zajistí, že URL odkazu bude absolutní."""
    if link.startswith("http://") or link.startswith("https://"):
        return link
    if link.startswith("/"):
        return base_url.rstrip("/") + link
    return base_url.rstrip("/") + "/" + link


def main():
    # Hlavní URL
    main_url = "http://vlada.cz"
    print(f"Stahuji hlavní stránku: {main_url}")

    # Zpracovat hlavní stránku
    main_title, main_links = parse_page(main_url)
    print(f"\nTitulek hlavní stránky: {main_title}")
    print(f"Počet odkazů na hlavní stránce: {len(main_links)}")

    # Vytvořit seznam unikátních absolutních URL odkazů
    unique_links = list({absolute_url(main_url, link) for link in main_links})

    # Zpracovat každou stránku na 2. úrovni
    print("\nZpracovávám odkazy na 2. úrovni...")
    for link in unique_links:
        print(f"\nNavštěvuji: {link}")
        title, links = parse_page(link)
        if title is not None:
            print(f"Titulek: {title}")
            print(f"Počet odkazů na stránce: {len(links)}")
        else:
            print("Chyba při zpracování stránky.")


if __name__ == "__main__":
    main()