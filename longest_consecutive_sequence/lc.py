from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # O(n)

        # edge case
        if len(nums) == 0:
            return 0

        num_set = set(nums)
        max_so_far = 1

        for num in num_set:
            if num - 1 not in num_set:
                value = num + 1
                counter = 1
                while value in num_set:
                    value += 1
                    counter += 1

                max_so_far = max(max_so_far, counter)
        return max_so_far


if __name__ == "__main__":
    s = Solution()
    print(s.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
