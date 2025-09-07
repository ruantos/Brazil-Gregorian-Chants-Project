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

def sanitize_name_for_matching(name):
    """
    Sanitizes a name (song name or filename) for matching purposes.
    Removes common suffixes, special characters, and converts to lowercase.
    """
    # Remove text in parentheses
    name = re.sub(r'\(.*\)', '', name)
    # Remove common source suffixes and other common non-alphanumeric characters
    name = re.sub(r'-(Dominican|Solesmes_\d{4}|Solesmes|Vatican|Sandhofe|Verona|Cistercian|Annamitice|Palmer_&_Burgess|Gregofacsimil|Hartker|Simplex|Novum|Triplex|Nivers|OSB|Portugal|Still_River|Tridentine|Finlandiae|Carmelitan|MEP|Polish|Sarum|Still_River|Toletano|Jouques|Le\u00f3n|Milano|Rouen|Stingl|Utrecht|Vallicellana|Benedictine|Chmerice|Fontevraud|Graduale_Aboense|Graduale_Romano-Seraphicum|Gregorio|Heiligenkreuz|Hildegard|Liturgia_Horarum|Mechliniae|Missale_Romanum|Missale_Romanum_2002|Mozarabic|Nabc|Original_composition,_never_printed|Puellae_Charitatis|Quebecensis|Rossini|Sagiense|San_Jose|Supplementum_Liber_Usualis|Traditional|Trinitarian|Ward_Method|Weller|BzG-Ei121|BzG-L239|I-Rss_XIV_L1|I-Rss_XIV_L1,_Humbert_Codex|I-Rss_XIV_L1,)-?', '', name, flags=re.IGNORECASE)
    name = re.sub(r'[-_.,;]', ' ', name) # Replace remaining separators with spaces
    name = re.sub(r'\u2591\u2591(\d+)\u2591\u2591', '\1', name) # Remove special number patterns like ░░17941░░ and keep the number
    name = name.replace("'", "") # Remove single quotes
    name = name.lower().strip()
    return name

def generate_html_list(songs, file_map, directory, title):
    """Generates an HTML list for the given songs and file map."""
    title_id = title.lower().replace(' ', '-')
    html_list = f'<h2 id="{title_id}">{title}</h2>\n<ul>\n'
    
    matched_files = []
    
    # Create a temporary copy of file_map to remove matched files
    temp_file_map = dict(file_map)

    if directory.startswith('laudate_dominum'): # For laudate_dominum files with number prefix
        for song in songs:
            number = int(song['Numeracao'])
            song_name = song['Nome_da_Musica']
            prefix = f"{number}_"
            found_filename = None
            for filename in temp_file_map:
                if filename.startswith(prefix):
                    found_filename = filename
                    break
            
            if found_filename:
                filepath = os.path.join(directory, found_filename)
                if os.path.exists(filepath):
                    matched_files.append({
                        'number': number,
                        'name': song_name,
                        'filename': found_filename
                    })
                    del temp_file_map[found_filename]
    else: # For gregobase files, try to match by song name, otherwise list all
        for song in songs:
            number = int(song['Numeracao'])
            song_name = song['Nome_da_Musica']
            sanitized_csv_name = sanitize_name_for_matching(song_name)
            
            found_filename = None
            best_match_score = -1
            
            for filename in temp_file_map:
                sanitized_filename = sanitize_name_for_matching(os.path.splitext(filename)[0])
                
                if sanitized_csv_name == sanitized_filename: # Exact match after sanitization
                    found_filename = filename
                    break
                
                if not found_filename: # Only try broader match if exact match not found
                    # Try matching the first few words of the song name
                    words = sanitized_csv_name.split()
                    if len(words) > 1:
                        search_phrase = " ".join(words[:2]) # Use first two words
                        if search_phrase in sanitized_filename:
                            found_filename = filename
                            break
                    elif len(words) == 1: # If only one word, just use that
                        search_phrase = words[0]
                        if search_phrase in sanitized_filename:
                            found_filename = filename
                            break
        
        if found_filename:
            # Check if the file actually exists before adding to the list
            filepath = os.path.join(directory, found_filename)
            if os.path.exists(filepath):
                matched_files.append({
                    'number': number,
                    'name': song_name,
                    'filename': found_filename
                })
                # Remove the matched file from the temporary map to avoid duplicate matches
                if found_filename in temp_file_map:
                    del temp_file_map[found_filename]
        
        # Add any remaining files from gregobase that were not matched by song name
        for filename in sorted(temp_file_map.keys()):
            # Try to extract a number from the filename if it follows the ░░number░░ pattern
            match = re.match(r'\u2591\u2591(\d+)\u2591\u2591', filename)
            display_name = os.path.splitext(filename)[0] # Default to filename without extension
            item_number = None
            if match:
                item_number = int(match.group(1))
                display_name = f"{item_number}. {os.path.splitext(filename)[0]}" # Fallback if no CSV match
            
            matched_files.append({
                'number': item_number,
                'name': display_name,
                'filename': filename
            })

    # Sort matched files by number if available, otherwise by name
    matched_files.sort(key=lambda x: (x['number'] is None, x['number'] if x['number'] is not None else 0, x['name']))

    for item in matched_files:
        html_list += f'<li><a href="{directory}/{item["filename"]}" download="{item["filename"]}">{item["name"]}</a></li>\n'
    
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
    gabc_laudate_title = 'laudate dominum arquivos GABC'
    pdf_laudate_title = 'laudate dominum arquivos PDF'
    gabc_gregobase_title = 'gregobase arquivos GABC'

    gabc_laudate_list = generate_html_list(songs, gabc_laudate_map, 'laudate_dominum/gabc', gabc_laudate_title)
    pdf_laudate_list = generate_html_list(songs, pdf_laudate_map, 'laudate_dominum/pdf', pdf_laudate_title)
    gabc_gregobase_list = generate_html_list(songs, gabc_gregobase_map, 'gregobase/gabc', gabc_gregobase_title)

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
            margin: 0;
            padding: 0;
        }}
        .menubar {{
            background-color: #f2f2f2;
            padding: 10px;
            border-bottom: 1px solid #ddd;
            display: flex;
            justify-content: space-around;
        }}
        .menubar a {{
            text-decoration: none;
            color: black;
            padding: 10px 15px;
        }}
        .menubar a:hover {{
            background-color: #ddd;
        }}
        #searchInput {{
            width: 98%;
            padding: 10px;
            margin: 10px;
            border: 1px solid #ddd;
        }}
        ul {{
            list-style-type: none;
            padding: 0;
        }}
        li {{
            margin-bottom: 5px;
            padding-left: 10px;
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
            padding-left: 10px;
        }}
    </style>
</head>
<body>

    <div class="menubar">
        <a href="#{gabc_laudate_title.lower().replace(' ', '-')}">Laudate Dominum GABC</a>
        <a href="#{pdf_laudate_title.lower().replace(' ', '-')}">Laudate Dominum PDF</a>
        <a href="#{gabc_gregobase_title.lower().replace(' ', '-')}">Gregobase GABC</a>
    </div>

    <h1>laudate dominum arquivos</h1>
    <a id="downloadAll" href="gabc_files.zip">Baixar Todos os Arquivos GABC</a>
    
    <input type="text" id="searchInput" onkeyup="searchFunction()" placeholder="Pesquisar por nome...">

    {gabc_laudate_list}
    {pdf_laudate_list}
    {gabc_gregobase_list}

    <script>
    function searchFunction() {{
        var input, filter, uls, li, a, i, txtValue;
        input = document.getElementById('searchInput');
        filter = input.value.toUpperCase();
        uls = document.getElementsByTagName('ul');
        for (j = 0; j < uls.length; j++) {{
            ul = uls[j];
            li = ul.getElementsByTagName('li');
            for (i = 0; i < li.length; i++) {{
                a = li[i].getElementsByTagName("a")[0];
                txtValue = a.textContent || a.innerText;
                if (txtValue.toUpperCase().indexOf(filter) > -1) {{
                    li[i].style.display = "";
                }} else {{
                    li[i].style.display = "none";
                }}
            }}
        }}
    }}
    </script>

</body>
</html>
"""

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)

    print("index.html generated successfully.")

if __name__ == '__main__':
    main()