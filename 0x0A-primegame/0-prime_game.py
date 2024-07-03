#!/usr/bin/python3
"""
Check if a number is prime.
"""


def isWinner(x, nums):
    """
    Determine the winner of the prime game after x rounds.
    """
    if x <= 0 or not nums:
        return None

    max_num = max(nums)

    # Sieve of Eratosthenes to find all primes up to max_num
    sieve = [True] * (max_num + 1)
    sieve[0], sieve[1] = False, False
    p = 2
    while (p * p <= max_num):
        if sieve[p]:
            for i in range(p * p, max_num + 1, p):
                sieve[i] = False
        p += 1
    primes = [p for p in range(max_num + 1) if sieve[p]]

    def play_game(n):
        """
        Simulate the game for a single round with upper limit n.
        """
        nums_set = set(range(1, n + 1))
        turn = 0  # Maria's turn if even, Ben's turn if odd

        while True:
            prime_found = False
            for prime in primes:
                if prime in nums_set:
                    prime_found = True
                    multiples = set(range(prime, n + 1, prime))
                    nums_set -= multiples
                    break
            if not prime_found:
                break
            turn += 1

        return "Maria" if turn % 2 == 1 else "Ben"

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_game(n)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
