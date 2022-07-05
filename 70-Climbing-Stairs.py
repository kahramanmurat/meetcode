class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp
        return one


n = int(input("Please enter the step numbers: "))
print(Solution.climbStairs(self=n, n=n))
