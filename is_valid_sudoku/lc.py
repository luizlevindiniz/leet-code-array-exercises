from typing import List


class Solution:
    # O(1)
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if not (self.check_if_rows_are_valid(matrix=board)):
            return False

        if not (self.check_if_columns_are_valid(matrix=board)):
            return False

        to_add = [0, 3, 6]

        for i in to_add:
            for j in to_add:
                are_3x3_squares_valid = self.check_if_3x3_squares_are_valid(
                    matrix=board, add_to_row=i, add_to_column=j
                )
                if not are_3x3_squares_valid:
                    return False

        return True

    def check_if_3x3_squares_are_valid(
        self, matrix: List[List[str]], add_to_row: int, add_to_column: int
    ) -> bool:
        seen = set()
        for row in range(0 + add_to_row, 3 + add_to_row):
            for column in range(0 + add_to_column, 3 + add_to_column):
                if matrix[row][column] == ".":
                    continue
                if matrix[row][column] in seen:
                    return False
                seen.add(matrix[row][column])

        return True

    def check_if_rows_are_valid(self, matrix: List[List[str]]) -> bool:

        seen = set()
        for row in matrix:
            for value in row:
                if value == ".":
                    continue
                if value in seen:
                    return False
                seen.add(value)
            seen = set()

        return True

    def check_if_columns_are_valid(self, matrix: List[List[str]]) -> bool:
        transposed_matrix: list = list(zip(*matrix))
        seen = set()
        for row in transposed_matrix:
            for value in row:
                if value == ".":
                    continue
                if value in seen:
                    return False
                seen.add(value)
            seen = set()

        return True
