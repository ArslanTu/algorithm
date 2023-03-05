class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        cur = 1
        dir = 1
        while time:
            if cur == 1:
                dir = 1
            elif cur == n:
                dir = -1
            cur += dir
            time -= 1
        return cur
sl = Solution()

p1 = 4
p2 = 5

print(sl.passThePillow(p1, p2))