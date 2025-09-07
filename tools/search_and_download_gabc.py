import csv
import os
import shutil

def load_chants(filename='laudate_dominum/laudate_dominum_corrigido_final.csv'):
    """Loads the list of chants from the CSV file."""
    chants = []
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                chants.append(row)
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        return None
    return chants

def search_chants(chants, search_term):
    """Searches for chants by title."""
    search_term = search_term.lower()
    results = []
    for chant in chants:
        if search_term in chant['Nome_da_Musica'].lower():
            results.append(chant)
    return results

def find_gabc_file(chant):
    """Finds the GABC file for a given chant."""
    chant_number = chant['Numeracao']
    # We need to find the file that starts with the chant number
    # in the laudate_dominum/gabc directory.
    gabc_dir = 'laudate_dominum/gabc'
    if not os.path.isdir(gabc_dir):
        return None
        
    for filename in os.listdir(gabc_dir):
        if filename.startswith(f"{chant_number}_") and filename.endswith(".gabc"):
            return os.path.join(gabc_dir, filename)
    return None

def download_gabc_file(gabc_path):
    """Copies the GABC file to the downloads directory."""
    if not gabc_path or not os.path.exists(gabc_path):
        print("Error: GABC file not found.")
        return

    downloads_dir = 'downloads'
    if not os.path.exists(downloads_dir):
        os.makedirs(downloads_dir)

    try:
        shutil.copy(gabc_path, downloads_dir)
        print(f"File {os.path.basename(gabc_path)} downloaded to '{downloads_dir}' directory.")
    except Exception as e:
        print(f"Error downloading file: {e}")

def main():
    """Main function to run the search and download tool."""
    chants = load_chants()
    if chants is None:
        return

    print("--- Gregorian Chant GABC File Search and Download ---")
    while True:
        search_term = input("Enter a search term (or 'q' to quit): ")
        if search_term.lower() == 'q':
            break

        results = search_chants(chants, search_term)

        if not results:
            print("No chants found matching your search term.")
            continue

        print("\n--- Search Results ---")
        for i, chant in enumerate(results):
            print(f"{i + 1}: {chant['Nome_da_Musica']}")

        while True:
            try:
                choice = input("Enter the number of the chant to download (or 'b' to go back): ")
                if choice.lower() == 'b':
                    break
                
                choice_index = int(choice) - 1
                if 0 <= choice_index < len(results):
                    selected_chant = results[choice_index]
                    gabc_file = find_gabc_file(selected_chant)
                    if gabc_file:
                        download_gabc_file(gabc_file)
                    else:
                        print("Could not find the GABC file for the selected chant.")
                    break
                else:
                    print("Invalid number. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

if __name__ == '__main__':
    main()
