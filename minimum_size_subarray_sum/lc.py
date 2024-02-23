from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_of_elements = 100001
        start = 0

        curr_sum = 0

        for end in range(0, len(nums)):
            curr_sum += nums[end]

            while curr_sum >= target:
                min_of_elements = min(min_of_elements, end - start + 1)
                curr_sum -= nums[start]
                start += 1

        if min_of_elements == 100001:
            return 0
        return min_of_elements


if __name__ == "__main__":
    s = Solution()
    print(s.minSubArrayLen(15, [5, 1, 3, 5, 10, 7, 4, 9, 2, 8]))
