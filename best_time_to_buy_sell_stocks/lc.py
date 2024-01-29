from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # len do array e os valores são de tal forma
        # que ambos variam de 1 até n. Só tenho inteiros positivos

        # edge case
        if(len(prices)==1):
            return 0

        # O(n)
        to_buy = 0
        to_sell = 1
        profit = 0

        while(to_sell < len(prices)):
            profit_of_day = prices[to_sell]-prices[to_buy]
            if(profit_of_day < 0):
                to_buy=to_sell
            else:
                if(profit_of_day > profit):
                    profit=profit_of_day
            to_sell +=1

        """ 
        # O(n2) - naive approach
        profit = 0
        for i in range(0,len(prices),1):
            for j in range(i,len(prices),1):
                if(prices[j]>prices[i]):
                    result = prices[j]-prices[i]
                    if(result>profit):
                        profit=result
         """
        return profit
