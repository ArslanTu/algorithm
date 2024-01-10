from typing import *

class Node:
    def __init__(self, num: int):
        self.num = num
        self.child_sum = 0
        self.nexts: List[Node] = []
        self.score = 0

class Solution:
    def maximumScoreAfterOperations(self, edges: List[List[int]], values: List[int]) -> int:
        nodes = [Node(values[i]) for i in range(len(values))]

        links = [[] for i in range(len(values))]
        for u, v in edges:
            links[u].append(v)
            links[v].append(u)
        
        def dfs(x):
            for next in links[x]:
                if nodes[x] not in nodes[next].nexts:
                    nodes[x].nexts.append(nodes[next])
                    dfs(next)

        dfs(0)


        layers = [[nodes[0]]]
        while True:
            cur_layer = layers[-1]
            next_layer = []
            for node in cur_layer:
                for next in node.nexts:
                    next_layer.append(next)
            if len(next_layer) == 0:
                break
            else:
                layers.append(next_layer)
        
        for i in range(len(layers) - 1, -1, -1):
            cur_layer = layers[i]
            for node in cur_layer:
                sub_score = 0
                for next in node.nexts:
                    node.child_sum += next.child_sum + next.num
                    sub_score += next.score
                if node.child_sum == 0:
                    node.score = 0
                else:
                    node.score = max(node.child_sum, node.num + sub_score)

        return nodes[0].score
        

sl = Solution()
# print(sl.maximumScoreAfterOperations([[0,1],[0,2],[0,3],[2,4],[4,5]], [5,2,5,2,1,1]))
# print(sl.maximumScoreAfterOperations([[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]], [20,10,9,7,4,3,5]))
print(sl.maximumScoreAfterOperations([[7,0],[3,1],[6,2],[4,3],[4,5],[4,6],[4,7]], [2,16,23,17,22,21,8,6]))

# 11
# 40
# 113