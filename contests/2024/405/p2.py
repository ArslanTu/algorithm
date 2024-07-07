"""
weekply contest p2
"""
from typing import *


class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans = ["0", "1"]
        if n == 1:
            return ans
        for i in range(1, n):
            _ans = []
            for a in ans:
                _ans.append(a+"1")
                if a[-1] == "1":
                    _ans.append(a+"0")
            ans = _ans
        return ans


def test():
    """
    test func
    """
    sl = Solution()
    examples = [
    ]
    for example in examples:
        ans = example
        print(f"Output: {sl}, Ans: {ans}")


if __name__ == "__main__":
    test()
