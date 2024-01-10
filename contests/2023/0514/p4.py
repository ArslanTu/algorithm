from collections import defaultdict
from typing import List

class UF:
    __fa = []
    __size = []
    __count = 0
    def __init__(self, n: int) -> None:
        self.__fa = list(range(n))
        self.__size = [1 for i in range(n)]
        self.__count = n
    def find(self, x: int) -> int:
        if self.__fa[x] != x: self.__fa[x] = self.find(self.__fa[x])
        return self.__fa[x]
    def union(self, x: int, y: int) -> None:
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY: return
        if self.__size[rootX] <= self.__size[rootY]:
            self.__fa[rootX] = rootY
            self.__size[rootY] += self.__size[rootX]
        else:
            self.__fa[rootY] = rootX
            self.__size[rootX] += self.__size[rootY]
        self.__count -= 1
    def isConnected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)
    def getCount(self) -> int:
        return self.__count

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # uf = UF(n)
        # graph = [set() for _ in range(n)]
        # for u,v in edges:
        #     uf.union(u, v)
        #     graph[u].add(v)
        #     graph[v].add(u)
        # ans = 0
        added = [1] * n
        graph = [set() for _ in range(n)]
        fa = []
        mapping = {}
        for u,v in edges:
            added[u] = 0
            added[v] = 0
            graph[u].add(v)
            graph[v].add(u)
            if u in mapping:
                fa[mapping[u]].add(v)
            elif v in mapping:
                fa[mapping[v]].add(u)
            else:
                tmp = set()
                tmp.add(u)
                tmp.add(v)
                fa.append(tmp)
                mapping[u] = len(fa) - 1
                mapping[v] = len(fa) - 1
        ans = sum(added)
        for s in fa:
            flag = True
            for t in s:
                if graph[t] | set([t]) != s:
                    flag = False
                    break
            if flag:
                ans += 1
        return ans

sl = Solution()
p1 = [[0,1],[0,2],[1,2],[3,4],[3,5]]
# p1 = [[0,1],[0,2],[1,2],[3,4]]
print(sl.countCompleteComponents(6, p1))