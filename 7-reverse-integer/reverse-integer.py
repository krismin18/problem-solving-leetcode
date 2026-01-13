class Solution(object):
    def reverse(self, x):
        s = -1 if x < 0 else 1
        rev, x = 0, abs(x)

        while x != 0:
            mod = x % 10
            rev = rev * 10 + mod
            x = x // 10
        
        if rev > 2**31 - 1:
            return 0
        return s * rev


        