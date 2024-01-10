class Solution:
    def minLength(self, s: str) -> int:
        t = str(s)
        a = 0
        while s != t or a ==0:
            a = 1
            s = str(t)
            t = t.replace("AB", "")
            t = t.replace("CD", "")
            
        return len(s)