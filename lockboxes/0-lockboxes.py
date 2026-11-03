#!/usr/bin/python3
"""Lockboxes module."""


def canUnlockAll(boxes):
    """Determines if all boxes can be opened."""
    if not boxes:
        return True

    opened = [0]
    visited = set()

    while opened:
        box = opened.pop()

        if box in visited:
            continue

        visited.add(box)

        for key in boxes[box]:
            if key < len(boxes) and key not in visited:
                opened.append(key)

    return len(visited) == len(boxes)
