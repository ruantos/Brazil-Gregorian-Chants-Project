
import os
from bs4 import BeautifulSoup

def find_pdf_path(soup, title):
    for link in soup.find_all('a'):
        if link.text == title and 'pdf' in link.get('href'):
            return link.get('href')
    return None

def main():
    index_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'index.html'))
    print(f"Reading index.html from: {index_path}")

    with open(index_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')

    gabc_links = []
    for link in soup.find_all('a'):
        if 'gabc' in link.get('href'):
            gabc_links.append(link)
    
    print(f"Found {len(gabc_links)} gabc links to process.")

    for link in gabc_links:
        title = link.text
        gabc_path = link.get('href')
        pdf_path = find_pdf_path(soup, title)

        if pdf_path:
            print(f"Updating link for: {title}")
            link['href'] = '#'
            link['onclick'] = f"openModal('{title}', '{gabc_path}', '{pdf_path}')"

    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(str(soup))
    
    print("Finished updating index.html")

if __name__ == '__main__':
    main()
