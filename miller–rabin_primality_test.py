from random import randrange
from math import log


def miller_rabin(n, k=30): # Miller-Rabin primality test
    probably_prime = True
    not_prime = False

    # 0. Test for some small primes
    if n == 1 or n == 2 or n == 3:
        return probably_prime
    if n % 2 == 0:
        print("Even number!")
        return not_prime
    # 1. Given n, find s so that n−1 = (2^s)*q for some odd q.
    s = log(n-1, 2)
    if s.is_integer():
        q = 1
        s = int(s)
    else:
        s = 0
        res = float(n-1)
        while res % 2 == 0:
            res = res/2
            s += 1
        q = int(res)

    # print(f" n = {n}\n n-1 = {n_minus_one}\n q = {q}\n s = {s}\n (2^s)*q = {(2**s)*q}")

    for j in range(0, k):
        # 2. Pick a random a that is in {1, ..., n−1}
        a = randrange(1, n-1)

        # 3. if a^q = 1 then n passes
        x = pow(a, q, n)  # a^q mod n #print(f"({a}^{q}) mod {n} = {x}")
        if x == 1 or x == n-1:
            continue

        # 4. For i = 0 ,... ,s−1 see if a^((2^i)*q) = −1. If so, n passes
        for i in range(1, s):
            x = pow(x, 2, n)  # a^((2^i)*q) mod n #print(f"({a}^{2*i*q}) mod {n} = {x}")
            if x == n-1:
                break

        # 5. Otherwise n is composite.
        else:
            return not_prime
    return probably_prime


def main():
    n = int(input("> Enter the number to be tested: "))
    result = miller_rabin(n)
    if result:
        print(f"{n} is probably prime")
    else:
        print(f"{n} is composite")


if __name__ == "__main__":
    main()



