from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:

        n = len(ratings)
        candies_per_child = [1] * n

        i = 0
        for j in range(1, n):
            if ratings[j] > ratings[i]:
                candies_per_child[j] = 1 + candies_per_child[i]
            i += 1

        i = n - 1
        for j in range(n - 2, -1, -1):
            if ratings[j] > ratings[i] and candies_per_child[j] <= candies_per_child[i]:
                candies_per_child[j] = 1 + candies_per_child[i]
            i -= 1

        return sum(candies_per_child)


if __name__ == "__main__":
    s = Solution()
    print(s.candy([1, 0, 2]))
