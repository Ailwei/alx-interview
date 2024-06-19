#!/usr/bin/python3
"""Making change O(n)"""

def makeChange(coins, total):
    """
     Determines the fewest number of coins needed to meet
     a given amount total.
    """
    if total <= 0:
        return 0
    
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    
    for coin in coins:
        for x in range(coin, total + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    
    return dp[total] if dp[total] != float('inf') else -1

if __name__ == '__main__':
    print(makeChange([1, 2, 25], 37))
    print(makeChange([1256, 54, 48, 16, 102], 1453))
