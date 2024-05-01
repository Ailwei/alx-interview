from collections import deque

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
