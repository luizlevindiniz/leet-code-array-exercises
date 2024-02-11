# 2133. Check if Every Row and Column Contains All Numbers
from typing import List


class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        possible_numbers = set(range(1, n + 1))

        for row in matrix:
            row_set = set(row)
            if row_set != possible_numbers or len(row_set) != len(possible_numbers):
                return False

        transposed_matrix: list = list(zip(*matrix))
        for row in transposed_matrix:
            row_set = set(row)
            if row_set != possible_numbers or len(row_set) != len(possible_numbers):
                return False

        return True
