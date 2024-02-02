"""
A jump means adding or subtracting 1.
“Converge” means all the elements get to the same value.
Given an integer array, find if all the elements could converge with 1 jump (or less) and return the converge value.

input elements could be numbers between 0 and 9 inclusive
9 plus 1, gives you 0
0 minus 1, gives you 9

Test Case
[ 1, 0, 9, 9, 1, 1, 0, 0]
Output = 0

Test Case
[ 1, 0, 9, 9, 1, 1, 0, 3]
Output = -1

Extras test cases
[0,9] -> 0
[1, 2, 3, 1, 1] -> 2

As if you jump down from 1 to 0 on all 1s, and you jump up on all 9 to 0, 
all numbers are going to converge into 0 value. So your output is the converge 
value, 0 in this case. Return -1 if there is no convergence like would be the 
case if in the example we add a “3” at the end (or any other number).
"""


def convergence(arr: list):
    # edge case
    if len(arr) == 0:
        return -1
    # edge case
    if len(arr) == 1:
        return arr[0]

    # base case
    number_stored = arr[0]
    is_stored = True

    number_plus = number_stored + 1
    is_plus = True

    number_minus = number_stored - 1
    is_minus = True

    # loop using the number_stored and is_stored
    for i in range(1, len(arr)):
        if arr[i] == number_stored:
            continue
        elif arr[i] + 1 == number_stored:
            continue
        elif arr[i] - 1 == number_stored:
            continue
        elif arr[i] == 0 and (number_stored == 9 or number_stored == 1):
            continue
        elif arr[i] == 9 and (number_stored == 8 or number_stored == 0):
            continue

        is_stored = False
        break

    # loop using the number_plus and is_plus
    for i in range(1, len(arr)):
        if arr[i] == number_plus:
            continue
        elif arr[i] + 1 == number_plus:
            continue
        elif arr[i] - 1 == number_plus:
            continue
        elif arr[i] == 0 and (number_plus == 9 or number_plus == 1):
            continue
        elif arr[i] == 9 and (number_plus == 8 or number_plus == 0):
            continue

        is_plus = False
        break

    # loop using the number_minus and is_minus
    for i in range(1, len(arr)):
        if arr[i] == number_minus:
            continue
        elif arr[i] + 1 == number_minus:
            continue
        elif arr[i] - 1 == number_minus:
            continue
        elif arr[i] == 0 and (number_minus == 9 or number_minus == 1):
            continue
        elif arr[i] == 9 and (number_minus == 8 or number_minus == 0):
            continue

        is_minus = False
        break

    if is_stored:
        return number_stored
    elif is_plus:
        return number_plus
    elif is_minus:
        return number_minus
    else:
        return -1


if __name__ == "__main__":
    print(
        convergence(
            [
                1,
                2,
                3,
                1,
                1,
            ]
        )
    )
