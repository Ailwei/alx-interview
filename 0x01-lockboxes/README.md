# 0x01. Lockboxes

## Algorithm

To determine if all boxes can be opened, we'll utilize graph traversal algorithms, such as Breadth-First Search (BFS). Each box can be considered a node in the graph, and the keys inside each box represent edges to other nodes. By traversing through the graph starting from the first box and keeping track of visited boxes, we can determine if all boxes are reachable.

## Python

### Must Know

For this project, you will need a solid understanding of several key concepts in order to develop a solution that can efficiently determine if all boxes can be opened. Here’s a list of concepts and resources that will be instrumental in tackling this project:

**Concepts Needed:**

- **Lists and List Manipulation:** Understanding how to work with lists, including accessing elements, iterating over lists, and modifying lists dynamically.
  - [Python Lists (Python Official Documentation)](https://docs.python.org/3/tutorial/datastructures.html)

- **Graph Theory Basics:** Knowledge of graph theory concepts, especially traversal algorithms like Depth-First Search (DFS) or Breadth-First Search (BFS), can be helpful in solving this problem.
  - [Graph Theory (Khan Academy)](https://www.khanacademy.org/computing/computer-science/algorithms)

- **Algorithmic Complexity:** Understanding time and space complexity is important for writing efficient algorithms.
  - [Big O Notation (GeeksforGeeks)](https://www.geeksforgeeks.org/understanding-time-complexity-simple-examples/)

- **Recursion:** Some solutions might require a recursive approach to traverse through the boxes and keys.
  - [Recursion in Python (Real Python)](https://realpython.com/python-thinking-recursively/)

- **Queue and Stack:** Knowledge of using queues and stacks is crucial for implementing BFS or DFS algorithms to traverse through the keys and boxes.
  - [Python Queue and Stack (GeeksforGeeks)](https://www.geeksforgeeks.org/queue-in-python/)

- **Set Operations:** Understanding how to use sets for keeping track of visited boxes and available keys can optimize the search process.
  - [Python Sets (Python Official Documentation)](https://docs.python.org/3/tutorial/datastructures.html#sets)

By reviewing these concepts and utilizing the provided resources, you will be well-equipped to develop an efficient solution for this project, applying both your algorithmic thinking and Python programming skills.

### Additional Resources

- **Mock Technical Interview**

### Requirements

- **General:**
  - Allowed editors: vi, vim, emacs
  - All files interpreted/compiled on Ubuntu 20.04 LTS using Python 3.4.3
  - All files should end with a new line
  - The first line of all files should be exactly `#!/usr/bin/python3`
  - A `README.md` file, at the root of the project folder, is mandatory
  - Code should be documented
  - Code should use PEP 8 style (version 1.7.x)
  - All files must be executable
