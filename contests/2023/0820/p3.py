from typing import *

class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        ans = 0
        offers.sort()

        class Node:
            def __init__(self, s=-1, e=-1, g=0) -> None:
                self.s = s
                self.e = e
                self.g = g
                self.n = []

        root = Node()

        def dfs_add(info, node, cur_be) -> bool:
            nonlocal ans
            if info[0] > node.e or node.s == -1:
                success = False
                for child in node.n:
                    success = success or dfs_add(info, child, cur_be + node.g)
                if not success:
                    p = Node(info[0], info[1], info[2])
                    node.n.append(p)
                    ans = max(ans, cur_be + node.g + info[2])
                else:
                    return True
            else:
                return False
            
        for of in offers:
            dfs_add(of, root, 0)

        return ans



sl = Solution()
examples = [
    (5, [[0,0,1],[0,2,2],[1,3,2]], 3),
    (5, [[0,0,1],[0,2,10],[1,3,2]], 10),
    (4, [[0,0,5],[3,3,1],[1,2,5],[0,0,7]], 13)
]
for example in examples:
    n, offers, ans = example
    print(f"Output: {sl.maximizeTheProfit(n, offers)}, Ans: {ans}")