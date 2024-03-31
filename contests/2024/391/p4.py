from typing import *


class Solution:
    def minimumDistance(self, points: List[List[int]]) -> int:
        def check(distance):
            count = 0
            j = 0
            for i in range(n):
                while j < n and points[j][0] - points[i][0] <= distance:
                    j += 1
                count += j - i - 1
            return count >= (n - 1) * (n - 2) // 2

        def manhattan_distance(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        n = len(points)
        points.sort()
        left, right = 0, 2 * 10**9
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left

# Example usage:
points = [[1, 2], [3, 5], [4, 6], [7, 8]]
print(minMaxDistance(points))  # Output will be 4





sl = Solution()
examples = [
    # ([[3,10],[5,15],[10,2],[4,4]], 12),
    # ([[1,1],[1,1],[1,1]], 0),
    ([[9,8],[1,8],[3,1],[9,1],[7,7],[3,6]], 13)
]
for example in examples:
    x, ans = example
    print(f"Output: {sl.minimumDistance(x)}, Ans: {ans}")