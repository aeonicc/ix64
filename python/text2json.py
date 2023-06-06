# Open the file in read-only mode
with open("ix.txt", "r") as f:
    # Read the contents of the file into a variable as a string
    text = f.read()

# Print the text
print(text)