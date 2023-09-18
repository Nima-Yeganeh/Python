import shutil

file1_path = 'C:/Users/Nimay/nima_git/Python/Z/zsample.txt'
file2_path = 'C:/Users/Nimay/nima_git/Python/Z/done.txt'
output_file_path = 'C:/Users/Nimay/nima_git/Python/Z/output.txt'  # Create a new file to store lines not in file2

# Read lines from file2 and store them in a set for faster lookup
lines_file2 = set()
with open(file2_path, 'r') as file2:
    for line in file2:
        lines_file2.add(line.strip())

# Open both files for reading and the output file for writing
with open(file1_path, 'r') as file1, open(output_file_path, 'w') as output_file:
    for line in file1:
        if line.strip() not in lines_file2:
            # Print the line to the console (optional)
            print(line.strip())
            # Write the line to the output file
            output_file.write(line)
            # If needed, you can replace file2 with the contents of the output file
            break
shutil.move(output_file_path, file2_path)
