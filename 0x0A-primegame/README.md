# 0x0A. Prime Game

## Algorithm
**Python**

### Project Overview
This project involves creating an algorithm to determine the winner of a game played by Maria and Ben. The game uses a set of consecutive integers starting from 1 up to `n`. Players take turns choosing a prime number from the set and removing that number and its multiples. The player who cannot make a move loses the game. 

You will implement the function `isWinner(x, nums)` where `x` is the number of rounds, and `nums` is an array of integers representing the value of `n` for each round. Your task is to determine who wins the most rounds.

### Key Concepts
- **Prime Numbers**: Understanding prime numbers and efficient algorithms to identify them.
- **Sieve of Eratosthenes**: An efficient algorithm for finding all prime numbers up to a given limit.
- **Game Theory**: Strategies for optimal play in competitive games.
- **Dynamic Programming/Memoization**: Techniques for optimizing calculations by using previously computed results.
- **Python Programming**: Implementing the game logic and algorithms in Python.

### Resources
- **Prime Numbers and Sieve of Eratosthenes**:
  - [Khan Academy: Prime Numbers](https://www.khanacademy.org/math/pre-algebra/factors-multiples/prime-numbers/v/prime-numbers)
  - [Sieve of Eratosthenes in Python](https://www.geeksforgeeks.org/sieve-of-eratosthenes/)
- **Game Theory Basics**:
  - [Game Theory Introduction](https://www.investopedia.com/terms/g/gametheory.asp)
- **Dynamic Programming**:
  - [What Is Dynamic Programming With Python Examples](https://www.digitalocean.com/community/tutorials/dynamic-programming-in-python)
- **Python Official Documentation**:
  - [Python Lists](https://docs.python.org/3/tutorial/datastructures.html)

### Requirements
- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.4.3)
- All files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file at the root of the project folder is mandatory
- Your code should use the PEP 8 style (version 1.7.x)
- All files must be executable
