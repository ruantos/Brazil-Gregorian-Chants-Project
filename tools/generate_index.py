import csv
import os
import re

def get_file_mapping(directory):
    """Creates a mapping from filename to filename for a given directory."""
    file_map = {}
    if not os.path.isdir(directory):
        return file_map
        
    for filename in os.listdir(directory):
        if filename.endswith('.gabc') or filename.endswith('.pdf'): # Only include gabc and pdf files
            file_map[filename] = filename
    return file_map

def sanitize_song_name(song_name):
    """Removes common suffixes and special characters for better matching."""
    song_name = re.sub(r'\(.*?\)', '', song_name) # Remove text in parentheses
    song_name = re.sub(r'[-_.,;]', '', song_name) # Remove common separators
    song_name = song_name.replace("'", "") # Remove single quotes
    return song_name.lower().strip()

def generate_html_list(songs, file_map, directory, title):
    """Generates an HTML list for the given songs and file map."""
    html_list = f"<h2>{title}</h2>\n<ul>\n"
    
    matched_files = []
    for song in songs:
        number = int(song['Numeracao'])
        song_name = song['Nome_da_Musica']
        
        found_filename = None
        
        if directory.startswith('laudate_dominum'): # For laudate_dominum files with number prefix
            prefix = f"{number}_"
            for filename in file_map:
                if filename.startswith(prefix):
                    found_filename = filename
                    break
        else: # For gregobase files without number prefix
            sanitized_csv_name = sanitize_song_name(song_name)
            best_match_score = -1
            
            for filename in file_map:
                sanitized_filename = sanitize_song_name(os.path.splitext(filename)[0])
                
                # Simple substring matching for now, can be improved with fuzzy matching
                if sanitized_csv_name in sanitized_filename:
                    # Calculate a score based on length difference, favoring shorter differences
                    score = len(sanitized_csv_name) / len(sanitized_filename)
                    if score > best_match_score:
                        best_match_score = score
                        found_filename = filename
        
        if found_filename:
            matched_files.append({
                'number': number,
                'name': song_name,
                'filename': found_filename
            })
            # Remove the matched file from the map to avoid duplicate matches
            if found_filename in file_map:
                del file_map[found_filename]
    
    # Sort matched files by number
    matched_files.sort(key=lambda x: int(x['number']))

    for item in matched_files:
        html_list += f'<li><a href="{directory}/{item["filename"]}" download="{item["filename"]}">{item["number"]}. {item["name"]}</a></li>\n'
    
    html_list += "</ul>\n"
    return html_list

def main():
    """Generates the index.html file."""
    # Read the CSV file
    try:
        with open('laudate_dominum/laudate_dominum_corrigido_final.csv', 'r', encoding='utf-8') as f:
            songs = list(csv.DictReader(f))
    except FileNotFoundError:
        print("Error: laudate_dominum/laudate_dominum_corrigido_final.csv not found.")
        return

    # Get file mappings
    gabc_laudate_map = get_file_mapping('laudate_dominum/gabc')
    pdf_laudate_map = get_file_mapping('laudate_dominum/pdf')
    gabc_gregobase_map = get_file_mapping('gregobase/gabc')


    # Generate HTML lists
    gabc_laudate_list = generate_html_list(songs, gabc_laudate_map, 'laudate_dominum/gabc', 'laudate dominum arquivos GABC')
    pdf_laudate_list = generate_html_list(songs, pdf_laudate_map, 'laudate_dominum/pdf', 'laudate dominum arquivos PDF')
    gabc_gregobase_list = generate_html_list(songs, gabc_gregobase_map, 'gregobase/gabc', 'gregobase arquivos GABC')

    html_content = f"""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>laudate dominum arquivos</title>
    <style>
        body {{
            font-family: sans-serif;
            background-color: white;
            color: black;
        }}
        ul {{
            list-style-type: none;
            padding: 0;
        }}
        li {{
            margin-bottom: 5px;
        }}
        a {{
            text-decoration: none;
            color: black;
        }}
        a:hover {{
            text-decoration: underline;
        }}
        h1, h2 {{
            margin-top: 20px;
        }}
    </style>
</head>
<body>

    <h1>laudate dominum arquivos</h1>
    <a id="downloadAll" href="gabc_files.zip">Baixar Todos os Arquivos GABC</a>

    {gabc_laudate_list}
    {pdf_laudate_list}
    {gabc_gregobase_list}

</body>
</html>
"""

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)

    print("index.html generated successfully.")

if __name__ == '__main__':
    main()