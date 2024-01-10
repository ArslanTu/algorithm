class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        n = len(s)
        for i in range(n//2):
            if s[i] == s[n - 1 - i]:
                continue
            else:
                if s[i] < s[n - 1 - i]:
                    s = s[:n - 1 - i] + s[i] + s[n - i:]
                else:
                    s = s[:i] + s[n - 1 - i] + s[i + 1:]
        return s
