# NessusConverter


### Description
This is a simple python script that converts all .nessus files in a directory into a CSV file you can open in Excel. Since .nessus files can really only be displayed in Nessus, I wanted another, more feasible method of viewing Nessus data. And since I would much prefer to read nessus data formatted in a spreadsheet form, I wrote a script to convert the .nessus files' XML format into CSV.

### How to Use
It's easy. Simply drag the file to to a directory containing the .nessus files, open up a command prompt, and run `python3 nessus_to_csv.py` (or `python nessus_to_csv.py`). When you see the terminal return to a command prompt, you will now have a nessus_file.csv file in the temp directory.

### Coming soon
I wanted to get the core piece up here for now but other features are coming soon:
* Outputting files to other directories (i.e., not platform dependent)
* Want to include more "Report Items" in the .csv file
