class Solution(object):
    def coinChange(self, coins, amount):
        d = [float('inf')] * (amount + 1)
        d[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    d[i] = min(d[i], d[i - coin] + 1)
        return d[amount] if d[amount] != float('inf') else -1
