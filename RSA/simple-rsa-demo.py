import random
from sympy import isprime, mod_inverse

def get_random_prime_candidate(bit_length):
    # Generate a random number of the given bit length
    candidate = random.getrandbits(bit_length)
    
    # Make sure highest bit is set and it's odd
    candidate |= (1 << (bit_length - 1))
    candidate |= 1
    return candidate

def get_prime(bit_length):
    # Keep trying until we find a prime
    p = get_random_prime_candidate(bit_length)
    while not isprime(p):
        # Just add 2 each time to get another odd candidate
        p += 2
    return p

def my_gcd(a, b):
    # A simple GCD function
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a

def make_keys(bits):
    # Generate two primes
    p = get_prime(bits)
    q = get_prime(bits)
    
    # Calculate n and phi
    n = p * q
    phi = (p - 1) * (q - 1)

    # Commonly used public exponent
    e = 65537

    # Very basic check if e is okay
    if my_gcd(e, phi) != 1:
        raise ValueError("e and phi(n) are not coprime.")
    
    # Compute private exponent
    d = mod_inverse(e, phi)
    
    # Return public and private keys
    return (n, e), (n, d)

def basic_encrypt(pub_key, plaintext):
    # Encrypt character by character
    n, e = pub_key
    encrypted_vals = []
    for ch in plaintext:
        c = pow(ord(ch), e, n)
        encrypted_vals.append(c)
    return encrypted_vals

def basic_decrypt(priv_key, ciphertext):
    # Decrypt character by character
    n, d = priv_key
    result = ""
    for val in ciphertext:
        m = pow(val, d, n)
        result += chr(m)
    return result

# Using small 8-bit primes (NOT SECURE, just for demonstration)
pub, priv = make_keys(8)

msg = "HELLO"
cipher = basic_encrypt(pub, msg)
print("Ciphertext:", cipher)

plain = basic_decrypt(priv, cipher)
print("Decrypted text:", plain)
