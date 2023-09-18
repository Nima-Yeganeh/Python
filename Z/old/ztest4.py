# Define the filenames for file1 and file2
file1_name = 'C:/Users/Nimay/nima_git/Python/Z/file1.txt'
file2_name = 'C:/Users/Nimay/nima_git/Python/Z/file2.txt'
# Read the contents of file2 into a set for efficient membership checking
with open(file2_name, 'r') as file2:
    lines_in_file2 = set(file2.read().splitlines())
# Open file1 in read mode
with open(file1_name, 'r') as file1:
    # Create a list to store lines that are not in file2
    lines_to_add = []
    # Check each line in file1
    for line in file1:
        lines_to_add = []
        if line.strip() not in lines_in_file2:
            # If the line is not in file2, add it to the list
            lines_to_add.append(line)
            # Open file2 in append mode and write the lines that are not in file2
            with open(file2_name, 'a') as file2:
                file2.writelines(lines_to_add)
            # Print the lines that were added to file2
            for line in lines_to_add:
                print(line.strip())
            print("Process completed.")
