from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # edge case
        if len(nums) == 1:
            return False

        # O(n)
        hash_map = {}

        for index, value in enumerate(nums):
            if value in hash_map:
                return True
            else:
                hash_map[value] = 1

        return False

        """
        # naive approach O(n2)
        has_duplicate = False
        
        for i,x in enumerate(nums):
            for j,y in enumerate(nums):
                if(i!=j and x==y):
                    has_duplicate = True
                    return has_duplicate
        """
