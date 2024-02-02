from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # O(n2)
        # base case
        answer = []
        nums.sort()
        for i, x in enumerate(nums):
            # skip duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            hash_table = {}
            holding = x
            target = -x

            for j, y in enumerate(nums):
                if i != j:
                    remaining = target - y
                    if y in hash_table:
                        answer.append([holding, y, hash_table[y]])
                    else:
                        hash_table[remaining] = y

        return [list(x) for x in {tuple(sorted(x)) for x in answer}]


if __name__ == "__main__":
    sol = Solution()
    arr = [-1, 0, 1, 2, -1, -4]
    resp = sol.threeSum(arr)
    print(resp)
