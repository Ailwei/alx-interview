#!/usr/bin/python3

"""Minimum Operations"""


def minOperations(target_count):
    """
    Calculates the fewest number of operations needed to result in exactly
    'target_count' number of 'H' characters in a text file, given only
    """
    if not isinstance(target_count, int):
        return 0

    operations = 0
    iterator = 2
    while iterator <= target_count:
        if target_count % iterator == 0:
            target_count //= iterator
            operations += iterator
            iterator = 1
        iterator += 1
    return operations
