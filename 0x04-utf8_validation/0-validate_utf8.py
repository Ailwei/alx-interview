#!/usr/bin/python3
"""
Module for validUtf8 method
"""


def validUTF8(data):
    """
    Check if a given data set represents a valid UTF-8 encoding.
    """
    def get_num_bytes(byte):
        if byte & 0b10000000 == 0:
            return 1
        elif byte & 0b11100000 == 0b11000000:
            return 2
        elif byte & 0b11110000 == 0b11100000:
            return 3
        elif byte & 0b11111000 == 0b11110000:
            return 4
        return 0

    n = len(data)
    i = 0

    while i < n:
        num_bytes = get_num_bytes(data[i])
        if num_bytes == 0 or i + num_bytes > n:
            return False

        for j in range(1, num_bytes):
            if data[i + j] & 0b11000000 != 0b10000000:
                return False

        i += num_bytes

    return True
