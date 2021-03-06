import os
import random as pyrandom


random = pyrandom.SystemRandom()


def random_number(bits=None, below=None, between=None):
    """Generates a random_number using one of the params.

    random_number(bits=24): number with 24 bits
    random_number(below=1000): number [0, 1000)
    random_number(between=[2,100]): number [2, 100]
    """
    assert (bits is not None) ^ (below is not None) ^ (between is not None)
    if bits is not None:
        return random.getrandbits(bits)
    elif below is not None:
        return random.randrange(below)
    elif between is not None:
        min_, max_ = between
        return random.randrange(min_, max_ + 1)
    assert False


def random_bytes(n):
    return os.urandom(n)
