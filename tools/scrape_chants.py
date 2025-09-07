import urllib.request
import csv
import os
import re
import time
import concurrent.futures

def sanitize_filename(name):
    """Sanitizes a string to be used as a filename."""
    # Remove any inner html tags like <i>
    name = re.sub('<.*?>', '', name).strip()
    # Remove invalid characters for filenames
    name = re.sub(r'[\/*?:"<>|]',"", name)
    name = name.replace(" ", "_")
    return name

def process_id(i):
    """Processes a single ID, fetches data, and downloads files."""
    chant_url = f"https://gregobase.selapa.net/chant.php?id={i}"
    
    try:
        with urllib.request.urlopen(chant_url) as response:
            html = response.read().decode('utf-8', errors='ignore')
        
        title = ""
        version = ""

        # Primarily look for the title and version inside the <div id="info">
        info_div_match = re.search(r'<div id="info">(.*?)</div>', html, re.DOTALL)
        
        if info_div_match:
            info_html = info_div_match.group(1)
            
            # Find title in h3 within the info div
            title_match = re.search(r'<h3>(.*?)</h3>', info_html, re.DOTALL)
            if title_match:
                title = title_match.group(1).strip()

            # Find version in h4 within the info div
            version_match = re.search(r'<h4>Version</h4>\s*<ul>\s*<li>(.*?)</li>', info_html, re.DOTALL | re.IGNORECASE)
            if version_match:
                version = version_match.group(1).strip()
        
        # Fallback for pages that might use a different structure (like h1 for title)
        if not title:
            title_match = re.search(r'<h1>(.*?)</h1>', html, re.DOTALL)
            if title_match:
                title = title_match.group(1).strip()
            # also get version for h1 pages
            version_match = re.search(r'<h4>Version</h4>\s*<ul>\s*<li>(.*?)</li>', html, re.DOTALL | re.IGNORECASE)
            if version_match:
                version = version_match.group(1).strip()

        if not title:
            #print(f"Could not find title for id {i}")
            return None

        print(f"Found: ID={i}, Title='{re.sub('<.*?>', '', title).strip()}'")

        # Sanitize filename
        sanitized_title = sanitize_filename(title)
        sanitized_version = sanitize_filename(version)
        
        filename_base = f"{sanitized_title}-{sanitized_version}" if sanitized_version else sanitized_title

        # Download GABC
        gabc_url = f"https://gregobase.selapa.net/download.php?id={i}&format=gabc&elem=1"
        try:
            with urllib.request.urlopen(gabc_url) as gabc_response:
                gabc_content = gabc_response.read()
            if gabc_content:
                gabc_filename = os.path.join('gabc', f"{filename_base}.gabc")
                with open(gabc_filename, 'wb') as f:
                    f.write(gabc_content)
        except urllib.error.HTTPError as e:
            if e.code != 404:
                print(f"Could not download GABC for id {i}: {e}")

        # Download PDF
        pdf_url = f"https://gregobase.selapa.net/download.php?id={i}&format=pdf"
        try:
            with urllib.request.urlopen(pdf_url) as pdf_response:
                pdf_content = pdf_response.read()
            if pdf_content:
                pdf_filename = os.path.join('pdf', f"{filename_base}.pdf")
                with open(pdf_filename, 'wb') as f:
                    f.write(pdf_content)
        except urllib.error.HTTPError as e:
            if e.code != 404:
                print(f"Could not download PDF for id {i}: {e}")
        
        return {'id': i, 'titulo': re.sub('<.*?>', '', title).strip(), 'version': version}

    except urllib.error.HTTPError as e:
        if e.code != 404:
            print(f"Error fetching id {i}: {e}")
    except Exception as e:
        print(f"An error occurred for id {i}: {e}")
    
    return None

def main():
    # Create directories if they don't exist
    if not os.path.exists('gabc'):
        os.makedirs('gabc')
    if not os.path.exists('pdf'):
        os.makedirs('pdf')

    # Open CSV file for writing (this will clear the file)
    with open('chants.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['id', 'titulo', 'version']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
            # Submit all tasks
            future_to_id = {executor.submit(process_id, i): i for i in range(1, 20243)}
            
            # Process results as they complete
            for future in concurrent.futures.as_completed(future_to_id):
                result = future.result()
                if result:
                    writer.writerow(result)
                    csvfile.flush() # Write to disk immediately

if __name__ == "__main__":
    main()
