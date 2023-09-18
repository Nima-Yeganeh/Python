# Input and output file paths
input_file_path = 'C:\\Users\\Nimay\\nima_git\\Python\\Z\\zsample.txt'
output_file_path = 'C:\\Users\\Nimay\\nima_git\\Python\\Z\\zsample2.txt'

# Read lines from the input file and store unique lines in a set
unique_lines = set()

with open(input_file_path, 'r') as input_file:
    for line in input_file:
        unique_lines.add(line.strip())

# Write the unique lines to the output file
with open(output_file_path, 'w') as output_file:
    for line in unique_lines:
        output_file.write(line + '\n')

print("Unique lines have been saved.")
