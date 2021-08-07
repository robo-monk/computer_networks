# parity bits => m
# total bits => n = 2^m -1
# data bits => k = 2^m - m -1


# 101, 0 => 1
# 101, 1 => 0
# 101, 2 => 1
def lsb(num, k=0):
    return bool(num & (1 << k))

def bit_len(num):
    return num.bit_length()

def bit_at(num, i, lsb=False):
    if lsb:
        return num >> i & 1 

    return bit_at(num, bit_len(num) - i - 1, True)

def hamming(data):

    parity_code = 0
    for i in range(bit_len(data)):
        if bit_at(data, i):
            parity_code ^= i

    ham_code = [0] * bit_len(data)

    for i in range(bit_len(data)):
        ham_code[i] = bit_at(data, i)

    print("before", ham_code)

    # construct hamming code
    for i in range(bit_len(parity_code)):
        ham_code.insert(2**i, bit_at(parity_code, i))

    print("after", ham_code)

    ham_code = int("".join(map(lambda x: str(x), ham_code)), 2)

    print(f"Hamming({bit_len(ham_code)}, {bit_len(data)}) of {format(data, 'b')} is {format(ham_code, 'b')}")
    return ham_code

# def hamming_check(data):


data = 0b101
print(hamming(data))

data = 0b1010
print(hamming(data))

data = 0b10101
print(hamming(data))

data = 0b101011111
print(hamming(data))

