from typing import List

class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        # retornar dois índices [x,y] de tal forma que
        # nums[x] + nums[y] = target
        # restrições: apenas 1 solução existe e não se
        # usa índices repetidos.

        # edge case
        if(len(nums)==2):
            return [0,1]

        """      # O(n2)
        for i,x in enumerate(nums):
            for j,y in enumerate(nums):
                if(x+y == target and i!=j):
                    return[i,j]
        """
        
        # O(n)
        hash_table = {}
        for index,value in enumerate(nums):
            complementary = target - value
            if value in hash_table:
                return[hash_table[value],index]
            else:
                hash_table[complementary]=index
        

        
        
if __name__ == "__main__":
    sol = Solution()
    arr = [2,7,11,15]
    resp = sol.two_sum(nums=arr,target=9)
    print(resp)