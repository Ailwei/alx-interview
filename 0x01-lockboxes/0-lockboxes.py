#!/usr/bin/python3

from collections import deque
"""
A python module that stermines if all boxes can can be opened from a list of lists
"""

def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
    - boxes (list of list of int): A list of boxes, where each box is represented by a list of integers
                                   indicating the keys it contains.

    Returns:
    - bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes:
        return False

    n = len(boxes)
    visited = [False] * n
    visited[0] = True
    queue = deque([0])

    while queue:
        box = queue.popleft()
        for key in boxes[box]:
            if 0 <= key < n and not visited[key]:
                visited[key] = True
                queue.append(key)

    return all(visited)

if __name__ == '__main__':
    boxes = [
                [1, 3],
                [2],
                [3, 0],
                [1, 2, 3],
            ]
    print(canUnlockAll(boxes))

    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))
