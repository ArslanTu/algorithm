from collections import defaultdict
from typing import List


class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        graph = [[] for _ in range(n)]
        weights = defaultdict()
        added = defaultdict(int)
        for a, b, w in edges:
            graph[a].append(b)
            graph[b].append(a)
            weights[(a, b)] = w
            weights[(b, a)] = w
        ans = []
        visited = [0] * n
        path = []

        def dfs(s, t, left, path, visited):
            nonlocal ans
            if (s, t) in weights:
                if weights[(s, t)] == left or weights[(s, t)] == -1:
                    path.append([s, t, left])
                    added[(s, t)] = 1
                    ans = list(path)
                    return True
            for v in graph[s]:
                if visited[v]:
                    continue
                weight = weights[(s, v)]
                if weight == -1:
                    weight = 1
                cur = [s, v, weight]
                if weight >= left:
                    continue
                path.append(cur)
                visited[v] = 1
                added[(s, v)] = 1
                if dfs(v, t, left - weight, path, visited):
                    return True
                path.pop()
                visited[v] = 0
                added[(s, v)] = 0
        visited[source] = 1
        dfs(source, destination, target, path, visited)

        if ans == []:
            return ans
        for a, b, w in edges:
            if (not added[(a, b)]) and (not added[(b, a)]):
                weight = abs(w)
                ans.append([a, b, weight])
                
        return ans


sl = Solution()
p = [[0,1,-1],[1,2,-1],[3,1,-1],[3,0,2],[0,2,5]]

print(sl.modifiedGraphEdges(4, p, 2, 3, 8))