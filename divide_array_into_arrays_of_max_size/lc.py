from typing import List


class Solution:
    # O(n log n)
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        result = [nums[i : i + 3] for i in range(0, len(nums), 3)]
        for triple in result:
            if abs(triple[0] - triple[2]) > k:
                return []
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.divideArray([5, 6, 6, 6, 7, 7, 10, 11, 11, 12, 12, 12], 2))
