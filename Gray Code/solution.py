class Solution(object):
    def grayCode(self, n):
        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]
        l = self.grayCode(n-1)
        return l + [2**(n-1)+i for i in l[::-1]]
