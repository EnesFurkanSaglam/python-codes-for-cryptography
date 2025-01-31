T = [(i & 0xFFFFFFFF) for i in range(1, 65)]

A = 0x01234567
B = 0x89ABCDEF
C = 0xFEDCBA98
D = 0x76543210

def leftCircularShift(bits, shiftAmount):
    return ((bits << shiftAmount) | (bits >> (32 - shiftAmount))) & 0xFFFFFFFF

def carrylessAddition(a, b):
    while b != 0:
        summation = (a ^ b) & 0xFFFFFFFF
        carry = ((a & b) << 1) & 0xFFFFFFFF
        a = summation
        b = carry
    return a

def fFunc(b, c, d):
    return (c & b) | (~b & d)

def gFunc(b, c, d):
    return (b & d) | (c & ~d)

def hFunc(b, c, d):
    return b ^ c ^ d

def iFunc(b, c, d):
    return c ^ (b | ~d)

def messageToBit(message):
    return ''.join(format(ord(char), '08b') for char in message)

def bitSlice(bits, sliceSize):
    padding_length = (sliceSize - (len(bits) % sliceSize)) % sliceSize
    bits += '0' * padding_length
    return [bits[i:i + sliceSize] for i in range(0, len(bits), sliceSize)]

def split512bitData(data):
    return [int(data[i:i+32], 2) for i in range(0, 512, 32)]


messageToHash = "selamss"

bitStringOfMessage = messageToBit(messageToHash)

splittedBitBlocks = bitSlice(bitStringOfMessage, 512)

for i in range(len(splittedBitBlocks)):
    block32 = split512bitData(splittedBitBlocks[i])

    a, b, c, d = A, B, C, D

    for j in range(16):
        result1 = fFunc(b, c, d)
        result2 = carrylessAddition(a, result1)
        result3 = carrylessAddition(block32[j], result2)
        result4 = carrylessAddition(result3, T[j])

        if j % 4 == 0:
            result5 = leftCircularShift(result4, 7)
        elif j % 4 == 1:
            result5 = leftCircularShift(result4, 12)
        elif j % 4 == 2:
            result5 = leftCircularShift(result4, 17)
        else:  # j % 4 == 3
            result5 = leftCircularShift(result4, 22)

        result6 = carrylessAddition(result5, b)
        a, b, c, d = d, result6, b, c

    
    for j in range(16):
        result1 = gFunc(b, c, d)
        result2 = carrylessAddition(a, result1)
        result3 = carrylessAddition(block32[j], result2)
        result4 = carrylessAddition(result3, T[j + 16])

        if j % 4 == 0:
            result5 = leftCircularShift(result4, 5)
        elif j % 4 == 1:
            result5 = leftCircularShift(result4, 9)
        elif j % 4 == 2:
            result5 = leftCircularShift(result4, 14)
        else:  # j % 4 == 3
            result5 = leftCircularShift(result4, 20)

        result6 = carrylessAddition(result5, b)
        a, b, c, d = d, result6, b, c

    
    for j in range(16):
        result1 = hFunc(b, c, d)
        result2 = carrylessAddition(a, result1)
        result3 = carrylessAddition(block32[j], result2)
        result4 = carrylessAddition(result3, T[j + 32])

        if j % 4 == 0:
            result5 = leftCircularShift(result4, 4)
        elif j % 4 == 1:
            result5 = leftCircularShift(result4, 11)
        elif j % 4 == 2:
            result5 = leftCircularShift(result4, 16)
        else:  # j % 4 == 3
            result5 = leftCircularShift(result4, 23)

        result6 = carrylessAddition(result5, b)
        a, b, c, d = d, result6, b, c

    
    for j in range(16):
        result1 = iFunc(b, c, d)
        result2 = carrylessAddition(a, result1)
        result3 = carrylessAddition(block32[j], result2)
        result4 = carrylessAddition(result3, T[j + 48])

        if j % 4 == 0:
            result5 = leftCircularShift(result4, 6)
        elif j % 4 == 1:
            result5 = leftCircularShift(result4, 10)
        elif j % 4 == 2:
            result5 = leftCircularShift(result4, 15)
        else:  # j % 4 == 3
            result5 = leftCircularShift(result4, 21)

        result6 = carrylessAddition(result5, b)
        a, b, c, d = d, result6, b, c

    A = carrylessAddition(A, a)
    B = carrylessAddition(B, b)
    C = carrylessAddition(C, c)
    D = carrylessAddition(D, d)


hash_result = ''.join(format(x & 0xFFFFFFFF, '08x') for x in [A, B, C, D])
print(f"Hash Result: {hash_result}")
