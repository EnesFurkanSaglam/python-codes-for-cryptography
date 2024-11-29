# This code takes an 8-bit binary number as input and uses an S-box to generate an output.

# S-box for substitution
S_box = [
    [0x6, 0xC, 0x9, 0x0, 0x3, 0x8, 0xD, 0xA, 0x2, 0x4, 0xB, 0x1, 0x7, 0xE, 0x5, 0xF],
    [0xF, 0x0, 0xA, 0x7, 0x4, 0x8, 0xE, 0xD, 0x1, 0x9, 0x6, 0x3, 0xC, 0xB, 0x5, 0x2],
    [0xA, 0x9, 0x1, 0xF, 0x7, 0x5, 0x3, 0xC, 0x0, 0xB, 0xE, 0x6, 0x4, 0xD, 0x2, 0x8],
    [0x3, 0xD, 0xB, 0x5, 0x9, 0x0, 0xA, 0x6, 0xF, 0x8, 0x4, 0xE, 0x7, 0x1, 0x2, 0xC],
    [0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7, 0x8, 0x9, 0xA, 0xB, 0xC, 0xD, 0xE, 0xF, 0x0],
    [0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7, 0x8, 0x9, 0xA, 0xB, 0xC, 0xD, 0xE, 0xF],
    [0xF, 0xE, 0xD, 0xC, 0xB, 0xA, 0x9, 0x8, 0x7, 0x6, 0x5, 0x4, 0x3, 0x2, 0x1, 0x0],
    [0x2, 0x3, 0x4, 0x5, 0x6, 0x7, 0x8, 0x9, 0xA, 0xB, 0xC, 0xD, 0xE, 0xF, 0x0, 0x1],
    [0x8, 0x9, 0xA, 0xB, 0xC, 0xD, 0xE, 0xF, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7],
    [0x7, 0x6, 0x5, 0x4, 0x3, 0x2, 0x1, 0x0, 0xF, 0xE, 0xD, 0xC, 0xB, 0xA, 0x9, 0x8],
    [0x4, 0x3, 0x2, 0x1, 0x0, 0xF, 0xE, 0xD, 0xC, 0xB, 0xA, 0x9, 0x8, 0x7, 0x6, 0x5],
    [0xD, 0xC, 0xB, 0xA, 0x9, 0x8, 0x7, 0x6, 0x5, 0x4, 0x3, 0x2, 0x1, 0x0, 0xF, 0xE],
    [0x5, 0x6, 0x7, 0x8, 0x9, 0xA, 0xB, 0xC, 0xD, 0xE, 0xF, 0x0, 0x1, 0x2, 0x3, 0x4],
    [0xA, 0xB, 0xC, 0xD, 0xE, 0xF, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7, 0x8, 0x9],
    [0x9, 0x8, 0x7, 0x6, 0x5, 0x4, 0x3, 0x2, 0x1, 0x0, 0xF, 0xE, 0xD, 0xC, 0xB, 0xA],
    [0x9, 0x8, 0x7, 0x6, 0x5, 0x4, 0x3, 0x2, 0x1, 0x0, 0xF, 0xE, 0xD, 0xC, 0xB, 0xA]
]

# Get 8-bit binary input from the user
binary_input = input("Enter an 8-bit binary number (e.g., 10101010): ")

# Validate the input
if len(binary_input) != 8 or not all(bit in '01' for bit in binary_input):
    print("Invalid input! Please enter an 8-bit binary number.")
else:
    # Calculate the row and column for the S-box
    row = int(binary_input[0:4], 2)  # Row is formed by the first four bits
    column = int(binary_input[4:], 2)  # Column is formed by the last four bits

    # Get the output from the S-box
    output = S_box[row][column]

    # Print the results
    print(f"Input: {binary_input}")
    print(f"Row: {row}, Column: {column}")
    print(f"S-box output: {hex(output)}")
