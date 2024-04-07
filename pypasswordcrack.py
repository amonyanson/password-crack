# Import the 'product' function from the 'itertools' module
# The 'product' function generates all possible combinations of a set of values
from itertools import product

# Set the input file name
# This is the file that contains the list of words to use for generating combinations
input_file = 'top_10_passwords.txt'

# Set the output file name
# This is the file where the generated combinations will be saved
output_file = 'bc_final_pwlist.txt'

# Try to open the input file in read mode
# This will allow us to read the contents of the file into a list
try:
    # Open the input file
    with open(input_file,'r') as f:
        # Loop through each line in the file
        for line in f.readlines():
            # Remove any whitespace from the beginning or end of the line
            # This will ensure that the words are stored in their purest form
            word = line.strip()

            # Add the word to the list
            words.append(word)

        # Convert all the words to uppercase
        # This will ensure that we generate combinations of both the original and uppercase words
        words += [word.upper() for word in words]

    # Try to open the output file in write mode
    # This will allow us to write the generated combinations to the file
    with open(output_files,'w') as f:
        # Use the 'product' function to generate all possible combinations of two words
        # The 'repeat' argument specifies how many times each word should be repeated
        # In this case, we want to generate combinations of two words, so we set 'repeat' to 2
        for combo in product(words,repeat=2):
            # Join the two words in the combination into a single string
            # Add a newline character to the end of the string
            # Write the string to the output file
            f.write(''.join(combo) + '\n')

# If an exception is raised, print an error message
# This will help us debug any issues that might arise during execution
except Exception as e:
    print("Something went wrong")
    print(f"Here is what went wrong: ({e})")