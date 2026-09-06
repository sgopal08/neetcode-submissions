class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # prices = [10,8,7,5,2]
        #                  l r

        # profit = 6
        # right - left = proft
        
        # check if right is LESS than left -> change if true
        # find lowest price to buy, highest to sell
        # two pointer method -> monotonic conditions (thing intervals on a graph)

        l = 0
        r = 1

        max_profit = 0

        while r < len(prices):
            profit = prices[r] - prices[l]

            max_profit = max(profit, max_profit)

            if prices[l] > prices[r]:
                l = r

            r += 1
        
        return max_profit
         # prices = [10,1,5,6,7,1] profit = 7, max_profit = 7
        #               l  
        #                       r

            






        