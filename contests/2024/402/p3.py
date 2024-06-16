"""
weekply contest p3
"""
from typing import *


class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        cnt = Counter(power)
        ans = 0
        cnt2 = Counter()
        for k in cnt.keys():
            if all(k + i not in cnt for i in [-2, -1, 1, 2]):
                ans += k * cnt[k]
            else:
                cnt2[k] = cnt[k]
        
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
