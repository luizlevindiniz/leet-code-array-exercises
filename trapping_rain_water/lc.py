from typing import List


class Solution:
    # O(n)
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefix = [height[0]]
        suffix = [height[n - 1]]

        traps_counter = 0

        # creating prefix arr
        for i in range(1, n):
            prefix.append(max(prefix[i - 1], height[i]))

        # creating suffix arr
        for i in range(1, n):
            suffix.append(max(suffix[i - 1], height[n - 1 - i]))

        suffix = list(reversed(suffix))

        # subtracting from original arr
        prefix_minus_height = [x - y for (x, y) in zip(prefix, height)]
        suffix_minus_height = [x - y for (x, y) in zip(suffix, height)]

        i = 0
        j = 1
        counter = 0
        while j < n:
            if prefix_minus_height[j] == 0 and prefix_minus_height[i] == 0:
                i = j
                traps_counter += counter
                counter = 0
            elif prefix_minus_height[j] == 0:
                i = j
            else:
                counter += prefix_minus_height[j]
            j += 1

        j = i + 1
        counter = 0
        while j < n:
            if suffix_minus_height[j] == 0 and suffix_minus_height[i] == 0:
                i = j
                traps_counter += counter
                counter = 0
            elif suffix_minus_height[j] == 0:
                i = j
            else:
                counter += suffix_minus_height[j]
            j += 1

        return traps_counter


if __name__ == "__main__":
    s = Solution()
    print(s.trap([5, 5, 1, 7, 1, 1, 5, 2, 7, 6]))
    print(s.trap([2, 0, 2]))
    print(s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    print(s.trap([4, 2, 0, 3, 2, 5]))
