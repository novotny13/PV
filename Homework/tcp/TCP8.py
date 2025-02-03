import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import time

def get_page_info(url):
    """Získá informace o stránce - titulek a odkazy"""
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Získání titulku
        title = soup.find('title')
        title_text = title.text.strip() if title else "Bez titulku"
        
        # Získání všech odkazů
        links = []
        for link in soup.find_all('a'):
            href = link.get('href')
            if href:
                # Převod relativních URL na absolutní
                absolute_url = urljoin(url, href)
                # Odfiltrování fragmentů a neplatných URL
                if absolute_url.startswith(('http://', 'https://')):
                    links.append(absolute_url)
        
        return title_text, links
    except Exception as e:
        print(f"Chyba při zpracování {url}: {str(e)}")
        return None, []

def main():
    # Hlavní URL
    start_url = "http://vlada.cz"
    
    # Získání informací o hlavní stránce
    print(f"\nZpracovávám hlavní stránku: {start_url}")
    title, main_links = get_page_info(start_url)
    
    if title:
        print(f"Titulek: {title}")
        print(f"Počet odkazů: {len(main_links)}")
    
    # Zpracování všech odkazů z hlavní stránky
    print("\nZpracovávám odkazy z hlavní stránky:")
    for i, link in enumerate(main_links, 1):
        print(f"\n{i}. Zpracovávám: {link}")
        title, links = get_page_info(link)
        if title:
            print(f"Titulek: {title}")
            print(f"Počet odkazů: {len(links)}")
        time.sleep(0.5)  # Krátká pauza mezi požadavky

if __name__ == "__main__":
    main()
