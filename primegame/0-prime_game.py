#!/usr/bin/python3
"""Module for the prime game function."""

def isWinner(x, nums):
    """Determines the winner of the prime game."""
    if not nums or x < 1:
        return None

    max_num = max(nums)
    if max_num < 2:
        return "Ben"

    crible = [True] * (max_num + 1)
    crible[0] = False
    crible[1] = False

    for i in range(2, int(max_num**0.5) + 1):
        if crible[i]:
            for j in range(i * i, max_num + 1, i):
                crible[j] = False
            
    prime_count = [0] * (max_num + 1)
    count = 0
    for i in range(max_num + 1):
        if crible[i]:
            count += 1
        prime_count[i] = count

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_count[n] % 2 != 0:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
