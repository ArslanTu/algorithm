from math import inf


class Solution:
    def minimumCost(self, s: str) -> int:
        n = len(s)
        mid = (n // 2) - 1
        # 1
        res_1 = 0
        i = mid
        while i >= 0 and s[i] == '1':
            i -= 1
        if i >= 0:
            res_1 += i + 1
            i -= 1
            while i >= 0:
                if s[i] != s[i + 1]:
                    res_1 += i + 1
                i -= 1
        i = mid + 1
        while i < n and s[i] == '1':
            i += 1
        if i < n:
            res_1 += n - i
            i += 1
            while i < n:
                if s[i] != s[i - 1]:
                    res_1 += n - i
                i += 1
        
        # 0
        res_0 = 0
        i = mid
        while i >= 0 and s[i] == '0':
            i -= 1
        if i >= 0:
            res_0 += i + 1
            i -= 1
            while i >= 0:
                if s[i] != s[i + 1]:
                    res_0 += i + 1
                i -= 1
        i = mid + 1
        while i < n and s[i] == '0':
            i += 1
        if i < n:
            res_0 += n - i
            i += 1
            while i < n:
                if s[i] != s[i - 1]:
                    res_0 += n - i
                i += 1
        return min(res_1, res_0)







sl = Solution()
p1 = "010101"

print(sl.minimumCost(p1))