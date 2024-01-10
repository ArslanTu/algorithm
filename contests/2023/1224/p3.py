from math import inf
from typing import *

def shortest_path(adj_matrix):
    num_vertices = len(adj_matrix)
    distances = [[float('inf') for _ in range(num_vertices)] for _ in range(num_vertices)]

    # 初始化距离矩阵
    for i in range(num_vertices):
        for j in range(num_vertices):
            if i == j:
                distances[i][j] = 0
            elif adj_matrix[i][j] != 0:
                distances[i][j] = adj_matrix[i][j]

    # 计算最短路径
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])

    return distances

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        G = [[inf for _ in range(26)] for _ in range(26)]
        for i in range(26):
            for j in range(26):
                if i == j:
                    G[i][j] = 0
        for i in range(len(original)):
            x = ord(original[i]) - ord('a')
            y = ord(changed[i]) - ord('a')
            G[x][y] = min(G[x][y], cost[i])
        
        min_dis = shortest_path(G)
        ans = 0
        for i in range(len(source)):
            x = ord(source[i]) - ord('a')
            y = ord(target[i]) - ord('a')
            if min_dis[x][y] == inf:
                return -1
            else:
                ans += min_dis[x][y]
        return ans

sl = Solution()
examples = [
    
]
for example in examples:
    ans = example
    print(f"Output: {sl}, Ans: {ans}")

