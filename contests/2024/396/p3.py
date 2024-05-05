"""
weekply contest p1
"""
from typing import *
from collections import Counter

class Solution:
    def minAnagramLength(self, s: str) -> int:
        n = len(s)
        cnt = Counter()
        for idx, c in enumerate(s):
            cnt[c] += 1
            if n % (idx + 1) == 0:
                if all(cnt == Counter(s[start:start+idx+1]) for start in range(idx + 1, n, idx + 1)):
                    return idx + 1
        return len(s)


def test():
    """
    test func
    """
    sl = Solution()
    examples = [("abba", 2), ("cdef", 4)]
    for example in examples:
        s, ans = example
        print(f"Output: {sl.minAnagramLength(s)}, Ans: {ans}")


if __name__ == "__main__":
    test()
