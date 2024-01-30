class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # O(3*n)

        # edge case
        if len(nums) == 1:
            return nums[0]

        # edge case - all negative
        all_negative = all(x < 0 for x in nums)
        if all_negative:
            return max(nums)

        # todo número positivo é potencial início de uma sequência
        sequence_sum = 0
        sequence_tracker = 0
        max_value = 0

        while sequence_tracker < len(nums):
            sequence_sum += nums[sequence_tracker]

            if sequence_sum > max_value:
                max_value = sequence_sum

            elif sequence_sum <= 0:
                sequence_sum = 0

            sequence_tracker += 1

        return max_value
