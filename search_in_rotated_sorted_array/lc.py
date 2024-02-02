from typing import List


class Solution:
    def check_and_split(
        self, arr: List[int], target: int, start: int, stop: int
    ) -> int:
        if start > stop:
            return -1

        mid = (start + stop) // 2

        if arr[mid] == target:
            return mid

        else:
            left = self.check_and_split(arr, target, start, mid - 1)
            right = self.check_and_split(arr, target, mid + 1, stop)

        if left != -1:
            return left
        elif right != -1:
            return right
        else:
            return -1

    def search(self, nums: List[int], target: int) -> int:
        # O(log n)

        # edge case
        if len(nums) == 1 and target == nums[0]:
            return 0

        # base case

        start = 0
        stop = len(nums) - 1

        return self.check_and_split(nums, target, start, stop)

        """
        # O(n) naive approach
        if target in nums:
            return nums.index(target)
        return -1
        """
