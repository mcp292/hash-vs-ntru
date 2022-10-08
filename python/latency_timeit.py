# Single latency: 970255 nano seconds
# Average latency: 740616 nano seconds

import hashlib
from timeit import timeit
import secrets


def sha256(input_bytes):
    """
    Takes input bytes and returns a sha256 digest.
    """
    sha = hashlib.sha256()
    sha.update(input_bytes)
    digest = sha.digest()

    return digest


def sha3_256(input_bytes):
    """
    Takes input bytes and returns a sha3_256 (fips 202) digest.
    """
    sha = hashlib.sha3_256()
    sha.update(input_bytes)
    digest = sha.digest()

    return digest


def hash_repeatedly(input_bytes, num_hashes):
    for hashes in range(num_hashes):
        # input_bytes = sha256(input_bytes)
        input_bytes = sha3_256(input_bytes)


def convert_to_nanoseconds(latency_seconds):
    return int(latency_seconds * 1e9)


NUM_HASHES = 1000
NUM_TIMES = 1000
NUM_BITS = 256
NUM_BYTES = NUM_BITS // 8

input_bytes = secrets.token_bytes(NUM_BYTES)

latency = timeit(
    lambda: hash_repeatedly(input_bytes, NUM_HASHES), number=1)

single_latency = convert_to_nanoseconds(latency)

latency = timeit(
    lambda: hash_repeatedly(input_bytes, NUM_HASHES), number=NUM_TIMES)

avg_latency = convert_to_nanoseconds(latency) // NUM_TIMES

print(f"Single latency: {single_latency} nano seconds")
print(f"Average latency: {avg_latency} nano seconds")
