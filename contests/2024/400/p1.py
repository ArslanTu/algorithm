"""
weekply contest p1
"""
from typing import *


class Solution:
    def minimumChairs(self, s: str) -> int:
        ans = 0
        t_ans = 0
        for c in s:
            if 'E' == c:
                ans +=1
            else:
                ans -= 1
            t_ans = max(ans, t_ans)
        return t_ans


def test():
    """
    test func
    """
    sl = Solution()
    examples = []
    for example in examples:
        ans = example
        print(f"Output: {sl}, Ans: {ans}")


if __name__ == "__main__":
    test()
