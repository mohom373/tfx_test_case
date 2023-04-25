import csv

input_file = 'penguin-data/full-set/data-full.csv'
output_file = 'penguin-data/incomplete-set/data-incomplete.csv'
column_index = 0  # Change this to the index of the column you want to check
string_to_match = 'Chinstrap'
max_count = 50  # Change this to the number of rows you want to remove

with open(input_file, 'r', newline='') as infile, open(output_file, 'w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # Write the header row
    header = next(reader)
    writer.writerow(header)

    count = 0
    for row in reader:
        if row[column_index] == string_to_match:
            count += 1
            if count > max_count:
                writer.writerow(row)
        else:
            writer.writerow(row)
