#!/usr/bin/ python3
"""Validate UTF-8 encoding."""


def validUTF8(data):
    """Determine if data is a valid UTF-8 encoding."""

    remaining = 0

    for d in data:
        byte = d & 0xFF

        if remaining == 0:
            if byte >> 7 == 0b0:
                continue
            elif byte >> 5 == 0b110:
                remaining = 1
            elif byte >> 4 == 0b1110:
                remaining = 2
            elif byte >> 3 == 0b11110:
                remaining = 3
            else:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
            remaining -= 1

    return remaining == 0