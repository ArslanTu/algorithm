from typing import *
from collections import Counter


class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        sum_of_digits = sum([int(digit) for digit in str(x)])
        return sum_of_digits if x % sum_of_digits == 0 else -1


sl = Solution()
examples = [
    (18, 9),
    (23, -1),
]
for example in examples:
    x, ans = example
    print(f"Output: {sl.sumOfTheDigitsOfHarshadNumber(x)}, Ans: {ans}")