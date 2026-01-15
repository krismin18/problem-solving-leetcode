class Solution(object):
    def compress(self, chars):
        n= len(chars)
        ind = 0
        i = 0
        while i < n:
            ch = chars[i]
            cnt = 0
            while i < n and chars[i] == ch:
                cnt += 1
                i += 1
            if cnt == 1:
                chars[ind] = ch
                ind += 1
            else:
                chars[ind] = ch
                ind += 1
                for digit in str(cnt):
                    chars[ind]  = digit
                    ind += 1
        chars[:] = chars[:ind]
        return ind