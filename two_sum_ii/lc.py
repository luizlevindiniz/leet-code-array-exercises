from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # base case O(n) approach
        i = 0
        j = len(numbers) - 1

        while i < j:
            result = numbers[i] + numbers[j]
            if result == target:
                return [i + 1, j + 1]
            elif result > target:
                j -= 1
            else:
                i += 1

        return []

        """
        # naive approach O(n2)
        for i in range(0,len(numbers)):
            for j in range(i+1,len(numbers)):
                if(numbers[i]+numbers[j]==target):
                    return [i+1,j+1]
        """
