from typing import List


class Solution:
    # O(n log n)
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        possibilities = []
        for i in range(1, 10):
            num = i
            next_digit = i
            for _ in range(1, 10 - i):
                next_digit += 1
                num = num * 10 + next_digit
                possibilities.append(num)

        possibilities.sort()
        result = list(filter(lambda x: x >= low and x <= high, possibilities))
        return result

    # naive approach O(n2) in time
    """
    def list_to_number(self, list_of_digits: list) -> int:
        s = "".join(map(str, list_of_digits))
        return int(s)

    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result = []

        low_str = str(low)
        low_f_digit = int(low_str[0])
        starting_point = []
        if low_f_digit > 10 - len(low_str):
            starting_point.append(1)

        low_digits = [int(d) for d in low_str]
        starting_point.extend(low_digits)

        if starting_point[0] == 9:
            starting_point[0] = 1
            starting_point.append(0)

        for index in range(1, len(starting_point)):
            starting_point[index] = starting_point[index - 1] + 1

        number = self.list_to_number(starting_point)
        result.append(number)

        while number < high:
            starting_point[0] += 1

            if starting_point[0] > 10 - len(starting_point):
                zeros_arr = [0] * len(starting_point)
                starting_point = []
                starting_point.append(1)
                starting_point.extend(zeros_arr)

            for index in range(1, len(starting_point)):
                starting_point[index] = starting_point[index - 1] + 1

            number = self.list_to_number(starting_point)
            result.append(number)

        result = list(filter(lambda x: x >= low and x <= high, result))
        return result

    """


if __name__ == "__main__":
    s = Solution()
    print(s.sequentialDigits(58, 155))
