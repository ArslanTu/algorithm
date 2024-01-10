from typing import *

class Node:
    def __init__(self, num):
        self.num = num
        self.nexts = []

class Solution:
    def findChampionHelp(self, grid: List[List[int]]) -> int:
        n = len(grid)
        nums = [1 for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    nums[j] = 0
        ans = -1
        for i in range(n):
            if nums[i] == 1:
                if ans != -1:
                    return -1
                else:
                    ans = i
        return ans

    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        grid = [[0 for _ in range(n)] for _ in range(n)]
        nodes = [Node(i) for i in range(n)]
        for u, v in edges:
            nodes[v].nexts.append(nodes[u])
        
        leaves = []
        
        for node in nodes:
            if len(node.nexts) == 0:
                leaves.append(node)
        if len(leaves) != 1:
            return -1
        else:
            return leaves[0].num


sl = Solution()
print(sl.findChampion(4, [[0,2],[1,3],[1,2]]))