import csv

# Input and output file paths
input_txt_file = "spellings.txt"
output_csv_file = "spellings.csv"

# Read the input .txt file and write to .csv
with open(input_txt_file, "r") as txt_file, open(output_csv_file, "w", newline="") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["Correct", "Misspellings"])  # Write header

    for line in txt_file:
        if ":" in line:
            correct, misspellings = line.strip().split(":", 1)
            csv_writer.writerow([correct.strip(), misspellings.strip()])