import sys
class Solution:
    def maxProfit(self, prices):
        profit,mini=0,sys.maxsize
        for price in prices:
            mini=min(mini,price)
            profit=max(profit,price-mini)

        return profit

test=Solution()
print(test.maxProfit([7,1,5,3,6,4]))