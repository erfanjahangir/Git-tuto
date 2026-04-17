import csv

input_file = "dossier/MFallDa.csv"
output_file = "figure.csv"

# Read first 2 lines
with open(input_file, newline='', encoding='utf-8') as infile:
    reader = csv.reader(infile)
    
    first_two_rows = []
    
    for i, row in enumerate(reader):
        if i < 2:
            print(row)  # echo to terminal
            first_two_rows.append(row)
        else:
            break

# Write them to a new file
with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
    writer = csv.writer(outfile)
    writer.writerows(first_two_rows)
