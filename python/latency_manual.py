# Single latency: 925236 nano seconds
# Average latency: 746765 nano seconds

import hashlib
import time
import secrets


def sha256(input_bytes):
    """
    Takes input bytes and returns a sha256 (fips 180-2) digest.
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


def hash_repeatedly_repeatedly(input_bytes, num_hashes, num_times):
    for times in range(num_times):
        hash_repeatedly(input_bytes, num_hashes)


NUM_HASHES = 1000
NUM_TIMES = 1000
NUM_BITS = 256
NUM_BYTES = NUM_BITS // 8

input_bytes = secrets.token_bytes(NUM_BYTES)

start = time.perf_counter_ns()
hash_repeatedly(input_bytes, NUM_HASHES)
stop = time.perf_counter_ns()

single_latency = stop - start

start = time.perf_counter_ns()
hash_repeatedly_repeatedly(input_bytes, NUM_HASHES, NUM_TIMES)
stop = time.perf_counter_ns()

avg_latency = (stop - start) // NUM_TIMES

print(f"Single latency: {single_latency} nano seconds")
print(f"Average latency: {avg_latency} nano seconds")
