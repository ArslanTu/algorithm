#
# @lc app=leetcode.cn id=1615 lang=python3
#
# [1615] 最大网络秩
#

# @lc code=start
from typing import List


class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        '''
        数据量较小，暴力可通过

        在 O(n) 解法中，要关注的不是最大和次大顶点，而是最大和次大值，
        或者说所有值等于最大和次大值的顶点。
        因此在找到最大和次大值后，要遍历所有等值的顶点，
        如果发现有组合间无连接，则输出最大值和次大值的和，
        否则输出其和减一。
        '''
        graph = [[False] * n for _ in range(n)]
        num_roads = [[i, 0] for i in range(n)]
        for v1, v2 in roads:
            graph[v1][v2] = True
            graph[v2][v1] = True
            num_roads[v1][1] += 1
            num_roads[v2][1] += 1
        num_roads.sort(key=lambda x:x[1], reverse=True)
        i = 0
        while i < n and num_roads[i][1] == num_roads[0][1]:
            j = i + 1
            while j < n and num_roads[j][1] == num_roads[1][1]:
                if not graph[num_roads[i][0]][num_roads[j][0]]:
                    return num_roads[0][1] + num_roads[1][1]
                j += 1
            i += 1
        return num_roads[0][1] + num_roads[1][1] - 1
# @lc code=end

