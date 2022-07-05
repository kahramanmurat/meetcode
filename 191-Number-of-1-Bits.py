class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n % 2
            n = n >> 1
        return res


n = 00000000000000000000000000001011
print(Solution.hammingWeight(self=n, n=n))
