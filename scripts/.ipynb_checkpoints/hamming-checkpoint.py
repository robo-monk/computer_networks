import random
import numpy as np
from functools import reduce
from rich import print
from random import randint

"""
if there's an error, does its position look like ..___1?
if there's an error, does its position look like ..__1_?
...
"""

def bit_count(bit_sequence):
    count = 0

    while bit_sequence:
        count += (bit_sequence & 1)
        bit_sequence >>= 1

    return count

def calc_parity_bits(msg):
    return reduce( lambda x, y: x ^ y, [ i for i, bit in enumerate(msg) if bit ] )

def prepare_block(msg):
    block = msg
    parity_bits = bin(calc_parity_bits(msg))[2:].zfill(int(len(msg)**.5))[::-1]
    for i, bit in enumerate(parity_bits):
        block[2**i] ^= int(bit)

    return block


def transmit_msg(msg, errors=1):
    msg = msg.copy()
    for _ in range(errors):
        r = randint(0, len(msg)-1)
        msg[r] = not msg[r]

    return msg


def generate_msg(size, ran=2):
    return np.random.randint(ran, size=size) 

def ham_distance(code) -> int:
    """
    Calculates the hamming distance of the given code, or returns -1 if it cannot be calculated.

    :param code: The code, consisting out of a list of codewords.
    :return: The hamming distance of the given code , or -1 if it cannot be calculated.
    """
    if len(code) <= 1: return -1

    ww = code[0]
    dist = min([ bit_count(w^ww) for i, w in enumerate(code[1:]) ])
    rest = ham_distance(code[1:])
    if rest != -1 and dist > rest: dist = rest

    return dist

msg = generate_msg(16)
print("message is", msg, "with random parity", calc_parity_bits(msg))

block = prepare_block(msg)
print("p block is", block, "with actual parity", calc_parity_bits(block))

print("transmitting msg...")
tblock = transmit_msg(block)
print(tblock)
print(np.array_equal(tblock, block))

parity_bits = calc_parity_bits(tblock)
print("correcting message at position", parity_bits)
tblock[parity_bits] = not tblock[parity_bits]
print(tblock)
print(np.array_equal(tblock, block))


# TODO implement extended hamming code

msg = [ 0b0000, 0b0011, 0b1100, 0b1111 ] # should be 2
msg = [ 0b00000000,
        0b00001111,
        0b11110000,
        0b11111111 ] # should be 4

print("testing ham distance code with", msg)
print("hamming distance is", ham_distance(msg))


