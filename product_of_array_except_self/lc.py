from typing import	 List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
       # time O(n) and space O(3n)
        
        n = len(nums)
        suffix_sum = [1]*n
        prefix_sum = [1]*n
        answer=[]

        prefix_sum[0] = nums[0]
        suffix_sum[n-1] = nums[n-1]
        
        # prefix loop
        for i in range(1,n,1):
            prefix_sum[i]=prefix_sum[i-1]*nums[i]

        # suffix loop
        for j in range(n-2,-1,-1):
            suffix_sum[j]=suffix_sum[j+1]*nums[j]

        # answer
        answer.append(suffix_sum[1])
        for z in range(2,n):
            answer.append(suffix_sum[z]*prefix_sum[z-2])
        answer.append(prefix_sum[n-2])

        return answer

        '''
        # first suffix and prefix sum try - O(n2) approach
        suffix_sum = []
        for i in range(0,len(nums)):
            product = 1
            for j in range(i,len(nums)):
                product*=nums[j]
            suffix_sum.append(product)

        prefix_sum = []
        prefix_sum.append(nums[0])

        for i in range(1,len(nums)):
            prefix_sum.append(nums[i]*prefix_sum[i-1])

        result = []
        result.append(suffix_sum[1])
        i = 2
        j = 0
        while(i<len(nums)):
            result.append(suffix_sum[i]*prefix_sum[j])
            i+=1
            j+=1

        result.append(prefix_sum[j])
        return result

        '''
        '''
        # naive approach O(n2)
        products = []
        for i,x in enumerate(nums):
            product=1
            for j,y in enumerate(nums):
                if(i!=j):
                    product*=y
            products.append(product)
        
        return(products)
        '''
        