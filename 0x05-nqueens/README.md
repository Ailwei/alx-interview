# 0x05. N Queens Algorithm

## Project Overview

The **0x05. N Queens** project is a classic challenge in computer science and mathematics. The goal is to place N non-attacking queens on an N×N chessboard using the backtracking algorithm. This README provides an overview of the project, necessary concepts, and resources to successfully complete it.

## Project Timeline

- **Start Date:** May 27, 2024, 6:00 AM
- **End Date:** May 31, 2024, 6:00 AM
- **Checker Release:** May 28, 2024, 6:00 AM
- **Auto Review:** Launched at the deadline

## Key Concepts

### Backtracking Algorithms

Backtracking is an algorithmic technique for solving problems recursively by trying to build a solution incrementally, one piece at a time, and removing solutions that fail to satisfy the problem constraints at any point of time.

- **Introduction to Backtracking:** [Backtracking Algorithm](https://www.geeksforgeeks.org/backtracking-algorithms/)

### Recursion

Recursion involves a function calling itself to solve smaller instances of the same problem. It is often used in backtracking algorithms.

- **Recursion in Python:** [Python Recursion](https://realpython.com/python-recursion/)

### List Manipulations in Python

Lists are versatile data structures in Python that can be used to store the positions of queens on the board.

- **Python Lists:** [Python List Manipulation](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)

### Python Command Line Arguments

Handling command-line arguments is essential for taking input directly from the user.

- **Command Line Arguments in Python:** [Command Line Arguments](https://docs.python.org/3/library/sys.html#sys.argv)

## Implementation Steps

1. **Understand the Problem:**
   - Place N queens on an N×N chessboard such that no two queens threaten each other.
   - A queen can attack another queen if they are on the same row, column, or diagonal.

2. **Set Up Your Environment:**
   - Ensure Python is installed on your system.
   - Create a new directory for the project and initialize a Git repository.

3. **Algorithm Design:**
   - Use backtracking to explore all potential placements for the queens.
   - Utilize a recursive function to place queens row by row.
   - Ensure each placement satisfies the constraints before proceeding to place the next queen.

4. **Implementation:**
   - Create a Python script to implement the backtracking algorithm.
   - Use lists to track the positions of the queens.
   - Handle command-line arguments to input the value of N.

5. **Testing:**
   - Test your implementation with different values of N.
   - Ensure that all solutions are correct and that the program runs efficiently.
