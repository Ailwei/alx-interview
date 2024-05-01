#!/usr/bin/python3
"""A module for determining if all boxes can be opened from a list of lists."""

def canUnlockAll(boxes=[]):
    """
    Determines if all the boxes can be opened.

    Args:
    - boxes (list of list of int): A list of boxes, where each box is represented by a list of integers
                                   indicating the keys it contains. Defaults to an empty list.

    Returns:
    - bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes:
        return False

    keys = set([0])
    for box_id, box in enumerate(boxes):
        for key in box:
            if key < len(boxes) and key != box_id:
                keys.add(key)

    if len(keys) != len(boxes):
        return False

    return True

if __name__ == '__main__':
    boxes = [
                [1, 3],
                [2],
                [3, 0],
                [1, 2, 3],
            ]
    print(unlockBoxes(boxes))

    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(unlockBoxes(boxes))

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(unlockBoxes(boxes))
