#!/usr/bin/python3

def makeChange(coins, total):
    # Follow this, If total is 0 or less, return 0
    if total <= 0:
        return 0

    # Initialize the dp array with infinity values except dp[0] = 0
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Fill the dp table
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If the total keep giving infinity as an outcome, return -1
    return dp[total] if dp[total] != float('inf') else -1
