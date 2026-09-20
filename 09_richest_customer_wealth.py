# Richest Customer Wealth (LeetCode #1672)
# Story: biggest box starts at 0; for each customer, sum their accounts;
#        if bigger than box, replace; return box.
# Time: O(m*k) - visit every account once.  Space: O(1)

class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        max_wealth = 0
        for customer in accounts:
            total = sum(customer)
            if total > max_wealth:
                max_wealth = total
        return max_wealth
