from math import sqrt, ceil


def up_to(seq, lim):
    for n in seq:
        if n < lim:
            yield n
        else:
            break


def get_primes():
    """Pretty good Sieve of Erotosthenes

    Skip the even nums, stop at sqrt(candidate)
    """
    yield 2
    candidate = 3
    found = []
    while True:
        lim = int(ceil(sqrt(candidate)))
        if all(candidate % prime != 0 for prime in up_to(found, lim)):
            yield candidate
            found.append(candidate)
        candidate += 2
