from typing import List


class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        total = m * n
        graph = [[] for _ in range(total)]
        nums = []

        # 有向无环图，从小值指向大值
        for i in range(m):
            for j in range(n):
                cur = i * n + j
                nums.append((mat[i][j], cur))
                # 遍历列（当前单元格以下）
                for k in range(i +1, m):
                    if mat[k][j] > mat[i][j]:
                        graph[cur].append(k * n + j)
                    elif mat[k][j] < mat[i][j]:
                        graph[k * n + j].append(cur)
                # 遍历行（从当前单元格往右）
                for k in range(j + 1, n):
                    if mat[i][k] > mat[i][j]:
                        graph[cur].append(i * n + k)
                    elif mat[i][k] < mat[i][j]:
                        graph[i * n + k].append(cur)

        # 从大到小遍历单元格
        nums.sort(reverse=True)
        dp = [1] * total

        for _, cur in nums:
            for next in graph[cur]:
                dp[cur] = max(dp[cur], dp[next] + 1)

        return max(dp)

sl = Solution()
p1 = [[3,1],[3,4]]
p2 = [[3,1,6],[-9,5,7]]
p3 = [[39,-7,48,-13,-23,34,34,13,23,-14,-49,24,34,1,19,47,-36,29,-1,1,-50,42,27,11,-5,-37,20,38,43,3,-23,-41,22]]

print(sl.maxIncreasingCells(p1))
print(sl.maxIncreasingCells(p2))
print(sl.maxIncreasingCells(p3))