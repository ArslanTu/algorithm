from typing import *
from collections import *

class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        return sum(h >= target for h in hours)


sl = Solution()

cases = [()]
for case in cases:

    print(f"expect: {ans}, output: {sl}")