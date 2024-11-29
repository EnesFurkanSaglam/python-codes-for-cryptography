import random

# This code generates round keys for DES (Data Encryption Standard) using a 64-bit master key.

# 56 bits
PC_1 = [
    57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 
    10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36,
    28, 20, 12, 4, 61, 53, 45, 37, 29, 21, 13, 5, 62, 54, 
    46, 38, 30, 22, 14, 6, 63, 55, 47, 39, 31, 23, 15, 7
]

# 48 bits
PC_2 = [
    14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4,
    26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47, 55, 30, 40,
    51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32
]

# Shifting table for left shifts
shifting_table = [1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 1, 2, 1, 2, 1, 2]

round_keys = []

def generate_64_bit_master_key():
    """Generates a random 64-bit master key."""
    key = [random.randint(0, 1) for _ in range(64)]
    return key

def apply_permutation(key, permutation_table):
    """Applies a permutation to the key using the provided permutation table."""
    return [key[i - 1] for i in permutation_table]

def shift_left(bits, n):
    """Shifts the bits to the left by n positions."""
    return bits[n:] + bits[:n]

def print_keys(round_keys):
    """Prints the generated round keys."""
    for i, key in enumerate(round_keys):
        print(f"Round {i + 1} Key: {' '.join(map(str, key))}")

# Generate master key and apply initial permutation
master_key = generate_64_bit_master_key()
key_after_pc1 = apply_permutation(master_key, PC_1)

# Split the key into two halves
C = key_after_pc1[:28]
D = key_after_pc1[28:]

# Generate round keys
for i in range(16):
    C = shift_left(C, shifting_table[i])  # Shift C left
    D = shift_left(D, shifting_table[i])  # Shift D left

    combined_key = C + D                    # Combine C and D
    round_key = apply_permutation(combined_key, PC_2)  # Apply PC-2 permutation

    round_keys.append(round_key)

# Print the generated round keys
print_keys(round_keys)
