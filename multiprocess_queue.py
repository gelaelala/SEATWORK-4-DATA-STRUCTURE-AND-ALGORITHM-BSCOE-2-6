import time
from hashlib import md5
from itertools import product
from string import ascii_lowercase

def reverse_md5(hash_value, alphabet=ascii_lowercase, max_length=6):
    for length in range(1, max_length + 1):
        for combination in product(alphabet, repeat=length):
            text_bytes = "".join(combination).encode("utf-8")
            hashed = md5(text_bytes).hexdigest()
            if hashed == hash_value:
                return text_bytes.decode("utf-8")

def main():
    t1 = time.perf_counter()
    text = reverse_md5("a9d1cbf71942327e98b40cf5ef38a960")
    print (f"{text} (found in {time.perf_counter() - t1:.1f}s)")

def chuck_indices(length, num_chucks):
    start = 0
    

if __name__ == "__main__":
    main()