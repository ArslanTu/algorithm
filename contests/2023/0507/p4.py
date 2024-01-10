from collections import deque
from math import log

from typing import List


class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        cost.insert(0, 0)
        ans = 0
        layer = int(log(n + 1, 2))
        leaf_num = int(pow(2, layer - 1))
        leaf = list(range(n - leaf_num + 1, n + 1))
        for i in range(1, n + 1):
            cost[i] += cost[i // 2]

        max_sum = max(cost[n - leaf_num + 1: n + 1])
        to_add = [0] * (n + 1)
        for le in leaf:
            to_add[le] = max_sum - cost[le]
        leaf = deque(leaf)
        while len(leaf) > 1:
            l = leaf.popleft()
            r = leaf.popleft()
            gre_diff = max(to_add[l], to_add[r])
            les_diff = min(to_add[l], to_add[r])
            pub_diff = les_diff
            per_diff = gre_diff - les_diff
            to_add[l // 2] += pub_diff
            ans += per_diff
            leaf.append(l // 2)

        ans += to_add[1]

        return ans
    
sl = Solution()
p1 = 7
p2 = [1,5,2,2,3,3,1]
print(sl.minIncrements(p1, p2))