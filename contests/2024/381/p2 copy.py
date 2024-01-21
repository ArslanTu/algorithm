from typing import *
import heapq

def dijkstra(graph, start):
    # 初始化距离字典，存储每个节点到起始节点的最短距离
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # 初始化优先队列，用于选择下一个要访问的节点
    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        # 如果当前节点已经被访问过，跳过当前循环
        if current_distance > distances[current_node]:
            continue

        # 遍历当前节点的邻居节点
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # 如果通过当前节点到达邻居节点的距离更短，更新最短距离
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances


class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        if x == y:
            return [(n - i) * 2 for i in range(1, n + 1)]
        G = {}
        for i in range(n):
            for j in range(n):
                if abs(i-j) == 1:
                    if G.get(i, None) == None:
                        G[i] = {}
                    if G.get(j, None) == None:
                        G[j] = {}
                    G[i][j] = 1

                    G[j][i] = 1
        G[x-1][y-1] = 1
        G[y-1][x-1] = 1
        ans = [0 for _ in range(n)]
        for i in range(n):
            dis = dijkstra(G, i)
            for v in dis.values():
                ans[v-1] += 1
        ans[-1] = 0
        return ans



sl = Solution()
examples = [
    (3, 1, 3, [6,0,0]),
    (5, 2, 4, [10,8,2,0,0]),
    (4, 1, 1, [6,4,2,0]),
    (2, 2, 1, [2, 0]),
    (5, 1, 5, [10,10,0,0,0])
]
for example in examples:
    n, x, y, ans = example
    print(f"Output: {sl.countOfPairs(n, x, y)}, Ans: {ans}")