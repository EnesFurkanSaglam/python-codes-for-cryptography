# This code takes a 4-bit binary number as input and uses an S-box to generate an output.

# S-box for substitution
S_box = [
    [0x6, 0xC, 0x9, 0x0],
    [0xF, 0x0, 0xA, 0x7],
    [0xA, 0x9, 0x1, 0xF],
    [0x3, 0xD, 0xB, 0x5]
]

# Get 4-bit binary input from the user
binary_input = input("Enter a 4-bit binary number (e.g., 1010): ")

# Validate the input
if len(binary_input) != 4 or not all(bit in '01' for bit in binary_input):
    print("Invalid input! Please enter a 4-bit binary number.")
else:
    # Calculate the row and column for the S-box
    row = int(binary_input[0] + binary_input[3], 2)  # Row is formed by the first and last bits
    column = int(binary_input[1:3], 2)                # Column is formed by the middle two bits
    
    # Get the output from the S-box
    output = S_box[row][column]

    # Print the results
    print(f"Input: {binary_input}")
    print(f"Row: {row}, Column: {column}")
    print(f"S-box output: {hex(output)}")
