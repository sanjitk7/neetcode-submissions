class Solution:
    def climbStairs(self, n: int) -> int:
        a,b = 1,0

        for i in range(n):
            steps = a
            a = a + b
            b = steps

        return a
            
