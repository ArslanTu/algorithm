class Solution:
    def smallestString(self, s: str) -> str:
        n = len(s)
        modified = False
        for i in range(n):
            if s[i] == 'a':
                if modified:
                    break
                else:
                    continue
            else:
                if not modified:
                    modified = True
                s = s[:i] + chr(ord(s[i]) - 1) + s[i + 1:]
        if not modified:
            s = s[:n - 1] + 'z'
        return s

sl = Solution()
p1 = "a"

print(sl.smallestString(p1))