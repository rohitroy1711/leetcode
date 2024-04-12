class Solution:
    cache = {}
    count = 0
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n in self.cache:
            return self.cache[n]
        self.cache[n] = self.climbStairs(n-1)+self.climbStairs(n-2)
        return self.cache[n]