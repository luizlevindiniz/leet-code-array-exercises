from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # edge case
        if len(nums) == 1:
            return nums[0]

        # O(n)
        max_till_now = 1
        min_till_now = 1
        max_product = nums[0]

        for i in range(0, len(nums)):
            max_value = max(nums[i], max_till_now * nums[i], min_till_now * nums[i])
            min_value = min(nums[i], max_till_now * nums[i], min_till_now * nums[i])

            max_so_far = max(max_value, min_value)

            if max_so_far > max_product:
                max_product = max_so_far

            max_till_now = max_value
            min_till_now = min_value

        return max_product


"""
        # naive approach O(n2)
        max_product = 0

        for i in range(0,len(nums)):
            product = nums[i]
            if(product>max_product):
                max_product=product
            for j in range(i+1,len(nums)):
                product *= nums[j]
                if(product>max_product):
                    max_product=product

        return max_product
        """

if __name__ == "__main__":
    sol = Solution()
    arr = [-4, -3, -2]
    answer = sol.maxProduct(arr)
    print(answer)


"""         index = 1
        while index < len(nums):
            if (nums[index] >= prefix_product[index]) and (nums[index] > max_product):
                max_product = nums[index]
            elif (prefix_product[index] >= nums[index]) and (
                prefix_product[index] > max_product
            ):
                max_product = prefix_product[index]
            index += 1
 """
