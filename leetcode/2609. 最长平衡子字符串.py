class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        ans = 0
        cur_0 = 0
        cur_1 = 0
        n = len(s)
        for i in range(n):
            if s[i] == '0':
                if (i > 0 and s[i - 1] == '1'):
                    ans = max(ans, min(cur_0, cur_1) * 2)
                    cur_0 = 1
                    cur_1 = 0
                else:
                    cur_0 += 1
            else:
                cur_1 += 1
        if s[-1] == '1':
            ans = max(ans, min(cur_0, cur_1) * 2)
        return ans


sl = Solution()
p1 = "001"
print(sl.findTheLongestBalancedSubstring(p1))