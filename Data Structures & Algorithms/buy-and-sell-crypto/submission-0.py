class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buy,sell = prices[0],prices[0]
        b,s=0,1
        profit = max(0,sell-buy)
        while b <= s < n :
            print(sell,buy)
            if prices[b]<buy:
                buy = prices[b]
                sell = buy
            if prices[s]>sell:
                sell = prices[s]
            profit = max(profit,sell-buy)
            b+=1
            s+=1
        return profit