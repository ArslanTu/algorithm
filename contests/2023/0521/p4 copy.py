from collections import defaultdict
from typing import List

import heapq

class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        # 替换权值为 -1 的边
        new_edges = []
        for u, v, w in edges:
            if w == -1:
                w = 2 * 10**9
            new_edges.append((u, v, w))
            new_edges.append((v, u, w))
        
        # 构建新图并执行 Dijkstra 算法
        graph = [[] for _ in range(n)]
        visited = [False] * n
        dist = [float("inf")] * n
        dist[source] = 0
        for u, v, w in new_edges:
            graph[u].append((v, w))
        heap = [(0, source)]
        while heap:
            d, u = heapq.heappop(heap)
            if visited[u]:
                continue
            visited[u] = True
            for v, w in graph[u]:
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    heapq.heappush(heap, (dist[v], v))
        
        # 找到可能对最终答案有作用的边
        candidates = set()
        for u, v, w in edges:
            if w != -1:
                continue
            if dist[u] + dist[v] + 1 == dist[destination]:
                candidates.add((u, v))
        
        # 修改边权并重新执行 Dijkstra 算法
        for u, v in candidates:
            new_edges.remove((u, v, 2 * 10**9))
            new_edges.remove((v, u, 2 * 10**9))
            new_edges.append((u, v, 1))
            new_edges.append((v, u, 1))
        graph = [[] for _ in range(n)]
        visited = [False] * n
        dist = [float("inf")] * n
        dist[source] = 0
        for u, v, w in new_edges:
            graph[u].append((v, w))
        heap = [(0, source)]
        while heap:
            d, u = heapq.heappop(heap)
            if visited[u]:
                continue
            visited[u] = True
            for v, w in graph[u]:
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    heapq.heappush(heap, (dist[v], v))
        
        # 判断是否存在符合要求的方案
        if dist[destination] != target:
            return []
        
        # 返回结果
        ans = [[u, v, w] for u, v, w in edges]
        for u, v in candidates:
            ans.append([u, v, 1])
        return ans



sl = Solution()
# p = [[0,1,-1],[1,2,-1],[3,1,-1],[3,0,2],[0,2,5]]
p = [[4,1,-1],[2,0,-1],[0,3,-1],[4,3,-1]]
# print(sl.modifiedGraphEdges(4, p, 2, 3, 8))
print(sl.modifiedGraphEdges(5, p, 0, 1, 5))