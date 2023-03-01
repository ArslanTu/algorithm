class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        link_row = 0
        n = len(s)
        idx = 0
        z_str = []
        step = 0
        while idx < n:
            if not link_row:
                step = min(n - idx, numRows)
                z_str.append(s[idx:idx + step])
            else:
                step = min(n - idx, numRows - 2)
                z_str.append(" " + " " * max(0, numRows - 2 - step) + s[idx + step - 1: idx - 1: -1] + " ")
            link_row = 1 - link_row
            idx += step
        z_str[-1] += (" " * (numRows - len(z_str[-1])))
        ans = ""
        print(z_str)
        for c in range(numRows):
            for r in range(len(z_str)):
                if z_str[r][c] != " ":
                    ans += z_str[r][c]
        return ans