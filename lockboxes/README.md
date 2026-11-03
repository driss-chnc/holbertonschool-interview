# Lockboxes

## Description

This project is part of the Holberton School curriculum.

The goal is to determine whether all the boxes in a list of boxes can be opened.

Each box is numbered sequentially from `0` to `n - 1`. Each box may contain keys that can unlock other boxes.

The first box, `boxes[0]`, is unlocked by default.

## Requirements

- All files must be interpreted/compiled on Ubuntu 20.04 LTS using Python 3.
- All files must end with a new line.
- The first line of all files must be exactly `#!/usr/bin/python3`.
- The code must follow the PEP 8 style.
- All files must be executable.
- All modules and functions must have documentation.

## Function Prototype

```python
def canUnlockAll(boxes):
```

## Function Description

The `canUnlockAll` function determines whether all boxes can be opened.

### Parameters

- `boxes`: A list of lists containing the keys available in each box.

### Return

- `True` if all boxes can be opened.
- `False` otherwise.

## Algorithm

1. Start with box `0`, which is already unlocked.
2. Maintain a list of boxes that can be explored.
3. Maintain a set of boxes that have already been visited.
4. For each unlocked box, retrieve its keys.
5. Add valid, unvisited boxes to the list of boxes to explore.
6. Continue until there are no more boxes to explore.
7. Return `True` if every box has been visited, otherwise return `False`.

## Example

```python
boxes = [[1], [2], [3], [4], []]

print(canUnlockAll(boxes))
```

Output:

```text
True
```

### Example 2

```python
boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]

print(canUnlockAll(boxes))
```

Output:

```text
True
```

### Example 3

```python
boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]

print(canUnlockAll(boxes))
```

Output:

```text
False
```

## Complexity

Let `n` be the number of boxes and `k` the total number of keys.

- **Time Complexity:** O(n + k)
- **Space Complexity:** O(n)

Each box is visited at most once, and each key is examined at most once.

## Author

Holberton School Student