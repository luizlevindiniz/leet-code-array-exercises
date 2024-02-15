from typing import List


class Solution:
    # O(n)
    def maximumTripletValue(self, nums: List[int]) -> int:
        prefix_pair_diff = []
        suffix_number_to_multiplicate = []
        max_num_so_far = 0
        for num in nums:
            max_num_so_far = max(max_num_so_far, num)
            prefix_pair_diff.append(max(max_num_so_far - num, 0))

        max_num_so_far = 0
        for num in reversed(nums):
            max_num_so_far = max(max_num_so_far, num)
            suffix_number_to_multiplicate.append(max_num_so_far)

        i = 1
        j = len(nums) - 3
        max_triplet_value = 0

        while i < len(nums) - 1:
            max_triplet_value = max(
                max_triplet_value,
                prefix_pair_diff[i] * suffix_number_to_multiplicate[j],
            )
            i += 1
            j -= 1

        return max_triplet_value

        """
        # O(n3)
            def run_calculation(self, i, j, k):
                calculation = (i - j) * k
                if calculation < 0:
                    return 0
                return calculation

            def maximumTripletValue(self, nums: List[int]) -> int:

                i = 0
                n = len(nums)

                max_value = 0
                max_i_so_far = nums[i]

                while i < n - 2:
                    if nums[i] >= max_i_so_far:
                        max_i_so_far = nums[i]
                        j = i + 1

                        min_j_so_far = nums[j]
                        while j < n - 1:
                            if nums[j] <= min_j_so_far:
                                min_j_so_far = nums[j]
                                k = j + 1

                                max_k_so_far = nums[k]
                                while k < n:
                                    if nums[k] > max_k_so_far:
                                        max_k_so_far = nums[k]

                                    k += 1

                                calculation = self.run_calculation(
                                    nums[i], min_j_so_far, max_k_so_far
                                )
                                if calculation > max_value:
                                    max_value = calculation
                            j += 1
                    i += 1

                return max_value
            """


if __name__ == "__main__":
    s = Solution()
    print(s.maximumTripletValue([12, 6, 1, 2, 7]))
