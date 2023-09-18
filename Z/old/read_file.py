# Read the content of done.txt and store it in a set for efficient membership checking
with open("C:\\Users\\Nimay\\nima_git\\Python\\Z\\done.txt", "r") as file:
    existing_lines = set(file.read().splitlines())
# Open sample.txt for reading and done.txt for appending
with open("C:\\Users\\Nimay\\nima_git\\Python\\Z\\sample.txt", "r") as file1, open("C:\\Users\\Nimay\\nima_git\\Python\\Z\\done.txt", "a") as file2:
    # Read and process each line from sample.txt
    for line in file1:
        stripped_line = line.strip()  # Remove leading/trailing whitespace and newlines
        if stripped_line not in existing_lines:
            file2.write(stripped_line + "\n")  # Add the line to done.txt
            existing_lines.add(stripped_line)  # Update the set for efficient checking
            # print(f"Added to done.txt: {stripped_line}")
            inputtext=stripped_line
            print(inputtext)
