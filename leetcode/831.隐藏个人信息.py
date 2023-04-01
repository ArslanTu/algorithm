#
# @lc app=leetcode.cn id=831 lang=python3
#
# [831] 隐藏个人信息
#

# @lc code=start
class Solution:
    def maskPII(self, s: str) -> str:
        ans = ""
        at_idx = s.find('@')
        if  at_idx != -1:
            # email address
            s = s.lower()
            ans += s[0] + "*****" + s[at_idx - 1:]
        else:
            # tel number
            useless = ['+', '-', '(', ')', ' ']
            for ch in useless:
                s = s.replace(ch, '')
            ans += "***-***-" + s[-4:]
            if len(s) > 10:
                ans = '+' + '*' * (len(s) - 10) + '-' + ans
        return ans
# @lc code=end

sl = Solution()
p1 = "1(234)567-890"
print(sl.maskPII(p1))