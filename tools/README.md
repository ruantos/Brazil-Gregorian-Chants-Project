# Gregorian Chant GABC File Search and Download

This script allows you to search for Gregorian chants and download their corresponding GABC files.

## Usage

1.  Make sure you have the required `laudate_dominum` directory with the `laudate_dominum_corrigido_final.csv` file and the `gabc` subdirectory containing the GABC files.
2.  Run the script from the root directory of the project:

    ```bash
    python tools/search_and_download_gabc.py
    ```

3.  The script will prompt you to enter a search term.
4.  The script will display a list of matching chants.
5.  Enter the number of the chant you want to download.
6.  The GABC file will be copied to the `downloads` directory.

## Dependencies

This script requires Python 3 and has no external dependencies.
