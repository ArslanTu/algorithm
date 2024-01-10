from typing import *


class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
        ans = 0
        for i in range(k):
            max_p = 0
            l, r = 0, 10 ** 10

            def check(p_num):
                total_cost = 0
                for j in range(n):
                    to_buy = (composition[i][j] * p_num - stock[j])
                    if to_buy > 0:
                        total_cost += to_buy * cost[j]
                if total_cost <= budget:
                    return True
                else:
                    return False
                
            while l < r:
                mid = (l + r) // 2
                if check(mid):
                    max_p = max(max_p, mid)
                    l = mid + 1
                else:
                    r = mid
            
            ans = max(ans, max_p)
        return ans




sl = Solution()
examples = [
    (2, 3, 10, [[2,1],[1,2],[1,1]], [1,1], [5,5], 2),
]
for example in examples:
    n, k, budget, composition, stock, cost, ans = example
    print(f"Output: {sl.maxNumberOfAlloys(n, k, budget, composition, stock, cost)}, Ans: {ans}")