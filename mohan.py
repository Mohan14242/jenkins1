def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    for p in range(2, int(n**0.5) + 1):
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False

    prime_numbers = [p for p, is_prime in enumerate(primes) if is_prime]
    return prime_numbers

n = 100
prime_list = sieve_of_eratosthenes(n)
print(f"Prime numbers less than or equal to {n}:")
print(prime_list)
