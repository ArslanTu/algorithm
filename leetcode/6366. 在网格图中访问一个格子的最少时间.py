from math import inf
from typing import List


class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        '''
        如果在时间 end_time 可以到达终点
        那么在更长的时间内也一定可以到达
        具有单调性，因此可以二分查找答案
        '''
        m, n = len(grid), len(grid[0])
        # 无法走出起始单元格
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1
        '''
        vis 用于记录当前单元格是否已经遍历过
        用当前正在 check 的 end_time 作为标记
        ''' 
        vis = [[-inf] * n for _ in range(m)]
        start_time = inf
        
        def check(end_time):
            # q 存储的是等待被遍历其周围单元格的单元格（本身已经遍历过）
            q = [(m - 1, n - 1)]
            vis[-1][-1] = end_time
            t = end_time
            while q:
                t -= 1
                tmp = q
                q = []
                for i, j in tmp:
                    # 遍历上下左右四个格子
                    for x, y in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                        # 如果行列号合法，也未被访问，且时间小于等于当前时间，说明可以被合法访问
                        if 0 <= x < m and 0 <= y < n and vis[x][y] != end_time and grid[x][y] <= t:
                            if x == 0 and y == 0:
                                nonlocal start_time
                                start_time = min(start_time, t)
                                return True
                            # 将当前单元格标记为已访问
                            vis[x][y] = end_time
                            # 将其入队，等待遍历其周围单元格
                            q.append((x, y))
            return False
        
        # 上下界均为开区间
        left = max(grid[-1][-1], m + n - 2) - 1
        right = max(map(max, grid)) + m + n
        
        while left + 1 < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid
        return right + start_time % 2

sl = Solution()

p1 = [[0,1,3,2],[5,1,2,5],[4,3,8,6]]


print(sl.minimumTime(p1))