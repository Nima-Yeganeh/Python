# Input variable
variable = "this is a house"

# Split the input variable into words
words = variable.split()

# Create xvariable by repeating each word twice with a space in between
xvariable = " ".join([word + " " + word for word in words])

# Print the result
print(xvariable)
