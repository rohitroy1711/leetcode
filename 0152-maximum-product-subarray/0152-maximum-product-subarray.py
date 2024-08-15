class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        currMax = 1
        currMin = 1
        for n in nums:
            if n == 0:
                currMax = 1
                currMin = 1
                continue
            temp = currMax * n
            currMax = max(temp,n*currMin,n)
            currMin = min(temp,n*currMin,n)
            res = max(currMax,res)
        return res