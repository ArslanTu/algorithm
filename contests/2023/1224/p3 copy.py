from math import inf
from typing import *


def get_min_dis(graph):
    n = len(graph)
    min_dis = [[inf for _ in range(n)] for _ in range(n)]

    # 初始化距离矩阵
    for i in range(n):
        for j in range(n):
            if i == j:
                min_dis[i][j] = 0
            elif graph[i][j] != 0:
                min_dis[i][j] = graph[i][j]

    # 计算最短路径
    for k in range(n):
        for i in range(n):
            for j in range(n):
                min_dis[i][j] = min(min_dis[i][j], min_dis[i][k] + min_dis[k][j])

    return min_dis


class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        graph = [[inf for _ in range(26)] for _ in range(26)]
        for i in range(26):
            graph[i][i] = 0
        for i in range(len(original)):
            x = ord(original[i]) - ord('a')
            y = ord(changed[i]) - ord('a')
            graph[x][y] = min(graph[x][y], cost[i])
        
        min_dis = get_min_dis(graph)
        res = 0
        for i in range(len(source)):
            x = ord(source[i]) - ord('a')
            y = ord(target[i]) - ord('a')
            if min_dis[x][y] == inf:
                return -1
            else:
                res += min_dis[x][y]
        return res


sl = Solution()
examples = [
    
]
for example in examples:
    ans = example
    print(f"Output: {sl}, Ans: {ans}")
